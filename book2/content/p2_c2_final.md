# How Compensation Shapes What Gets Built

The VP ran a clean meeting. Clear agenda, good facilitation, no rambling. She came prepared. And when the discussion turned to Q3 staffing, she made the decision she'd made every quarter for the past two years: staff the features, defer the migration.

The engineering director sitting across from her had made the same case again. The cross-team migration would reduce the incident rate by an estimated 40%. The debt it addressed was eating roughly half a day per week per engineer in workarounds and context-switching. Over twelve months, deferring it was costing more than doing it. He'd shown the math.

She acknowledged the math. She said the org couldn't absorb a slow quarter right now. She said they'd revisit in Q4.

Here's what the director didn't know: the VP's annual bonus was structured 70% on features shipped, 30% on customer satisfaction scores, with features measured by count against the annual roadmap. The migration would ship zero features. It would not show up in customer satisfaction scores for at least two quarters. By the VP's incentive structure, the migration was not a project — it was a cost with no measurable return inside her bonus window.

She wasn't wrong to do what she did. She was doing exactly what the compensation structure was designed to produce. This is the thing engineers almost never learn, and spend years being confused by: the compensation structure doesn't just reward certain behaviors. In any organization where people are making rational decisions, it *defines* them.

---

## The Mechanism

The same logic destroyed mortgage lending quality during one of the industry's most destructive cycles. Originators were paid per loan closed, regardless of whether the loan was ever repaid. This separated the person taking the action — and receiving the reward — from the person bearing the consequence of the action. Quality collapsed because quality was not in the incentive function. This wasn't an industry staffed by bad people. These were professionals responding accurately to the rewards in front of them. The separation of action from consequence was built into the structure.

Goodhart's Law formalizes the underlying mechanism: when a measure becomes a target, it ceases to be a good measure. The observation applies wherever measurement feeds into reward — which is to say, everywhere in an organization that has a compensation structure.

Engineering is not immune. Consider story points per sprint. Lines of code committed. Pull requests merged per week. Incident time-to-close measured without tracking recurrence. Each of these became, at some point, someone's performance metric, and each was subsequently gamed. Not because the engineers involved were bad at their jobs, but because they were good at their jobs: they identified what was being measured and optimized for it. The metric and the underlying thing it was supposed to measure decoupled. The organization got exactly what it measured for, and then wondered why the underlying thing had deteriorated.

The point here is not that metrics are bad. It's that the incentive structure doesn't encourage certain behavior — it defines it. When there is a divergence between what an organization says it values and what it measures and rewards, the measurement and reward win. Every time. Not occasionally. Every time. The stated values become a kind of organizational aspiration that exists in documents and presentations and never quite survives contact with review season.

---

## Reading the Comp Structure

Engineers are rarely given a clear view of how compensation works above their immediate level. They see their own performance rubric. They may not know how their manager's bonus is calculated, what metrics drive the VP's annual review, or whether headcount factors into title progression. This opacity is itself a feature of most comp structures — explicit visibility would make the misalignment too obvious.

But the structure is legible if you know what to look for.

Start with what feeds into performance review. Not the formal rubric, which usually lists admirable things like "technical leadership" and "cross-functional collaboration." Start with what actually moves the needle when the calibration conversation happens. What do managers highlight in positive terms when someone gets promoted? What kinds of work are conspicuously absent from the people who stall at a given level?

You can observe this directly over a review cycle without being told anything. What language appears in promotion announcements for people who got through at your target level? What does a manager bring up first when describing someone who had a strong year? In many organizations, the pattern is consistent: visible output that can be attributed to an individual and described in one sentence to someone who wasn't present. Features shipped. Projects led. Incidents resolved. These are the things that survive calibration. Infrastructure that silently improves reliability doesn't. Mentorship that leveled up a junior engineer doesn't. Documentation that saved the next team six weeks doesn't. You can also ask: a manager who trusts you will often answer "what would make this year's calibration harder for me to make a case for?" directly if you frame it as career planning, not grievance.

