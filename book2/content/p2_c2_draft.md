# How Compensation Shapes What Gets Built

The VP ran a clean meeting. Clear agenda, good facilitation, no rambling. She came prepared. And when the discussion turned to Q3 staffing, she made the decision that she'd made every quarter for the past two years: staff the features, defer the migration.

The engineering director sitting across from her had made the same case again. The cross-team migration would reduce the incident rate by an estimated 40%. The debt it addressed was eating roughly half a day per week per engineer in workarounds and context-switching. Over twelve months, deferring it was costing more than doing it. He'd shown the math.

She acknowledged the math. She said the org couldn't absorb a slow quarter right now. She said they'd revisit in Q4.

Here's what the director didn't know: the VP's annual bonus was structured 70% on features shipped, 30% on customer satisfaction scores, with features measured by count against the annual roadmap. The migration would ship zero features. It would also not show up directly in customer satisfaction scores for at least two quarters. By the VP's incentive structure, the migration was not a project — it was a cost with no measurable return inside her bonus window.

She wasn't wrong to do what she did. She was doing exactly what the compensation structure was designed to produce. This is the thing engineers almost never learn, and spend years being confused by: the compensation structure doesn't just reward certain behaviors. In any organization where people are making rational decisions, it *defines* them.

---

## The Mechanism

In the 1970s, Soviet factories were given nail production quotas measured by weight. The result: factories produced enormous useless nails. A few large nails made quota easily. Nobody wanted them. The quotas switched to count. Factories produced enormous quantities of tiny tacks. Nobody wanted those either. The actual goal — useful nails in the distribution the economy needed — was never in the incentive function, so it never got produced.

This is not a story about Soviet central planning specifically. It's a story about what happens when you attach a reward to a proxy measure. The proxy becomes the goal. The actual goal becomes irrelevant to the people being evaluated. Soviet factory managers weren't foolish. They were rational. The problem was the measurement.

Goodhart's Law formalizes this: when a measure becomes a target, it ceases to be a good measure. The observation applies wherever measurement feeds into reward — which is to say, everywhere in an organization that has a compensation structure.

The same logic destroyed mortgage lending quality in the years before the 2008 financial crisis. Originators were paid per loan closed, regardless of whether the loan was ever repaid. This separated the person taking the action — and receiving the reward — from the person bearing the consequence of the action. Quality collapsed because quality was not in the incentive function. This wasn't an industry staffed by bad people. These were professionals responding accurately to the rewards in front of them. The separation of action from consequence was built into the structure.

Engineering is not immune to this. Consider story points per sprint. Lines of code committed. Pull requests merged per week. Incident time-to-close measured without tracking recurrence. Each of these became, at some point, someone's performance metric, and each was subsequently gamed. Not because the engineers involved were bad at their jobs, but because they were good at their jobs: they identified what was being measured and optimized for it. The metric and the underlying thing it was supposed to measure decoupled. The organization got exactly what it measured for, and then wondered why the underlying thing had deteriorated.

The point here is not that metrics are bad. It's that the incentive structure doesn't encourage certain behavior. It defines it. When there is a divergence between what an organization says it values and what it measures and rewards, the measurement and reward win. Every time. Not occasionally. Every time. The stated values become a kind of organizational aspiration that exists in documents and presentations and never quite survives contact with review season.

---

## Reading the Comp Structure

Engineers are rarely given a clear view of how compensation works above their immediate level. They see their own performance rubric. They may not know how their manager's bonus is calculated, what metrics drive the VP's annual review, or whether headcount factors into title progression. This opacity is itself a feature of most comp structures — explicit visibility would make the misalignment too obvious.

But the structure is legible if you know what to look for.

Start with what feeds into performance review. Not the formal rubric, which usually lists admirable things like "technical leadership" and "cross-functional collaboration." Start with what actually moves the needle when the calibration conversation happens. What do managers bring up in positive terms when someone gets promoted? What kinds of work are conspicuously absent from the people who stall at a given level? In many organizations, this turns out to be: visible output that can be attributed to an individual and described in one sentence to someone who wasn't present. Features shipped. Projects led. Incidents resolved. These are the things that survive calibration. Infrastructure that silently improves reliability doesn't. Mentorship that leveled up a junior engineer doesn't. Documentation that saved the next team six weeks doesn't.

