Compile all final chapter files into a print-ready PDF.

Steps:
1. Create `book/output/` if it doesn't exist.
2. Check which `_final.md` files exist in `book/content/`. Warn about any missing finals
   but continue with what's available.
3. Concatenate the final files in narrative order (see below). Between chapters, insert:
   - A blank line
   - `\newpage` (so each chapter starts on a fresh page in the PDF)
4. Prepend a title page block at the very top of the combined file:
   ```
   ---
   title: "The AI-Native Executive"
   subtitle: "How to Lead When AI Does the Work"
   author: "[Author]"
   date: ""
   documentclass: book
   fontsize: 11pt
   geometry: "margin=1.25in"
   linestretch: 1.4
   colorlinks: true
   ---
   ```
5. Write the combined file to `book/output/manuscript.md`
6. Check whether `pandoc` is installed (`pandoc --version`). If not, install it:
   `apt-get install -y pandoc`
7. Check whether a LaTeX engine is available (`xelatex --version` or `pdflatex --version`).
   If not, install: `apt-get install -y texlive-xetex texlive-fonts-recommended`
8. Run pandoc:
   ```
   pandoc book/output/manuscript.md \
     --output book/output/book.pdf \
     --pdf-engine=xelatex \
     --toc \
     --toc-depth=1 \
     --number-sections
   ```
9. Report the output file size and page count (`pdfinfo book/output/book.pdf` if available),
   and list which chapters were included vs. missing.

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
- xelatex produces better typography than pdflatex for body text; prefer it.
- If a cover image exists at `book/assets/cover.jpg`, insert it after the title block.
- If LaTeX installation is too large for the environment, fall back to:
  `--pdf-engine=weasyprint` (install with `pip install weasyprint`) or
  `--pdf-engine=wkhtmltopdf` (install with `apt-get install -y wkhtmltopdf`).
