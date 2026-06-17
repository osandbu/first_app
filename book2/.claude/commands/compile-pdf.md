Compile all final chapter files into a print-ready PDF.

Steps:
1. Create `book2/output/` if it doesn't exist.
2. Check which `_final.md` files exist in `book2/content/`. Warn about any missing finals
   but continue with what's available.
3. Concatenate the final files in narrative order (see below). Between chapters, insert:
   - A blank line
   - `\newpage` (so each chapter starts on a fresh page in the PDF)
4. Prepend a title page block at the very top of the combined file:
   ```
   ---
   title: "Engineering Beyond Code"
   subtitle: "Not another software engineering book."
   author: "[Author]"
   date: ""
   documentclass: book
   fontsize: 11pt
   geometry: "margin=1.25in"
   linestretch: 1.4
   colorlinks: true
   ---
   ```
5. Write the combined file to `book2/output/manuscript.md`
6. Check whether `pandoc` is installed (`pandoc --version`). If not, install it:
   `apt-get install -y pandoc`
7. Check whether a LaTeX engine is available (`xelatex --version` or `pdflatex --version`).
   If not, install: `apt-get install -y texlive-xetex texlive-fonts-recommended`
8. Run pandoc:
   ```
   pandoc book2/output/manuscript.md \
     --output book2/output/book.pdf \
     --pdf-engine=xelatex \
     --toc \
     --toc-depth=1 \
     --number-sections
   ```
9. Report the output file size and page count (`pdfinfo book2/output/book.pdf` if available),
   and list which chapters were included vs. missing.

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
- xelatex produces better typography than pdflatex for body text; prefer it.
- If a cover image exists at `book2/assets/cover.jpg`, insert it after the title block.
- If LaTeX installation is too large for the environment, fall back to:
  `--pdf-engine=weasyprint` (install with `pip install weasyprint`) or
  `--pdf-engine=wkhtmltopdf` (install with `apt-get install -y wkhtmltopdf`).
