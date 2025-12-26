---
name: pdf2audio_batch
description: 批量将小说章节PDF转换为MP3有声书（并行处理）
argument-hint: <故事名> <章节范围> [声音名]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, Skill
---

# 批量PDF转音频

通过并行使用 `/pdf2audio-minimax` SKILL 将多个PDF章节同时转换为MP3。

## 参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `$1` 故事名 | 故事目录名（必填） | `星际迷航` |
| `$2` 章节范围 | 支持范围、列表、混合（必填） | `01-03`、`01,03,05`、`01,03-05` |
| `$3` 声音名 | 可选，默认 Gentleman | `Sweet_Lady` |

**常用声音：**
- `Gentleman` - 成熟男声（默认）
- `Sweet_Lady` - 温柔女声
- `Cute_Spirit` - 童话/儿童
- `News_Anchor` - 新闻播报

## 工作流程

### 1. 验证输入
- 检查目录 `$1/chapters/` 是否存在
- 解析章节范围 `$2`，匹配 PDF 文件：`$1/chapters/$1-*.pdf`

### 2. 并行转换
使用 Task 工具启动多个 Agent，每个调用：
```
/pdf2audio-minimax $1/chapters/$1-XX.pdf [$3]
```

### 3. 汇总报告
收集所有 Agent 输出，报告成功/失败的文件。

## 示例

**命令：**
```
/pdf2audio_batch 星际迷航 01-03 Sweet_Lady
```

**执行：**
- Agent 1: `/pdf2audio-minimax 星际迷航/chapters/星际迷航-01.pdf Sweet_Lady`
- Agent 2: `/pdf2audio-minimax 星际迷航/chapters/星际迷航-02.pdf Sweet_Lady`
- Agent 3: `/pdf2audio-minimax 星际迷航/chapters/星际迷航-03.pdf Sweet_Lady`

**输出：** `星际迷航/audiobook/星际迷航-01.mp3` 等
