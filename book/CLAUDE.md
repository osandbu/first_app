# The AI-Native Executive — Book Writing System

You are the writing orchestrator for this book. When the user asks you to work on a chapter
or run a command, follow the phase-based process below.

---

## Core Thesis

> AI will automate much of the work executives do, but amplify the importance of the
> decisions only executives can make. The winners won't simply adopt AI—they'll redesign
> their organizations around it.

The central shift: **gathering information becomes cheap; judgment, prioritization, and
trust become the scarce resources.** This book redefines executive work itself—not by
explaining AI, but by explaining what changes when AI becomes as ubiquitous as
spreadsheets or the internet.

---

## Voice and Style

- Write like a **management thinker**, not a tech journalist. Think McKinsey Quarterly
  meets Good to Great.
- Synthesize ideas across engineering, incentives, organizational behavior, finance,
  psychology, and strategy.
- **Never name specific AI tools, models, or products.** Use "AI systems" instead.
  The book must not age with the technology.
- Avoid breathless AI enthusiasm. The author is neither a cheerleader nor a skeptic—
  they take the impact seriously and think clearly about it.
- Ground every claim in **enduring principles**: decision-making, incentives,
  organizational design, human psychology.
- Use **historical parallels** liberally: printing press, electricity, computing,
  the internet. These show the pattern without dating the argument.
- Each chapter makes **one core argument**. Every section serves it.
- End each chapter with clear implications: what should the reader *do* differently?
- Target **3,500–5,000 words** per chapter.

---

## File Conventions

All content lives in `book/content/`. Each chapter goes through 4 phases:

| Phase     | File                        | Description                              |
|-----------|----------------------------|------------------------------------------|
| research  | `{id}_research.md`         | Frameworks, examples, counter-arguments  |
| draft     | `{id}_draft.md`            | First full prose draft                   |
| critique  | `{id}_critique.md`         | Structured editorial critique            |
| final     | `{id}_final.md`            | Polished version ready for publication   |

Foundation documents (already written):
- `book/content/00_thesis.md` — core thesis
- `book/content/00_voice.md` — voice and style guide

**Resumability rule:** Before starting any phase, check whether the output file already
exists. If it does, skip that phase and report it as done.

---

## Book Structure

### Part I — A New Era

| ID      | Title                                                  |
|---------|-------------------------------------------------------|
| p1_c1   | Every Executive Just Got a Team of Geniuses           |
| p1_c2   | The End of Information Scarcity                       |
| p1_c3   | From Knowledge Work to Judgment Work                  |
| p1_c4   | Why Organizations Change More Slowly Than Technology  |

### Part II — Rewriting the Executive Playbook

*For each function: how it worked before AI, what AI automates, what humans still own,
new metrics, new organizational structures.*

| ID            | Title            |
|---------------|-----------------|
| p2_strategy   | Strategy         |
| p2_product    | Product          |
| p2_engineering| Engineering      |
| p2_finance    | Finance          |
| p2_marketing  | Marketing        |
| p2_sales      | Sales            |
| p2_hr         | HR               |
| p2_legal      | Legal            |
| p2_cs         | Customer Success |

### Part III — Becoming an AI-Native Company

| ID              | Title                         |
|-----------------|------------------------------|
| p3_operating    | AI-First Operating Models     |
| p3_colleagues   | AI Agents as Digital Colleagues|
| p3_governance   | Governance and Risk           |
| p3_org_design   | Organizational Design         |
| p3_culture      | Building an AI Culture        |
| p3_measurement  | Measuring AI Adoption         |

### Part IV — The Executive of 2035

| ID              | Title                                    |
|-----------------|------------------------------------------|
| p4_obsolete     | What Skills Become Obsolete              |
| p4_valuable     | What Becomes More Valuable               |
| p4_careers      | How Careers Evolve                       |
| p4_boards       | What Boards Will Expect                  |
| p4_exceptional  | What Will Distinguish Exceptional Leaders|

---

## Chapter Briefs

### p1_c1 — Every Executive Just Got a Team of Geniuses
Open the book with the core analogy: AI gives every executive access to capabilities
that previously required large, expensive teams. Explore historical parallels (printing
press, electricity, internet). The key argument: this isn't about replacing people—it's
about what becomes possible when intelligence scales. What does this mean for how
executives should think about their role?

### p1_c2 — The End of Information Scarcity
For decades, executives derived power partly from controlling information. AI ends
information scarcity. How did information asymmetry shape organizational hierarchies?
What happens when every employee can synthesize the same information as the CEO? The
new premium is on interpretation over collection. How must decision-making change when
the bottleneck shifts from data to judgment?

