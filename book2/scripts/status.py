#!/usr/bin/env python3
"""Book progress reporter. Run from the repo root: python3 book2/scripts/status.py"""

import os

CONTENT = "book2/content"
PHASES  = ["research", "draft", "critique", "final"]
WIDTHS  = {"research": 8, "draft": 5, "critique": 8, "final": 5}
ID_W    = 15
TITLE_W = 31
COL1_W  = ID_W + TITLE_W  # 46

PARTS = [
    ("Part I — The Hidden Curriculum", [
        ("p1_c1", "Nobody Told You This Was the Job"),
        ("p1_c2", "The Org Chart Is a Lie"),
        ("p1_c3", "Your Mental Model of a Company Is Wrong"),
    ]),
    ("Part II — Incentives and Behavior", [
        ("p2_c1", "Everyone Is Rational, Given Their Incentives"),
        ("p2_c2", "How Compensation Shapes What Gets Built"),
        ("p2_c3", "The Principal-Agent Problem Is Everywhere"),
        ("p2_c4", "Metrics Eat Culture"),
        ("p2_c5", "Why Good Engineers Do Bad Things"),
    ]),
    ("Part III — Organizations as Systems", [
        ("p3_c1", "Conway's Law Is Not a Metaphor"),
        ("p3_c2", "The Coordination Tax"),
        ("p3_c3", "Team Topologies and Why They Matter"),
        ("p3_c4", "The Communication Architecture You Actually Have"),
        ("p3_c5", "Why Reorgs Rarely Work"),
    ]),
    ("Part IV — The Work Nobody Teaches", [
        ("p4_c1", "How Decisions Actually Get Made"),
        ("p4_c2", "The Written Word Is Infrastructure"),
        ("p4_c3", "Technical Debt Is a Financial Concept"),
        ("p4_c4", "Build vs. Buy Is a Strategy Question"),
        ("p4_c5", "Cost of Delay: The Number Nobody Calculates"),
        ("p4_c6", "Platform Thinking for People Who Build Platforms"),
    ]),
    ("Part V — Leadership Without the Title", [
        ("p5_c1", "Influence Without Authority Is a Skill"),
        ("p5_c2", "The Multiplier Effect"),
        ("p5_c3", "What Staff Engineers Actually Do"),
        ("p5_c4", "The First Ninety Days as a Manager"),
        ("p5_c5", "Leading Through Ambiguity"),
        ("p5_c6", "The Feedback Nobody Wants to Give"),
    ]),
]


def phase_exists(id_, phase):
    if phase == "final":
        return os.path.isfile(f"{CONTENT}/final/{id_}.md")
    return os.path.isfile(f"{CONTENT}/working/{id_}_{phase}.md")


def mark(id_, phase):
    return "✓" if phase_exists(id_, phase) else "·"


def header():
    cols = " | ".join(f"{p:<{WIDTHS[p]}}" for p in PHASES)
    sep  = "-+-".join("-" * WIDTHS[p] for p in PHASES)
    print(f"{'Chapter':<{COL1_W}} | {cols}")
    print("-" * COL1_W + "-+-" + sep)


def print_row(id_, title, counts):
    if len(title) > TITLE_W:
        title = title[:TITLE_W - 3] + "..."
    label = f"{id_:<{ID_W}}{title}"
    cells = " | ".join(f"{mark(id_, p):^{WIDTHS[p]}}" for p in PHASES)
    print(f"{label:<{COL1_W}} | {cells}")

    done = sum(phase_exists(id_, p) for p in PHASES)
    counts["total"] += 1
    if   done == 4: counts["fully"]    += 1
    elif done  > 0: counts["progress"] += 1
    else:           counts["none"]     += 1


def main():
    counts = {"total": 0, "fully": 0, "progress": 0, "none": 0}
    for part_name, chapters in PARTS:
        print(f"\n{part_name}")
        header()
        for id_, title in chapters:
            print_row(id_, title, counts)

    t, f, p, n = counts["total"], counts["fully"], counts["progress"], counts["none"]
    print(f"\nTotal chapters : {t}")
    print(f"Fully done     : {f}  (all 4 phases complete)")
    print(f"In progress    : {p}  (1–3 phases complete)")
    print(f"Not started    : {n}  (no phases yet)")


if __name__ == "__main__":
    main()
