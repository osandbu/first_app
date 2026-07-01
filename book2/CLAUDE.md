# Engineering Beyond Code — Book Writing System

You are the writing orchestrator for this book. When the user asks you to work on a chapter
or run a command, follow the phase-based process below.

---

## Core Thesis

> Engineers are promoted for technical excellence and then surprised to discover the job
> has changed entirely. The skills that got you here — architecture, debugging,
> optimization — are necessary but no longer sufficient. This book covers the curriculum
> that CS education skips: incentives, organizational behavior, decision-making,
> economics, communication, and leadership. Not because these are soft skills, but
> because they are the actual job.

The central shift: **individual contribution gives way to organizational influence.**
The engineer who understands incentives, communication structures, and decision-making
is not just more effective — they are playing a fundamentally different and more
powerful game than the one CS programs teach.

---

## Voice and Style

- Write like a **candid senior peer**, not a management consultant. Think Will Larson's
  *An Elegant Puzzle* meets Patrick McKenzie's blog: technically credible, practically
  useful, occasionally contrarian, no buzzwords.
- The audience is technical. They can handle precision and specificity. Don't water
  things down.
- **Never name specific software tools, vendors, frameworks, or companies** by name.
  The book must not age with the technology or become embarrassing if a named company
  fails. Use categories: "a large financial institution," "a mid-size SaaS company."
- Avoid buzzwords that have been drained of meaning: "psychological safety," "servant
  leadership," "agile mindset." Either define precisely or use plainer language.
- Ground every claim in **enduring principles**: incentives, organizational behavior,
  behavioral economics, human psychology.
- Use **engineering history** liberally: Brooks's Law, Conway's Law, the Mythical
  Man-Month, Dijkstra, the structured programming debates, open source. The audience
  knows these. They establish credibility and show these problems aren't new.
- Each chapter makes **one core argument**. Every section serves it.
- End each chapter with **"What Changes Monday"**: concrete, direct, second-person.
  What to stop doing. What to start doing. The longer-term shift.
- Target **3,000–4,500 words** per chapter.

---

## File Conventions

Content lives in `book2/content/` with two subdirectories:

- `book2/content/final/` — published chapters, one file per chapter (`{id}.md`)
- `book2/content/working/` — working files for each chapter

Each chapter goes through 4 phases:

| Phase     | File                              | Description                              |
|-----------|-----------------------------------|------------------------------------------|
| research  | `working/{id}_research.md`        | Frameworks, examples, counter-arguments  |
| draft     | `working/{id}_draft.md`           | First full prose draft                   |
| critique  | `working/{id}_critique.md`        | Structured editorial critique            |
| final     | `final/{id}.md`                   | Polished version ready for publication   |

Foundation documents (already written):
- `book2/content/00_thesis.md` — core thesis
- `book2/content/00_voice.md` — voice and style guide

**Resumability rule:** Before starting any phase, check whether the output file already
exists. If it does, skip that phase and report it as done.

---

## Book Structure

### Part I — The Hidden Curriculum

*Why CS education skips the most important parts of the job. Sets up the book's premise:
the skills that determine career trajectory after senior engineer are almost never taught.*

| ID    | Title                                    |
|-------|------------------------------------------|
| p1_c1 | Nobody Told You This Was the Job         |
| p1_c2 | The Org Chart Is a Lie                   |
| p1_c3 | Your Mental Model of a Company Is Wrong  |

### Part II — Incentives and Behavior

*The single most underrated framework in organizational life. Once you see incentives
clearly, organizational behavior stops seeming irrational.*

| ID    | Title                                          |
|-------|------------------------------------------------|
| p2_c1 | Everyone Is Rational, Given Their Incentives   |
| p2_c2 | How Compensation Shapes What Gets Built        |
| p2_c3 | The Principal-Agent Problem Is Everywhere      |
| p2_c4 | Metrics Eat Culture                            |
| p2_c5 | Why Good Engineers Do Bad Things               |

