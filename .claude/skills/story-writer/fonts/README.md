# Chinese Fonts for Story Writer

This directory contains Chinese fonts that are compatible with `reportlab` for PDF generation.

## Why These Fonts?

macOS system fonts often come in `.ttc` (TrueType Collection) format with **CFF/PostScript outlines**, which `reportlab` does not support. Only fonts with **TrueType outlines** work with reportlab.

The fonts in this directory are standalone `.ttf` files with TrueType outlines, extracted from macOS system fonts.

## Available Fonts

| Font File | Chinese Name | Style | Best For |
|-----------|--------------|-------|----------|
| `STHeiti.ttf` | 华文黑体 | Sans-serif | UI, titles, modern text |
| `STFangsong.ttf` | 华文仿宋 | Serif (Fangsong) | Novel body text, classic style |
| `STKai.ttf` | 华文楷体 | Script (Kai) | Elegant headers, traditional |
| `Hei.ttf` | 黑体 | Sans-serif | Clean, minimal text |
| `STXihei.ttf` | 华文细黑 | Thin Sans-serif | Light, modern look |

## Usage with ReportLab

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register fonts
font_dir = ".claude/skills/story-writer/fonts"
pdfmetrics.registerFont(TTFont('STHeiti', f'{font_dir}/STHeiti.ttf'))
pdfmetrics.registerFont(TTFont('STFangsong', f'{font_dir}/STFangsong.ttf'))
pdfmetrics.registerFont(TTFont('STKai', f'{font_dir}/STKai.ttf'))

# Use in canvas
c.setFont('STFangsong', 12)
c.drawString(100, 700, "这是一段中文文本")
```

## Usage with Matplotlib

```python
import matplotlib.font_manager as fm

font_path = ".claude/skills/story-writer/fonts/STHeiti.ttf"
prop = fm.FontProperties(fname=font_path)
ax.text(0.5, 0.5, "中文标题", fontproperties=prop)
```

## Recommended Pairings

- **Novel/Story**: `STFangsong` for body, `STKai` for chapter titles
- **Modern/Sci-Fi**: `STHeiti` for body, `STXihei` for captions
- **Traditional**: `STKai` throughout

## Source

These fonts are copied from macOS system fonts (Apple's Huawen series). They are included for development convenience within this project.