Then look at bonus timing and structure. Annual bonuses create a horizon of approximately twelve months. Quarterly targets shorten it further. The structural consequence is simple and profound: any project whose costs arrive before the bonus period ends but whose benefits arrive after it is systematically disadvantaged, regardless of its actual value. Technical debt paydown is the canonical case. The cost is engineering time spent now. The benefit — faster delivery, lower incident rate, less cognitive overhead — arrives in the next period. A manager who defers that investment looks better this year. The manager who makes the investment looks worse this year and may not be present to collect the credit when the benefit arrives.

Finally, look at whether headcount tracks manager status. In many organizations, a manager's compensation band and title progression correlate with the number of people they manage. This creates an incentive to accumulate headcount that is independent of whether additional headcount creates value. Engineers in these organizations observe the pattern without naming its mechanism: projects staffed at 150% of what they require, coordination costs that scale with team size rather than complexity, managers who resist efficient restructuring because it means reducing their own organizational footprint. The manager who would be absorbed in a sensible reorg has a structurally sound reason to resist it.

There is a practical diagnostic that clarifies most of this. Ask: what would a rational actor do, given this comp structure? Map it out. Now compare that to what the organization claims to value. The gap between those two things is the organization's real gap — not the gap between its values and its behavior, but the gap between its incentive structure and its stated strategy. Everything in that gap will tend to happen according to the incentive structure, regardless of what the slides say.

---

## The Tournament Problem

In 1981, economists Edward Lazear and Sherwin Rosen formalized what they called tournament theory: instead of paying people based on absolute output, you pay them based on relative rank. The analysis explained several features of real compensation structures that were otherwise puzzling — why pay often increases faster than productivity at the top of hierarchies, why executives in similar roles sometimes earn wildly different amounts. Tournaments are cheap to administer. You only need to rank people, not measure their absolute output. And they can generate intense effort from participants who believe they can win.

What tournament theory underweighted, and what the decades of organizational research that followed made clear, is that tournaments convert colleagues into competitors. In any setting where an individual's compensation and advancement depend on performing better than the people around them, helping those people is a direct threat to one's own position. The tournament creates a perverse incentive: information-sharing, collaboration, and mentorship all improve the performance of people who are, in the compensation structure, your rivals.

Stack ranking is a tournament. Forced distributions — requiring that a fixed percentage of employees be rated top performers, a fixed percentage average, and a fixed percentage underperformers — are a tournament. Any review process where the grade curves, where raises are capped as a pool that gets divided, where promotion slots are limited regardless of performance, is a tournament.

The documented outcomes are consistent across organizations that have used these systems at scale. A large software company that used forced distributions for over a decade documented the pattern before discontinuing it: engineers began steering toward solo-attributable work, knowledge-sharing in design reviews declined measurably, and infrastructure staffing became chronically difficult. Research on relative performance evaluation in controlled settings has reproduced the information-hoarding effect: participants share less with peers when their pay depends on outranking them than when it depends on their absolute output. Engineers stop sharing knowledge about hard problems because a colleague who solves a hard problem improves their competitor's rank. Reviews get gamed toward solo-attributable visible work because collaborative work is difficult to claim.

Consider a concrete version of this. An infrastructure engineer builds a new deployment pipeline that triples team delivery speed. The work is genuinely excellent. At the end of the year, she sits in a calibration alongside the engineer who shipped three user-facing features with direct revenue attribution. The infrastructure work is real. The impact is real. But in a forced distribution, where someone has to rank in the bottom third, her work is harder to quantify, her impact harder to trace directly, her contribution less legible to people who weren't watching closely. She ranks in the middle.

The next year, she starts working on user-facing features. This is rational. It is also a loss: the next deployment pipeline is nobody's job.

This pattern has a name worth knowing: the promotion-motivated rewrite. An engineer approaching a promotion threshold needs to demonstrate scope and impact in a form legible to a calibration committee. The most legible form is leading a large, visible technical project. A functioning but unglamorous service gets rewritten from scratch — six months, significant risk, team migration cost, and the result is a system roughly equivalent in quality to the one it replaced. The engineer gets promoted. The team absorbed the migration. This is not unique behavior. It is the expected output of a promotion system that rewards legible scope over quiet reliability.

If you are doing infrastructure work in a tournament system, you face a genuine choice: make the work legible in terms the tournament rewards — quantify the impact, attribute it clearly, write it up before review season, not after — accept that the system will undervalue it and plan accordingly, or work to change the measurement. Each of these is a rational response. What isn't rational is continuing to do invisible work and expecting the tournament to reward it.