### Part III — Organizations as Systems

*Teams, structures, and communication patterns as systems that produce predictable
outputs — including predictable failures.*

| ID    | Title                                               |
|-------|-----------------------------------------------------|
| p3_c1 | Conway's Law Is Not a Metaphor                      |
| p3_c2 | The Coordination Tax                                |
| p3_c3 | Team Topologies and Why They Matter                 |
| p3_c4 | The Communication Architecture You Actually Have    |
| p3_c5 | Why Reorgs Rarely Work                              |

### Part IV — The Work Nobody Teaches

*Decision making, communication, economics, and leadership — the actual job of senior
engineers and above.*

| ID    | Title                                             |
|-------|---------------------------------------------------|
| p4_c1 | How Decisions Actually Get Made                   |
| p4_c2 | The Written Word Is Infrastructure                |
| p4_c3 | Technical Debt Is a Financial Concept             |
| p4_c4 | Build vs. Buy Is a Strategy Question              |
| p4_c5 | Cost of Delay: The Number Nobody Calculates       |
| p4_c6 | Platform Thinking for People Who Build Platforms  |

### Part V — Leadership Without the Title

*Influence, multiplier effects, and what it means to lead at the individual contributor
and early management level.*

| ID    | Title                                     |
|-------|-------------------------------------------|
| p5_c1 | Influence Without Authority Is a Skill    |
| p5_c2 | The Multiplier Effect                     |
| p5_c3 | What Staff Engineers Actually Do          |
| p5_c4 | The First Ninety Days as a Manager        |
| p5_c5 | Leading Through Ambiguity                 |
| p5_c6 | The Feedback Nobody Wants to Give         |

---

## Chapter Briefs

### p1_c1 — Nobody Told You This Was the Job
Open the book with the experience of becoming a tech lead or senior engineer and
discovering that the problems aren't purely technical anymore. The work that got you
promoted — architectural clarity, debugging acuity, delivery discipline — is still
necessary, but the problems multiplying on your desk are organizational: misaligned
incentives, communication failures, decisions made for reasons that have nothing to do
with the best technical outcome. This chapter names that experience and makes explicit
what the book will do about it. Voice: candid, slightly rueful, immediately recognizable
to anyone who has been through it.

### p1_c2 — The Org Chart Is a Lie
The formal org chart describes reporting relationships, not how work actually gets done
or how influence actually flows. This chapter introduces informal power networks, the
gap between authority and effectiveness, and why engineers who only read the org chart
keep being surprised by how decisions get made. Practical implication: how to map the
actual influence network you operate in.

### p1_c3 — Your Mental Model of a Company Is Wrong
Engineers are trained to think of companies as machines to be optimized. They're
actually organisms shaped by incentives, politics, history, and identity. A company that
appears to be making obviously wrong decisions is usually making decisions that are
locally rational for the people making them. This chapter is the foundation for
everything in Part II: until you update the mental model, the behavior will keep
seeming inexplicable.

### p2_c1 — Everyone Is Rational, Given Their Incentives
The core reframe: behavior that looks irrational from the outside is almost always
rational from inside the incentive structure. Walk through canonical examples —
the manager who hoards headcount, the team that avoids the codebase no one owns, the
VP who kills technically superior projects. In each case: show the incentive structure
that makes the behavior locally rational. The chapter ends with a practical tool: before
attributing organizational dysfunction to stupidity or malice, map the incentives.

### p2_c2 — How Compensation Shapes What Gets Built
Quarterly bonuses, stack ranking, equity vesting cliffs, headcount as a proxy for
importance — each shapes what gets prioritized. This chapter makes the mechanism
concrete: how does a VP's compensation structure affect which projects get resourced?
How does individual performance review shape what engineers work on? The chapter gives
engineers and managers a framework for reading compensation structures as signals about
what an organization actually values (vs. what it says it values).

