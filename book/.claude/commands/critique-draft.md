Run only the critique phase on an existing draft, then immediately apply fixes to produce the final.

Usage: /critique-draft <chapter_id>

This is a shortcut for chapters where you've already written the draft and want to
go straight to critique + final edit in one pass.

Steps:
1. Check that `book/content/{chapter_id}_draft.md` exists
2. Read the thesis (`book/content/00_thesis.md`) and the draft
3. Run the critique phase and save `book/content/{chapter_id}_critique.md`
4. Immediately run the final edit phase, applying the critique's priority fixes
5. Save `book/content/{chapter_id}_final.md`
6. Report word counts for both files

The $ARGUMENTS variable contains the chapter_id.
