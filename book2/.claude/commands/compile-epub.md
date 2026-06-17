Compile all final chapter files into a Kindle-ready EPUB.

Steps:
1. Create `book2/output/` if it doesn't exist
2. Check which `_final.md` files exist in `book2/content/`. Warn about any missing finals
   but continue with what's available.
3. Concatenate the final files in narrative order (see below), adding a blank line and
   a `---` page-break marker between chapters.
4. Write the combined file to `book2/output/manuscript.md`
5. Run pandoc to produce the EPUB:

```
pandoc book2/output/manuscript.md \
  --output book2/output/book.epub \
  --metadata title="Engineering Beyond Code" \
  --metadata author="[Author]" \
  --metadata lang="en-US" \
  --toc \
  --toc-depth=1 \
  --epub-chapter-level=1
```

6. Report the output file size and which chapters were included vs. missing.

## Narrative chapter order

Part I — The Hidden Curriculum:
  p1_c1, p1_c2, p1_c3

Part II — Incentives and Behavior:
  p2_c1, p2_c2, p2_c3, p2_c4, p2_c5

Part III — Organizations as Systems:
  p3_c1, p3_c2, p3_c3, p3_c4, p3_c5

Part IV — The Work Nobody Teaches:
  p4_c1, p4_c2, p4_c3, p4_c4, p4_c5, p4_c6

Part V — Leadership Without the Title:
  p5_c1, p5_c2, p5_c3, p5_c4, p5_c5, p5_c6

## Notes
- Use `pandoc --version` first to confirm pandoc is installed. If not, install it with
  `apt-get install -y pandoc` (or `brew install pandoc` on Mac) and then proceed.
- The EPUB can be uploaded directly to Amazon KDP — no MOBI conversion needed.
- If a cover image exists at `book2/assets/cover.jpg`, add `--epub-cover-image=book2/assets/cover.jpg` to the pandoc command.
