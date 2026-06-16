# Machine-readable book structure — mirrors the chapter table in CLAUDE.md.
# Used for scripting and verification; the authoritative source is CLAUDE.md.

CHAPTER_IDS = [
    "p1_c1", "p1_c2", "p1_c3", "p1_c4",
    "p2_strategy", "p2_product", "p2_engineering", "p2_finance",
    "p2_marketing", "p2_sales", "p2_hr", "p2_legal", "p2_cs",
    "p3_operating", "p3_colleagues", "p3_governance",
    "p3_org_design", "p3_culture", "p3_measurement",
    "p4_obsolete", "p4_valuable", "p4_careers", "p4_boards", "p4_exceptional",
]

PARTS = {
    "p1": ["p1_c1", "p1_c2", "p1_c3", "p1_c4"],
    "p2": ["p2_strategy", "p2_product", "p2_engineering", "p2_finance",
           "p2_marketing", "p2_sales", "p2_hr", "p2_legal", "p2_cs"],
    "p3": ["p3_operating", "p3_colleagues", "p3_governance",
           "p3_org_design", "p3_culture", "p3_measurement"],
    "p4": ["p4_obsolete", "p4_valuable", "p4_careers", "p4_boards", "p4_exceptional"],
}

PHASES = ["research", "draft", "critique", "final"]
