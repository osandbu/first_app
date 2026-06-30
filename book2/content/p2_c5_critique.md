# Critique: p2_c5 — Why Good Engineers Do Bad Things

## Chapter's core argument (as stated)

> "Most performance problems that look like character problems are situation problems. This is not an excuse. It is a more accurate diagnosis, and a more accurate diagnosis leads to interventions that actually work."

Restated in the chapter's own terms: dysfunctional engineer behavior is almost always structurally caused; the fundamental attribution error leads us to blame individuals rather than fix structures; understanding the structural cause is the first step to change.

---

## Criterion 1: Thesis Alignment

The chapter's central argument is stated clearly and held through most of the draft. But two sections create drift worth naming.

---

**Issue 1.1 — "Normal Accident Theory" shifts from thesis support to genre switch**

> "In 1984, sociologist Charles Perrow published a study of industrial accidents that changed how people thought about safety and organizational failure. His argument: in systems that are both *complex* and *tightly coupled*, accidents are not anomalies. They are properties of the system."

The Challenger and Therac-25 cases are doing genuine thesis work: they show capable people making locally rational decisions inside structures that made bad outcomes predictable. The Perrow subsection shifts the chapter's frame from "individual behavior explained by structure" to "systems theory" at large. Perrow is about accident *inevitability* in complex-tightly-coupled systems. The chapter's argument is about individual *behavior* shaped by incentives and organizational design. These are related but not the same, and the subsection never fully completes the bridge.

The paragraph that follows — "the engineer is not the cause. They are the point of failure that a well-designed system would have been resilient to" — actually does the thesis work. The Perrow subsection is scaffolding for that sentence. The question is whether four paragraphs of systems theory are needed to earn one sentence, and whether a reader who has absorbed Challenger and Therac-25 needs it at all.

More precisely: Normal Accident Theory argues that accidents are *inevitable* in certain system configurations. The chapter's thesis is more circumscribed — that behavior attributed to character is better explained by structure. These two claims are compatible but the stronger Perrow claim (accidents are inevitable, period) can undercut the chapter's more actionable argument (if you change structures, you change behavior), because it implies some outcomes are unreachable by structural redesign.

**Suggested fix:** Either compress the Perrow section to two sentences that extract the one relevant insight — "systems that are tightly coupled and complex fail through component interactions, not individual decisions" — or drop the framing label entirely and integrate the insight directly into the Therac-25 analysis, where the tight coupling (dependencies that accumulated around the deferred fix) is already on the page. The concepts are useful; the named theory creates a mini-lecture that interrupts the chapter's narrative momentum.

---

**Issue 1.2 — "Slack Is Not Waste" is the chapter's most thesis-aligned section but slightly undersells its connection to the opening argument**

The DeMarco section is strong and correctly positioned. Its thesis connection is clear: running at full capacity produces the same behaviors (skipping documentation, deferring maintenance, cutting corners) that earlier sections show being misattributed to character. The structural cause is resource allocation, not personal values.

The one gap: the section explains *why* these behaviors occur under constraint (cognitive narrowing, hyperbolic discounting) but doesn't explicitly invoke the fundamental attribution error that anchors the chapter's thesis. A manager reading this section and watching an engineer ship known risks will not automatically make the connection to the opening argument without one bridging sentence.

**Suggested fix:** After "This is a failure of resource allocation" — add a single sentence: "And yet the postmortem attribution is almost always to the team lead's risk tolerance, not to the schedule that made that tolerance rational." This closes the loop back to the chapter's opening scene and makes the FAE the spine that connects all five behavioral examples.

---

## Criterion 2: Aging Risk

This draft handles aging risk well overall. No software tools, frameworks, or company names appear. Two items warrant attention.

---

**Issue 2.1 — Challenger and Therac-25 as engineering history examples**

> "**Challenger, 1986.** ... **Therac-25, 1985–1987.**"

