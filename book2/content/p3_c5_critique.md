# Editorial Critique: p3_c5 — "Why Reorgs Rarely Work"

---

## Overall Assessment

This is one of the stronger drafts in the book. The iceberg model is memorable, the historical case studies are substantive, and the "What Changes Monday" section is among the most actionable in the project so far. The core argument is stated clearly in the introduction and maintained throughout. The issues that follow are mostly matters of degree — tightening, clarifying, and cutting — rather than structural repair. One naming violation needs fixing, and a handful of passages drift into consulting boilerplate.

---

## Criterion 1: Thesis Alignment

The core argument is: reorganizations are a structural answer to what are usually incentive, communication, or strategy problems; structure is the most visible and least powerful lever; understanding which iceberg layer the problem lives in is the prerequisite for effective intervention.

**Every major section serves this argument.** The exceptions are minor:

### Issue 1.1 — "Six Patterns You've Seen Before" partially drifts

> "Each one follows the same script: a structural intervention, an unchanged actual bottleneck, eventual discovery that the change fixed nothing."

The six patterns section is the chapter's weakest thesis-alignment moment — not because the patterns are wrong, but because they function as a listicle rather than an argument. Five of the six scenarios end with a one-line conclusion ("The bottleneck was...," "The organizational container changed. The disagreement didn't.") that summarizes without extending the argument. After five examples, the reader has not learned anything new about *why* structure fails; they've seen confirmation of what the earlier sections already established. The section could be cut to three examples and use the reclaimed space to deepen the iceberg model or sharpen the diagnostics.

**Fix:** Cut two or three of the six patterns (the weakest are "merger that assumes away the real problem" and "flatness that isn't" — both restate earlier points without adding texture). Use the space to add a diagnostic prompt after each remaining example: what layer of the iceberg does this scenario point to, and what specifically would have needed to change?

### Issue 1.2 — The "Hard Alternative" section front-loads its weakest point

> "If the problem is genuine architectural misalignment between team structure and system structure, then a reorg is warranted..."

This appears *third* in the "Hard Alternative" section, after incentive and communication advice. But Conway's Law misalignment is the most rigorous justification for a reorg in the chapter, and it's already been developed at length in the "When Structure Actually Is the Problem" section. By repeating it here, the section implies the reader hasn't absorbed what came just before. This creates a pacing problem: the reader feels like the chapter is backing up when it should be landing.

**Fix:** In the "Hard Alternative" section, replace the Conway's Law paragraph with a forward reference ("If structural misalignment is the root cause — as diagnosed above — then restructure, but do it with the checklist from the previous section") and use that space to add more texture to the culture change timeline, which is currently the most hand-wavy of the four cases.

---

## Criterion 2: Aging Risk

The brief specifies: no company names, no specific tools, no named vendors. The draft almost adheres to this — but not completely.

### Issue 2.1 — Named company implied in the imaging technology case

> "An imaging technology company invented a key digital sensor in 1975."

This description narrows to exactly one company in the reader's mind. The 1975 digital sensor invention is a well-known historical footnote tied to a single named firm. Readers who know the story will supply the name. Readers who don't will look it up. The CLAUDE.md brief is explicit: use category descriptions only.

**Fix:** Change to: "A company that had dominated the physical imaging market for decades invented a key digital sensor in the mid-1970s." Remove "1975" specifically — that date is the identifier. Also remove the direct CEO quote ("'the enemy,' an 'evil juggernaut'") — it is sourced from a named interview and will invite attribution. Paraphrase it: "One CEO said publicly that the new technology would destroy the chemical business. That wasn't rhetorical excess — it was an accurate description of the incentive structure."

### Issue 2.2 — Named company implied in the computing company case

> "A major computing company, dominant in its market for decades, entered the late 1980s facing a changed competitive landscape..."

The description — dominant computing company, late 1980s, eight years of restructuring, decentralization into semi-autonomous lines of business, the CEO who reversed it — is specific enough to resolve to one company. The CEO quote ("'Culture isn't just one aspect of the game — it is the game'") is widely attributed to a named individual and would surface immediately in a search.

**Fix:** Paraphrase the CEO quote and genericize the timeline. Replace the quote with: "The CEO who ultimately reversed the strategy was direct: the problem was not the reporting lines. It was that internal culture rewarded divisional competition over customer outcomes." Remove the specific characterization of the CEO's turnaround philosophy; keep the structural point (incentive change accompanying structural change) without the attributed framing.

### Issue 2.3 — Hannan and Freeman citation

> "Sociologists Michael Hannan and John Freeman formalized this in their 1984 work on structural inertia theory."

