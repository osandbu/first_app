# How Decisions Actually Get Made

On a Thursday in October, a platform team prepared to present an architectural proposal to a cross-functional review meeting. Three engineers had spent six weeks on the analysis. There were slides. There was a trade-off matrix. There were references to comparable decisions at similar-scale organizations. The meeting was scheduled for ninety minutes.

The decision had been made the previous Monday.

The VP of Engineering had walked out of a quarterly business review and bumped into the platform team lead in the hallway. They chatted for ten minutes. The VP, still processing a pointed conversation with the CFO about infrastructure costs, asked whether the proposed architectural direction could be adjusted to reduce cloud spend. The platform team lead said yes, with one modification. The VP said "let's go with that then."

Thursday's meeting ran on schedule. People raised substantive concerns. One engineer identified a failure mode no one had considered. The room was engaged. At the end, the VP thanked everyone for their input and said the team would proceed with the modified approach — which happened to be the approach he'd agreed to on Monday. The attendees filed out, a few mildly suspicious, most satisfied that they'd participated in a decision.

None of them were told what had happened in the hallway.

This is not a story about a dysfunctional organization. The VP was not acting in bad faith. He had new information — real cost pressure with a near-term deadline — and he had a trusted source who confirmed the modification was feasible. The formal process continued, as it was supposed to, and the discussion was real. It just wasn't determinative. The decision was a social process that had reached its conclusion before the designated decision-making event occurred.

Most engineers have an implicit model of how their organization makes decisions. In this model, a decision is essentially an optimization problem: parties gather information, evaluate options against criteria, and select the best one. There may be politics around the edges, but fundamentally the best analysis wins. This model is wrong — not occasionally, not in dysfunctional organizations, but as a general description of how organizational decisions work. Understanding why is not a concession to cynicism. It's a prerequisite to being effective.

---

## How Experienced People Actually Decide

In the late 1980s, a psychologist named Gary Klein was hired to study how firefighters make decisions. The research question was practical: commanders facing structure fires had to make fast calls with incomplete information. What decision process did they use?

The answer surprised the researchers. The firefighters weren't doing comparative analysis. They weren't generating multiple options and evaluating them against criteria. What Klein found was a process he eventually called the Recognition-Primed Decision model: experienced commanders would perceive a situation, pattern-match it against prior experience, generate a single course of action that seemed plausible, mentally simulate it for fatal flaws, and execute if no fatal flaw appeared. Only if the simulation revealed a serious problem would they consider an alternative.

This was not intuition in the mystical sense. It was rapid, tacit expertise — thousands of hours of experience compressed into a pattern library that could process complex situations faster than any formal option comparison. It was also highly reliable in familiar situations and systematically fragile in novel ones, where the pattern match was wrong but the confidence was indistinguishable from confidence in a correct match.

Klein later replicated the finding with military commanders in the field, then with ICU nurses, then with chess grandmasters. Across domains, expert decision-making under time pressure looked the same: not comparative analysis, but pattern recognition followed by simulation.

The organizational implication takes a moment to land. When a senior engineer or VP receives your technical analysis, they are not running your analysis as an input to a calculation they're doing. They are checking whether your analysis disrupts a pattern match they've already made. They have seen enough situations, launched enough products, navigated enough architectural decisions, that most new situations register as variants of situations they've handled before. The option that looks obvious to them is obvious because their experience has pattern-matched the current situation to a prior one where that option worked.

This means that if the pattern match is correct — if the current situation really is relevantly similar to their prior experience — your analysis will mostly confirm what they expected, and they will confirm the decision they'd already reached. If the pattern match is incorrect — if this situation is genuinely different in ways that matter — your analysis will produce friction without necessarily changing anything, because you're presenting information about features they've already processed and a pattern match they've already committed to.

To actually change a decision in this mode, you need to disrupt the pattern match. Not provide a cleaner version of the same analysis. Show them something genuinely novel about the current situation — something that makes clear why the prior experience doesn't transfer. This requires understanding what the prior experience actually is, which requires knowing the person and their history rather than just knowing the analysis.

This also applies to organizations at a larger scale. Kahneman's dual-process framework — the "fast thinking" of heuristics and pattern-matching against the "slow thinking" of deliberate analysis — is frequently cited as an individual cognitive phenomenon. It operates equally as an organizational one. Most engineering organizations run under genuine time pressure: quarterly planning cycles, launch commitments, incident response. Under that pressure, organizations systematically produce fast, heuristic-driven decisions on questions that would benefit from deliberation. This is not a bug attributable to poor leadership. It's a structural consequence of the operating environment. The goal isn't to eliminate it. It's to identify which decisions have enough consequence and limited reversibility that they warrant — and can actually get — a genuine pause.

