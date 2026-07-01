# Critique: p1_c1 Draft — "Nobody Told You This Was the Job"

---

## 1. Thesis Alignment

**Overall:** The draft's thesis is stated clearly and most sections serve it. The core claim — that the skills that get engineers promoted are necessary but not sufficient, and that nobody explains the transition — is present throughout. However, two sections drift or underdeliver.

---

**Issue 1.1 — "This Book and What It Isn't" drifts into table-of-contents territory**

> "The topics covered — incentives, organizational structure, decision-making, communication, the economics of technical work, leadership without formal authority — are not peripheral to the engineering job at senior levels. They are the job."

The paragraph before this does the right thing: it defines what the book is not. But the section then shifts from the chapter's core argument (the transition nobody explains) into previewing the rest of the book. That's a structural function, not an argument. The reader at this point wants to be told what to do differently, not what the next fifteen chapters cover.

**Fix:** Compress the book-orientation content to two sentences maximum and redirect the section toward reinforcing the core thesis: the organizational domain is real, learnable, and part of the senior engineering job. Cut the laundry list of topic areas. If a preview of the book is needed, fold it into the "What Changes Monday" closing.

---

**Issue 1.2 — The opening scene sets up but doesn't fully pay off**

The opening is strong — vivid, immediately recognizable, drops the reader into a specific experience. But it ends with: "You walked out thinking the decision was wrong. Maybe it was. But you also didn't fully understand what you were playing." This is the right beat, but it's followed by a section heading break and then a new section rather than a direct escalation. The first paragraph of the following section ("There's a structural dishonesty built into how engineering organizations promote people...") is actually a stronger thesis statement than anything in the opening.

**Fix:** The opening scene should build directly to the chapter's thesis statement rather than cutting away. Either close the opening scene with the explicit thesis, or use a short transitional paragraph before the first section header that names what the rest of the chapter will do.

---

## 2. Aging Risk

**Issue 2.1 — No hard aging risks found**

There are no named tools, vendors, frameworks, or companies in the draft. The historical references (Brooks, Peter, Dijkstra, Weick, Simon) are all durable and appropriate for the audience. The scenarios use categories ("a team at a mid-size organization," "a tech lead," "a VP") as instructed.

**Minor note:** The phrase "survey after survey" in the "This Book and What It Is" section is vague enough to be acceptable, but could be slightly strengthened with a more precise characterization — "project failure studies spanning several decades" or similar.

---

## 3. Argument Quality

**Issue 3.1 — The Weick/sensemaking reference is introduced but not applied**

> "Karl Weick's work on organizational sensemaking helps here. Organizations, he argued, are not rational machines that process inputs into optimal outputs. They're collections of people constructing coherent narratives about ambiguous situations... given the information they have, the incentives they're operating under, and the narrative they're constructing, what are they doing that's locally rational?"

This is the right framework. But the draft introduces it and then pivots to Herbert Simon in the very next section, and the sensemaking lens is never used to analyze a specific scenario. It reads as a citation rather than an argument. The Scenario C material (the technically correct rewrite proposal that gets deprioritized) is the natural place to apply sensemaking: the VP isn't irrational — they're constructing a coherent narrative about risk, given the failed migration in organizational memory. The draft hints at this but doesn't name it.

**Fix:** When the Scenario C example lands in "The Rule Change Nobody Announced," explicitly tie the VP's behavior back to the sensemaking frame introduced earlier. "This is what Weick's sensemaking looks like in practice" — or just say it without attribution: the VP is constructing a coherent story about risk based on available information, not blocking good engineering.

---

**Issue 3.2 — The Peter Principle reference is under-used**

> "Laurence Peter observed in 1969 that people tend to be promoted until they reach the level of their incompetence. In engineering, this observation has a specific and non-comedic form..."

This is correctly introduced as applying specifically to engineering. But it disappears after being mentioned. The "non-comedic form" (the absence of training in a different set of skills) is stated once but not illustrated with a scenario. Scenario F from the research notes — the new tech lead who keeps coding — is the perfect illustration and is conspicuously absent from the draft.

**Fix:** Add a version of Scenario F (the tech lead who keeps producing code rather than doing the actual tech lead work) either in "What the Promotion Was Actually For" or in "The New Problems Don't Look Like Problems." It's the most vivid illustration of the Peter Principle claim and makes the abstract point concrete.

---

**Issue 3.3 — The skeptic's turn addresses only one of the two counter-arguments**

The research notes identified two strong counter-arguments:
1. "This is just management work — stay technical"
2. "The organizations are just broken — fix the org, don't ask engineers to adapt"

The draft handles counter-argument 1 well. Counter-argument 2 is not addressed. A reader who agrees that organizational dynamics are important will still push back: "Fine, but the answer is organizational reform, not asking individuals to cope with dysfunction." This objection is more sophisticated and the reader who is already sympathetic to organizational analysis will raise it.

**Fix:** Add one paragraph in the skeptic section — or a brief acknowledgment in "This Book and What It Is" — that addresses counter-argument 2. The response from the research notes is the right one: both things are simultaneously true. The organizations are structurally broken in ways this book describes. Understanding the dysfunction is the precondition for changing it, not a substitute for changing it. The goal is legibility as a precondition for leverage.

---

**Issue 3.4 — Word count is below the target floor**

