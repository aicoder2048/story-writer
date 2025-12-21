#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown",
#     "weasyprint",
# ]
# ///
"""
Markdown to PDF converter with Chinese font support and vintage paper style.

Usage:
    uv run md2pdf.py input.md output.pdf [--style style.css] [--title "Title"]

    # Or make executable and run directly:
    chmod +x md2pdf.py
    ./md2pdf.py input.md output.pdf
"""

import os
import sys
from pathlib import Path

# macOS: Ensure library path is set for WeasyPrint
# DYLD_LIBRARY_PATH must be set before process starts, so re-exec if needed
if sys.platform == "darwin":
    homebrew_lib = "/opt/homebrew/lib"
    current_path = os.environ.get("DYLD_LIBRARY_PATH", "")

    if Path(homebrew_lib).exists() and homebrew_lib not in current_path:
        # Re-execute with correct library path
        os.environ["DYLD_LIBRARY_PATH"] = f"{homebrew_lib}:{current_path}" if current_path else homebrew_lib
        os.execv(sys.executable, [sys.executable] + sys.argv)

import argparse

import markdown
from weasyprint import HTML, CSS


# Default CSS style - vintage paper look with Chinese font support
DEFAULT_CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm;
    background-color: #FAF6F0;

    @bottom-center {
        content: counter(page);
        font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", serif;
        font-size: 10pt;
        color: #6B5344;
    }
}

body {
    font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", "STSong", "SimSun", serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #4A3728;
    background-color: #FAF6F0;
    text-align: justify;
}

h1 {
    font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", serif;
    font-size: 24pt;
    font-weight: bold;
    color: #3D2B1F;
    margin-top: 0;
    margin-bottom: 1.5em;
    text-align: left;
    border-bottom: none;
}

h2 {
    font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", serif;
    font-size: 18pt;
    font-weight: bold;
    color: #3D2B1F;
    margin-top: 1.5em;
    margin-bottom: 0.8em;
}

h3 {
    font-family: "Noto Serif SC", "Source Han Serif SC", "Songti SC", serif;
    font-size: 14pt;
    font-weight: bold;
    color: #3D2B1F;
    margin-top: 1.2em;
    margin-bottom: 0.6em;
}

p {
    margin-bottom: 1em;
    text-indent: 2em;
}

/* First paragraph after heading - no indent */
h1 + p, h2 + p, h3 + p, hr + p {
    text-indent: 0;
}

/* Blockquote styling */
blockquote {
    margin: 1.5em 2em;
    padding: 0.5em 1em;
    border-left: 3px solid #8B7355;
    color: #5D4E37;
    font-style: italic;
    background-color: rgba(139, 115, 85, 0.1);
}

/* Horizontal rule - section divider */
hr {
    border: none;
    border-top: 1px solid #C4B5A5;
    margin: 2em auto;
    width: 40%;
}

/* Code blocks */
code {
    font-family: "Source Code Pro", "Menlo", monospace;
    font-size: 10pt;
    background-color: rgba(139, 115, 85, 0.15);
    padding: 0.2em 0.4em;
    border-radius: 3px;
}

pre {
    background-color: rgba(139, 115, 85, 0.1);
    padding: 1em;
    border-radius: 5px;
    overflow-x: auto;
    line-height: 1.4;
}

pre code {
    background-color: transparent;
    padding: 0;
}

/* Lists */
ul, ol {
    margin-bottom: 1em;
    padding-left: 2em;
}

li {
    margin-bottom: 0.3em;
}

/* Links */
a {
    color: #6B5344;
    text-decoration: none;
    border-bottom: 1px dotted #6B5344;
}

/* Strong and emphasis */
strong {
    font-weight: bold;
    color: #3D2B1F;
}

em {
    font-style: italic;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
}

th, td {
    border: 1px solid #C4B5A5;
    padding: 0.5em 1em;
    text-align: left;
}

th {
    background-color: rgba(139, 115, 85, 0.2);
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: rgba(139, 115, 85, 0.05);
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
}

/* Dialog styling - for quoted speech */
p:has(> :first-child:is(strong)):has(+ blockquote) {
    margin-bottom: 0.5em;
}
"""


def convert_md_to_pdf(
    input_path: str,
    output_path: str,
    custom_css: str = None,
    title: str = None
) -> bool:
    """
    Convert a Markdown file to PDF.

    Args:
        input_path: Path to the input Markdown file
        output_path: Path for the output PDF file
        custom_css: Optional path to custom CSS file
        title: Optional document title

    Returns:
        True if conversion successful, False otherwise
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return False

    # Read markdown content
    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'sane_lists', 'smarty'])
    html_content = md.convert(md_content)

    # Determine title
    if not title:
        # Try to extract title from first h1
        lines = md_content.split('\n')
        for line in lines:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:
            title = input_path.stem

    # Build full HTML document
    html_doc = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
{html_content}
</body>
</html>
"""

    # Determine CSS to use
    css_content = DEFAULT_CSS
    if custom_css:
        css_path = Path(custom_css)
        if css_path.exists():
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
        else:
            print(f"Warning: Custom CSS file not found: {css_path}, using default style")

    # Convert to PDF
    try:
        html = HTML(string=html_doc, base_url=str(input_path.parent))
        css = CSS(string=css_content)
        html.write_pdf(output_path, stylesheets=[css])
        print(f"Successfully created: {output_path}")
        return True
    except Exception as e:
        print(f"Error creating PDF: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to PDF with Chinese font support'
    )
    parser.add_argument('input', help='Input Markdown file')
    parser.add_argument('output', help='Output PDF file')
    parser.add_argument('--style', '-s', help='Custom CSS style file')
    parser.add_argument('--title', '-t', help='Document title')

    args = parser.parse_args()

    success = convert_md_to_pdf(
        args.input,
        args.output,
        custom_css=args.style,
        title=args.title
    )

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
