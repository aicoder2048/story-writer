#!/usr/bin/env python3
"""Create chapter covers for 文明的最后一个变量 using Quantum Parchment design philosophy."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import os

# Register fonts
font_dir = "/Users/szou/Python/Playground/StoryWriter/.claude/skills/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont('Italiana', f"{font_dir}/Italiana-Regular.ttf"))
pdfmetrics.registerFont(TTFont('Jura', f"{font_dir}/Jura-Light.ttf"))
pdfmetrics.registerFont(TTFont('JuraMedium', f"{font_dir}/Jura-Medium.ttf"))
pdfmetrics.registerFont(TTFont('CrimsonPro', f"{font_dir}/CrimsonPro-Regular.ttf"))
pdfmetrics.registerFont(TTFont('CrimsonProItalic', f"{font_dir}/CrimsonPro-Italic.ttf"))
pdfmetrics.registerFont(TTFont('PoiretOne', f"{font_dir}/PoiretOne-Regular.ttf"))

# For Chinese text, we need a font that supports it - use system font
try:
    pdfmetrics.registerFont(TTFont('PingFang', '/System/Library/Fonts/PingFang.ttc', subfontIndex=0))
    CHINESE_FONT = 'PingFang'
except:
    try:
        pdfmetrics.registerFont(TTFont('STHeiti', '/System/Library/Fonts/STHeiti Light.ttc'))
        CHINESE_FONT = 'STHeiti'
    except:
        CHINESE_FONT = 'Helvetica'

# Color palette - Quantum Parchment
IVORY = Color(0.97, 0.95, 0.91, 1)
CHAMPAGNE = Color(0.95, 0.92, 0.85, 1)
SOFT_GOLD = Color(0.82, 0.75, 0.58, 0.5)
WARM_GRAY = Color(0.45, 0.42, 0.38, 1)
DEEP_CHARCOAL = Color(0.18, 0.16, 0.14, 1)
TRACE_LINE = Color(0.70, 0.65, 0.55, 0.35)
ACCENT_COPPER = Color(0.72, 0.52, 0.38, 0.7)

# Book data
book_title = "文明的最后一个变量"
book_subtitle = "THE LAST VARIABLE OF CIVILIZATION"

# Chapter data
chapters = [
    {
        "num": 1,
        "title": "审定",
        "subtitle": "THE ASSESSMENT",
    },
    {
        "num": 2,
        "title": "相遇",
        "subtitle": "THE ENCOUNTER",
    },
    {
        "num": 3,
        "title": "审判",
        "subtitle": "THE JUDGMENT",
    },
    {
        "num": 4,
        "title": "悖论",
        "subtitle": "THE PARADOX",
    },
    {
        "num": 5,
        "title": "变量",
        "subtitle": "THE VARIABLE",
    },
]

def draw_orbital_lines(c, width, height, chapter_num):
    """Draw delicate orbital/trajectory lines unique to each chapter."""
    c.saveState()
    c.setStrokeColor(TRACE_LINE)
    c.setLineWidth(0.4)

    center_x = width / 2
    center_y = height * 0.52

    # Different patterns for each chapter
    if chapter_num == 1:
        # Concentric circles suggesting observation
        for i in range(5):
            radius = 55 + i * 22
            c.circle(center_x, center_y, radius, stroke=1, fill=0)
    elif chapter_num == 2:
        # Intersecting arcs suggesting meeting
        for i in range(3):
            c.arc(center_x - 90 - i*18, center_y - 60,
                  center_x + 90 + i*18, center_y + 60, 20, 140)
            c.arc(center_x - 90 - i*18, center_y - 60,
                  center_x + 90 + i*18, center_y + 60, 200, 140)
    elif chapter_num == 3:
        # Grid suggesting structure/judgment
        for i in range(-3, 4):
            c.line(center_x + i*35, center_y - 90, center_x + i*35, center_y + 90)
        for i in range(-3, 4):
            c.line(center_x - 105, center_y + i*26, center_x + 105, center_y + i*26)
    elif chapter_num == 4:
        # Möbius-like curves suggesting paradox
        c.setLineWidth(0.5)
        for i in range(3):
            phase = i * math.pi / 3
            prev_x, prev_y = None, None
            for t in range(101):
                t_val = t / 100 * 2 * math.pi
                x = center_x + 70 * math.sin(t_val + phase)
                y = center_y + 35 * math.sin(2 * t_val)
                if prev_x is not None:
                    c.line(prev_x, prev_y, x, y)
                prev_x, prev_y = x, y
    else:  # chapter 5
        # Scattered points suggesting unpredictability/variables
        import random
        random.seed(42)  # For reproducibility
        c.setFillColor(TRACE_LINE)
        for _ in range(60):
            x = center_x + random.gauss(0, 55)
            y = center_y + random.gauss(0, 70)
            size = random.uniform(0.8, 2.5)
            c.circle(x, y, size, stroke=0, fill=1)

    c.restoreState()

def draw_geometric_accent(c, width, height, chapter_num):
    """Draw the main geometric symbol for each chapter."""
    c.saveState()
    center_x = width / 2
    center_y = height * 0.52

    c.setStrokeColor(ACCENT_COPPER)
    c.setLineWidth(1.2)

    if chapter_num == 1:
        # Circle with center dot
        c.circle(center_x, center_y, 40, stroke=1, fill=0)
        c.setFillColor(ACCENT_COPPER)
        c.circle(center_x, center_y, 2.5, stroke=0, fill=1)
    elif chapter_num == 2:
        # Two overlapping circles
        c.circle(center_x - 22, center_y, 32, stroke=1, fill=0)
        c.circle(center_x + 22, center_y, 32, stroke=1, fill=0)
    elif chapter_num == 3:
        # Square
        size = 65
        c.rect(center_x - size/2, center_y - size/2, size, size, stroke=1, fill=0)
    elif chapter_num == 4:
        # Diamond (rotated square)
        path = c.beginPath()
        size = 45
        path.moveTo(center_x, center_y + size)
        path.lineTo(center_x + size, center_y)
        path.lineTo(center_x, center_y - size)
        path.lineTo(center_x - size, center_y)
        path.close()
        c.drawPath(path, stroke=1, fill=0)
    else:  # chapter 5
        # Infinity symbol
        c.setLineWidth(1.5)
        prev_x, prev_y = None, None
        for i in range(101):
            t = i / 100 * 2 * math.pi
            scale = 40
            denom = 1 + math.sin(t)**2
            x = center_x + scale * math.cos(t) / denom
            y = center_y + scale * math.sin(t) * math.cos(t) / denom
            if prev_x is not None:
                c.line(prev_x, prev_y, x, y)
            prev_x, prev_y = x, y

    c.restoreState()

def create_cover(chapter_data, output_path):
    """Create a single chapter cover."""
    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)

    # Background
    c.setFillColor(IVORY)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Subtle gradient overlay at top
    c.setFillColor(CHAMPAGNE)
    c.rect(0, height * 0.87, width, height * 0.13, stroke=0, fill=1)

    # Draw orbital lines (background element)
    draw_orbital_lines(c, width, height, chapter_data["num"])

    # Draw geometric accent
    draw_geometric_accent(c, width, height, chapter_data["num"])

    # Story title at top - elegant and minimal (Chinese)
    c.setFillColor(WARM_GRAY)
    c.setFont(CHINESE_FONT, 11)
    c.drawCentredString(width/2, height - 42*mm, "文明的最后一个变量")

    # Thin separator line
    c.setStrokeColor(SOFT_GOLD)
    c.setLineWidth(0.6)
    c.line(width/2 - 45*mm, height - 48*mm, width/2 + 45*mm, height - 48*mm)

    # Chapter number - subtle, technical
    c.setFillColor(TRACE_LINE)
    c.setFont('JuraMedium', 9)
    c.drawCentredString(width/2, height - 58*mm, f"CHAPTER {chapter_data['num']:02d}")

    # Chapter title in Chinese - main focal point
    c.setFillColor(DEEP_CHARCOAL)
    c.setFont(CHINESE_FONT, 48)
    c.drawCentredString(width/2, height * 0.28, chapter_data["title"])

    # English subtitle - whisper quiet
    c.setFillColor(WARM_GRAY)
    c.setFont('CrimsonProItalic', 12)
    c.drawCentredString(width/2, height * 0.28 - 16*mm, chapter_data["subtitle"])

    # Bottom accent - thin line
    c.setStrokeColor(SOFT_GOLD)
    c.setLineWidth(0.6)
    c.line(width/2 - 25*mm, 32*mm, width/2 + 25*mm, 32*mm)

    # Small roman numeral at bottom
    roman = ['I', 'II', 'III', 'IV', 'V'][chapter_data["num"]-1]
    c.setFillColor(TRACE_LINE)
    c.setFont('CrimsonProItalic', 14)
    c.drawCentredString(width/2, 20*mm, roman)

    c.save()
    print(f"Created: {output_path}")

def draw_book_cover_pattern(c, width, height):
    """Draw a sophisticated pattern for the book cover."""
    c.saveState()
    center_x = width / 2
    center_y = height * 0.52

    # Multiple concentric circles with varying opacity
    c.setStrokeColor(TRACE_LINE)
    c.setLineWidth(0.3)
    for i in range(8):
        radius = 30 + i * 18
        c.circle(center_x, center_y, radius, stroke=1, fill=0)

    # Grid of dots suggesting data/variables
    import random
    random.seed(2049)
    c.setFillColor(TRACE_LINE)
    for _ in range(120):
        x = center_x + random.gauss(0, 80)
        y = center_y + random.gauss(0, 100)
        size = random.uniform(0.5, 2.0)
        c.circle(x, y, size, stroke=0, fill=1)

    # Central infinity symbol (representing the variable/unpredictability)
    c.setStrokeColor(ACCENT_COPPER)
    c.setLineWidth(2.0)
    prev_x, prev_y = None, None
    for i in range(101):
        t = i / 100 * 2 * math.pi
        scale = 55
        denom = 1 + math.sin(t)**2
        x = center_x + scale * math.cos(t) / denom
        y = center_y + scale * math.sin(t) * math.cos(t) / denom
        if prev_x is not None:
            c.line(prev_x, prev_y, x, y)
        prev_x, prev_y = x, y

    c.restoreState()

def create_book_cover(output_path):
    """Create the main book cover (Cover-0)."""
    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)

    # Background
    c.setFillColor(IVORY)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Subtle gradient overlay at top
    c.setFillColor(CHAMPAGNE)
    c.rect(0, height * 0.85, width, height * 0.15, stroke=0, fill=1)

    # Draw the book cover pattern
    draw_book_cover_pattern(c, width, height)

    # Book title in Chinese - large and prominent
    c.setFillColor(DEEP_CHARCOAL)
    c.setFont(CHINESE_FONT, 42)
    c.drawCentredString(width/2, height * 0.25, book_title)

    # English subtitle - elegant and understated
    c.setFillColor(WARM_GRAY)
    c.setFont('CrimsonProItalic', 11)
    c.drawCentredString(width/2, height * 0.25 - 14*mm, book_subtitle)

    # Genre label at top
    c.setFillColor(TRACE_LINE)
    c.setFont('JuraMedium', 8)
    c.drawCentredString(width/2, height - 35*mm, "SCIENCE FICTION")

    # Top decorative line
    c.setStrokeColor(SOFT_GOLD)
    c.setLineWidth(0.8)
    c.line(width/2 - 35*mm, height - 42*mm, width/2 + 35*mm, height - 42*mm)

    # Bottom decorative line
    c.setStrokeColor(SOFT_GOLD)
    c.setLineWidth(0.8)
    c.line(width/2 - 50*mm, 35*mm, width/2 + 50*mm, 35*mm)

    # Small decorative element at bottom
    c.setFillColor(ACCENT_COPPER)
    c.circle(width/2, 25*mm, 2, stroke=0, fill=1)

    c.save()
    print(f"Created: {output_path}")

def main():
    output_dir = "/Users/szou/Python/Playground/StoryWriter/文明的最后一个变量_V3/chapters"

    # Create book cover (Cover-0)
    book_cover_path = os.path.join(output_dir, "Cover-0.pdf")
    create_book_cover(book_cover_path)

    # Create chapter covers
    for chapter in chapters:
        output_path = os.path.join(output_dir, f"Cover-{chapter['num']}.pdf")
        create_cover(chapter, output_path)

    print("\nAll covers created successfully!")

if __name__ == "__main__":
    main()