---

## The Reversibility Principle

Not all decisions deserve the same amount of process. This seems obvious when stated directly, and is systematically violated in most organizations, in both directions.

The most useful framework for calibrating decision effort is reversibility. A decision that's easy to reverse — try it, observe the outcome, adjust — deserves fast treatment with minimal process. Spending three meetings deliberating over a feature flag configuration is organizational waste. The cost of being wrong is low; recover and move on.

A decision that's hard or impossible to reverse deserves slow, deliberate, documented process. Moving fast on an architectural commitment, a hiring decision, or a security model is a different kind of organizational waste: the waste of consequences you could have avoided with thirty more minutes of deliberate analysis at the moment of decision.

The practical complication is that reversibility is not a fixed property of a decision. It changes over time as downstream dependencies accumulate.

Consider a team that adopts a service mesh infrastructure layer. The pitch is sensible: it solves a real problem, and adoption feels gradual and low-stakes. "We can always rip it out," someone says, and they're correct — at month one, you probably can. The choice is technically reversible. But over the next eighteen months, every service in the organization gets built with assumptions about the mesh's capabilities. The on-call rotation acquires mesh-specific runbooks. New engineers are trained on it. When it begins causing latency problems at a scale that wasn't visible earlier, no one revisits the original decision. Instead they add layers to work around the limitations, because the cost of reversal now requires coordinating with every team that has built assumptions on top of it.

The decision that felt reversible became a constraint. Not because of technical lock-in in any formal sense — you could still, technically, rip it out. But because the organizational weight of accumulated assumptions closed the practical window for reversal faster than anyone noticed.

This pattern repeats across domains. An architectural choice that was genuinely revisable in month one may be effectively permanent by month eighteen. A vendor relationship that seemed easy to exit at contract signing becomes deeply entangled when the team has organized their workflow around the vendor's specific API behaviors. The window closes faster than engineers realize, and usually faster than anyone said out loud when the decision was made.

Two failure modes follow from misreading reversibility. The first is treating irreversible decisions as reversible: moving fast on architectural choices because "we can always revisit this," and discovering that the revisitation cost is orders of magnitude higher than anyone estimated. This failure mode shows up as the impossible-to-complete migration, the legacy system that everyone agrees is wrong but that no one can afford to replace.

The second failure mode is treating every decision as irreversible: creating analysis paralysis on decisions that could simply be tried. This shows up as teams that spend four meetings on a naming convention, or that won't ship a reversible change without sign-off from three levels of management. The cost here is subtler — not one spectacular failure, but a persistent drag on the organization's ability to move.

The discipline is forcing yourself to ask the reversibility question before investing decision effort, rather than after. Not "what's the right answer?" but first: "how hard would it be to reverse this in six months, and how much of that answer is actually knowable right now?"

---

## Two Tools That Help

Every useful organizational decision-making tool shares a property: it slows down the decisions that benefit from slowing down, without adding drag to decisions that don't. Two tools are worth having in regular use.

**The pre-mortem.** Gary Klein developed the technique in the same research tradition as his work on expert decision-making. The setup is deceptively simple: before committing to a significant decision, tell the group to assume it's already happened — and assume it went badly. Not "what might go wrong?" but "we're six months from now and this has failed spectacularly. What happened?"

The mechanism that makes this effective is psychological reframing. In a normal pre-decision discussion, raising concerns is structurally awkward. A group that is converging toward a decision has social momentum behind the decision. Expressing doubt feels like obstruction. People hedge. People wait to see if someone else will raise the concern first. Concerns that everyone is privately holding often go unvoiced because the cost of voicing them is borne individually while the benefit is distributed to the group.

The pre-mortem reframes the task. Raising concerns isn't obstruction — it's participation. You're not doubting the decision; you're performing the assigned analysis. The technique also de-anchors the group from the outcome they're anticipating, making it easier to think clearly about failure modes.

In one infrastructure migration, a project lead ran a pre-mortem twenty-four hours before the team was about to formally commit to a launch timeline. Three people immediately identified the same failure mode: the rollback plan assumed a clean production state that wouldn't exist when the migration ran on live data. Two others raised a dependency on a third-party system with a maintenance window that conflicted with the planned migration window. Neither issue was subtle. Both had been in the room throughout the planning. Neither had been stated clearly until the question was framed as "why did this fail?"