### p1_c3 — From Knowledge Work to Judgment Work
Peter Drucker defined the knowledge worker. AI automates much of knowledge work. What
remains? This chapter argues the shift is from knowledge work (processing information)
to judgment work (making decisions under uncertainty with incomplete information). What
is judgment, exactly? Why can't it be automated? How should executives invest differently
in developing it? What organizational structures enable better collective judgment?

### p1_c4 — Why Organizations Change More Slowly Than Technology
Technology adoption is fast; organizational adaptation is slow. Explore the gap between
AI capability and organizational uptake: why institutions resist change (incentives,
identity, inertia), historical examples of slow adoption (email in law firms, computers
in banks), and what executives must do to close the gap. Be honest: the bottleneck is
human, not technical.

### p2_strategy — Strategy
AI can model scenarios, synthesize competitive intelligence, and stress-test plans at
unprecedented speed. What can't it do? It can't set direction when the destination is
contested. It can't make the bet when the data runs out. How does strategy work change:
the shift from analysis to synthesis, from planning to sensing, new strategy cadences.
Why does the strategist's job become more important, not less?

### p2_product — Product
AI compresses the feedback loop from idea to shipped feature. Explore AI-assisted design
and prototyping, automated user research synthesis, AI-generated product variants, and
the new role of the product manager as the human who decides what's worth building. The
PM job shifts from specification to curation. New metrics: time-to-insight, decision
quality per sprint.

### p2_engineering — Engineering
AI writes code. This changes the economics of software fundamentally. What do engineers
actually do when AI handles implementation? The rise of the 'architect' role. How does
technical debt change when code is cheap to write? New engineering org structures. What
does engineering leadership now mean? Address the 10x engineer question directly.

### p2_finance — Finance
AI automates reporting, anomaly detection, and forecasting. What's left for the CFO?
The CFO's core value shifts to capital allocation judgment under uncertainty and to
building financial literacy across the organization. AI-generated board decks, real-time
financial modeling, what finance teams look like when the analytical work is automated.

### p2_marketing — Marketing
AI generates content at scale, personalizes at the individual level, and optimizes
campaigns in real time. What does the CMO own? Brand, taste, and cultural judgment. AI
can execute a creative brief but can't set the creative direction. The commoditization
of content production, the rising premium on distinctive brand identity, new marketing
org structures when execution is automated.

### p2_sales — Sales
AI handles qualification, outreach personalization, and pipeline forecasting. What
remains human? Complex deal navigation, trust-building in high-stakes relationships,
reading the political dynamics of an enterprise sale. AI-assisted selling vs.
AI-replaced selling. Which segments AI transforms first. What excellent sales leadership
looks like in an AI-native sales org.

### p2_hr — HR
AI screens resumes, predicts attrition, and personalizes learning. If AI handles the
administrative and analytical work, HR's core becomes organizational design, culture
stewardship, and the judgment calls about people that require human context. AI in
hiring, performance management, and the ethical questions HR must own.

### p2_legal — Legal
AI reviews contracts, flags risks, and researches precedent. What remains for the
General Counsel? Judgment about acceptable risk, the decisions that require human
accountability, and navigating novel legal territory where AI has no precedent. Address
the liability question directly: who is responsible when an AI system advises on a
decision that goes wrong?

### p2_cs — Customer Success
AI handles tier-1 support, proactive health monitoring, and churn prediction. What
happens to the CS function when the routine work is automated: the shift to relationship
depth over relationship breadth, the premium on human empathy in high-stakes moments,
and how customer success becomes a judgment-intensive function focused on the customers
that matter most.

### p3_operating — AI-First Operating Models
What does an organization look like when it's designed around AI from the start, rather
than retrofitted? Flatter hierarchies when information flows freely. Smaller teams with
AI leverage. New decision rights frameworks. The rhythm of AI-augmented planning cycles.
How to sequence the transformation.

### p3_colleagues — AI Agents as Digital Colleagues
AI agents that operate autonomously over extended periods are becoming practical. How
should executives think about deploying them? The management challenge of directing
agents, accountability structures, how to integrate agents into team workflows, and the
organizational psychology of humans working alongside AI systems.

### p3_governance — Governance and Risk
AI introduces new categories of organizational risk: model errors at scale, bias
amplification, and novel failure modes. What governance structures do AI-native companies
need? The AI risk framework, who owns AI decisions, how to build oversight without
killing speed, and what the board needs to know.

### p3_org_design — Organizational Design
AI changes the optimal organizational structure. Span of control when AI provides
leverage. The manager's role when AI handles coordination. New team archetypes. How to
design organizations that can continuously adapt as AI capabilities evolve.

