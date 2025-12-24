#!/usr/bin/env python3
"""Create book covers for 《重写时间的源代码》"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
import math
import os

# Register fonts
font_dir = "/Users/szou/Python/Playground/StoryWriter/.claude/skills/canvas-design/canvas-fonts"
pdfmetrics.registerFont(TTFont('Italiana', os.path.join(font_dir, 'Italiana-Regular.ttf')))
pdfmetrics.registerFont(TTFont('WorkSans', os.path.join(font_dir, 'WorkSans-Regular.ttf')))
pdfmetrics.registerFont(TTFont('WorkSans-Bold', os.path.join(font_dir, 'WorkSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont('Jura-Light', os.path.join(font_dir, 'Jura-Light.ttf')))
pdfmetrics.registerFont(TTFont('SongtiSC', os.path.join(font_dir, 'SongtiSC.ttc'), subfontIndex=0))

# Colors following the Temporal Alchemy philosophy
IVORY = HexColor('#FAF8F5')
WARM_GRAY = HexColor('#E8E4DF')
CHAMPAGNE_GOLD = HexColor('#C9A961')
BRONZE = HexColor('#8B7355')
SOFT_CHARCOAL = HexColor('#4A4A4A')
FADED_GOLD = HexColor('#D4C4A8')
PALE_COPPER = HexColor('#B8997A')

def draw_dna_helix(c, x, y, height, width=40, turns=3, alpha=0.3):
    """Draw a stylized DNA helix as decorative element"""
    c.saveState()
    c.setStrokeColor(CHAMPAGNE_GOLD)
    c.setLineWidth(0.5)

    steps = 60
    for i in range(steps):
        t = i / steps
        y_pos = y + t * height
        offset = math.sin(t * turns * 2 * math.pi) * width/2

        if i > 0:
            prev_t = (i-1) / steps
            prev_y = y + prev_t * height
            prev_offset = math.sin(prev_t * turns * 2 * math.pi) * width/2

            # Draw both strands
            c.setStrokeAlpha(alpha * (0.3 + 0.7 * abs(math.sin(t * turns * 2 * math.pi))))
            c.line(x + prev_offset, prev_y, x + offset, y_pos)
            c.line(x - prev_offset, prev_y, x - offset, y_pos)

            # Draw connecting rungs occasionally
            if i % 5 == 0:
                c.setStrokeAlpha(alpha * 0.5)
                c.line(x - offset, y_pos, x + offset, y_pos)

    c.restoreState()

def draw_molecular_structure(c, cx, cy, radius, nodes=6, alpha=0.4):
    """Draw an abstract molecular structure"""
    c.saveState()
    c.setStrokeColor(BRONZE)
    c.setFillColor(CHAMPAGNE_GOLD)
    c.setStrokeAlpha(alpha)
    c.setFillAlpha(alpha * 0.3)

    # Draw connections
    c.setLineWidth(0.5)
    points = []
    for i in range(nodes):
        angle = i * 2 * math.pi / nodes - math.pi/2
        px = cx + radius * math.cos(angle)
        py = cy + radius * math.sin(angle)
        points.append((px, py))

    # Draw hexagonal bonds
    for i in range(nodes):
        c.line(points[i][0], points[i][1],
               points[(i+1) % nodes][0], points[(i+1) % nodes][1])
        # Connect to center
        c.setStrokeAlpha(alpha * 0.3)
        c.line(cx, cy, points[i][0], points[i][1])
        c.setStrokeAlpha(alpha)

    # Draw nodes
    for px, py in points:
        c.circle(px, py, 3, fill=1, stroke=0)

    # Center node
    c.setFillAlpha(alpha * 0.5)
    c.circle(cx, cy, 4, fill=1, stroke=0)

    c.restoreState()

def draw_concentric_circles(c, cx, cy, max_radius, num_circles=5, alpha=0.2):
    """Draw concentric circles suggesting orbital paths"""
    c.saveState()
    c.setStrokeColor(FADED_GOLD)
    c.setLineWidth(0.3)

    for i in range(1, num_circles + 1):
        r = max_radius * i / num_circles
        c.setStrokeAlpha(alpha * (1 - i / (num_circles + 1)))
        c.circle(cx, cy, r, fill=0, stroke=1)

    c.restoreState()

def draw_time_markers(c, x, y, width, alpha=0.3):
    """Draw subtle time markers like a timeline"""
    c.saveState()
    c.setStrokeColor(BRONZE)
    c.setStrokeAlpha(alpha)
    c.setLineWidth(0.3)

    # Main line
    c.line(x, y, x + width, y)

    # Tick marks
    num_ticks = 12
    for i in range(num_ticks + 1):
        tick_x = x + (width * i / num_ticks)
        tick_height = 3 if i % 4 == 0 else 1.5
        c.line(tick_x, y - tick_height, tick_x, y + tick_height)

    c.restoreState()

def create_book_cover(output_path):
    """Create the main book cover (Cover-0)"""
    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)

    # Background
    c.setFillColor(IVORY)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Subtle gradient overlay at top
    for i in range(50):
        c.setFillColor(WARM_GRAY)
        c.setFillAlpha(0.02 * (1 - i/50))
        c.rect(0, height - i*10, width, 10, fill=1, stroke=0)

    # DNA helix decorative elements (left side)
    draw_dna_helix(c, 60, 150, 500, width=25, turns=4, alpha=0.15)

    # DNA helix (right side, mirrored feel)
    draw_dna_helix(c, width - 60, 200, 450, width=20, turns=3.5, alpha=0.12)

    # Molecular structures scattered
    draw_molecular_structure(c, 100, height - 200, 30, alpha=0.25)
    draw_molecular_structure(c, width - 120, 180, 25, alpha=0.2)
    draw_molecular_structure(c, width/2 + 80, height/2 + 100, 20, alpha=0.15)

    # Concentric circles (suggesting cellular/molecular structure)
    draw_concentric_circles(c, width/2, height/2 - 50, 180, num_circles=7, alpha=0.08)

    # Time markers
    draw_time_markers(c, 80, 120, width - 160, alpha=0.2)
    draw_time_markers(c, 80, height - 100, width - 160, alpha=0.15)

    # Central decorative element - large molecular ring
    c.saveState()
    c.setStrokeColor(CHAMPAGNE_GOLD)
    c.setStrokeAlpha(0.3)
    c.setLineWidth(1)
    c.circle(width/2, height/2, 120, fill=0, stroke=1)
    c.setStrokeAlpha(0.15)
    c.setLineWidth(0.5)
    c.circle(width/2, height/2, 140, fill=0, stroke=1)
    c.circle(width/2, height/2, 100, fill=0, stroke=1)
    c.restoreState()

    # Title - Chinese
    c.setFillColor(SOFT_CHARCOAL)
    c.setFont('SongtiSC', 42)
    title = "重写时间的源代码"
    title_width = c.stringWidth(title, 'SongtiSC', 42)
    c.drawString((width - title_width)/2, height/2 + 20, title)

    # Subtitle / English
    c.setFont('Italiana', 16)
    c.setFillColor(BRONZE)
    subtitle = "REWRITING THE SOURCE CODE OF TIME"
    subtitle_width = c.stringWidth(subtitle, 'Italiana', 16)
    c.drawString((width - subtitle_width)/2, height/2 - 20, subtitle)

    # Genre indicator
    c.setFont('Jura-Light', 11)
    c.setFillColor(PALE_COPPER)
    genre = "科 幻 短 篇 小 说"
    genre_width = c.stringWidth(genre, 'Jura-Light', 11)
    c.drawString((width - genre_width)/2, height/2 - 50, genre)

    # Decorative line under title
    c.setStrokeColor(CHAMPAGNE_GOLD)
    c.setStrokeAlpha(0.5)
    c.setLineWidth(0.5)
    line_width = 200
    c.line((width - line_width)/2, height/2 - 70, (width + line_width)/2, height/2 - 70)

    # Small decorative dots
    c.setFillColor(CHAMPAGNE_GOLD)
    c.setFillAlpha(0.4)
    c.circle((width - line_width)/2 - 10, height/2 - 70, 2, fill=1, stroke=0)
    c.circle((width + line_width)/2 + 10, height/2 - 70, 2, fill=1, stroke=0)

    c.save()
    print(f"Created: {output_path}")

def create_chapter_cover(output_path, chapter_num, chapter_title):
    """Create a chapter cover"""
    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)

    # Background
    c.setFillColor(IVORY)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Subtle texture overlay
    for i in range(30):
        c.setFillColor(WARM_GRAY)
        c.setFillAlpha(0.015 * (1 - i/30))
        c.rect(0, height - i*15, width, 15, fill=1, stroke=0)

    # Single DNA helix on one side (varies by chapter)
    if chapter_num % 2 == 1:
        draw_dna_helix(c, 50, 100, 400, width=20, turns=3, alpha=0.12)
    else:
        draw_dna_helix(c, width - 50, 150, 380, width=18, turns=2.5, alpha=0.12)

    # Molecular structure
    positions = [
        (width - 100, height - 180),
        (100, 150),
        (width - 80, 200),
        (120, height - 150),
        (width/2 + 100, 180)
    ]
    pos = positions[chapter_num - 1]
    draw_molecular_structure(c, pos[0], pos[1], 25, alpha=0.2)

    # Concentric circles (smaller for chapter covers)
    draw_concentric_circles(c, width/2, height/2, 100, num_circles=4, alpha=0.06)

    # Chapter number - large and elegant
    c.setFont('Italiana', 72)
    c.setFillColor(CHAMPAGNE_GOLD)
    c.setFillAlpha(0.3)
    num_str = f"0{chapter_num}"
    num_width = c.stringWidth(num_str, 'Italiana', 72)
    c.drawString((width - num_width)/2, height/2 + 80, num_str)

    # Chapter indicator
    c.setFillAlpha(1)
    c.setFont('Jura-Light', 12)
    c.setFillColor(PALE_COPPER)
    chapter_label = f"第 {chapter_num} 章"
    label_width = c.stringWidth(chapter_label, 'Jura-Light', 12)
    c.drawString((width - label_width)/2, height/2 + 30, chapter_label)

    # Chapter title
    c.setFont('SongtiSC', 28)
    c.setFillColor(SOFT_CHARCOAL)
    title_width = c.stringWidth(chapter_title, 'SongtiSC', 28)
    c.drawString((width - title_width)/2, height/2 - 20, chapter_title)

    # Decorative line
    c.setStrokeColor(CHAMPAGNE_GOLD)
    c.setStrokeAlpha(0.4)
    c.setLineWidth(0.5)
    line_width = 150
    c.line((width - line_width)/2, height/2 - 50, (width + line_width)/2, height/2 - 50)

    # Book title at bottom
    c.setFont('SongtiSC', 11)
    c.setFillColor(BRONZE)
    c.setFillAlpha(0.6)
    book_title = "重写时间的源代码"
    bt_width = c.stringWidth(book_title, 'SongtiSC', 11)
    c.drawString((width - bt_width)/2, 60, book_title)

    # Time marker at bottom
    draw_time_markers(c, 100, 40, width - 200, alpha=0.15)

    c.save()
    print(f"Created: {output_path}")

if __name__ == "__main__":
    base_dir = "/Users/szou/Python/Playground/StoryWriter/重写时间的源代码/chapters"

    # Create book cover
    create_book_cover(os.path.join(base_dir, "Cover-0.pdf"))

    # Chapter titles
    chapters = [
        (1, "完美候选"),
        (2, "验证"),
        (3, "对峙"),
        (4, "失控"),
        (5, "余响")
    ]

    # Create chapter covers
    for num, title in chapters:
        create_chapter_cover(os.path.join(base_dir, f"Cover-{num}.pdf"), num, title)