### p2_c3 — The Principal-Agent Problem Is Everywhere
The gap between what a company wants and what an individual does when their incentives
diverge. Introduce principal-agent theory without the jargon: why delegation is hard,
why monitoring is expensive, why the solutions (better incentive alignment, reputation
systems, culture) each have limits. Make it concrete: the manager who delegates a
project but gets the credit, the team that over-engineers because complexity justifies
headcount, the vendor who recommends the solution they make more margin on.

### p2_c4 — Metrics Eat Culture
Goodhart's Law applied to engineering: when a measure becomes a target, it ceases to
be a good measure. Walk through the engineering-specific cases: velocity, code coverage,
DORA metrics, OKRs, NPS. In each case: the metric was a reasonable proxy, became a
target, and then generated behavior that improved the metric while degrading the thing
it was meant to measure. The chapter is not anti-measurement — it's pro-thinking-clearly
about what you measure and how you use it.

### p2_c5 — Why Good Engineers Do Bad Things
Why smart engineers cut corners, defer maintenance, over-engineer, hoard knowledge,
and fail to communicate. This chapter is empathetic but clear: these are structural
causes, not character flaws. The engineer deferring maintenance is usually doing it
under deadline pressure with no slack in the system. The engineer hoarding knowledge
is often doing it in a culture where specialization is rewarded and knowledge-sharing
is invisible. Understanding the structural causes is the first step to changing them.

### p3_c1 — Conway's Law Is Not a Metaphor
Conway's Law (systems mirror the communication structure of the organizations that build
them) is often cited as an interesting observation. This chapter argues it's a
structural law with predictive power. Teams that don't talk build systems with seams
where the teams don't talk. Monoliths reflect centralized teams. Microservices reflect
distributed teams — or produce distributed teams where centralized teams existed.
Make the implication concrete: if you want a different architecture, you may need a
different organization, and vice versa. The Inverse Conway Maneuver.

### p3_c2 — The Coordination Tax
Why large teams are slower than small ones. The math behind Brooks's Law. Meeting
overhead, decision latency, the cost of synchronizing mental models across many people.
This chapter gives engineers the vocabulary to explain organizational drag in economic
terms — not as a complaint about bureaucracy, but as a predictable cost of scale.
Practical implications: when to split teams, how to reduce coordination surface area,
why small autonomous teams often outperform large coordinated ones.

### p3_c3 — Team Topologies and Why They Matter
Stream-aligned teams, platform teams, enabling teams, and complicated-subsystem teams
— but grounded in the problems they solve, not the taxonomy. The right team structure
depends on what you're trying to optimize for: speed of delivery vs. reuse vs.
cognitive load reduction. The chapter gives engineers a framework for diagnosing why
their current team structure is producing friction and what to propose instead.

### p3_c4 — The Communication Architecture You Actually Have
A practical audit tool: how to map the actual communication structure in your
organization — who talks to whom, what flows freely and what gets blocked, where
decisions get made vs. where they appear to get made. This chapter is the companion to
p3_c1: if Conway's Law tells you that communication structure determines system
structure, this chapter tells you how to understand the communication structure you
actually have (vs. the one the org chart implies).

### p3_c5 — Why Reorgs Rarely Work
Reorgs are usually the wrong solution, deployed too fast, for problems with structural
economic causes that survive any org change. Walk through the mechanics: why reorgs feel
like they're fixing things (they create motion, they reset social dynamics, they give
management a sense of control) while often leaving the underlying incentive and
communication structures unchanged. When reorgs are warranted and when they're theater.

### p4_c1 — How Decisions Actually Get Made
The gap between how engineers think decisions should work (analysis → optimal choice)
and how they actually work (political negotiation, incomplete information, reversibility,
regret minimization). Frameworks that help: reversible vs. irreversible decisions, the
pre-mortem, the decision log. The chapter is practical: how to be more effective in
organizational decision-making processes that don't look like the decision trees from
algorithms class.

