#!/usr/bin/env python3
"""Compile final chapter files into clean plain-text for ElevenLabs audiobook generation."""

import re
import os

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'content')
AUDIO_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'audio')

CHAPTERS = [
    ('p1_c1',        1,  'Every Executive Just Got a Team of Geniuses'),
    ('p1_c2',        2,  'The End of Information Scarcity'),
    ('p1_c3',        3,  'From Knowledge Work to Judgment Work'),
    ('p1_c4',        4,  'Why Organizations Change More Slowly Than Technology'),
    ('p2_strategy',  5,  'Strategy'),
    ('p2_product',   6,  'Product'),
    ('p2_engineering',7, 'Engineering'),
    ('p2_finance',   8,  'Finance'),
    ('p2_marketing', 9,  'Marketing'),
    ('p2_sales',     10, 'Sales'),
    ('p2_hr',        11, 'HR'),
    ('p2_legal',     12, 'Legal'),
    ('p2_cs',        13, 'Customer Success'),
    ('p3_operating', 14, 'AI-First Operating Models'),
    ('p3_colleagues',15, 'AI Agents as Digital Colleagues'),
    ('p3_governance',16, 'Governance and Risk'),
    ('p3_org_design',17, 'Organizational Design'),
    ('p3_culture',   18, 'Building an AI Culture'),
    ('p3_measurement',19,'Measuring AI Adoption'),
    ('p4_obsolete',  20, 'What Skills Become Obsolete'),
    ('p4_valuable',  21, 'What Becomes More Valuable'),
    ('p4_careers',   22, 'How Careers Evolve'),
    ('p4_boards',    23, 'What Boards Will Expect'),
    ('p4_exceptional',24,'What Will Distinguish Exceptional Leaders'),
]

CHAR_LIMIT = 50_000


def clean_markdown(text, chapter_num, chapter_title):
    # Remove fenced code blocks entirely
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'~~~[\s\S]*?~~~', '', text)

    # Remove setext-style headers (underline with = or -)
    text = re.sub(r'^(.+)\n[=]{2,}\s*$', r'\n\n\1\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'^(.+)\n[-]{2,}\s*$', r'\n\n\1\n\n', text, flags=re.MULTILINE)

    # Remove ATX headers (# ## ### etc.) — keep title text as plain paragraph
    text = re.sub(r'^#{1,6}\s+(.+)$', r'\n\n\1\n\n', text, flags=re.MULTILINE)

    # Remove horizontal rules
    text = re.sub(r'^(---+|\*\*\*+|___+)\s*$', '', text, flags=re.MULTILINE)

    # Remove blockquote markers
    text = re.sub(r'^>\s?', '', text, flags=re.MULTILINE)

    # Strip bold and italic: ***text***, **text**, *text*, __text__, _text_
    text = re.sub(r'\*{3}(.+?)\*{3}', r'\1', text)
    text = re.sub(r'\*{2}(.+?)\*{2}', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_{2}(.+?)_{2}', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)

    # Remove inline code backticks
    text = re.sub(r'`(.+?)`', r'\1', text)

    # Collapse 3+ consecutive blank lines to 2
    text = re.sub(r'\n{3,}', '\n\n', text)

    # Prepend chapter heading
    heading = f"Chapter {chapter_num}: {chapter_title}"
    text = heading + '\n\n' + text.strip() + '\n'

    return text


def word_count(text):
    return len(text.split())


def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)

    processed = []
    missing = []
    all_texts = []
    total_words = 0

    for chapter_id, num, title in CHAPTERS:
        src = os.path.join(CONTENT_DIR, f'{chapter_id}_final.md')
        dst = os.path.join(AUDIO_DIR, f'{chapter_id}.txt')

        if not os.path.exists(src):
            print(f"  MISSING: {src}")
            missing.append((num, title))
            continue

        with open(src, encoding='utf-8') as f:
            raw = f.read()

        cleaned = clean_markdown(raw, num, title)
        char_count = len(cleaned)
        words = word_count(cleaned)
        total_words += words

        with open(dst, 'w', encoding='utf-8') as f:
            f.write(cleaned)

        warn = ' *** EXCEEDS 50k char limit' if char_count > CHAR_LIMIT else ''
        print(f"  Chapter {num:2d}: {title:<45} {words:>5} words  {char_count:>6} chars{warn}")
        processed.append((chapter_id, cleaned))
        all_texts.append(cleaned)

    # Write combined file
    combined_path = os.path.join(AUDIO_DIR, 'full_audiobook.txt')
    with open(combined_path, 'w', encoding='utf-8') as f:
        f.write('\n\n---\n\n'.join(all_texts))

    minutes = total_words / 150
    hours = int(minutes // 60)
    mins = int(minutes % 60)

    print()
    print(f"Chapters processed : {len(processed)}")
    if missing:
        print(f"Chapters missing   : {len(missing)} — {', '.join(t for _, t in missing)}")
    print(f"Total word count   : {total_words:,}")
    print(f"Estimated duration : ~{hours}h {mins}m  (at 150 wpm)")
    print(f"Output directory   : {os.path.abspath(AUDIO_DIR)}")
    print(f"Combined file      : {combined_path}")


if __name__ == '__main__':
    main()
