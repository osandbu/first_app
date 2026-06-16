Write all chapters in a specific book part through all phases.

Usage: /write-part <part_id>

Valid part IDs: p1, p2, p3, p4

Steps:
1. Identify all chapters in the specified part (from CLAUDE.md book structure)
2. For each chapter in sequence, run all missing phases (research → draft → critique → final)
3. Skip phases that already have output files
4. After each chapter completes, print a brief summary

The $ARGUMENTS variable contains the part ID.