The launch date moved by three weeks. At the time this felt like a setback. Six months later, when the team reviewed what had actually happened during the migration, it was clear that both problems would have materialized, and the third-week delay had prevented something significantly worse.

The pre-mortem is most valuable for exactly the decisions where it's least comfortable: high-stakes, low-reversibility, time-pressure situations where the group has already developed momentum toward a specific path. Apply it before commitment, not after.

**The decision log.** The premise is simple: record the context, options considered, decision made, owner, and expected outcome — at the moment of decision, before the outcome is known.

Most organizations have retrospectives without decision logs. The retrospective asks "what went wrong?" without being able to ask "what did we expect would happen?" Those are different questions, and the second one is often the more important one. Did the decision fail because the implementation was poor, or because the original assumptions were wrong? Without a record of the original assumptions, you can't know. What looks like an execution failure may be an assumption failure. What looks like bad luck may be predictable from the original analysis if you go back and look at it.

The decision log is not accountability theater. Don't deploy it as a way to establish blame when things go wrong — that creates an incentive to write vague logs that commit to nothing. The value is organizational learning: the ability to build an empirical picture of which categories of decisions your organization tends to get right and which it tends to misjudge. Over time, an organization with good decision logs gets better at calibrating its own uncertainty. An organization without them keeps repeating the same classes of mistakes while attributing each one to bad luck.

---

## The Political Context Is Not Separate from the Decision

In 1971, political scientist Graham Allison published an analysis of the Cuban Missile Crisis that changed how scholars thought about governmental decision-making. Allison examined the crisis through three competing models.

The "rational actor" model assumed that governments acted as unified agents pursuing coherent national interests. Under this model, you could explain the crisis by asking: what option best served American interests? What option best served Soviet interests? The model produced a clean analytical structure and failed badly at explaining what actually happened.

The "organizational process" model did better: governments execute their standard operating procedures, and the crisis could be explained by understanding which procedures each institution's standard playbook called for. But it still missed things.

The "bureaucratic politics" model explained the most. What emerged from the crisis — not just the resolution, but the specific form it took, the specific concessions made, the specific timing — was a negotiated outcome among officials with different institutional interests, different threat assessments, and different career incentives. The Secretary of Defense was not running the same calculation as the Joint Chiefs. The Soviet ambassador was not acting on the same constraints as the Soviet military. The outcome was not the optimized choice of a unified actor. It was the product of a social process among actors with partially overlapping and partially competing interests.

Engineering organizations run the same three models simultaneously. The rational actor model — leadership makes decisions that optimize for technical outcomes — is the model most engineers implicitly use when they're frustrated by organizational decisions. The bureaucratic politics model is closer to reality. When a proposal fails, the relevant question is often not "what was wrong with the technical analysis?" but "whose institutional interests did this proposal threaten, and did anyone address those interests before the meeting?"

Consider a team that spends three months building the case for migrating a legacy system to a more maintainable architecture. The technical argument is airtight. Lower operational cost. Better observability. Faster feature development. They present to a cross-functional review. The proposal fails.

What happened? The review included a director whose team had built the legacy system over the previous four years. That system was a significant career achievement — the proof of concept that had grown into production, the platform that kept the business running. The migration proposal, however carefully framed, carried an implicit message: the legacy system was wrong. No one had spoken to the director before the meeting. No one had asked what he cared about going forward — his team's future, their relevance in the new architecture, whether their expertise would transfer — instead of what he cared about in the past. The technical analysis was perfect. It was irrelevant to the actual decision being made.

This brings in a concept from political science that has a useful organizational analog: the Overton Window. In politics, the window describes the range of policy options that are actually viable at a given moment — not what's theoretically possible, but what stakeholders will actually accept without organized resistance. In engineering organizations, the same concept applies. The technically optimal option doesn't get made if it's outside the range of options that the relevant stakeholders will support.

Engineers routinely underestimate how narrow that window is. They also underestimate the available mechanisms for moving it. Sometimes the most effective path to a decision isn't to make a better argument for the option you want — it's to change the context so that option enters the window. Run a blameless postmortem that makes a previously invisible problem visible. Build a coalition before you propose the solution. Let a bad decision accumulate enough consequences that the window shifts organically. This is not manipulation. It's recognizing that decisions happen inside social contexts that have their own dynamics, and that those dynamics can be influenced.

---

## The Skeptic's Turn

There's a clean objection to everything in this chapter: "If you teach engineers to navigate organizational politics, you're normalizing it. You're describing dysfunction and calling it reality. Better analysis should win. Better data should win. The right response to dysfunctional decision processes is to fix them, not to adapt to them."