Then look at bonus timing and structure. Annual bonuses create a horizon of approximately twelve months. Quarterly targets shorten it further. The structural consequence is simple and profound: any project whose costs arrive before the bonus period ends but whose benefits arrive after it is systematically disadvantaged, regardless of its actual value. Technical debt paydown is the canonical case. The cost is engineering time spent now. The benefit — faster delivery, lower incident rate, less cognitive overhead — arrives in the next period. Under annual bonus structures, a manager who defers that investment looks better this year. The manager who makes the investment looks worse this year and may not be present to collect the credit when the benefit arrives.

This is not a mystery, and it does not require bad actors. It is the predictable output of a compensation structure with a short time horizon applied to decisions with long payoff periods. The decision about whether to invest in infrastructure or ship a feature is, in practice, a decision about who bears the cost and who receives the benefit, and those people are often in different review cycles.

Finally, look at whether headcount tracks manager status. In many organizations, a manager's compensation band and title progression correlate with the number of people they manage. This creates an incentive to accumulate headcount that is independent of whether additional headcount creates value. Engineers in these organizations observe the pattern without necessarily naming its mechanism: projects staffed at 150% of what they require, coordination costs that scale with team size rather than complexity, managers who resist efficient restructuring because it means reducing their own organizational footprint. The manager who would be absorbed in a sensible reorg has a structurally sound reason to resist it. The behavior isn't political in the pejorative sense — it's a rational response to a compensation structure that makes headcount loss expensive.

There is a practical diagnostic that clarifies most of this. Ask: what would a rational actor do, given this comp structure? Map it out. Now compare that to what the organization claims to value. The gap between those two things is the organization's real gap — not the gap between its values and its behavior, but the gap between its incentive structure and its stated strategy. Everything in that gap will tend to happen according to the incentive structure, regardless of what the slides say.

---

## The Tournament Problem

In 1981, economists Edward Lazear and Sherwin Rosen formalized what they called tournament theory: instead of paying people based on absolute output, you pay them based on relative rank. The analysis explained several features of real compensation structures that were otherwise puzzling — why pay often increases faster than productivity at the top of hierarchies, why executives in similar roles sometimes earn wildly different amounts. Tournaments are cheap to administer. You only need to rank people, not measure their absolute output. And they can generate intense effort from participants who believe they can win.

What tournament theory underweighted, and what the subsequent thirty years of organizational research made clear, is that tournaments convert colleagues into competitors. In any setting where an individual's compensation and advancement depend on performing better than the people around them, helping those people is a direct threat to one's own position. The tournament creates a perverse incentive: information-sharing, collaboration, and mentorship all improve the performance of people who are, in the compensation structure, your rivals.

Stack ranking is a tournament. Forced distributions — requiring that a fixed percentage of employees be rated top performers, a fixed percentage average, and a fixed percentage underperformers — are a tournament. Any review process where the grade curves, where raises are capped as a pool that gets divided, where promotion slots are limited regardless of performance, is a tournament.

The documented outcomes are consistent across organizations that have used these systems. Engineers stop sharing knowledge about hard problems because a colleague who solves a hard problem improves their competitor's rank. Reviews get gamed toward solo-attributable visible work because collaborative work is difficult to claim. High-value infrastructure work, which requires deep coordination and benefits many teams, becomes harder to staff because it doesn't produce the individual attribution the tournament rewards.

Consider a concrete version of this. An infrastructure engineer builds a new deployment pipeline that triples team delivery speed. The work is genuinely excellent. At the end of the year, she sits in a calibration alongside the engineer who shipped three user-facing features with direct revenue attribution. The infrastructure work is real. The impact is real. But in a forced distribution, where someone has to rank in the bottom third, her work is harder to quantify, her impact harder to trace directly, her contribution less legible to people who weren't watching closely. She ranks in the middle.

The next year, she starts working on user-facing features. This is rational. It is also a loss: the next deployment pipeline is nobody's job.

This is not a failure of individual judgment. It is the expected output of a system that rewards legible, individually attributable work over infrastructure that benefits everyone and can be attributed to no one in particular. The compensation structure produced that outcome as surely as the Soviet factory produced useless nails. You built the measurement. The engineers optimized it.

---

## Short-Termism by Design

The quarter is a fiction. Not a harmful fiction — coordination requires shared time horizons — but a fiction nonetheless. Nothing about software development, system architecture, or technical debt naturally aligns to three-month increments. A quarterly bonus cycle imposes that window as the operative planning horizon, and every tradeoff made inside that window is shaped by it.

Here is the structural problem in its simplest form: any investment whose costs are paid now but whose benefits arrive later is disadvantaged by short bonus windows, regardless of the investment's actual value. The future benefit is discounted not by risk or uncertainty, but by the fact that it will accrue to the company in a period after the current compensation cycle closes.

