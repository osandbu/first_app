Write a book chapter through all phases (or a specific phase).

Usage: /chapter <chapter_id> [phase]

Examples:
  /chapter p1_c1              — run all 4 phases for chapter p1_c1
  /chapter p2_strategy draft  — run only the draft phase
  /chapter p3_culture         — run all phases, skipping any already done

Steps:
1. Look up the chapter ID in the book structure (CLAUDE.md)
2. Check which phase files already exist in `book/content/`
3. Run only the missing phases, in order: research → draft → critique → final
4. After each phase, report what was saved and its word count

The $ARGUMENTS variable contains the chapter_id and optional phase name.
