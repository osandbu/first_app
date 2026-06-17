#!/usr/bin/env python3
"""Compile final chapter files into clean plain-text for ElevenLabs audiobook generation."""

import re
import os

CONTENT_DIR = os.path.join(os.path.dirname(__file__), '..', 'content')
AUDIO_DIR = os.path.join(os.path.dirname(__file__), '..', 'output', 'audio')

CHAPTERS = [
    ('p1_c1',  1,  'Nobody Told You This Was the Job'),
    ('p1_c2',  2,  'The Org Chart Is a Lie'),
    ('p1_c3',  3,  'Your Mental Model of a Company Is Wrong'),
    ('p2_c1',  4,  'Everyone Is Rational, Given Their Incentives'),
    ('p2_c2',  5,  'How Compensation Shapes What Gets Built'),
    ('p2_c3',  6,  'The Principal-Agent Problem Is Everywhere'),
    ('p2_c4',  7,  'Metrics Eat Culture'),
    ('p2_c5',  8,  'Why Good Engineers Do Bad Things'),
    ('p3_c1',  9,  "Conway's Law Is Not a Metaphor"),
    ('p3_c2',  10, 'The Coordination Tax'),
    ('p3_c3',  11, 'Team Topologies and Why They Matter'),
    ('p3_c4',  12, 'The Communication Architecture You Actually Have'),
    ('p3_c5',  13, 'Why Reorgs Rarely Work'),
    ('p4_c1',  14, 'How Decisions Actually Get Made'),
    ('p4_c2',  15, 'The Written Word Is Infrastructure'),
    ('p4_c3',  16, 'Technical Debt Is a Financial Concept'),
    ('p4_c4',  17, 'Build vs. Buy Is a Strategy Question'),
    ('p4_c5',  18, 'Cost of Delay: The Number Nobody Calculates'),
    ('p4_c6',  19, 'Platform Thinking for People Who Build Platforms'),
    ('p5_c1',  20, 'Influence Without Authority Is a Skill'),
    ('p5_c2',  21, 'The Multiplier Effect'),
    ('p5_c3',  22, 'What Staff Engineers Actually Do'),
    ('p5_c4',  23, 'The First Ninety Days as a Manager'),
    ('p5_c5',  24, 'Leading Through Ambiguity'),
    ('p5_c6',  25, 'The Feedback Nobody Wants to Give'),
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