Technical debt paydown is the canonical example. The cost is engineering time taken away from feature delivery in the current quarter. The benefit — a team that delivers faster, a codebase that's easier to reason about, an incident rate that declines — arrives in the following quarters. Under a quarterly target structure, the team that invests in the paydown looks slower this quarter. The team that defers the paydown looks faster this quarter. The debt compounds.

Consider a specific version. A team estimates that accumulated technical debt is cutting delivery speed by roughly 40%. The fix requires two slow quarters. Every quarterly planning cycle, the product manager argues that the debt paydown should happen "after this launch." The engineering manager agrees, because their quarterly goals are measured identically. Nobody in the room has an incentive to absorb two bad quarters for future benefit. The debt grows. The team gets slower. In year two, the 40% estimate becomes 50%, and the cost of the fix has grown to match.

Now consider the VP from the opening. Her bonus is 70% features shipped, 30% customer satisfaction. She has a cross-team migration that would reduce future incident rates and, eventually, improve customer satisfaction — but wouldn't show up in either metric this year. She has two features that check boxes on the annual roadmap and will be counted in Q4. The migration is the higher-value investment. She staffs the features.

This is worth saying clearly: she is not making a bad decision. She is making the decision her compensation structure was designed to produce. If you designed a structure to produce a different decision — if her bonus included a component tied to long-term reliability, or if her performance review included the engineering team's velocity improvement over two years — she would make different choices. The conversation with the engineering director would end differently. The math he brought into the room would become relevant.

Architecture investment suffers from the same distortion. Good architectural decisions are often invisible in the short term — they matter most years later, when the system needs to change and can, or cannot. The architectural choices made under a quarterly target structure will systematically reflect that horizon: pragmatic in the near term, fragile at the edges where flexibility was sacrificed to speed. The engineers making those choices aren't being reckless. They're being rational given the time horizon embedded in their performance management system.

The same logic affects project selection at every level. Long-horizon, high-value projects are systematically undervalued by systems with short compensation windows. The infrastructure migration. The platform investment. The rewrite that would simplify the next three years of development. All of these have costs that arrive before the benefits. In a system where compensation tracks short-term output, the people who champion these investments absorb the cost and may not collect the credit. Rational people stop championing them.

---

## The Equity Trap

Equity vesting is frequently described as a retention mechanism. That description is accurate. What it obscures is that retention and engagement are different things, and the mechanisms that produce one can actively undermine the other.

A senior engineer with eighteen months left until a four-year cliff has done the math. The number is meaningful — enough to affect material life decisions. She has also concluded, after two years on the team, that the technical direction is wrong, the manager is ineffective, and her skills are stagnating in ways that will cost her later. None of this is surprising to the people who work alongside her.

The financially rational response is to stay, perform at a level that avoids a formal performance improvement process, and collect the grant. This is not laziness. It is a straightforward response to an incentive structure that makes departure expensive. The comp structure has created a captive.

The team now absorbs a senior engineer who is physically present and professionally disengaged. The performance review system is not designed to catch this. Marginal acceptable performance is not the same as low performance. The gap between an engaged senior engineer and a vesting senior engineer is often invisible on any formal metric and obvious to anyone who works with them daily. Knowledge doesn't flow. Design reviews go through the motions. Problems that would have been caught in a more engaged state get through.

The organization has achieved retention. It has not achieved engagement. These are frequently conflated because the measurement — is the engineer still here? — is identical. The thing being measured is not.

The inverse version of this trap is equally real. The engineers who would contribute most in a given role may be the ones who leave when equity structures fail to account for the actual value of unglamorous, unglamorous work. The engineer who maintains the critical service no one wants to own, who de-escalates the cross-team conflict that would have consumed a sprint, who mentors the junior engineers who ship the features — this person may not be building the legible scope that equity conversations reward. If the compensation structure doesn't see that work, the people doing it have good reason to find roles where what they do is legible.

Equity creates retention. It does not create engagement. Organizations that conflate the two end up confused about why their headcount is stable and their output is declining.

---

## What You Can Change and What You Cannot

The objection worth addressing directly: "This is how organizations coordinate. Compensation aligns incentives by design. You're describing features, not bugs."

This is mostly right, and this chapter is not arguing otherwise. Incentive structures work. The mortgage originators were doing what their structure told them to do. The VP is staffing features because her structure says to. These are the systems functioning as designed. The critique is not that incentives produce behavior — it is that most engineering organizations haven't thought carefully about what behaviors their incentive structures actually produce, and they express surprise at the results.

