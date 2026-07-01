# Editorial Critique: p5_c3 — What Staff Engineers Actually Do

---

## 1. Thesis Alignment

**Overall:** The chapter holds its thesis well. The core claim — staff engineering is a categorically different job whose product is direction, synthesis, and organizational clarity — is stated early and revisited throughout. Most sections earn their place. Two alignment issues worth addressing.

**The archetypes section mostly works, but drifts at the edges.**

> "There is a useful framework here, not as a taxonomy but as a diagnostic. Four archetypes describe the range of ways staff engineering manifests in practice, and the most useful question is not 'which one am I?' but 'which description of the week sounds like the work my organization actually needs from me?'"

The framing disclaimer ("not as a taxonomy but as a diagnostic") is good instinct. The execution is uneven. The Tech Lead, Architect, and Solver descriptions each tie back to the thesis: different scope, different product, different success criteria. The Right Hand description is where it drifts:

> "A Right Hand at a growing organization might spend their week on something that doesn't look like engineering from the outside at all, but that is shaping the technical trajectory of the whole organization through the decisions they inform."

This is vague enough to describe a management role as easily as a staff engineering role. The sentence that was supposed to distinguish the Right Hand from management ("without being management itself") is doing all the load-bearing work without support. Either give a concrete example of what a Right Hand does that a VP of Engineering would not, or cut the archetype to three.

**Fix:** Add one specific example to the Right Hand description — something like: a senior staff engineer who has no direct reports sits in on every major organizational decision in an advisory capacity and writes the technical analysis that shapes the final call. The VP makes the decision; this person makes the VP's decision better. That distinction is worth making explicit.

**The scope model is stated clearly and works diagnostically.**

> "Ask yourself: what is the largest unit whose success is materially affected by my work?"

This is the cleanest diagnostic question in the chapter. It appears early in "The Job Changed When You Weren't Looking" and threads through coherently. No fix needed — keep it prominent.

**Minor drift in the Skeptic's Turn.** The second objection ("staff engineer is a made-up title with no consistent meaning") is a legitimate argument to address, but the response meanders into Bell Labs history before landing. The history is interesting and consistent with the book's voice, but the transition from the three-question diagnostic to the title-inconsistency argument feels abrupt. The Skeptic's Turn has two distinct objections that are not clearly separated — consider a brief signpost between them.

---

## 2. Aging Risk

**The chapter is largely clean.** No named companies, tools, or frameworks appear. Three items warrant scrutiny.

**Item 1: No violation.** The "glue work" observation is not attributed to any named person.

> "There is a well-documented observation about the category of work called glue work..."

"Well-documented" is sufficient. No attribution, no aging risk. Good.

**Item 2: Bell Labs Fellow track — approved.** The Bell Labs reference appears once in the Skeptic's Turn:

> "The role exists because organizations face a structural problem that the Bell Labs research labs understood in the mid-twentieth century..."

This is in the approved exception list. No issue.

**Item 3: Knuth — approved.** The Knuth reference appears once in "Staying Technical Without Getting Stuck in the Code":

> "Knuth's career makes a clean illustration of the principle, even if the scale is unusual."

Approved exception. No issue.

**Item 4: The guild system reference — approved with a note.** The guild/medieval master analogy in "The Work That Doesn't Show Up in the Commit Log" is endorsed by the approved list. One note: the analogy is used well but the word "maybe" in the final sentence weakens it unnecessarily:

> "A master who lost the craft depth became something else — a guild administrator, maybe useful, but not a master in the substantive sense."

"Maybe useful" reads as hedging. "Sometimes useful, always diminished" is more precise and keeps the register consistent.

**No violations found.** The chapter is clean on aging risk.

---

## 3. Argument Quality

**The scope model is diagnostic; the commit-log section is concrete; the Skeptic's Turn has a gap.**

**The scope model works.**

> "Ask yourself: what is the largest unit whose success is materially affected by my work? For a strong senior engineer, the honest answer is usually your team... For staff engineering, the honest answer should be multiple teams."

The three-tier progression (team → multiple teams → organization) is stated clearly and reinforced with specific examples. The test is actionable: a newly-promoted staff engineer can answer the question honestly and see the gap. This is one of the strongest passages in the chapter.

