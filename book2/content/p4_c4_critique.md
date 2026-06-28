# Critique: Build vs. Buy Is a Strategy Question

---

## 1. Thesis Alignment

The chapter's argument is coherent and stated explicitly: build vs. buy is a strategy question, and engineers keep losing these decisions because they answer it in technical terms. That thesis is strong, and the opening scene earns it — the engineering team that did everything right technically and still lost the room is the right hook. The chapter delivers on the promise.

The structural problem is that the chapter has five substantial sections where three would do the work better. "The Commodity Ladder" and "Lock-In Is Not One Thing" are both necessary. The PC operating system case study in the following section, however, mostly re-illustrates the commodity ladder point, and its length (the longest narrative block in the draft) is not proportionate to the additional argumentative weight it carries. By the time you've explained that the commodity layer of today can become the differentiator of tomorrow in "The Commodity Ladder," you've already made the central claim of the historical case. The case study then retells it at length.

The section "The Skeptic's Turn" is the one structural choice that genuinely risks thesis drift. It introduces three substantial objections — build for understanding, buy-and-customize as worst of both worlds, and open source as a third category — each of which is partially developed and none of which fully resolves into the chapter's central argument. The open source passage in particular:

> "One more case that deserves mention: open source software occupies a third category — neither build nor buy but adopt — and carries risks that neither framing captures well."

This is a real point, but dropped at the end of a section that's already running long. It feels like material that wandered in from the next chapter. Cut it or promote it. If open source deserves treatment, give it a section. If it doesn't, cut the paragraph.

---

## 2. Aging Risk

The chapter handles the no-named-tools rule almost perfectly. The Prahalad and Hamel citation is correct and appropriate — named academics with a datable, verifiable publication. All the vendor examples are kept in categories (a vendor, a platform, a dominant hardware company).

One near-miss worth flagging. The historical case study is recognizable to anyone with basic industry knowledge:

> "In the early 1980s, a dominant hardware company was designing a personal computer on an accelerated timeline... sourced the operating system from a small company — which had itself acquired the operating system from another small company days before the deal closed."

This is not a problem with the naming rule, which the chapter correctly follows, but with the assumption that a senior engineering audience in 2030 will have the same cultural frame of reference. The case is heavily relied upon — the chapter gives it more space than any other section — and its instructive weight assumes the reader either knows the story or will find the unnamed sketch sufficient. If they don't know the story, the lesson still lands. If they do, the anonymization adds nothing and occasionally creates unnecessary indirection ("a dominant hardware company" where a proper noun would read more crisply).

The stronger aging risk is in the feature flagging example:

> "Consider the team that spent a quarter building a feature flagging system. The reasoning was defensible at the time: the existing commodity solutions were more than they needed..."

Feature flagging is accurately described as commodity now, but the example reads as period-specific. More importantly, the claim "existing commodity solutions were more than they needed" is unverifiable and feels like a reconstructed rationalization. Replace the framing: instead of characterizing the original reasoning, let the post-mortem logic stand on its own. The chapter's point doesn't require that the team was wrong at the time — it requires that the commodity trajectory made building the wrong long-run call. That argument doesn't need to put words in the team's mouth.

---

## 3. Argument Quality

The chapter's strongest sustained argument is the disaggregation of lock-in into four distinct types. This is genuinely useful intellectual work — most practitioners do conflate switching cost, capability atrophy, data lock-in, and network lock-in, and the distinctions matter for how you mitigate. The data lock-in example (the CRM migration that took eighteen months) is specific and credible.

There is one significant logical gap in the abstraction layer passage:

> "A common engineering response to lock-in risk is to build an abstraction layer... This is a reasonable idea that frequently produces the wrong outcome."

The chapter then gives a single example where the abstraction layer failed. That's a data point, not a demonstration that the approach "frequently produces the wrong outcome." The argument as written commits the same error the chapter warns against in the motivated reasoning paragraph — reaching a strong conclusion on insufficient evidence. The claim is probably right. The support is one example. Fix it by either softening the claim ("often produces poor tradeoffs") or adding the condition that triggers failure: abstraction layers fail when the abstraction leaks, when the capabilities they expose are a strict subset of the underlying platform's capabilities, or when the thing you're abstracting away has real structural variation between implementations. That's a useful addition, not just a hedge.

The Prahalad and Hamel section has a buried argument that deserves more development:

> "Engineers make the determination themselves, often using technical interest as a proxy for strategic importance."

This is the sharpest sentence in the chapter and it's treated as a transitional observation. It should be the lead claim of that section, with more development. The motivated reasoning paragraph that follows it is the right content; the framing undersells it.

One weak analogy: "motivated reasoning wearing analysis as a costume" is colorful, but it conflates two different problems. An engineer excited about building and an engineer avoiding a hairy integration are both doing motivated reasoning, but in opposite directions. The chapter treats them symmetrically, but they produce different errors with different organizational consequences. The build-biased engineer creates strategic overreach; the buy-biased engineer creates commodity dependency that looks like efficiency. The symmetry in the writing loses this distinction.

---

## 4. Voice Check

