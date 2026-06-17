Prepare clean plain-text files from all final chapters for ElevenLabs audiobook generation.

ElevenLabs Projects expects clean prose — no Markdown syntax, no headers with `#`,
no bold/italic markers. This command strips all of that and saves one `.txt` file per
chapter, plus a single combined file for uploading as a full project.

Steps:
1. Create `book2/output/audio/` if it doesn't exist.
2. For each final chapter file (in narrative order — see below), read
   `book2/content/{id}_final.md` and apply these transformations:
   - Remove ATX headers: replace `## Section Title` with `\n\nSection Title\n\n`
     (keep the title as a plain-text paragraph so the narrator has natural pause points)
   - Remove setext headers (underline style) similarly
   - Strip bold: `**text**` → `text`
   - Strip italic: `*text*` or `_text_` → `text`
   - Remove horizontal rules (`---`, `***`, `___`) entirely
   - Remove blockquote markers: `> text` → `text`
   - Remove inline code backticks: `` `text` `` → `text`
   - Remove fenced code blocks entirely (they shouldn't appear in final chapters)
   - Collapse 3+ consecutive blank lines into 2
   - Add a chapter heading line at the top: `Chapter [N]: [Full Title]` followed by two blank lines
3. Save the cleaned text to `book2/output/audio/{id}.txt`
4. After processing all chapters, concatenate all `.txt` files in narrative order into
   `book2/output/audio/full_audiobook.txt` with `\n\n---\n\n` between chapters.
5. Report: chapters processed, total word count, and estimated listening time
   (average audiobook pace is ~150 words per minute).

Alternatively, run the script directly:
```
python3 book2/scripts/compile_audio.py
```

## Narrative chapter order and titles

1.  p1_c1  — Nobody Told You This Was the Job
2.  p1_c2  — The Org Chart Is a Lie
3.  p1_c3  — Your Mental Model of a Company Is Wrong
4.  p2_c1  — Everyone Is Rational, Given Their Incentives
5.  p2_c2  — How Compensation Shapes What Gets Built
6.  p2_c3  — The Principal-Agent Problem Is Everywhere
7.  p2_c4  — Metrics Eat Culture
8.  p2_c5  — Why Good Engineers Do Bad Things
9.  p3_c1  — Conway's Law Is Not a Metaphor
10. p3_c2  — The Coordination Tax
11. p3_c3  — Team Topologies and Why They Matter
12. p3_c4  — The Communication Architecture You Actually Have
13. p3_c5  — Why Reorgs Rarely Work
14. p4_c1  — How Decisions Actually Get Made
15. p4_c2  — The Written Word Is Infrastructure
16. p4_c3  — Technical Debt Is a Financial Concept
17. p4_c4  — Build vs. Buy Is a Strategy Question
18. p4_c5  — Cost of Delay: The Number Nobody Calculates
19. p4_c6  — Platform Thinking for People Who Build Platforms
20. p5_c1  — Influence Without Authority Is a Skill
21. p5_c2  — The Multiplier Effect
22. p5_c3  — What Staff Engineers Actually Do
23. p5_c4  — The First Ninety Days as a Manager
24. p5_c5  — Leading Through Ambiguity
25. p5_c6  — The Feedback Nobody Wants to Give

## Notes
- Skip any chapter whose `_final.md` doesn't exist yet; report it as missing.
- The per-chapter `.txt` files are ideal for ElevenLabs Projects "upload chapters"
  workflow. The `full_audiobook.txt` works for a single-project upload.
- ElevenLabs recommends keeping individual segments under ~50,000 characters;
  warn if any chapter exceeds this.
