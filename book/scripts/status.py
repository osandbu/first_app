#!/usr/bin/env python3
"""Book progress reporter. Run from the repo root: python3 book/scripts/status.py"""

import os

CONTENT = "book/content"
PHASES  = ["research", "draft", "critique", "final"]
WIDTHS  = {"research": 8, "draft": 5, "critique": 8, "final": 5}
ID_W    = 15
TITLE_W = 31
COL1_W  = ID_W + TITLE_W  # 46

PARTS = [
    ("Part I — A New Era", [
        ("p1_c1",          "Every Executive Just Got a Team of Geniuses"),
        ("p1_c2",          "The End of Information Scarcity"),
        ("p1_c3",          "From Knowledge Work to Judgment Work"),
        ("p1_c4",          "Why Organizations Change More Slowly Than Technology"),
    ]),
    ("Part II — Rewriting the Executive Playbook", [
        ("p2_strategy",    "Strategy"),
        ("p2_product",     "Product"),
        ("p2_engineering", "Engineering"),
        ("p2_finance",     "Finance"),
        ("p2_marketing",   "Marketing"),
        ("p2_sales",       "Sales"),
        ("p2_hr",          "HR"),
        ("p2_legal",       "Legal"),
        ("p2_cs",          "Customer Success"),
    ]),
    ("Part III — Becoming an AI-Native Company", [
        ("p3_operating",   "AI-First Operating Models"),
        ("p3_colleagues",  "AI Agents as Digital Colleagues"),
        ("p3_governance",  "Governance and Risk"),
        ("p3_org_design",  "Organizational Design"),
        ("p3_culture",     "Building an AI Culture"),
        ("p3_measurement", "Measuring AI Adoption"),
    ]),
    ("Part IV — The Executive of 2035", [
        ("p4_obsolete",    "What Skills Become Obsolete"),
        ("p4_valuable",    "What Becomes More Valuable"),
        ("p4_careers",     "How Careers Evolve"),
        ("p4_boards",      "What Boards Will Expect"),
        ("p4_exceptional", "What Will Distinguish Exceptional Leaders"),
    ]),
]


def phase_exists(id_, phase):
    return os.path.isfile(f"{CONTENT}/{id_}_{phase}.md")


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