The chapter's voice is largely clean. The opening is excellent — the CFO decision scene is specific, grounded, and does real work without editorializing. The Prahalad and Hamel section moves well. Most of the lock-in taxonomy is clear.

A few passages slip:

> "The commodity ladder doesn't tell you what to build — it tells you which capabilities have a limited shelf life as sources of competitive value, so you can price the cost of owning them accordingly."

"Price the cost of owning them accordingly" is vague. Own means own — the chapter has already established that. What does it mean to "price the cost"? This is the kind of sentence that sounds precise but leaves the reader with nothing to do. Rewrite: "The commodity ladder tells you which capabilities are heading toward freely available — so you can ask whether the investment will pay off before it becomes irrelevant."

> "Strategic assets, once given away, do not come back."

This closes the PC operating system section and tries to land as an aphorism. It's not wrong, but it's too general to be useful and too obvious to earn the rhetorical weight it's assigned. The actually interesting lesson — that software economics are fundamentally different from hardware economics because of near-zero marginal cost — is buried two paragraphs earlier. Restructure so the software/hardware economics distinction is the closing point, not the "strategic assets don't come back" truism.

> "Engineers who can make that case, in that language, are engineers who get to participate in the decision. Engineers who show up with a benchmark comparison and an integration timeline are answering a question that was settled before they walked in."

Strong. This is the voice the chapter should sustain throughout.

> "The trap is the gap between 'we'll just customize a few things' (what people say at contract signing) and 'we've spent eighteen months building on top of a vendor API that keeps changing, and now we can't migrate off it' (what happens three years later)."

Also strong. The parenthetical contrast is efficient and credible. Keep this.

---

## 5. Practitioner Utility

The "What Changes Monday" section is mostly good. The three directives — name the core competency question explicitly, disaggregate lock-in, design the exit — are concrete and actionable. "Design the exit before you sign" is the best of the three: it's specific, it's something you can do Tuesday, and it changes behavior rather than mindset.

The first directive has a gap:

> "State which side of the strategic line this capability falls on... This is not a technical judgment. It requires understanding what your organization believes is actually differentiating, which means talking to people with strategic visibility before you do the technical analysis."

The advice to "talk to people with strategic visibility" is correct but underspecified. Who are those people? What do you ask them? A senior engineer reading this knows that "strategic visibility" is unevenly distributed and that the people who have it are often unavailable. Give the reader a more specific in: "Before you model the integration cost, schedule thirty minutes with the product leader who owns the roadmap for this area. Ask one question: 'If we owned this capability internally and could evolve it at our own pace, how would that change what we build in the next two years?' Their answer tells you whether this is strategic."

The second directive ("disaggregate lock-in risk") is sound but references concepts developed earlier in the chapter. In practice, someone reading "What Changes Monday" first will need to flip back. Consider adding a one-sentence anchor: "Use the four types from earlier in the chapter — switching cost, capability atrophy, data, and network lock-in."

The closing paragraphs after "What Changes Monday" are redundant. The chapter already ends on the CFO callback:

> "The CFO in that opening meeting was not wrong to override the technical recommendation. She was asking a question that the technical recommendation didn't answer."

This is the right ending — it closes the loop on the opening scene. Cut the preceding two paragraphs about "whose room you're in," which say the same thing less efficiently.

---

## Three Things That Work Well

**1. The lock-in taxonomy.** Breaking lock-in into four named types is the most practically useful piece of the chapter. The data lock-in example — the CRM migration that was estimated at three months and took eighteen — is concrete, credible, and will resonate with anyone who has lived through a platform migration. This is the section a reader will screenshot and share.

**2. The opening scene.** The engineering team that did everything right technically and lost the room anyway is specific enough to be credible and universal enough to be recognizable. It earns the thesis without stating it first. The callback to this scene at the end is structurally sound.

**3. The core competency framework application.** The move from Prahalad and Hamel's original three tests to "the things that meet all three tests are what you build and own" is the right use of a named academic framework — it grounds a practical heuristic in something with analytical rigor rather than pure assertion.

---

## Top 3 Priority Fixes

**1. Cut the PC operating system section to one paragraph.** The commodity ladder section already makes the argument that matters: capabilities on the path to commoditization should have a higher bar for building. The historical case illustrates the same lesson at greater length without adding analytical content. Condense it to the software economics insight (near-zero marginal cost means software value compounds in a way hardware value does not) and cut the narrative reconstruction. Redirect that space to strengthening "The Skeptic's Turn," which currently raises good objections without fully resolving them.

**2. Fix the abstraction layer claim.** "Frequently produces the wrong outcome" is not supported by one example. Either add the conditions under which abstraction layers fail (the abstraction leaks; the underlying platforms have real structural variation; the hedged risk has low probability) or soften the claim. This matters because the abstraction layer recommendation is a real engineering decision that readers face, and an overconfident takedown of the approach will produce the wrong behavior in cases where it's the right call.

**3. Sharpen "What Changes Monday" on the core competency directive.** "Talk to people with strategic visibility" is not actionable at the level the rest of the section achieves. Give the reader a specific question to ask a specific kind of person. The design-the-exit directive is a model for what this should look like: concrete, bounded, doable Tuesday morning. The core competency directive needs the same level of specificity to land with equal force.
