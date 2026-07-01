#!/usr/bin/env python3
"""Compile all final chapters into a single PDF."""

import re
import sys
from pathlib import Path

BOOK_ROOT = Path(__file__).parent.parent
CONTENT = BOOK_ROOT / "content"
OUTPUT = BOOK_ROOT / "engineering_beyond_code.pdf"

PARTS = [
    ("Part I — The Hidden Curriculum", ["p1_c1", "p1_c2", "p1_c3"]),
    ("Part II — Incentives and Behavior", ["p2_c1", "p2_c2", "p2_c3", "p2_c4", "p2_c5"]),
    ("Part III — Organizations as Systems", ["p3_c1", "p3_c2", "p3_c3", "p3_c4", "p3_c5"]),
    ("Part IV — The Work Nobody Teaches", ["p4_c1", "p4_c2", "p4_c3", "p4_c4", "p4_c5", "p4_c6"]),
    ("Part V — Leadership Without the Title", ["p5_c1", "p5_c2", "p5_c3", "p5_c4", "p5_c5", "p5_c6"]),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;600&display=swap');

@page {
    margin: 1.2in 1.1in 1.2in 1.1in;
    @bottom-center {
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #888;
    }
}

@page :first {
    @bottom-center { content: none; }
}

* { box-sizing: border-box; }

body {
    font-family: 'Merriweather', Georgia, serif;
    font-size: 11pt;
    line-height: 1.75;
    color: #1a1a1a;
    max-width: 100%;
}

/* Title page */
.title-page {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 85vh;
    text-align: center;
    padding: 2in 0;
}

.title-page h1 {
    font-family: 'Inter', sans-serif;
    font-size: 28pt;
    font-weight: 600;
    letter-spacing: -0.5px;
    color: #111;
    margin: 0 0 0.3in 0;
    border: none;
}

.title-page .subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 13pt;
    font-weight: 400;
    color: #555;
    margin: 0;
}

/* Table of contents */
.toc {
    page-break-after: always;
}

.toc h2 {
    font-family: 'Inter', sans-serif;
    font-size: 11pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #888;
    border: none;
    margin-bottom: 0.4in;
}

.toc-part {
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #888;
    margin: 0.25in 0 0.1in 0;
}

.toc-entry {
    font-family: 'Inter', sans-serif;
    font-size: 10.5pt;
    color: #222;
    padding: 3px 0;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #ddd;
    margin-bottom: 4px;
}

.toc-entry .toc-num {
    color: #aaa;
    font-size: 9pt;
    margin-right: 0.15in;
    flex-shrink: 0;
}

/* Part divider */
.part-divider {
    page-break-before: always;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 70vh;
}

.part-divider .part-label {
    font-family: 'Inter', sans-serif;
    font-size: 9pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: #aaa;
    margin-bottom: 0.2in;
}

.part-divider h2 {
    font-family: 'Inter', sans-serif;
    font-size: 22pt;
    font-weight: 600;
    color: #111;
    border: none;
    line-height: 1.3;
    margin: 0;
}

/* Chapter */
.chapter {
    page-break-before: always;
}

h1 {
    font-family: 'Inter', sans-serif;
    font-size: 19pt;
    font-weight: 600;
    color: #111;
    line-height: 1.3;
    margin: 0 0 0.4in 0;
    border-bottom: 2px solid #111;
    padding-bottom: 0.15in;
}

h2 {
    font-family: 'Inter', sans-serif;
    font-size: 11pt;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: #555;
    margin: 0.5in 0 0.15in 0;
    border: none;
}

h3 {
    font-family: 'Inter', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #333;
    margin: 0.3in 0 0.1in 0;
}

p {
    margin: 0 0 0.9em 0;
    orphans: 3;
    widows: 3;
}

blockquote {
    border-left: 3px solid #ddd;
    margin: 1.2em 0 1.2em 0;
    padding: 0.1em 0 0.1em 1.2em;
    color: #444;
    font-style: italic;
}

blockquote p { margin-bottom: 0.4em; }

strong { font-weight: 700; color: #111; }

em { font-style: italic; }

ul, ol {
    margin: 0.5em 0 1em 0;
    padding-left: 1.5em;
}

li {
    margin-bottom: 0.4em;
    line-height: 1.7;
}

hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 1.5em 0;
}