**The "canonical staff week" is the most useful concrete passage.**

The Monday-through-Friday reconstruction is specific enough to be recognizable and useful. The parenthetical at the end — "Note what is not in that week: writing production code. Note what is hard to measure: almost all of it" — lands cleanly. No fix needed.

**The Skeptic's Turn addresses the failure mode but the three-question diagnostic is partly broken.**

> "Is your technical judgment still current and accurate? Not 'do you feel confident in your opinions' — that is not the same thing. Ask: when you weighed in on a technical decision in the last six months, did the outcome validate the judgment, or did the engineers who implemented it find that your model of the system was wrong in important ways?"

Question one is honest and usable. But it assumes the staff engineer has access to outcome data — that they stayed close enough to the implementation to know whether their call was right. A staff engineer whose judgment has genuinely drifted is also likely to have drifted away from implementation feedback loops. The diagnostic may fail precisely where it is most needed. The question needs a fallback: "If you don't know whether your recommendation held up, that absence of feedback is itself diagnostic."

> "Are teams producing better outcomes because of your engagement? Not better outcomes than teams without any staff engineer. Better outcomes than they would have produced from you specifically."

This is a well-framed question, but "better outcomes" is underspecified. Better in what sense? Faster? More architecturally sound? Less rework? Without a concrete proxy, "better outcomes" is an easy rationalization — the staff engineer tells themselves yes and moves on. Suggest adding: "Name one decision a team made differently because of your input, and describe the outcome."

> "Is there work that could only have happened with you involved? Something that required the specific combination of context, judgment, and organizational position you have..."

Question three is the strongest. The phrasing "required the specific combination" is precise. This is the question the audit in "What Changes Monday" extends — the two passages could reference each other more explicitly.

**The technical credibility argument needs one more sentence.**

> "The minimum bar is this: a staff engineer should be able to read a design document for a system they have not been working on daily and identify whether the assumptions are current and whether the approach is consistent with the organization's technical direction."

This is good. It is concrete and testable. The gap is that it does not say what to do if you can't meet this bar. The chapter mentions "becoming technically uncomfortable again" in the Skeptic's Turn, but the mechanism is vague. One sentence here — "The way back is deliberate immersion: take the next non-trivial technical investigation yourself rather than delegating it" — would make the passage actionable rather than diagnostic-only.

---

## 4. Voice Check

**The chapter's voice is mostly strong — candid peer, technically grounded.** Two passages slip toward HR rubric.

**Passage 1:**

> "You are no longer optimizing your own work. You are optimizing the conditions under which other engineers do their best work."

The phrase "do their best work" is soft-focus management language. It sounds like a performance review template. The chapter is making a sharp point — your output is now other people's output — but the phrasing undercuts the sharpness.

**Suggested rewrite:** "You are no longer optimizing your own output. You are the conditions under which other engineers' output gets better or worse." Blunter, more accurate, consistent with the chapter's register.

**Passage 2:**

> "If you are a senior engineer who wants to grow toward this role, there are three things to start doing now."

The "three things" list construction is a tic of management content. Each of the three things is substantive and specific, but the framing sounds like a LinkedIn carousel. The instructions are concrete enough to survive the critique, but the opening sentence could be more direct.

**Suggested rewrite:** "If you want to grow toward this role, stop waiting for the title to start the work." Then continue with the three practices, framed as habits to build rather than a checklist to execute.

**Passage 3 (minor):**

> "The path forward is not to conclude that staff engineering is pointless. It is to understand what makes the role valuable — technical synthesis, credible direction-setting, multiplying others — and to start doing those things, which may mean becoming technically uncomfortable again."

"Multiplying others" is a phrase that has been used enough in engineering management writing to feel borrowed rather than coined. It also appears in the adjacent p5_c2 chapter (The Multiplier Effect), so it carries cross-chapter weight. Consider: "amplifying other engineers' judgment" or simply "making the engineers around you more effective on problems that exceed any one of them."

---

## 5. Practitioner Utility

**The three-audience structure in "What Changes Monday" dilutes focus.**

