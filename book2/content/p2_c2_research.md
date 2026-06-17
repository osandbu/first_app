# Research Notes: p2_c2 — "How Compensation Shapes What Gets Built"

## Core Argument

Compensation structures are not just HR mechanics — they are the most reliable signal of what an organization actually values. When the stated strategy diverges from what gets rewarded, watch the compensation structure win every time. Engineers who understand this can read an org's real priorities from its pay design, not from its all-hands slides.

---

## 1. Historical Parallels

### Soviet Quota System (nails by weight vs. by count)
The canonical case study in Goodhart's Law applied to production. When Soviet factories were given nail quotas measured by weight, they produced a small number of enormous, useless nails. When quotas switched to count, factories produced enormous quantities of tiny nails. The metric became the goal; the actual goal (useful nails) was abandoned. The lesson: the moment you attach a reward to a proxy measure, people optimize the proxy. This is not malice — it is rational behavior under the incentive system provided.

Application to engineering: story points per sprint, lines of code committed, number of PRs merged, incident response time measured only by time-to-close (not recurrence). Any metric that gets tied to performance review will be gamed, first unconsciously and then deliberately.

### Mortgage Origination and the 2008 Financial Crisis
Mortgage originators were paid per loan closed, regardless of whether the loan was ever repaid. This created a clean separation between the person taking the risk (the eventual MBS holder) and the person being rewarded (the originator). Quality collapsed because quality was not in the incentive function. Originators were not evil; they were responding rationally to the rewards in front of them.

Application to engineering: when engineers are rewarded for shipping features and not for what happens to those features afterward — adoption, stability, maintenance burden — the same separation of action from consequence occurs. The engineer who ships a fragile system and moves to the next project before the pager goes off is behaving exactly like the mortgage originator.

### Stack Ranking at Large Technology Companies
Multiple large technology companies adopted forced-distribution performance reviews through the 1990s and 2000s. The most aggressive versions required that a fixed percentage of employees be rated "top performers," a fixed percentage "average," and a fixed percentage "underperformers" who were at risk of termination. The documented outcomes were consistent: engineers stopped collaborating on hard problems because helping a colleague improve their performance was a direct threat to one's own relative ranking. Interviews with engineers from these companies describe deliberately not sharing knowledge, steering colleagues toward easier problems that would not compete with their own review scores, and avoiding high-risk high-reward projects in favor of visible incremental work.

The structural problem: tournament-style compensation converts colleagues into competitors. The behavior it produces is individually rational and collectively destructive.

Reference: Pfeffer & Sutton's research on competition within organizations; also Kohn's "Punished by Rewards" (1993) on the corrosive effects of competitive reward structures on intrinsic motivation.

---

## 2. Key Frameworks

### Pay-for-Performance Research
The empirical record on pay-for-performance is deeply mixed. For simple, well-defined, measurable tasks with clear output (piece-rate manufacturing, sales calls made), performance incentives work as advertised. For complex cognitive work with hard-to-measure outputs and strong interdependencies, the evidence is weaker and frequently negative.

Deci, Koestner & Ryan's 1999 meta-analysis (Psychological Bulletin) of 128 studies found that tangible, expected rewards contingent on performing a task significantly undermined intrinsic motivation for interesting tasks. The effect was robust across settings.

Dan Ariely's research on performance bonuses for cognitive tasks (conducted with MIT, Carnegie Mellon, University of Chicago) found that higher bonuses led to worse performance on tasks requiring creativity, judgment, and problem-solving. The mechanism: the reward makes people anxious, which narrows cognitive attention in a way that hurts complex work.

Engineering takeaway: the tasks where incentives are most likely to be counterproductive are exactly the tasks that make senior engineering valuable — system design, architectural tradeoffs, debugging hard problems, mentoring.

### Tournament Theory
Edward Lazear and Sherwin Rosen (1981) formalized tournament theory: instead of paying people based on absolute output, you pay based on relative rank. The upside is that tournaments are cheap to administer (you only need to rank people, not measure absolute output) and they can generate intense effort from participants who believe they can win.

