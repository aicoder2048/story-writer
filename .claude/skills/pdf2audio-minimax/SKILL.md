---
name: pdf2audio-minimax
description: "Convert PDF files to MP3 audio using MiniMax MCP Server's text-to-audio tool. Use when user wants to convert a PDF to audio/MP3, create audiobook from PDF, or text-to-speech for PDF documents. Requires PDF file path; voice ID is optional (auto-selects based on content)."
---

# PDF to Audio Converter (MiniMax)

Convert PDF documents to MP3 audio files using MiniMax text-to-audio.

## Input Format

```
/pdf2audio-minimax <pdf_file_path> [voice_id]
```

**Examples:**
- `/pdf2audio-minimax /path/to/story.pdf` (auto-select voice)
- `/pdf2audio-minimax /path/to/story.pdf Chinese (Mandarin)_Gentleman`

## Workflow

### 1. Parse Arguments

Extract from user input:
- `pdf_path`: Full path to the PDF file (required)
- `voice_id`: Voice identifier (optional)

### 2. Read PDF Content

```
Read: file_path = <pdf_path>
```

### 3. Extract Text

Extract readable text, skipping page numbers and headers. Keep chapter titles, body text, dialogue.

### 4. Select Voice

**If voice_id provided:** Use the specified voice.

**If voice_id not provided:** Auto-select based on content keywords:

| Content Keywords | Voice ID |
|-----------------|----------|
| 童话、儿童、小朋友、冒险 | `Chinese (Mandarin)_Cute_Spirit` |
| 言情、爱情、浪漫、甜蜜 | `Chinese (Mandarin)_Sweet_Lady` |
| 科幻、悬疑、历史、战争 | `Chinese (Mandarin)_Gentleman` |
| 新闻、报告、公告 | `Chinese (Mandarin)_News_Anchor` |
| Default | `Chinese (Mandarin)_Gentleman` |

For complete voice list, see [references/voices.md](references/voices.md).

### 5. Convert to Audio

```
mcp__MiniMax__text_to_audio:
  text: <extracted_text>
  voice_id: <selected_voice_id>
  output_directory: <same directory as input PDF>
  language_boost: "Chinese"
  speed: 1
```

### 6. Output

MP3 saved to the same directory as the input PDF.

## Quick Reference: Common Voices

| Use Case | Voice ID |
|----------|----------|
| Audiobook (male) | `Chinese (Mandarin)_Gentleman` |
| Audiobook (female) | `Chinese (Mandarin)_Soft_Girl` |
| Children's story | `Chinese (Mandarin)_Cute_Spirit` |
| News/Formal | `Chinese (Mandarin)_News_Anchor` |

Full voice reference: [references/voices.md](references/voices.md)