The citation is appropriate — Hannan and Freeman are enduring academics whose work is not going to age out or become embarrassing. However, the specific year (1984) adds a footnote-like precision that will feel out of place in a book that otherwise avoids academic citation. More importantly, the passage introduces the theory without using it: the next two sentences restate points already made without adding what Hannan and Freeman specifically contribute.

**Fix:** Either use the citation to add a specific insight from the theory that isn't already in the chapter (e.g., the concept of organizational "density dependence" or how selection pressures on reliability create path dependence in structure), or cut the citation and keep the insight in plain language. Keeping a name without the value of the citation creates the impression of credentialing without substance.

---

## Criterion 3: Argument Quality

### Issue 3.1 — The "roughly three-quarters" statistic is unanchored

> "The research on reorganization outcomes is bleak: roughly three-quarters of corporate reorganization efforts fail to meet their objectives, with a substantial fraction never completed at all."

This statistic is doing load-bearing work (it substantiates the chapter's central premise) but it floats without sourcing. "The research" is not the same as naming a study. The 75% figure circulates widely in management literature, often with conflicting definitions of "failure." A reader who investigates will find the number contested.

**Fix:** Either anchor the claim with a source type ("A widely-cited analysis of major corporate restructurings across two decades found...") and make the definition of failure precise, or change the framing to be more epistemically honest: "Estimates of reorg failure rates range widely in management research, but the consistent finding is that structural changes alone — without accompanying changes to incentives or decision rights — rarely sustain the behavior changes they were designed to produce."

### Issue 3.2 — The matrix management case buries its strongest point

> "The names changed. The underlying tension, and the underlying structural response, did not."

The matrix management history is well-told, but it ends one sentence too early. The case demonstrates the sixty-year cycle of structural rediscovery — which is compelling — but the payoff line ("the underlying tension did not") doesn't explain *why* the tension persists across reinventions. The explanation is already in the iceberg model: the functional-vs-project tension is an incentive and measurement problem (who does a functional specialist's performance review when they're embedded in a project team?), not a reporting-line problem. The matrix case is actually the best illustration of this point in the chapter, and the chapter doesn't use it.

**Fix:** Add two sentences at the end of the matrix paragraph: "The functional-project tension that matrix was designed to solve is an incentive problem: whose interests does the specialist serve when their functional manager and their project lead want different things? Every reinvention of matrix structure — under whatever name — imports that same unresolved measurement question. The structure changes; the incentive conflict doesn't."

### Issue 3.3 — The culture-change advice is hand-wavy

> "Culture changes through sustained changes in what is rewarded and what is penalized in practice, who gets promoted, what leaders model in their own behavior, and what stories the organization tells about itself."

This is accurate but abstract enough to be unhelpful. Four mechanisms are listed; none are explained with enough precision for a reader to act on them. "What stories the organization tells about itself" in particular sounds like management-book filler.

**Fix:** Cut "what stories the organization tells about itself" and replace with a concrete mechanism: "and what incidents get treated as defining versus forgettable — the postmortem that becomes a case study versus the one that gets quietly filed away." Then add one sentence explaining why this timescale matters: "Culture lags incentive changes by roughly eighteen to thirty-six months because it requires enough instances of the new behavior being rewarded — and the old behavior not being — for the pattern to become internalized as a norm."

---

## Criterion 4: Voice Check

### Issue 4.1 — "Clearer ownership, better alignment, more focus" list is consulting boilerplate

> "If the answer is vague ('clearer ownership,' 'better alignment,' 'more focus'), push for specificity."

The passage correctly identifies these phrases as vague, but reproducing them three times in a row mimics the very language it's critiquing. The parenthetical functions like a management consulting slide of buzzwords. The irony may be intentional, but the effect is that the reader skims it as more management-speak rather than seeing the critique land.

**Fix:** Replace the parenthetical with a single concrete example of a vague answer and its specific interrogation: "If the answer is 'clearer ownership,' ask: ownership of what decision, measured how, backed by what budget authority? If no one can answer that, the reorg is theatrical."

### Issue 4.2 — "phenomenologically indistinguishable from actual progress" is consultant jargon

> "The volume of visible change activity is phenomenologically indistinguishable from actual progress."

"Phenomenologically" is a word that belongs in a philosophy seminar, not a book whose voice guide says "write like a candid senior peer." The sentence is trying to be precise but reads as affected.

**Fix:** "The volume of visible change activity looks, from outside the room, exactly like progress."

### Issue 4.3 — The action bias introduction over-explains itself

> "Action bias is well-documented in high-stakes contexts: a goalkeeper diving to one side during a penalty kick even though staying in the center would improve their odds; a physician ordering additional tests that provide no diagnostic value; a general ordering troop movements that generate visible activity with no strategic payoff."

Three examples in a row following the definition reads like a business-book padding pattern: define term, provide three illustrative cases, return to main argument. The goalkeeper example is the strongest and most memorable. The physician and general examples dilute it without adding more.

**Fix:** Keep the goalkeeper (it's concrete and memorable). Drop the physician and the general, or replace both with one sentence: "The same pattern appears anywhere high-stakes decisions are made under time pressure and uncertainty."

---

## Criterion 5: Practitioner Utility

### Issue 5.1 — "Do the layer diagnosis before you reach for structure" needs a tool

> "Instead, ask: which layer of the iceberg does this actually live in? Is the problem that the org chart creates the wrong communication routing, or is the problem that the incentive structure creates the wrong behavior?"

This is good advice but it requires the reader to hold the entire iceberg model in mind and apply it without any scaffold. The chapter has already built the model; the "What Changes Monday" section should operationalize it. Instead it restates the model.

**Fix:** Add a four-question diagnostic the reader can use in the next friction-filled meeting: "(1) If we changed nothing but the reporting lines, would the behavior change? (2) If we changed what people are measured on, would the behavior change? (3) If we changed who attends which meetings, would the behavior change? (4) If nothing is different a year from now, what specifically hasn't changed — and where in the iceberg does that live?" This converts the model from an explanatory frame to a practical tool.

### Issue 5.2 — The post-reorg window advice is the sharpest practitioner content and should come first

> "If a reorg is genuinely coming and you cannot stop it, use the window it creates."

This is the most tactically useful paragraph in the chapter — it gives a reader who cannot stop a reorg something concrete to do. But it appears last in the "What Changes Monday" section, after three paragraphs of more general advice. Readers who are facing a reorg right now — which is the scenario where this advice is most urgent — have to wade through general principles to get to it.

**Fix:** Move this paragraph to second position in the "What Changes Monday" section, immediately after the "stop treating a new org chart as an intervention" paragraph. Sequence the section: (1) what to do when you're skeptical of a reorg being designed, (2) what to do when a reorg is happening anyway, (3) what to do when you're in a position to change incentives directly, (4) how to run the layer diagnosis.

### Issue 5.3 — "Change those, and the structure will find itself" is too cute for the book's register

> "Change those, and the structure will find itself."

The final sentence tries to land with an aphorism, but "the structure will find itself" is ambiguous and slightly precious. The book's voice is direct. This sounds like a chapter ending in a management book trying to close on a memorable note.

**Fix:** Replace with something that closes on the actual argument: "Change those, and the structure becomes secondary — because the real work was never about the chart."

---

## What Works Well

**1. The opening paragraph earns its length.** The description of reading a reorg announcement email — "You read it twice" — is immediately recognizable and sets up the chapter's argument in scene rather than statement. This is the book's voice at its best: specific, slightly rueful, technically credible. Do not cut it.

**2. The iceberg model is load-bearing in exactly the right way.** The four-layer model (visible structure / behavior / culture / incentive architecture) is introduced early, referenced throughout, and operationalized at the end. It gives the chapter's argument a concrete scaffolding that the reader can carry into their own organization. This is the chapter's most durable contribution.

**3. The "When Structure Actually Is the Problem" section is the strongest counterargument handling in the Part III drafts.** The chapter doesn't just gesture at exceptions — it gives the reader a real diagnostic ("is the current structure actively misrouting communication or decision authority?") and a checklist for a load-bearing reorg. This is honest about the limits of the core argument in a way that strengthens rather than undermines it.

---

## Top 3 Priority Fixes

**Priority 1: Remove the company-identifying details from both historical cases (Issue 2.1, 2.2).** This is a brief violation and the most pressing fix before this draft advances. The imaging company case needs the 1975 date removed and the CEO quote paraphrased. The computing company case needs the CEO quote genericized. Both cases retain their argumentative value with these changes — the specific dates and quotes add color but not substance.

**Priority 2: Add a four-question diagnostic tool to the "What Changes Monday" section (Issue 5.1).** The chapter's central framework is the iceberg model. The "What Changes Monday" section restates the model but doesn't operationalize it. A concrete four-question diagnostic converts the chapter's best idea into something a reader can use in the room next Tuesday. This is the highest-leverage addition available to this chapter.

**Priority 3: Cut the "Six Patterns" section to three examples and add iceberg-layer callouts to each remaining one (Issue 1.1).** The six-pattern section is the chapter's pacing problem. Three strong examples with explicit iceberg-layer analysis would be more effective than six brief examples that confirm what the reader already knows. Each remaining example should end with a sentence like: "The root cause is in the incentive layer, not the structure layer — and no new reporting line fixes it."
