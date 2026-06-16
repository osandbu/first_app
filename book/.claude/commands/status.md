Show the current writing progress for all 24 chapters.

Steps:
1. List the files in `book/content/` (use Bash: `ls book/content/`)
2. For each chapter below, check whether its phase files exist in that listing
3. Print the status table (format below)
4. Print the summary line

Phase file naming: `book/content/{id}_{phase}.md` where phase is one of:
research, draft, critique, final

Use ✓ if the file exists, · if it does not.

---

## Chapter list

### Part I — A New Era
| ID      | Title                                               |
|---------|-----------------------------------------------------|
| p1_c1   | Every Executive Just Got a Team of Geniuses         |
| p1_c2   | The End of Information Scarcity                     |
| p1_c3   | From Knowledge Work to Judgment Work                |
| p1_c4   | Why Organizations Change More Slowly Than Technology|

### Part II — Rewriting the Executive Playbook
| ID             | Title             |
|----------------|-------------------|
| p2_strategy    | Strategy          |
| p2_product     | Product           |
| p2_engineering | Engineering       |
| p2_finance     | Finance           |
| p2_marketing   | Marketing         |
| p2_sales       | Sales             |
| p2_hr          | HR                |
| p2_legal       | Legal             |
| p2_cs          | Customer Success  |

### Part III — Becoming an AI-Native Company
| ID              | Title                          |
|-----------------|--------------------------------|
| p3_operating    | AI-First Operating Models      |
| p3_colleagues   | AI Agents as Digital Colleagues|
| p3_governance   | Governance and Risk            |
| p3_org_design   | Organizational Design          |
| p3_culture      | Building an AI Culture         |
| p3_measurement  | Measuring AI Adoption          |

### Part IV — The Executive of 2035
| ID              | Title                                     |
|-----------------|-------------------------------------------|
| p4_obsolete     | What Skills Become Obsolete               |
| p4_valuable     | What Becomes More Valuable                |
| p4_careers      | How Careers Evolve                        |
| p4_boards       | What Boards Will Expect                   |
| p4_exceptional  | What Will Distinguish Exceptional Leaders |

---

## Output format

Print the table grouped by part. Truncate titles to ~45 chars. Example:

```
Part I — A New Era
Chapter                                       | research | draft | critique | final
----------------------------------------------|----------|-------|----------|------
p1_c1  Every Executive Just Got a Team of...  |    ✓     |   ✓   |    ✓     |  ✓
p1_c2  The End of Information Scarcity        |    ✓     |   ·   |    ·     |  ·

Part II — Rewriting the Executive Playbook
...
```

After the table, print a summary:
- Total chapters: 24
- Fully done (all 4 phases ✓): N
- In progress (1–3 phases ✓): N
- Not started (0 phases ✓): N