The tournament complaint, the short-termism, the equity retention trap — these are not accidental. They are predictable outputs of specific structural choices. The factory that measures nails by weight is not surprised to get large nails. The engineering organization that measures individual velocity and never measures infrastructure impact should not be surprised when infrastructure is underinvested. The organization whose managers' comp tracks headcount should not be surprised at resistance to efficient restructuring. The surprise is itself a failure: it indicates that the people who designed the compensation structure did not think through what it would produce, or that the people experiencing its outputs don't have the framework to trace the cause.

Engineers and engineering managers benefit from being able to read comp structures as signals. This is a diagnostic skill, not a design specification. If you understand that a VP's bonus is 70% tied to features shipped, you can predict which tradeoff conversations will go well and which won't. That knowledge is useful regardless of whether the structure changes. You stop wasting political capital on conversations that the structure will not permit, and you start framing the ones you need to have in terms that reach across the incentive gap.

Some things are within your reach. Advocating for outcome-based metrics — metrics that are hard to decouple from actual value creation — is almost always worth doing, even if the org moves slowly. Making long-term investments legible to the people whose comp depends on short-term output is something every technical lead can do: translate "we need to address this debt" into "here is what delivery speed looks like in two quarters if we do this versus if we don't, in terms of features per sprint." The abstract investment becomes a concrete feature comparison. That framing can move conversations that pure technical argument cannot.

Recognize which battles won't be won on technical merit alone. The VP is not going to fund the migration because the technical case is strong. She will fund it when the case is legible in her incentive language — when someone has translated "this reduces incident rate" into "this improves the customer satisfaction component of your bonus by roughly this much, in this timeframe." Making that translation is not capitulating to a flawed system. It's speaking the language of the room you're in.

There's a specific pattern worth naming because it recurs: the promotion-motivated rewrite. An engineer approaching the senior-to-staff transition needs to demonstrate scope and impact in a form that's legible to a calibration committee. The most legible form is leading a large, visible technical project. The most legible metric for impact is a quantifiable improvement. A functioning but unglamorous service gets rewritten from scratch — six months, significant risk, team migration cost, and the result is a system roughly equivalent in quality to the one it replaced. The engineer gets promoted. The team absorbed the migration. This is not unique behavior. It is the expected output of a promotion system that rewards legible scope over quiet reliability.

Understanding this doesn't mean accepting it. It means making the work that is actually valuable visible before review cycles, not after. The engineer who maintains the critical service, who catches the edge cases in design review, whose quiet interventions save the team a week of debugging — this person needs to make that work legible on a regular cadence, in writing, in the language that calibration committees use. Not to game the system, but because the alternative is that valuable work goes unrewarded, and then the people doing it stop doing it, and then no one does it. Making invisible work visible is not self-promotion. It is information provision.

The deeper shift, for engineers who internalize this: organizations are not hypocritical when they say they value infrastructure investment but fund features. They are following their measurement systems exactly as designed. The path to different outcomes is not better arguments for the right answer. It is either changing the measurement or making the investment legible enough to survive the current one.

---

## What Changes Monday

Stop being surprised when the organization chooses the thing its compensation structure rewards over the thing it says it values. This is not cynicism — it is the most accurate description of how these systems work. The next time a VP funds the features over the migration, the next time a manager resists a reorg that would make the organization more efficient, the next time an engineer chooses a visible project over an unglamorous one, ask yourself: what does their comp structure actually measure? The answer will almost always explain the choice completely. The energy you've been spending on surprise and frustration is better spent on understanding the structure.

Start reading the compensation structure explicitly. Not the stated values. Not the all-hands slides. The actual measurement and reward mechanisms. What feeds into the calibration that determines raises and promotions? What's in the bonus formula, and what's the weighting? What is a manager's title progression correlated with — scope measured by headcount, or scope measured by impact? Once you can answer these questions, the organizational behavior that used to seem random will start to look like arithmetic. Run the diagnostic: what would a rational actor do, given this structure? If that behavior is not what the organization claims to want, you have found the gap — and you know where the leverage is.

The longer-term shift is this: start operating with explicit awareness of which investments are legible in the current incentive system and which aren't, and surface that distinction before decisions get made, not after. The infrastructure project that will improve delivery speed in six months is not going to get funded because it's the right technical choice. It will get funded when someone has translated its value into the language of the measurement system currently in use — or when someone has changed the measurement system to include it. Your job, at the senior level, is increasingly to be the person who makes that translation. Not because you've given up on getting the right thing done, but because this is how the right thing actually gets done.