Both are engineering classics and their use is appropriate. Challenger is widely known outside engineering culture. Therac-25 is firmly established in software engineering education — Nancy Leveson's analysis has been assigned reading for decades. No aging risk here; these are the right kind of historical anchor.

One mild concern: Feynman's dissent is referenced by name ("Richard Feynman, in his famous dissent..."). Feynman remains a credible citation, but calling the dissent "famous" invites the question: famous to whom? A senior engineer in 2030 joining from a non-US background or a non-traditional path may not have that as a reference point. The word "famous" is unnecessary and slightly self-satisfied.

**Suggested fix:** Drop "famous" — "Richard Feynman, in his dissent from the Rogers Commission report" carries the same authority without the implicit assumption of shared cultural knowledge.

---

**Issue 2.2 — DeMarco citation is handled well but the book title is absent**

> "In 2001, Tom DeMarco published a short book arguing that the most costly mistake in managing knowledge workers is running them at full capacity."

The book is *Slack* and not naming it is probably the right call — book titles date and the specific title "Slack" has acquired a competing meaning. The framing ("a short book") is appropriately unanchored. No fix needed; noting this as a correct authorial choice.

---

## Criterion 3: Argument Quality

---

**Issue 3.1 — The fundamental attribution error is introduced but never precisely defined**

> "There is a well-documented tendency in human judgment called the fundamental attribution error. The name comes from work in social psychology in the 1970s, and the finding is this: when we observe other people's behavior, we systematically overweight their character and underweight their situation as explanations."