---

## Short-Termism by Design

The quarter is a fiction. Not a harmful fiction — coordination requires shared time horizons — but a fiction nonetheless. Nothing about software development, system architecture, or technical debt naturally aligns to three-month increments. A quarterly bonus cycle imposes that window as the operative planning horizon, and every tradeoff made inside that window is shaped by it.

The short-termism problem compounds in a way that's easy to understate. A team that defers a significant technical investment in Q1 doesn't merely face the same decision in Q2. The cost of the investment has grown — the debt has accumulated, the systems have diverged further, and the engineers who understood the original context have moved on. More importantly, in Q2, the team also faces the cost of still delivering under a slower, more complex codebase. The rational case for deferral looks the same in Q2 as it did in Q1. And in Q3. Each deferred quarter makes the next deferral easier to justify and harder to justify stopping. This is not an incidental feature. It is a structural property of compensation cycles applied to compounding problems.

The same distortion shows up in architectural decisions, and here the stakes are higher. The architectural choices made under a quarterly target structure will systematically reflect that horizon: pragmatic in the near term, fragile at the edges where flexibility was sacrificed for speed. Short-term compensation windows push toward decisions that are legible and deferrable: keep the monolith because migrating to services would cost two slow quarters, buy the vendor solution because evaluating owned alternatives takes too long, defer the platform investment because the platform's value shows up in other teams' metrics and not in yours. These are often the wrong architectural choices. They are also the rational ones, given the time horizon embedded in the performance management system.

Architecture that was good for the current compensation window is frequently bad for the system that needs to change three years later. The engineers making those choices aren't being reckless. They're being rational given the incentives they're operating under. The VP in the opening staffs the features over the migration not because she's failing to understand the long-term consequence, but because the long-term consequence falls outside her compensation window and the short-term cost falls squarely inside it. If her bonus included a component tied to long-term engineering velocity, or if her performance review included her team's delivery rate improvement over two years, she would make different choices. The math the engineering director brought into the room would become relevant. The same inputs, the same people, a different structure — a different outcome.

---

## The Equity Trap

Equity vesting is frequently described as a retention mechanism. That description is accurate. What it obscures is that retention and engagement are different things, and the mechanisms that produce one can actively undermine the other.

A senior engineer with eighteen months left until a four-year cliff has done the math. The number is meaningful — enough to affect material life decisions. She has also concluded, after two years on the team, that the technical direction is wrong, the manager is ineffective, and her skills are stagnating in ways that will cost her later. None of this is surprising to the people who work alongside her.

The financially rational response is to stay, perform at a level that avoids a formal performance improvement process, and collect the grant. This is not laziness. It is a straightforward response to an incentive structure that makes departure expensive. The comp structure has created a captive.

The team now absorbs a senior engineer who is physically present and professionally disengaged. The performance review system is not designed to catch this. Marginal acceptable performance is not the same as low performance. The gap between an engaged senior engineer and a vesting senior engineer is often invisible on any formal metric and obvious to anyone who works with them daily. Knowledge doesn't flow. Design reviews go through the motions. Problems that would have been caught in a more engaged state get through.

When you see a senior engineer who is present but checked out — who produces acceptable work but never stretches, who stops advocating for architectural investments, who moves toward safe and visible work rather than the problems that need solving — ask yourself what their vesting schedule looks like. The comp structure may be producing exactly that behavior. The diagnostic is not "this person has lost motivation." It is "the vesting cliff is doing its job, and something else needs to change." That is a structural fix: accelerated vesting schedules, more frequent cliff events, clear paths to new problems before the current role has stagnated. Retention instruments that don't account for engagement will produce exactly this outcome, reliably, and then attribute it to something else.

The inverse problem is equally real, and it belongs in the same analysis: the engineers who contribute most through unglamorous, unlegible work — maintaining the critical service nobody wants to own, de-escalating the cross-team conflict that would have consumed a sprint, mentoring the junior engineers who eventually ship the features — are also the engineers most likely to leave when the compensation structure doesn't see what they do. An organization that uses equity primarily as a retention mechanism ends up measuring whether people are still here and calling it engagement. The gap between the two shows up in design reviews that go through the motions and architectural decisions that nobody will own in a year.