> "If you are a senior engineer who wants to grow toward this role... If you are newly promoted to staff... If you are an established staff engineer..."

Three audiences in one closing section is one too many. The newly-promoted engineer is the most critical audience for this chapter — they are the person most likely to be confused and ineffective for exactly the reasons the chapter describes. The aspiring senior engineer advice (scope your thinking, write synthesis documents, attend cross-team reviews) is good but could appear earlier in the chapter as observable habits rather than a closing checklist. The established staff engineer audit question is strong and should not be buried.

**Fix:** Collapse the closing section to two audiences: newly-promoted and established. Move the "scope your thinking / write synthesis / attend cross-team reviews" guidance into the body of the chapter, attached to whichever section it serves best. The senior engineer aspiring to the title does not need a dedicated closing paragraph — the whole chapter is already useful to them.

**The audit question is operational, but needs one more sentence.**

> "Over the last month: what work happened only because you existed? What would have happened anyway, maybe just more slowly or less well? What would not have happened at all?"

This is a strong audit. The three-tier distinction (happened because of you / happened anyway / didn't happen without you) is precise and usable. It does not need heavy scaffolding. One addition would sharpen it: tell the reader what a passing answer looks like. "If the third category is empty or you can't name a specific example, that is the answer." Without a reference point, engineers will grade themselves on a curve.

**The newly-promoted advice is not specific enough.**

> "You already know how to do excellent senior engineering. The new job is to ask, at the end of each week, whether the scope of your impact extended beyond your team — and to be honest about the answer."

The weekly scope check is a useful habit, but "be honest about the answer" is the weakest sentence in the chapter's closing. It invites self-assessment without giving the engineer any tools to correct a bad answer. The chapter has already established the scope question as diagnostic — this passage should point back to a specific corrective action, not to honesty in the abstract.

**Suggested rewrite:** "At the end of the week, ask whether anything you did affected a team other than your own. If the honest answer is no three weeks in a row, you are still doing senior engineering. The fix is to deliberately take on one piece of cross-team work — a design review for a team you don't normally engage with, a synthesis of two initiatives that aren't talking to each other — and see what it surfaces."

---

## 3 Things That Work Well

**1. The scope diagnostic question.** "What is the largest unit whose success is materially affected by my work?" is the best single sentence in the chapter. It is concrete, honest, and gives the reader a self-test they can apply immediately without interpretation. Keep it prominent and do not dilute it.

**2. The canonical staff week.** The Monday-through-Friday reconstruction is the chapter's most useful passage for someone who has never seen the role from the inside. It is specific enough to be recognizable and honest about what is absent (production code) and what is hard to measure (nearly everything else). It deserves to stay exactly as written.

**3. The guild master analogy.** The medieval master/craft depth argument earns its place. It is historically grounded, the parallel is precise (not just decorative), and it clarifies the distinction between glue work with technical substance and glue work without it in a way that a clinical description would not. It also fits the book's voice — engineering history used as credibility, not ornament.

---

## Top 3 Priority Fixes

**Priority 1: Repair the three-question diagnostic in the Skeptic's Turn.**
Question one needs a fallback for the engineer who has lost access to implementation feedback loops. Question two needs a concrete proxy for "better outcomes" to prevent easy rationalization. These are the most technically important fixes in the chapter — the Skeptic's Turn is where the reader most needs precision, and the diagnostic as written has at least two paths to false negatives.

**Priority 2: Collapse "What Changes Monday" to two audiences and strengthen the newly-promoted advice.**
The aspiring senior engineer advice belongs in the body of the chapter. The closing section should focus on the two readers most at risk: the newly-promoted staff engineer who is still doing senior engineering, and the established staff engineer auditing their leverage. The newly-promoted advice currently ends with "be honest about the answer" — it needs a specific corrective action, not a call to self-awareness.

**Priority 3: Fix the two voice violations.**
"Do their best work" and "multiplying others" both drift toward management-content register. Neither is a major problem in isolation, but together they soften a chapter that otherwise maintains a harder, more useful edge. The rewrites are minor — one sentence each — but they matter for the chapter's authority and for consistency with the book's stated voice.