### p4_c2 — The Written Word Is Infrastructure
At senior levels, the quality of your thinking is judged by the quality of your writing.
PRDs, RFCs, architecture docs, postmortems, strategy memos. The written word is the
coordination mechanism of engineering organizations — it's how decisions persist, how
context travels, how thinking gets reviewed asynchronously. Most engineers are not
taught this. The chapter covers: what good technical writing looks like, why it's hard,
the specific documents that matter most at the senior level, and how to develop the skill.

### p4_c3 — Technical Debt Is a Financial Concept
Reframe technical debt as a financial concept: it has compounding interest, a balance
sheet effect, and a carrying cost. This gives engineers the vocabulary to talk about it
in terms finance leaders and executives understand — and to make the economic case for
paying it down. The chapter also addresses the limits of the metaphor: not all technical
debt is equal, the "debt" framing can obscure complexity debt and architectural drift,
and the decision to take on debt vs. pay it down is a real options problem.

### p4_c4 — Build vs. Buy Is a Strategy Question
Not a technical question — a strategic one about core competency. What to own (things
that differentiate you), what to buy (commodity capabilities), how vendor lock-in works
as a risk, when open source changes the calculation. Engineers who treat build vs. buy
as purely technical keep getting overruled because they're not speaking the language of
the decision. This chapter gives them that language.

### p4_c5 — Cost of Delay: The Number Nobody Calculates
One of the most useful frameworks in product and engineering that almost nobody uses
explicitly. Cost of delay (the value you lose by not delivering something sooner) changes
every prioritization conversation. The chapter makes it concrete with worked examples
and shows how it changes trade-offs between speed and scope, between refactoring and
shipping, between parallelism and sequencing.

### p4_c6 — Platform Thinking for People Who Build Platforms
Internal platforms are products. The customers are developers. Developer experience is
a product problem. This chapter is for everyone who has ever built internal tooling and
wondered why nobody used it — and for everyone who has to decide whether to invest in
an internal platform at all. Topics: the platform product manager role, measuring
platform adoption and impact, the "build a platform vs. build a product" decision, and
why successful internal platforms require the same customer development that successful
external products do.

### p5_c1 — Influence Without Authority Is a Skill
At senior levels, you can't just decide things — you have to persuade. The chapter makes
influence a learnable skill: understanding stakeholder interests, sequencing
conversations, building coalitions, making your reasoning visible so others can
engage with it rather than just being asked to accept conclusions. Practical tools:
the pre-alignment conversation, the working-backwards document, the "I need a decision
by" email.

### p5_c2 — The Multiplier Effect
The shift from individual contribution to making other engineers more effective.
One person whose judgment others trust and whose clarity unblocks teams is worth more
than the same person producing individual output. The chapter explains how to operate
at that level: what to delegate, what to keep, how to give feedback that changes
trajectories, and how to measure your impact when your output is other people's output.

### p5_c3 — What Staff Engineers Actually Do
Demystify staff engineering: what does a staff engineer actually do on a daily basis?
It varies by company, but the chapter identifies the common threads: setting technical
direction, managing cross-team dependencies, mentoring senior engineers, representing
engineering in product discussions, being the person who synthesizes technical context
across initiatives. Practical: how to know whether you're operating at the staff level
and what to change if you're not.

### p5_c4 — The First Ninety Days as a Manager
A candid guide for the engineer who just became a manager. What to stop doing (writing
most of the code). What to start doing (one-on-ones, understanding what each person
needs to do their best work, mapping the team's context). The mental model shift that
most new managers take years to complete: your output is your team's output, not your
own output. What to do in the first week, first month, first quarter.

### p5_c5 — Leading Through Ambiguity
The ability to keep a team moving when the path is unclear is the most distinctive
skill of senior leadership. The chapter is concrete about how to do it: how to
communicate what you know and don't know (and why honesty builds more trust than
false confidence), how to make reversible bets that generate information, how to keep
morale high without being dishonest about difficulty, and how to know when ambiguity
has resolved enough to commit.