This objection conflates two separate things: the quality of the analysis and the adoption of the analysis. These are different problems, and solving the first doesn't solve the second.

A technically correct recommendation that fails to account for the organizational context in which it will be evaluated will fail regardless of data quality. This is not a defect in organizations. It is a predictable consequence of the fact that organizations are composed of people with legitimate interests that differ. The director whose team built the legacy system has a legitimate interest in his team's future. The VP who agreed to the modified architectural approach in the hallway had legitimate information — real cost pressure — that shaped his view. These interests are not the same as the organization's purely technical interest in the best architecture, but they are not illegitimate interests. They are the interests of real people who will live with the consequences of whatever is decided.

The descriptive claim and the normative claim are different things. This chapter describes how decisions actually get made. A cardiologist explaining the mechanism of heart disease is not endorsing it. Understanding the mechanism is the prerequisite to addressing it. Engineers who operate only in the world they want to exist — where analysis wins on its merits, where political considerations are irrelevant, where the rational actor model describes reality — consistently lose to people who operate in the world that does exist.

But the objection has a legitimate version that deserves a direct answer: where does understanding organizational dynamics end and rationalizing genuinely dysfunctional outcomes begin?

The NASA Challenger launch decision is the boundary case. The night before the January 1986 launch, engineers at the solid rocket booster manufacturer argued against it. Their data showed that the O-ring seals on the boosters had not been tested at the ambient temperatures forecast for launch day. The engineering argument was sound and the data was real.

What happened in that conversation is the warning sign: the question changed. The normal question — "have we demonstrated this is safe to launch?" — became "can you prove it's not safe to launch?" The burden of proof flipped. That flip is not a feature of organizational decision-making. It's a pathology. When the question changes from "why should we do this?" to "prove we shouldn't," the decision has already been made and evidence is being collected to ratify it. The engineers were no longer participants in a decision process. They were obstacles to a decision already reached.

Understanding organizational decision-making doesn't mean accepting every outcome. It means being able to identify which pattern you're in. The VP who adjusted an architectural direction after a hallway conversation with real new information was acting in the normal range of organizational behavior. The managers who overruled their engineers by inverting the burden of proof were in a different pattern, one with a well-documented failure mode. You can only see the difference if you understand what you're looking at.

The practical tools in this chapter — the pre-mortem, the decision log, the reversibility assessment — are not substitutes for rigorous analysis. They're complements to it. They help good analysis survive contact with real organizational decision processes. They also create the conditions under which the burden-of-proof flip becomes visible: if you've documented what you expected when the decision was made, you can identify later when the question changed.

---

## What Changes Monday

Before the next significant decision your team is involved in, ask a question you probably haven't been asking: who is the actual decision-maker, versus who is the nominal decision-maker? The meeting invite and the org chart will tell you the nominal answer. The actual answer requires a different kind of attention. Where are the informal conversations happening? Who will the VP talk to before the review? Who has established credibility with the relevant stakeholders by working through previous decisions? If you're not in those conversations, you're not in the decision process, regardless of whether your name is on the invite. This isn't defeatism — it's information. Act on it by identifying who you need to talk to before the formal event, not during it.

In the next quarter, run a pre-mortem on one high-stakes, low-reversibility decision before your team commits to it. Don't wait for organizational adoption of the practice; just do it. Schedule sixty minutes. Frame the question: "Assume we're twelve months from now and this failed badly. What happened?" Assign the task of raising concerns as participation rather than obstruction. Then actually act on what you hear. If the pre-mortem surfaces concerns that are dismissed rather than addressed, that itself is signal about the decision process you're in.

The longer-term shift is a habit of classification. Before investing significant effort in a decision — before the analysis, before the stakeholder conversations, before the slide deck — ask whether the decision is actually hard to reverse. Not "is it hard?" in the abstract, but "how reversible will this be in six months, and what would close the reversal window?" The discipline runs in both directions. Don't slow-walk what can be easily revisited; the process cost is real and recurring. And don't fast-track what can't be undone. The asymmetry between those two kinds of mistakes is enormous, and most organizations learn it by making the expensive one first.

Decisions are not output from an optimization function. They're the sediment of social processes — shaped by information, by timing, by relationships, by institutional interests, and occasionally by someone running into someone else in a hallway after a meeting about costs. The engineer who understands that is not less rigorous. They're operating in the actual environment, with the actual constraints, on the actual problem. That's the job.