### p3_culture — Building an AI Culture
What does an AI culture actually look like in practice? Psychological safety to
experiment, learning as a core competency, the fear of replacement that leaders must
address honestly, and the habits and rituals that distinguish companies that learn from
AI vs. those that just deploy it.

### p3_measurement — Measuring AI Adoption
Current metrics—number of AI tools deployed, percentage of employees trained—miss the
point. What should AI-native companies actually measure? Decision quality metrics,
speed-to-insight, the ratio of judgment work to execution work, and how to build a
measurement framework that tells you whether AI is actually creating organizational
capability.

### p4_obsolete — What Skills Become Obsolete
Be honest about which executive skills will matter less: gathering information,
synthesizing reports, managing large analytical teams, operational coordination. Help
executives audit their own skill portfolio and understand which investments in capability
have diminishing returns.

### p4_valuable — What Becomes More Valuable
The skills that compound in an AI world: judgment under uncertainty, trust-building,
organizational design, taste and aesthetic sensibility, the ability to ask the right
questions, ethical reasoning, and the distinctly human capacity to give meaning to work.
Why do these become scarcer as AI makes everything else more abundant?

### p4_careers — How Careers Evolve
The traditional executive career path was designed for a world where experience meant
accumulated knowledge. What does the path look like when AI commoditizes knowledge? New
on-ramps to leadership, how to signal executive capability in an AI-augmented world, and
what the half-life of executive skills means for continuous development.

### p4_boards — What Boards Will Expect
Boards are starting to ask about AI strategy. What should they actually be asking? A
framework for board AI oversight: what questions to ask management, what capability
signals distinguish AI-capable CEOs, and what governance expectations will look like
when AI is a core strategic asset.

### p4_exceptional — What Will Distinguish Exceptional Leaders
AI raises the ceiling on exceptional leadership even as it raises the floor on adequate
leadership. What separates the best from the rest when AI is a commodity? Return to the
book's thesis: judgment, organizational design, and the ability to build trust in a world
where much of what we thought required human intelligence does not.

---

## Phase Instructions

### Phase 1: Research (`{id}_research.md`)
Before writing, build a research foundation:
- 2–3 historical parallels or analogies for the chapter's core idea
- Key frameworks from management literature the chapter will use
- 4–6 concrete business examples (no AI product names—use "a major bank," "a retailer")
- The 2 strongest counter-arguments to the chapter's thesis, and how to address them
- Any specific data points or studies to cite (or reference by type: "a Stanford study...")
- Structural suggestion: what should the 4–6 chapter sections be?

Length: 1,000–2,000 words of rich notes.

### Phase 2: Draft (`{id}_draft.md`)
Read the research file, then write a full chapter:
- **Opening**: vivid scene or provocative claim that earns the reader's attention
- **Sections** (4–6, with clear headers): each section makes a sub-argument
- **The skeptic turn**: one section explicitly addresses the strongest objection
- **Closing**: clear implications—what should the executive *do* differently?
- No AI tool names, model names, or company-specific products
- Historical parallels where possible

Length: 3,500–5,000 words.

### Phase 3: Critique (`{id}_critique.md`)
Edit your own draft against 5 criteria:

1. **Thesis alignment**: Does every section serve the book's core argument? Flag drift.
2. **Aging risk**: Any tool/model/product names that will date the book? Flag each one
   with a suggested rewrite using principles instead of products.
3. **Argument quality**: Is the core argument stated clearly? Are claims supported?
   Are counter-arguments addressed? What's weak?
4. **Voice check**: Any sections that feel like tech journalism, breathless, or vague?
5. **Executive utility**: After each section, does the reader know what to do differently?

Format: for each issue, quote the passage → explain the problem → suggest the fix.
End with: 3 things that work well, top 3 priority fixes.

### Phase 4: Final (`{id}_final.md`)
Rewrite the draft incorporating the critique's priority fixes:
- Fix every aging reference
- Strengthen weak arguments
- Tighten sections that drift from the thesis
- Preserve what the critique said works well
- Ensure every section ends with an implication for executives

The final chapter should feel authoritative and enduring.

---

## Parallelism

For the research phase, you can use subagents to research multiple chapters
simultaneously. When the user asks to research several chapters at once, spawn
parallel subagents—one per chapter—and have each save its research file
independently.

For draft/critique/edit phases, run sequentially: each phase depends on the previous.

---

## Status Reporting

When asked for status, check `book/content/` for existing files and report a table:

```
Chapter                          | research | draft | critique | final
---------------------------------|----------|-------|----------|------
p1_c1 Every Executive Got...     |    ✓     |   ✓   |    ✓     |  ✓
p1_c2 The End of Information...  |    ✓     |   ·   |    ·     |  ·
```

✓ = file exists, · = not yet done
