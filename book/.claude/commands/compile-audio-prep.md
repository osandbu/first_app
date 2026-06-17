Prepare clean plain-text files from all final chapters for ElevenLabs audiobook generation.

ElevenLabs Projects expects clean prose — no Markdown syntax, no headers with `#`,
no bold/italic markers. This command strips all of that and saves one `.txt` file per
chapter, plus a single combined file for uploading as a full project.

Steps:
1. Create `book/output/audio/` if it doesn't exist.
2. For each final chapter file (in narrative order — see below), read
   `book/content/{id}_final.md` and apply these transformations:
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
3. Save the cleaned text to `book/output/audio/{id}.txt`
4. After processing all chapters, concatenate all `.txt` files in narrative order into
   `book/output/audio/full_audiobook.txt` with `\n\n---\n\n` between chapters.
5. Report: chapters processed, total word count, and estimated listening time
   (average audiobook pace is ~150 words per minute).

## Narrative chapter order and titles

1.  p1_c1  — Every Executive Just Got a Team of Geniuses
2.  p1_c2  — The End of Information Scarcity
3.  p1_c3  — From Knowledge Work to Judgment Work
4.  p1_c4  — Why Organizations Change More Slowly Than Technology
5.  p2_strategy    — Strategy
6.  p2_product     — Product
7.  p2_engineering — Engineering
8.  p2_finance     — Finance
9.  p2_marketing   — Marketing
10. p2_sales       — Sales
11. p2_hr          — HR
12. p2_legal       — Legal
13. p2_cs          — Customer Success
14. p3_operating   — AI-First Operating Models
15. p3_colleagues  — AI Agents as Digital Colleagues
16. p3_governance  — Governance and Risk
17. p3_org_design  — Organizational Design
18. p3_culture     — Building an AI Culture
19. p3_measurement — Measuring AI Adoption
20. p4_obsolete    — What Skills Become Obsolete
21. p4_valuable    — What Becomes More Valuable
22. p4_careers     — How Careers Evolve
23. p4_boards      — What Boards Will Expect
24. p4_exceptional — What Will Distinguish Exceptional Leaders

## Notes
- Skip any chapter whose `_final.md` doesn't exist yet; report it as missing.
- The per-chapter `.txt` files are ideal for ElevenLabs Projects "upload chapters"
  workflow. The `full_audiobook.txt` works for a single-project upload.
- ElevenLabs recommends keeping individual segments under ~50,000 characters;
  warn if any chapter exceeds this.
