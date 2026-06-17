Compile all final chapter files into a Kindle-ready EPUB.

Steps:
1. Create `book/output/` if it doesn't exist
2. Check which `_final.md` files exist in `book/content/`. Warn about any missing finals
   but continue with what's available.
3. Concatenate the final files in narrative order (see below), adding a blank line and
   a `---` page-break marker between chapters.
4. Write the combined file to `book/output/manuscript.md`
5. Run pandoc to produce the EPUB:

```
pandoc book/output/manuscript.md \
  --output book/output/book.epub \
  --metadata title="The AI-Native Executive" \
  --metadata author="[Author]" \
  --metadata lang="en-US" \
  --toc \
  --toc-depth=1 \
  --epub-chapter-level=1
```

6. Report the output file size and which chapters were included vs. missing.

## Narrative chapter order

Part I — A New Era:
  p1_c1, p1_c2, p1_c3, p1_c4

Part II — Rewriting the Executive Playbook:
  p2_strategy, p2_product, p2_engineering, p2_finance, p2_marketing,
  p2_sales, p2_hr, p2_legal, p2_cs

Part III — Becoming an AI-Native Company:
  p3_operating, p3_colleagues, p3_governance, p3_org_design, p3_culture, p3_measurement

Part IV — The Executive of 2035:
  p4_obsolete, p4_valuable, p4_careers, p4_boards, p4_exceptional

## Notes
- Use `pandoc --version` first to confirm pandoc is installed. If not, install it with
  `apt-get install -y pandoc` (or `brew install pandoc` on Mac) and then proceed.
- The EPUB can be uploaded directly to Amazon KDP — no MOBI conversion needed.
- If a cover image exists at `book/assets/cover.jpg`, add `--epub-cover-image=book/assets/cover.jpg` to the pandoc command.