---

## What You Can Change and What You Cannot

The path to different outcomes is not better arguments for the right answer. It is either changing the measurement or making the investment legible enough to survive the current one. Everything else in this section is downstream of that distinction.

The objection worth addressing directly: "This is how organizations coordinate. Compensation aligns incentives by design. You're describing features, not bugs."

This is partly right, and this chapter is not arguing otherwise. Incentive structures work. The mortgage originators were doing what their structure told them to do. The VP is staffing features because her structure says to. These are systems functioning as designed. The critique is not that incentives produce behavior — it is that most engineering organizations haven't thought carefully about what behaviors their specific incentive structures actually produce, and they express surprise at the results.

But there's a sharper version of the objection that deserves a real answer: "If you're telling me to translate technical arguments into incentive language, you're accepting that incentive language is the only language that matters. Isn't that just capitulation?"

No — and the distinction is important. Understanding how a room is wired is not the same as endorsing how it's wired. The engineer who learns to speak incentive language and uses it to get the right infrastructure investment funded is not endorsing short-termism as a philosophy. They are getting the right thing built. Contrast this with what happens when the engineer refuses to speak that language: the better technical choice loses, the infrastructure doesn't get funded, the system continues to accumulate debt, and the compensation structure continues unchanged. The translation is a tool, not a concession. The goal is to get the right thing made. The framing is in service of that goal, not a substitute for it.

What is within reach: advocating for outcome-based metrics, which are harder to decouple from actual value creation, is almost always worth doing even if the org moves slowly. Making long-term investments legible to people whose comp depends on short-term output is something every technical lead can do. This means translating "we need to address this debt" into something that lands in the other person's incentive language — and the VP's bonus formula is already a worked example.

The engineering director brought math to that meeting. The math was right. What the math didn't do was show up in the VP's incentive language. The same case, reframed: "This migration would reduce our incident rate by an estimated 40%. Based on the current correlation between our incident rate and our NPS data, that's roughly a three-point NPS improvement over two quarters — which moves the needle meaningfully against the customer satisfaction component of your annual target." The argument hasn't changed. The framing has. That is the translation. It doesn't require accepting that NPS is the only thing that matters. It requires knowing that NPS is what the person across the table is measured on, and showing them that the right technical decision also advances their measurement.

What is usually not within reach: changing another person's bonus formula, eliminating a forced distribution from above your level, restructuring equity vesting for someone else's team. These are real problems. They are solved at the level of organizational design, not at the level of individual conversation. Recognize which battles won't be won on technical merit alone, and be honest about which problems require structural change rather than better framing.

The deeper shift, for engineers who internalize this: organizations are not hypocritical when they say they value infrastructure investment but fund features. They are following their measurement systems exactly as designed. The surprise is itself a diagnostic failure — it indicates that the people expressing it don't yet have the framework to trace the cause. Building that framework is the work.

---

## What Changes Monday

Stop being surprised when the organization chooses the thing its compensation structure rewards over the thing it says it values. This is not cynicism — it is the most accurate description of how these systems work. The next time a VP funds features over the migration, the next time a manager resists a reorg that would make the organization more efficient, the next time an engineer chooses a visible project over an unglamorous one, ask: what does their comp structure actually measure? The answer will almost always explain the choice completely. The energy you've been spending on surprise and frustration is better spent on understanding the structure.

Start reading the compensation structure explicitly. Not the stated values. Not the all-hands slides. The actual measurement and reward mechanisms. What feeds into the calibration that determines raises and promotions? What's in the bonus formula, and what's the weighting? What is a manager's title progression correlated with — scope measured by headcount, or scope measured by impact? Run the diagnostic: what would a rational actor do, given this structure? Map it against what the organization claims to want. That gap is where the actual decisions live — and it predicts them almost every time.

The longer-term shift is this: start operating with explicit awareness of which investments are legible in the current incentive system and which aren't, and surface that distinction before decisions get made, not after. The infrastructure project that will improve delivery speed in six months is not going to get funded because it's the right technical choice. It will get funded when someone has translated its value into the language of the measurement system currently in use — or when someone has changed the measurement system to include it. Your job, at the senior level, is increasingly to be the person who makes that translation. Not because you've given up on getting the right thing done, but because this is how the right thing actually gets done.
