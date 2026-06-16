Run the research phase for all chapters that don't yet have a research file.

Spawn parallel subagents—one per chapter—so multiple chapters are researched
simultaneously. Each subagent should:
1. Read `book/content/00_thesis.md` and `book/content/00_voice.md`
2. Generate research notes for its chapter (per the research phase instructions in CLAUDE.md)
3. Save to `book/content/{chapter_id}_research.md`

After all subagents complete, report how many research files were created and list them.

Check existing files first—skip any chapter that already has a research file.