code {
    font-family: 'Courier New', monospace;
    font-size: 9.5pt;
    background: #f5f5f5;
    padding: 1px 4px;
    border-radius: 2px;
}
"""


def parse_chapter_title(md: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def md_to_html(md: str) -> str:
    """Minimal markdown-to-HTML for the chapter body (after stripping the h1)."""
    lines = md.splitlines()
    # Strip the leading h1
    body_lines = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.startswith("# "):
            skipped_h1 = True
            continue
        body_lines.append(line)
    md = "\n".join(body_lines).strip()

    try:
        import markdown
        return markdown.markdown(md, extensions=["extra", "sane_lists"])
    except ImportError:
        pass

    # Fallback: basic conversion
    html = []
    in_blockquote = False
    in_ul = False
    in_ol = False
    para_lines = []

    def flush_para():
        if para_lines:
            text = " ".join(para_lines).strip()
            if text:
                html.append(f"<p>{inline(text)}</p>")
            para_lines.clear()

    def inline(text):
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        return text

    for line in md.splitlines():
        if line.startswith("### "):
            flush_para()
            html.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_para()
            html.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            flush_para()
            html.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.startswith("> "):
            flush_para()
            if not in_blockquote:
                html.append("<blockquote>")
                in_blockquote = True
            html.append(f"<p>{inline(line[2:])}</p>")
        elif line.startswith("- ") or line.startswith("* "):
            flush_para()
            if not in_ul:
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{inline(line[2:])}</li>")
        elif re.match(r'^\d+\. ', line):
            flush_para()
            if not in_ol:
                html.append("<ol>")
                in_ol = True
            item_text = re.sub(r'^\d+\. ', '', line)
            html.append(f"<li>{inline(item_text)}</li>")
        elif line.strip() == "---" or line.strip() == "***":
            flush_para()
            html.append("<hr>")
        elif line.strip() == "":
            if in_blockquote:
                html.append("</blockquote>")
                in_blockquote = False
            if in_ul:
                html.append("</ul>")
                in_ul = False
            if in_ol:
                html.append("</ol>")
                in_ol = False
            flush_para()
        else:
            para_lines.append(line)

    flush_para()
    if in_blockquote:
        html.append("</blockquote>")
    if in_ul:
        html.append("</ul>")
    if in_ol:
        html.append("</ol>")

    return "\n".join(html)


def build_html():
    sections = []

    # Title page
    sections.append("""
<div class="title-page">
  <h1>Engineering Beyond Code</h1>
  <p class="subtitle">The curriculum CS education skips</p>
</div>
""")

    # Collect chapter info for TOC
    toc_entries = []
    chapter_num = 0
    for part_title, chapter_ids in PARTS:
        toc_entries.append(("part", part_title, None))
        for cid in chapter_ids:
            chapter_num += 1
            path = CONTENT / f"{cid}_final.md"
            text = path.read_text()
            title = parse_chapter_title(text)
            toc_entries.append(("chapter", title, chapter_num))

    # TOC
    toc_html = ['<div class="toc"><h2>Contents</h2>']
    for kind, title, num in toc_entries:
        if kind == "part":
            # Strip "Part N — " prefix for display
            label = re.sub(r'^Part [IVX]+ — ', '', title)
            toc_html.append(f'<div class="toc-part">{title}</div>')
        else:
            toc_html.append(
                f'<div class="toc-entry">'
                f'<span><span class="toc-num">{num:02d}</span>{title}</span>'
                f'</div>'
            )
    toc_html.append("</div>")
    sections.append("\n".join(toc_html))

    # Parts and chapters
    chapter_num = 0
    for part_idx, (part_title, chapter_ids) in enumerate(PARTS):
        part_num_roman = ["I", "II", "III", "IV", "V"][part_idx]
        part_subtitle = re.sub(r'^Part [IVX]+ — ', '', part_title)
        sections.append(f"""
<div class="part-divider">
  <div class="part-label">Part {part_num_roman}</div>
  <h2>{part_subtitle}</h2>
</div>
""")
        for cid in chapter_ids:
            chapter_num += 1
            path = CONTENT / f"{cid}_final.md"
            text = path.read_text()
            title = parse_chapter_title(text)
            body = md_to_html(text)
            sections.append(f"""
<div class="chapter">
  <h1>{title}</h1>
  {body}
</div>
""")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Engineering Beyond Code</title>
<style>{CSS}</style>
</head>
<body>
{"".join(sections)}
</body>
</html>"""
    return html


def main():
    print("Building HTML...")
    html = build_html()

    html_path = BOOK_ROOT / "engineering_beyond_code.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"HTML written to {html_path}")

    print("Converting to PDF (this may take a moment)...")
    try:
        from weasyprint import HTML
        HTML(string=html, base_url=str(BOOK_ROOT)).write_pdf(str(OUTPUT))
        size_mb = OUTPUT.stat().st_size / 1_048_576
        print(f"PDF written to {OUTPUT} ({size_mb:.1f} MB)")
    except Exception as e:
        print(f"PDF generation failed: {e}", file=sys.stderr)
        print("HTML is available for manual conversion.")
        sys.exit(1)


if __name__ == "__main__":
    main()