The definition is accurate but partial. The standard formulation of the FAE includes the actor-observer asymmetry (we attribute others' behavior to character; we attribute our own to situation) — which the chapter does include two sentences later. But the chapter doesn't name the theorists (Lee Ross, Fritz Heider) or the research lineage, which is probably fine for this audience. The more significant omission is that the chapter attributes the FAE to "human judgment" generically but then applies it specifically to managers and peers in postmortems — without establishing *why postmortems in particular* produce this error at such high rates.

The implicit answer is present elsewhere (it requires less information, it's more emotionally satisfying), but the connection between the general cognitive tendency and the specific postmortem context could be made explicitly. Why is the postmortem environment structurally designed to activate this error? The named-individual-in-the-hot-seat, the retrospective lens, the social need to explain — each amplifies the FAE beyond baseline. The chapter gestures at this but doesn't land it.

**Suggested fix:** After "Blaming the engineer requires only the name and the call" — add one sentence naming the structural feature of postmortems that amplifies the FAE: "The postmortem format, focused on a timeline of events and decisions, directs attention toward the person who made each call — which is exactly the prompt that activates character explanation over situational explanation." This tightens the bridge between the cognitive science and the organizational context.

---

**Issue 3.2 — The five behavioral examples are uneven in analytical depth**

The five cases in "What the Reward System Actually Rewards" vary noticeably in how thoroughly the structural cause is developed:

- *Deferring maintenance* and *Not writing documentation*: both excellent. The structural diagnosis is precise (backlog prioritization process, absence of documentation as sprint deliverable). The reader can see the mechanism.
- *Hoarding knowledge*: good. The job security incentive is clear. The one gap: the section doesn't address why *organizations* set up this incentive structure — specialization as career advancement is a compensation system choice, and naming that would deepen the diagnosis.
- *Over-engineering under ambiguity*: solid but the structural fix is missing. The diagnosis (ambiguous requirements + technically capable people + no cost feedback = over-engineering) is correct. But "The requirements failure produced the over-engineering" is where the section ends. What structural change prevents it? A requirements standard? A cost constraint mechanism? The section identifies the cause without proposing the intervention, which breaks the chapter's pattern.
- *Going silent*: the analysis is correct but the structural fix is stated at the level of a principle rather than a mechanism: "change what happens when they do." This is accurate but vague. Change it to what? The other sections name the specific structural intervention (make documentation a sprint deliverable, change performance criteria for knowledge transfer). This section stops one level of specificity short.

**Suggested fix for over-engineering:** Add one sentence on the structural fix: "The prevention is specific: requirements that include explicit constraints — target request volume, latency budget, cost ceiling — make the simpler solution obviously correct and eliminate the technical optionality argument. Vague requirements are not just unhelpful; they are a structural input to gold-plating."

**Suggested fix for going silent:** Replace "change what happens when they do" with a mechanism: "The structural fix is to make visible what happened the last three times someone persisted in objecting after being overruled — and to ensure those outcomes are part of the record the team can point to. If the record shows those people were labeled 'not team players,' the reward structure is documented. You cannot fix a hidden incentive."

---

**Issue 3.3 — The counter-argument section addresses two objections but misses the strongest one**

> "The first version of the objection: if everything is structural, nobody is responsible for anything."
> "The second objection: some engineers really are just difficult."

Both are handled well. The diagnostic question — "if I change the structure, does the behavior change?" — is the chapter's most useful tool. But the strongest objection to the chapter's thesis is absent: *the chapter's own framing might produce learned helplessness in engineers*. If behavior is structurally determined, what is an individual engineer supposed to do inside a bad structure? Concluding that "the structure is the cause" without addressing what an engineer who cannot change the structure should do leaves the reader with a sophisticated diagnosis and no personal agency.

The chapter does gesture at this in "What Changes Monday" but frames it as advice for people who run postmortems or design reward systems — i.e., people with structural authority. It doesn't directly address the engineer who is subject to the bad structure, not its designer.

**Suggested fix:** Add a brief paragraph in "Structure Isn't Everything" that addresses this: "A third version of the objection is personal: what does this mean for the engineer who understands the structural cause but can't fix it? Two things. First, understanding that your behavior is being shaped by incentives gives you the option to choose differently with your eyes open — the cost of that choice is real and shouldn't be romanticized, but it is a choice. Second, naming the structural cause precisely, in the right forum, is itself an intervention: it is the difference between 'I raised a concern and was overruled' and 'the decision-making process overruled concerns in a way that will produce this outcome again.' The second framing is a proposal, not a complaint." This thread is already implicit in the final section but making it explicit serves readers who are not in a position to change structures directly.

---

## Criterion 4: Voice Check

The chapter's voice is generally strong — grounded in specific behavioral examples, not abstractions. Three passages drift.

---

**Issue 4.1 — The opening of "The Blame Instinct and Why It Fails" slips into academic register**

> "There is a well-documented tendency in human judgment called the fundamental attribution error. The name comes from work in social psychology in the 1970s, and the finding is this..."

"There is a well-documented tendency in human judgment" reads like a textbook introduction rather than a peer talking. The chapter opens with an excellent concrete scene; this paragraph reopens with a different register. The contrast makes the section feel like a gear change.

**Suggested fix:** Open the section in the same register as the scene: "Two days after the incident, twelve people in a conference room, and the blame had already found someone to land on. This is not unusual — it is reliable. There is a well-documented pattern in how people explain other people's behavior, and it consistently points toward character over situation..." The "well-documented tendency" framing can stay but it lands more naturally after one sentence that reconnects to the opening scene.

---

**Issue 4.2 — "Structure Isn't Everything" contains one management-consultant hedge**

> "You can hold people accountable and fix structures simultaneously. They are not mutually exclusive."

This is a reasonable claim, but "not mutually exclusive" is the kind of phrase that appears in every management consulting deck after a contentious slide. The chapter's voice elsewhere is more precise and confident. The point being made is actually sharper than this phrase communicates: individual accountability conversations are useful for the individual; structural fixes are the only thing that helps anyone else. That asymmetry is the chapter's argument, and "not mutually exclusive" flattens it into a diplomatic both-sides statement.

**Suggested fix:** Replace with the actual claim: "Individual accountability matters. But it operates at person-scale. A structural fix operates at role-scale — it changes behavior for everyone who holds that position, not just the current occupant. Do both, but don't confuse the purpose of each." This is more direct and more useful.

---

**Issue 4.3 — The closing paragraph of "What Changes Monday" shifts into encouragement mode**

> "The engineers who are most effective at changing their organizations are the ones who have learned the difference — who can take a dysfunction, trace it to its structural cause, and propose the structural change that would produce a different outcome. That's not soft skill territory. That's the job."

"That's the job" is a strong closer and the right register. The problem is the sentence before it: "The engineers who are most effective at changing their organizations are the ones who have learned the difference" is aspirational framing rather than instructional. It tells the reader what effective engineers do without telling them how to become one. It reads as a motivational close rather than a practical one — the kind of sentence that lands in a conference keynote but feels slightly vague in a book that has been precise throughout.

**Suggested fix:** Replace the aspirational frame with one concrete example of what tracing to structural cause looks like in practice: "That looks like this: instead of 'we need to improve our documentation culture,' you write 'documentation needs to appear as a sprint deliverable at the same weight as a shipped feature, in the roadmap and in the performance review criteria.' The first is a wish. The second is a proposal. Learn to tell the difference between them — in your own drafts, in your team's retros, in the postmortems you run. That's not soft skill territory. That's the job." The book already has this example earlier in the same section; pulling it to the close tightens the ending.

---

## Criterion 5: Practitioner Utility

---

**Issue 5.1 — The diagnostic question is the chapter's most useful tool but is introduced too late and without a worked example**

> "Here is the diagnostic question that separates structural causes from individual ones: if I change the structure, does the behavior change?"

This is the most portable tool in the chapter and it appears near the end of "Structure Isn't Everything" — the penultimate section. It should be introduced earlier, ideally at the end of "The Blame Instinct and Why It Fails," so that the five behavioral examples in the following section function as worked applications of the diagnostic. The reader currently encounters the diagnostic after the examples, which means the examples don't teach it — they just illustrate a pattern that was never named as a tool.

Additionally, the worked examples that follow the diagnostic question (knowledge hoarding stops if you fix the incentive structure; one person still hoards after the fix, so it's individual) are brief and schematic. An engineer sitting in a postmortem needs the diagnostic rendered in postmortem language, not in the abstract.

**Suggested fix:** Move the diagnostic question to the end of "The Blame Instinct and Why It Fails" as a forward-looking frame: "The question that redirects this is structural: what would happen to this behavior if I changed the conditions? If the answer is 'the same thing, because this is a character issue,' the individual conversation is warranted. If the answer is 'a different engineer in the same conditions would probably do the same thing,' you are looking at a structural cause — and individual intervention will not fix it." Then let the five behavioral examples in the next section demonstrate the diagnostic in practice.

---

**Issue 5.2 — "What Changes Monday" addresses managers more than it addresses engineers**

> "Look at your team's reward system and name the invisible work it doesn't recognize."
> "In the next postmortem or performance review you run or participate in..."

Both pieces of advice require structural authority to act on. Changing performance criteria, redesigning sprint deliverables, running postmortems — these are actions available to managers and tech leads with scope over process. A senior individual contributor who has no control over performance criteria or postmortem formats gets advice they cannot act on.

The chapter's thesis applies equally to engineers who are subject to bad structures and engineers who design them. The "What Changes Monday" section currently speaks almost entirely to the designer, not the subject.

**Suggested fix:** Add one paragraph addressing the engineer without structural authority: "If you're not in a position to change the structure — not running the postmortem, not setting performance criteria — the most useful thing you can do is name the structural cause precisely in the conversation it belongs in. Not 'I wasn't given enough time' (character defense) but 'the sprint had no slack budgeted for this, and when the choice was between missing the commit or shipping with the known risk, the schedule made one of those decisions much more expensive than the other' (structural account). You are not shifting blame. You are giving the organization the information it needs to fix the right thing. Whether they act on it is not within your control. Whether you said it clearly is."

---

**Issue 5.3 — The five behavioral examples give structural diagnoses but four of five do not complete the loop to structural fix**

See Issue 3.2 above for specific cases. The pattern is that the section identifies "what the reward system rewards" in terms of behaviors but is inconsistent about completing the sequence from behavior → structural cause → structural fix. Documentation and knowledge hoarding are the most complete. Over-engineering and going silent are incomplete.

This matters for practitioner utility because a reader who can identify a structural cause but can't articulate the corresponding structural fix is left with a diagnosis and no prescription. The chapter argues that naming the structural cause is "the first step to change" — but the examples stop at naming without modeling how to take the second step.

**Suggested fix:** Review each of the five examples and ensure each ends with a specific structural change, not just a structural insight. The test: can a reader read the fix and write a proposal from it? "The structural fix is to make documentation a sprint deliverable with the same standing as a feature ticket" passes this test. "Change what you reward and the behavior changes" does not.

---

## What Works Well

1. **The opening scene is the chapter's strongest asset and one of the best in the book.** The postmortem that spends forty minutes on the individual and forty seconds on the deployment process — then gets the same outcome three months later with a different engineer — is precise, recognizable, and makes the entire thesis argument before stating it. The detail "a different engineer in the same role made a similar judgment call with similar consequences" is the chapter in one sentence. A reader who has been in that meeting room will feel located immediately.

2. **The Challenger and Therac-25 analyses are analytically rigorous, not just illustrative.** Most books that cite Challenger use it as an emotional appeal (lives were lost, therefore take safety seriously). This draft uses it as a mechanism demonstration: the information architecture of the organization degraded the risk signal at exactly the point it was needed most. The Feynman observation about genuine differences in probability estimates — not dishonesty, but organizational filtering — is precisely the kind of structural explanation that the chapter argues is missing from standard blame narratives. The Therac-25 case adds a different structural mechanism (removed redundancy, isolated accountability, no incident aggregation) without repeating the Challenger lesson. Both cases are doing real analytical work, not just providing dramatic examples.

3. **The "going silent" example is the most psychologically honest passage in the book so far.** The calculation attributed to the senior engineer — probability that further objection changes the outcome, weighed against the concrete cost of being labeled "not a team player" — is more precise than how this situation is usually described. Most writing on speaking up frames silence as failure of courage. This draft frames it as the result of a rational calculation on imperfect information about an environment that has documented its responses to dissent. "People don't withhold dissent because they lack courage. They withhold it because the environment has taught them that courage is punished." This is the chapter's best sentence and it is as precisely stated as the argument gets anywhere in the book.

---

## Top 3 Priority Fixes

**Priority 1: Complete the structural-fix loop for over-engineering and going-silent examples.**
Four of five behavioral examples in "What the Reward System Actually Rewards" diagnose the structural cause but do not model the corresponding structural fix at actionable specificity. The documentation and deferring-maintenance cases set a standard (specific, proposal-grade) that the others don't match. A reader who absorbs the chapter's diagnostic framework needs to see it completed all the way through — behavior → cause → intervention — in every case, not just two of five. The over-engineering fix is one sentence (explicit constraints in requirements); the going-silent fix requires naming the mechanism by which the environment documents its responses to dissent. Neither requires more than two sentences.

**Priority 2: Move the diagnostic question to the end of "The Blame Instinct and Why It Fails" and let the behavioral examples teach it.**
The chapter's most portable practical tool — "if I change the structure, does the behavior change?" — currently arrives after the five examples it should be framing. Moving it forward converts the behavioral catalog from a list of interesting cases into a set of worked applications of an explicit tool. It also gives the reader something to carry into the postmortem before the chapter has finished, rather than discovering it in the penultimate section.

**Priority 3: Add one paragraph in "What Changes Monday" for engineers who cannot change structures.**
The closing section currently addresses people with structural authority (postmortem facilitators, performance review designers, reward system owners). A substantial portion of the book's audience — senior individual contributors below the level where they set criteria or run processes — gets advice they cannot act on this Monday. One paragraph that addresses what they *can* do (provide a structural account rather than a character defense, make the structural cause visible in the conversation where it belongs) completes the chapter's practical promise for the full audience.