The downsides that are underemphasized:
- Tournaments discourage cooperation (helping others improve their rank reduces yours)
- They generate sabotage risk (degrading colleagues' work improves your relative position)
- They incentivize working on visible, legible, solo-attributable work over collaborative infrastructure
- The variance in outcomes discourages risk-taking in the middle of the tournament (safe incremental delivery vs. ambitious uncertain projects)

Stack ranking is a tournament. So is any compensation structure where raises or equity grants are determined by relative peer comparison.

### Goodhart's Law in Compensation Contexts
"When a measure becomes a target, it ceases to be a good measure." Applied to compensation: any metric that feeds into bonus calculation or performance review will be optimized for, and the optimization degrades the metric's signal value. Organizations respond by adding more metrics. This adds bureaucracy without improving signal quality, because engineers learn to optimize the new metrics too.

The stable state is a measurement arms race. The solution is not better metrics — it is structuring incentives around outcomes that are difficult to decouple from actual value creation.

### Short-Termism in Compensation
Annual bonus cycles create a natural horizon of approximately 12 months. Quarterly targets shorten it further. The structural consequence: any project whose costs are paid in the current period but whose benefits arrive in the next period is disadvantaged, regardless of its NPV. Technical debt paydown is the canonical case — the cost is now (engineering time), the benefit is later (faster future delivery, lower incident rate). Under an annual bonus structure, the manager who defers that investment looks better this year. The manager who makes the investment looks worse this year and may not be around to collect the credit.

Equity vesting introduces the inverse problem: engineers with unvested equity are strongly incentivized not to leave, which can produce retention of disengaged engineers who are actively reducing team velocity but cannot afford to quit. The performance review system then has to deal with the results of the retention system.

### Headcount as a Status Signal
In many organizations, a manager's compensation, title, and internal status are correlated with the number of people they manage. This creates an incentive to grow headcount independent of whether additional headcount creates value. Engineers in these organizations observe: projects get staffed at 150% of what they require, coordination costs rise, and the manager who led the large team gets promoted while the manager who ran a lean high-output team struggles to justify their level.

This is not exclusively a compensation story — it is also an org design story — but compensation is the mechanism that makes headcount accumulation sticky. Managers who trim their teams are frequently reducing their own compensation and status.

---

## 3. Concrete Scenarios (no company names)

**Scenario A: The Q4 Feature VP**
A VP's annual bonus is tied 70% to features shipped and 30% to customer satisfaction scores, with features measured by count. In Q3, the VP faces a choice: staff a cross-team migration that would reduce future incident rates but ships no user-visible feature, or staff two new features that check boxes on the annual plan. The migration is the higher-value investment. The VP staffs the features. This is not a failure of judgment — it is the compensation structure producing exactly the output it was designed to produce.

**Scenario B: The Vesting Cliff Engineer**
A senior engineer has 18 months left until a four-year cliff. Their honest assessment: the technical direction is wrong, the manager is ineffective, and their skills are stagnating. The financially rational response is to stay, do enough to avoid a PIP, and collect the grant. The team absorbs a senior engineer who is physically present but mentally absent. The performance review system is not designed to catch this; marginal acceptable performance is not the same as low performance. The comp structure has created a captive with every incentive to coast.

**Scenario C: Stack Ranking and the Infrastructure Engineer**
An infrastructure engineer builds the deployment pipeline that triples team delivery speed. Her work is undeniably high value. But at review time, the ranking committee compares her to the engineer who shipped three user-facing features with direct revenue attribution. The infrastructure work is hard to quantify in the forced-distribution model. She ranks in the middle. The next year, she starts working on user-facing features. The pipeline is nobody's job.

**Scenario D: The Manager Building Empire**
An engineering manager's comp band and title progression are determined in part by org size. A reorg opportunity arises that would efficiently merge two teams doing related work. The manager who would absorb the other team gets a promotion. The manager who would be merged into the other team loses headcount, potentially loses title, and resists. The reorg stalls. The organizational inefficiency persists because the incentive structure makes the efficient outcome personally costly to one of the two parties with veto power.

**Scenario E: Quarterly Targets and Technical Debt**
A team has accumulated enough technical debt that engineers estimate delivery speed is roughly 40% of what it could be. The fix requires two quarters of slower feature output while the debt is addressed. Every quarterly planning cycle, the product org argues that the debt paydown should happen "after this launch." The engineering manager agrees because their quarterly goals are measured the same way as the product manager's. Nobody has an incentive to absorb two bad quarters for future benefit. The debt compounds.

**Scenario F: The Promotion-Motivated Rewrite**
An engineer approaching the senior-to-staff transition needs to demonstrate "scope and impact." The most legible form of scope is leading a large technical project. The most legible form of impact is a rewrite with quantifiable improvements. A functioning but unglamorous service gets rewritten from scratch — six months of engineering time, significant risk, and the new system is roughly equivalent in quality. The engineer gets promoted. The team has absorbed the migration cost. This is not unique behavior; it is the expected output of a promotion system that rewards legible scope over quiet reliability.

---

## 4. Counter-Arguments

**Counter-argument 1: "Compensation aligns incentives by design — this is how organizations coordinate."**
This is mostly right, and the chapter should not argue otherwise. Incentives are coordination mechanisms. The problem is not that compensation structures produce behavior — it is that organizations frequently design compensation structures for one goal while claiming to pursue another, and then express surprise at the gap. The 2008 mortgage originators were doing exactly what their compensation told them to do. The VP shipping features in Q4 is doing exactly what their bonus plan instructs. The critique is not that incentives work — it is that most engineering orgs have not thought carefully about what behaviors their incentive structures actually produce, and they pay the price in the form of technical debt, attrition, and misallocated effort.

**Counter-argument 2: "You can't design perfect compensation — this is just human nature."**
True. The chapter is not prescribing a perfect compensation structure. The argument is narrower: engineers and engineering managers benefit from being able to read compensation structures as signals of what the organization will actually prioritize. This is a diagnostic skill, not a design specification. If you understand that your VP's bonus is 70% tied to features shipped, you can predict which tradeoff conversations will go well and which will not. That knowledge is useful regardless of whether the compensation structure changes.

---

## 5. Data Points and Studies

- Deci, Koestner & Ryan (1999): Meta-analysis of 128 studies. Contingent tangible rewards undermine intrinsic motivation for interesting tasks. Effect size is large and consistent.
- Ariely et al. (2005/2008): "Large Stakes and Big Mistakes" — high performance bonuses hurt outcomes on cognitive/creative tasks. Replicated in US and India samples.
- Lazear (2000): "Performance Pay and Productivity" — natural experiment study of pay-for-performance in manufacturing. Strong effects for piece-rate work, minimal in complex team environments.
- Lazear & Rosen (1981): Tournament theory original formulation. Foundation for understanding stack ranking economics.
- Staw (1981): "The Escalation of Commitment" — sunk cost effects are amplified when the original decision-maker is also the person being evaluated on outcomes. Relevant to project cancellation dynamics.
- Pfeffer (1998): "The Human Equation" — broad critique of rank-and-yank and incentive pay systems in knowledge work organizations.
- Survey data from compensation consulting firms consistently shows engineers rank "interesting work" and "growth opportunity" above total compensation in stated preferences — but revealed preferences (where people actually go) are more complicated and context-dependent.

---

## 6. Suggested Chapter Structure

1. **The mechanism** — how compensation produces behavior (Goodhart intro, Soviet nails, mortgage originator). Establish that this is not about bad actors but rational responses to incentive structures.

2. **Reading the comp structure** — a framework for inferring organizational priorities from how people are paid. Bonus timing, what feeds into review, how headcount factors in. Engineers rarely see these structures explicitly; this section explains what to look for.

3. **The tournament problem** — stack ranking, forced distributions, and why competition destroys collaboration. What the research says. The infrastructure engineer scenario.

4. **Short-termism by design** — annual/quarterly horizons and their structural effects on technical debt, architecture investment, and project selection. The VP Feature scenario and the debt accumulation scenario.

5. **The equity trap** — vesting cliffs, retention-vs-engagement, and what to do when you realize your team has people who are financially captive but disengaged.

6. **What you can change and what you cannot** — the chapter should not end with helplessness. Engineers and engineering managers can: advocate for outcome-based metrics, structure projects to make long-term investments legible, understand which battles won't be won on technical merit alone, and recognize when the compensation structure makes a certain org unable to make certain decisions.

---

## Tone Notes

The chapter should resist the temptation to moralize about "bad incentives." The more powerful frame is analytical: these structures are not mistakes, they are choices, and they produce predictable outputs. The engineer who can predict those outputs is more effective than one who is perpetually surprised that the organization doesn't behave according to its stated values.

Avoid economic jargon where possible. Tournament theory can be introduced through the observable behavior (colleagues competing instead of collaborating) before the academic label is attached. Goodhart's Law is best explained through the Soviet nail example before naming it.

The target reader has experienced these dynamics firsthand. The chapter's job is to give them language and frameworks for something they already half-understand intuitively.