The draft is approximately 2,735 words against a target of 3,000–4,500. The under-length is partly attributable to the Scenario F omission (above) and the thin skeptic section. The final should land at 3,000–3,500 words after the fixes above; that's the right length for this content.

---

## 4. Voice Check

**Issue 4.1 — "This Book and What It Is" has a management-book register in places**

> "This is not an argument that organizational concerns should override technical judgment. Organizations make technically wrong decisions all the time; they have broken incentive structures; they reward the wrong things."

The sentiment is correct and the book's voice guide permits directness. But "they have broken incentive structures; they reward the wrong things" is a list that sounds like a management consultant's problem taxonomy. The voice should be more specific and more rueful — more "here is a thing you've seen happen" and less "here are the pathologies we have identified."

**Fix:** Ground each observation in a specific, brief scene rather than listing abstractions. "Organizations make technically wrong decisions because the person with the most organizational capital won the room, not because the technical case was weak" is more direct and more honest than "organizations reward the wrong things."

---

**Issue 4.2 — The closing line risks being too tidy**

> "Nobody told you this was the job. Now you know."

This callback to the title is earned — it closes the loop. But it comes after a "What Changes Monday" section that is already doing the closing work, so the final sentence feels slightly like a motivational poster. The section would be stronger if it ended on the concrete actionable note rather than a rhetorical flourish.

**Fix:** Either cut "Nobody told you this was the job. Now you know." or move it to the *beginning* of the "What Changes Monday" section, where it would function as a transition into the actionable content rather than a closing epigram. Ending on concrete action is stronger than ending on a memorable phrase.

---

**Issue 4.3 — Dijkstra's EWD manuscript reference is slightly name-droppy without adding content**

> "Dijkstra — whose technical credentials nobody questioned — wrote extensively in his unpublished manuscripts about the separation between what computers do and what the organizations around computers do..."

The parenthetical "(whose technical credentials nobody questioned)" is doing insecurity-signaling work — it's a defensive move that the voice guide says to avoid. The point doesn't need defending if it's made well.

**Fix:** Drop the credentialing parenthetical. Just: "Dijkstra wrote extensively about the separation between what computers do and what the organizations around computers do as the central unsolved problem of computing."

---

## 5. Practitioner Utility

**Issue 5.1 — "The New Problems Don't Look Like Problems" ends without a concrete takeaway**

The section describes the problem well (organizational work has diffuse outputs and long feedback loops) but doesn't give the reader a tool for recognizing it in the moment. A senior engineer reading this section will nod, but what does it change about Monday?

**Fix:** Close the section with a brief, concrete diagnostic question: "When the thing in front of you doesn't have a spec and doesn't have a test suite, ask whether it's actually an organizational problem wearing a technical disguise." Or equivalent — the specific phrasing matters less than giving the reader something to do with the observation.

---

**Issue 5.2 — "What Changes Monday" is good but could be more specific about the diagnosis step**

> "Instead, ask: what are the incentives and constraints of the people involved, and do I actually understand them?"

This is better than generic advice, but it's still a principle rather than a method. The reader needs a starting point for the diagnosis — what specifically to look for, or what question to ask first.

**Fix:** Add one more sentence: "Start with the person whose buy-in you don't have. What would they lose if this proposal succeeded? What do they care about that the proposal doesn't address? Those answers are usually findable before the meeting, not after."

---

## What Works Well

1. **The opening scene is immediately effective.** The three-week architectural proposal that got overridden for organizational reasons — the sales commitment nobody mentioned, the conversations that happened in rooms the engineer wasn't in — is specific, recognizable, and drops the reader into the experience without setup. It doesn't explain itself. That's exactly right.

2. **The satisficing framework and Scenario C are genuinely useful.** The treatment of Herbert Simon's satisficing in "The Rule Change Nobody Announced" does what the voice guide asks: it takes an abstract framework and applies it to a concrete engineering scenario in a way that changes how the reader might approach their next proposal. The observation that "a technically sound proposal that accounts for organizational reality will almost always outperform a technically superior proposal that doesn't" is the kind of sentence a reader will remember.

3. **The skeptic section is honest about the limits of the argument.** The counter-argument ("I'm an engineer; that's what managers are for") is presented fairly before being rebutted. The rebuttal doesn't strawman the objection — it grants the logic and then shows why the premise (that someone else is managing the organizational dynamics well) is usually false. That's the right way to handle a strong objection.

---

## Top 3 Priority Fixes

1. **Add Scenario F (the tech lead who keeps coding) to "What the Promotion Was Actually For" or "The New Problems Don't Look Like Problems."** This is the single best illustration of the Peter Principle claim in the research notes and its absence makes the most practically useful section of the chapter less concrete than it should be.

2. **Address counter-argument 2 ("fix the org, don't ask engineers to adapt") in the skeptic section.** The current version handles one of two strong counter-arguments. The second one — that individual adaptation is the wrong response to structural dysfunction — is more sophisticated and will be raised by the most thoughtful readers. The draft needs to address it.

3. **Revise "What Changes Monday" to include a specific diagnostic method for understanding stakeholder incentives**, not just the instruction to ask about them. The section currently names the right question; it needs to give the reader a starting point for answering it. End on the concrete action, not the rhetorical callback to the title.
