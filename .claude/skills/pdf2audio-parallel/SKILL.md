---
name: pdf2audio-parallel
description: "Parallel PDF to MP3 conversion using MiniMax. Convert multiple PDF chapters to audio simultaneously using parallel subagents. Use when: (1) User says 'generate mp3 for the story of [STORY_NAME]', (2) User says '为故事[STORY_NAME]生成mp3', (3) User says '为故事[STORY_NAME]第[X]章生成mp3', (4) User says 'generate mp3 for story of [STORY_NAME], chapter [X]', (5) Converting a range of PDFs like 'story-[01-05].pdf' to MP3, (6) Batch audiobook creation from PDF chapters. Handles file naming normalization to ensure output matches input pattern."
---

# Parallel PDF to Audio Converter

Convert multiple PDF chapters to MP3 audio in parallel using MiniMax text-to-audio.

## Trigger Phrases

This skill triggers on natural language requests:

| User Says | Action |
|-----------|--------|
| "generate mp3 for the story of 我的故事" | Convert all chapters |
| "为故事我的故事生成mp3" | Convert all chapters |
| "为故事我的故事第[01, 03-04]章生成mp3" | Convert specified chapters |
| "generate mp3 for story of 我的故事, chapter [01-05]" | Convert specified chapters |

## Input Format

**Direct command:**
```
/pdf2audio-parallel "<story_dir>/chapters/<story_name>-[chapter_pattern].pdf" [voice_name] [count]
```

**Examples:**
- `/pdf2audio-parallel "重写时间的源代码/chapters/重写时间的源代码-[01-05].pdf" "Cute Spirit" 5`
- `/pdf2audio-parallel "我的故事/chapters/我的故事-[01, 03-04].pdf" "Gentleman" 3`
- `/pdf2audio-parallel "星际迷航/chapters/星际迷航-[01-02, 05-07].pdf" "Soft Girl" 5`

## Workflow

### 1. Parse Input Parameters

**From natural language:** Extract story name, then discover chapters:
```bash
# Find story directory
ls -d <STORY_NAME>/

# List available PDF chapters
ls <STORY_NAME>/chapters/<STORY_NAME>-*.pdf
```

**From direct command:** Extract from path pattern:
- `story_dir`: Story directory name (e.g., `重写时间的源代码`)
- `story_name`: Story name from filename pattern (usually same as directory)
- `chapter_pattern`: Chapter numbers (e.g., `01-05` or `[01, 03-04]`)
- `voice_name`: Voice name for TTS (maps to Voice ID)
- `count`: Number of parallel agents (= number of chapters to convert)

**Voice Name Mapping:**

| Voice Name | Voice ID |
|-----------|----------|
| Cute Spirit | `Chinese (Mandarin)_Cute_Spirit` |
| Sweet Lady | `Chinese (Mandarin)_Sweet_Lady` |
| Gentleman | `Chinese (Mandarin)_Gentleman` |
| Soft Girl | `Chinese (Mandarin)_Soft_Girl` |
| News Anchor | `Chinese (Mandarin)_News_Anchor` |

### 2. Generate Chapter List

Parse the chapter pattern and expand into individual files.

**Supported Patterns:**

| Pattern | Expands To |
|---------|------------|
| `[01-05]` | 01, 02, 03, 04, 05 |
| `[03]` | 03 |
| `[01, 03-04]` | 01, 03, 04 |
| `[01-02, 05-07]` | 01, 02, 05, 06, 07 |
| `[01, 03, 05]` | 01, 03, 05 |

**Example:** `我的故事/chapters/我的故事-[01, 03-04].pdf` expands to:
- `我的故事/chapters/我的故事-01.pdf`
- `我的故事/chapters/我的故事-03.pdf`
- `我的故事/chapters/我的故事-04.pdf`

### 3. Launch Parallel Agents

Use Task tool to spawn N agents simultaneously, each handling one PDF conversion.

**Agent Prompt Template:**

```
Convert PDF to MP3:
1. Read PDF: <story_dir>/chapters/<story_name>-XX.pdf
2. Extract text content (skip page numbers/headers)
3. Convert to audio using mcp__MiniMax__text_to_audio:
   - text: <extracted_text>
   - voice_id: <mapped_voice_id>
   - output_directory: <story_dir>/chapters
   - language_boost: "Chinese"
4. After conversion, rename output file to: <story_name>-XX.mp3

IMPORTANT: MiniMax may generate files with names like:
  t2a_第X章:标题_YYYYMMDD_HHMMSS.mp3

You MUST rename to the standard format:
  <story_name>-XX.mp3

Example: If converting 重写时间的源代码-01.pdf
  - Expected output: 重写时间的源代码-01.mp3
  - Wrong output (needs rename): t2a_第1章:完美候选_20251224_090451.mp3
```

### 4. File Naming Normalization

After each agent completes, verify and fix output filename:

**Expected Format:**
```
<story_name>-XX.mp3
```

**Rename Logic:**
```bash
# Find the most recent mp3 in the directory that doesn't match expected pattern
# Rename to expected pattern
scripts/rename_audio.py <story_dir>/chapters <story_name> <chapter_number>
```

### 5. Collect Results

Gather outputs from all agents and report:
- Successfully converted files
- Final file paths with correct naming
- Any errors encountered

## Quick Examples

### Example 1: Simple Range

**User Input:**
```
/pdf2audio-parallel "我的故事/chapters/我的故事-[01-03].pdf" "Cute Spirit" 3
```

**Parallel Agent Tasks:**
1. Agent 1: Convert `我的故事-01.pdf` → `我的故事-01.mp3`
2. Agent 2: Convert `我的故事-02.pdf` → `我的故事-02.mp3`
3. Agent 3: Convert `我的故事-03.pdf` → `我的故事-03.mp3`

### Example 2: Mixed Pattern

**User Input:**
```
/pdf2audio-parallel "星际迷航/chapters/星际迷航-[01, 03-04].pdf" "Gentleman" 3
```

**Parallel Agent Tasks:**
1. Agent 1: Convert `星际迷航-01.pdf` → `星际迷航-01.mp3`
2. Agent 2: Convert `星际迷航-03.pdf` → `星际迷航-03.mp3`
3. Agent 3: Convert `星际迷航-04.pdf` → `星际迷航-04.mp3`

## Scripts

### scripts/rename_audio.py

Utility script to normalize MP3 filenames after MiniMax generation.