### p5_c6 — The Feedback Nobody Wants to Give
The chapter most readers will find hardest to act on. Why engineers avoid hard feedback
(it's uncomfortable, it's risky, the culture may not support it), what it costs
(compounding — the problem grows the longer you wait), and how to give it in ways that
people can actually use. Concrete frameworks: the situation-behavior-impact structure,
the "I'm going to say something hard" opener, the distinction between feedback and
judgment. The chapter closes the book on the same register it opened: here is the thing
nobody tells you, and here is how to do it anyway.

---

## Phase Instructions

### Phase 1: Research (`{id}_research.md`)
Before writing, build a research foundation:
- 2–3 historical parallels or analogies for the chapter's core idea (prefer engineering
  history: Brooks, Conway, Dijkstra, Unix, open source, well-known engineering failures)
- Key frameworks from engineering management, organizational behavior, and behavioral
  economics literature the chapter will use
- 4–6 concrete scenarios (no company names — use "a team under deadline pressure,"
  "a platform team at a large organization") that illustrate the core argument
- The 2 strongest counter-arguments to the chapter's thesis, and how to address them
- Any specific data points or studies to reference (by type: "a study of software
  project failure rates..." not by URL)
- Structural suggestion: what should the 4–6 chapter sections be?

Length: 1,000–2,000 words of rich notes.

### Phase 2: Draft (`{id}_draft.md`)
Read the research file and `book2/content/00_voice.md`, then write a full chapter:
- **Opening**: a scene, observation, or claim that earns the reader's attention in the
  first paragraph. No slow wind-ups.
- **Sections** (4–6, with clear headers): each section makes a sub-argument that
  advances the chapter's thesis
- **The skeptic turn**: one section explicitly addresses the strongest objection
- **"What Changes Monday"**: the closing section — direct, second-person, concrete.
  What to stop doing. What to start doing. The longer-term shift.
- No software tool names, model names, or company-specific products
- Engineering history and organizational examples where possible

Length: 3,000–4,500 words.

### Phase 3: Critique (`{id}_critique.md`)
Edit your own draft against 5 criteria:

1. **Thesis alignment**: Does every section serve the chapter's core argument? Flag drift.
2. **Aging risk**: Any tool/vendor/company names that will date the book? Flag each one
   with a suggested rewrite using principles instead of products.
3. **Argument quality**: Is the core argument stated clearly? Are claims supported?
   Are counter-arguments addressed? What's weak or hand-wavy?
4. **Voice check**: Any sections that feel like management consultant boilerplate,
   vague encouragement, or tech journalism? Name them.
5. **Practitioner utility**: After each section, does a senior engineer reading this
   know what to do differently? Avoid generic advice that sounds good but changes nothing.

Format: for each issue, quote the passage → explain the problem → suggest the fix.
End with: 3 things that work well, top 3 priority fixes.

### Phase 4: Final (`{id}_final.md`)
Rewrite the draft incorporating the critique's priority fixes:
- Fix every aging reference
- Strengthen weak or hand-wavy arguments
- Tighten sections that drift from the thesis
- Preserve what the critique said works well
- Ensure the "What Changes Monday" section is as concrete and actionable as possible

The final chapter should feel authoritative, useful, and like something a senior engineer
would forward to a colleague.

---

## Parallelism

For the research phase, use subagents to research multiple chapters simultaneously.
When the user asks to research several chapters at once, spawn parallel subagents —
one per chapter — and have each save its research file independently.

For draft/critique/final phases, run sequentially: each phase depends on the previous.

---

## Status Reporting

When asked for status, run:

```
python3 book2/scripts/status.py
```

Or check `book2/content/` for existing files and report a table:

```
Chapter                          | research | draft | critique | final
---------------------------------|----------|-------|----------|------
p1_c1 Nobody Told You...         |    ✓     |   ✓   |    ✓     |  ✓
p1_c2 The Org Chart Is a Lie     |    ✓     |   ·   |    ·     |  ·
```

✓ = file exists, · = not yet done
