# Why Reorgs Rarely Work

The email arrives on a Tuesday. It has a subject line like "Exciting Organizational Update" or "New Chapter for Our Team" and is written in the flattened prose of corporate announcement — passive voice, careful optimism, a quoted senior leader offering enthusiasm for the change. You read it twice. The boxes on the new org chart have different labels. Some managers have new titles. A few dotted lines have become solid lines, a few solid lines have become dotted.

And you know, with the weary certainty of someone who has been through this before, that the problem it was meant to fix will not be fixed. The funding fight that caused the original friction is still controlled by the same budget process. The architectural dispute that produced the inter-team hostility is still unresolved. The incentive misalignment that makes cross-functional collaboration feel like pulling teeth is still embedded in how people are measured and promoted. The boxes are new. The pathology is not.

This chapter is about why that keeps happening, and what to do instead.

The core argument is narrow and worth stating plainly: reorganizations are predominantly a management action reflex — a structural answer to what are usually incentive, communication, or strategy problems. Because structure is visible and changeable on a short timeline, it gets changed. Because incentives, informal power, and culture are harder to see and slower to change, they don't. The result is new boxes on the org chart and the same pathologies underneath.

---

## The Reflex

When something is wrong in an organization — products slipping, cross-team friction escalating, talent leaving, customers complaining — there is an enormous gravitational pull toward structural intervention. A new team. A reorganized reporting chain. A newly-minted VP. A merged division, or a split one.

The pull has a name in the behavioral economics literature: action bias. Under uncertainty and perceived threat, doing something feels better than doing nothing, even when the action is disconnected from the actual cause of the problem. The clearest illustration: a goalkeeper diving to one side during a penalty kick even though staying in the center would improve their odds. The dive feels like action. Standing still feels like passivity. The same pattern appears anywhere high-stakes decisions are made under time pressure and uncertainty.

Organizations under pressure exhibit the same pattern. Restructuring is not just an available action — it's the action that most visibly signals that leadership is responding. New org charts circulate. Town halls are held. Managers are introduced in new roles. The volume of visible change activity looks, from outside the room, exactly like progress. Progress requires changing outcomes; restructuring requires only changing the chart. The chart is much easier.

If the answer to "what will the reorg fix?" is "clearer ownership," ask: ownership of what decision, measured how, backed by what budget authority? If no one can answer that, the reorg is theatrical.

There is a second driver, specific to engineering organizations, that compounds the action bias: the new-manager reorg reflex. When a new senior leader joins an organization — a new VP of Engineering, a new CTO, a new Director who inherited three teams — they reorganize their area. Not always, but often enough that engineers who have been around for a few years simply wait it out. "The new VP hasn't done their reorg yet" is a sentence said with the resigned familiarity of a weather forecast. The exact structure before will not be the exact structure after. Both were probably fine. The disruption was the point — it establishes the new leader's authority, lets them put their stamp on the organization, and creates the appearance of decisive action in the critical early months when they are being closely watched.

The effect of this reflex, compounded across leadership layers and years, is organizations that restructure every twelve to twenty-four months — a pace at which no structure can demonstrate its effectiveness before the next disruption begins. Estimates of reorg failure rates vary in management research, but the consistent finding is that structural changes alone — without accompanying changes to incentives or decision rights — rarely sustain the behavior changes they were designed to produce. The most common failure mode is not that the restructuring is poorly executed. It's that the restructuring doesn't address the actual problem.

---

## What Survives Any Reorg

Imagine an iceberg.

The visible portion is the org chart: titles, reporting relationships, team names, budget envelopes. This is what a reorg changes. You can update the org chart in a presentation, send it to HR, and have it implemented by Monday. The visible layer is genuinely visible — it's the part leadership can draw, explain, and revise.

Below the waterline is everything that actually determines how work gets done.

Just below the surface is the behavior layer: how people actually make decisions, who gets consulted informally before a decision is "official," whose objection will block a proposal regardless of whether they are in the formal approval chain, which engineers get pulled into the hard architectural debates. This layer shifts after a reorg, but slowly and partially. The informal influence of a technically respected engineer doesn't evaporate because their manager now reports to a different VP. The informal habit of consulting the long-tenured principal engineer before committing to any database change doesn't end because that engineer is now technically on a different team.

Deeper still is the culture and norms layer: what is rewarded in practice versus what is stated in the annual review rubric; which behaviors are tacitly penalized even when they're explicitly encouraged; the real criteria by which careers advance or stall. This layer changes on a timescale measured in years, not quarters, and does not respond to reporting-line changes at all.

Deepest of all is the incentive architecture: compensation structures, metric definitions, performance review criteria, career path dependencies. This layer is the most powerful and the least touched by structural change. If engineers are measured on delivery velocity and not on the quality of the code they leave behind, the same behavior follows them regardless of which team they sit on. If platform teams are measured on infrastructure uptime and product teams are measured on feature output, the same misalignment will express itself in friction, regardless of whether platform reports to the CTO or to a new Infrastructure VP.

Organizations resist fundamental architectural change not because leaders are timid, but because reliability and consistency are primary sources of organizational survival. Stakeholders — customers, employees, regulators, investors — reward organizations that behave predictably and consistently. Structural change disrupts the routines that produce that reliability, making the organization more vulnerable during the transition period. The inertial forces are not in the reporting lines. They are in the culture, the coalitions, the sunk costs, and the precedents that have become norms. Structural change leaves those forces intact.

This is why the post-reorg period so often disappoints. The organization heals around the change. Informal power networks re-establish themselves around new titles. Political coalitions reform. Budget control migrates back to whoever controls the actual funding decisions, regardless of the org chart position. Within twelve to twenty-four months, the organization functionally resembles its pre-reorg state — same informal dynamics, slightly different letterhead.

---

## Three Structural Traps

The abstract principle becomes concrete in historical patterns. Three examples from the past sixty years illustrate the same failure mode at different scales.

**The decade of structural churn.** A major computing company, dominant in its market for decades, entered the late 1980s facing a changed competitive landscape it was structurally ill-equipped to navigate. Over several years, the company ran through multiple major restructurings. An early wave aimed at reducing bureaucratic layers and focusing on profit. Then a far more radical decentralization: the company broke itself into semi-autonomous lines of business — separate units for storage, software, processors, peripherals, services. The logic was that a company of its scale could not compete against focused specialists by remaining integrated. Each unit would be leaner, faster, more accountable.

The practical result was increased internal complexity. The units competed with each other for the same customers. Transfer pricing disputes between divisions became a management preoccupation. Sales forces from different units showed up in front of the same clients with conflicting pitches. Leadership presided rather than acted. The company posted staggering losses. Spinoff of the individual units was under active consideration.

The CEO who ultimately reversed the strategy was direct: the problem was not the reporting lines. It was that internal culture rewarded divisional competition over customer outcomes. He reversed the decentralization and reorganized around how customers bought rather than around how the company manufactured. But critically — and this is what distinguishes the intervention that worked from the interventions that didn't — he changed the incentive structure simultaneously. Executives were required to own company stock outright rather than merely holding options, directly aligning their financial interests with shareholder outcomes rather than divisional performance metrics.

The structural change was one element of a package. It was the incentive and culture changes that made it hold.

**The knowledge they couldn't act on.** A company that had dominated the physical imaging market for decades invented a key digital sensor in the mid-1970s. For the next three decades, it watched digital technology approach and then consume its core business while undertaking repeated structural maneuvers that addressed none of the underlying conflict.

The problem was not knowledge. The company's engineers understood what was happening. The problem was incentive architecture. The existing business generated high margins. The new technology generated thin margins and would cannibalize the high-margin business at scale. One CEO said publicly that the new technology would destroy the chemical business. That wasn't rhetorical excess — it was an accurate description of the incentive structure. Every dollar of digital revenue replaced several dollars of much higher-margin legacy revenue.

In response to this conflict, the company created a dedicated digital group. This was a structural change intended to signal organizational commitment to the new technology. The group had a budget, a charter, and a mandate. It did not have an incentive structure uncoupled from the business it was supposed to eventually replace. It was funded from the profits of the high-margin legacy business and was tacitly expected not to destroy that business while it figured out how to replace it. The contradiction was structural, and no structural change could resolve it. The company went bankrupt decades after inventing the technology that disrupted it.

The lesson is precise: the organization had the knowledge and lacked the incentive alignment to act on it. A new box on the org chart doesn't close that gap.

**The sixty-year cycle.** Matrix management — dual reporting to both a functional manager and a project or product manager — has now been adopted, abandoned, and rediscovered multiple times in living memory. It originated in aerospace in the early 1960s, where it addressed a genuine dual-mandate problem: how to run mission-specific project teams drawing on specialists who also had to maintain functional excellence. The structure was load-bearing in that context. Projects had clear scope and end dates; functional departments had ongoing knowledge that needed to remain coherent across multiple projects simultaneously. Matrix addressed that exact tension.

When matrix spread through corporate management in the 1970s, it carried the structure without the context. Companies without the dual-mandate problem adopted it because it looked modern. The pathologies emerged predictably: unclear accountability when the two reporting lines disagreed, political conflict between functional and project managers, decision paralysis, excessive coordination overhead. By the early 2000s, matrix was broadly considered a cautionary tale in management circles.

Then the underlying coordination problem reasserted itself — how do you maintain functional excellence while delivering cross-functional products? — and organizations began reintroducing dual-reporting structures under new names: chapter-tribe models, platform-stream models, enabling team structures. The names changed. The underlying tension, and the underlying structural response, did not.

The functional-project tension that matrix was designed to solve is an incentive problem: whose interests does the specialist serve when their functional manager and their project lead want different things? Every reinvention of matrix structure — under whatever name — imports that same unresolved measurement question. The structure changes; the incentive conflict doesn't.

The matrix story is a microcosm of the broader reorg cycle. A genuine problem produces a structural solution. The structure addresses one dimension of the problem and creates new problems. The structure is abandoned. The original problem reasserts itself because its non-structural causes were never addressed. The structural solution is rediscovered by people who don't remember why it was abandoned. Repeat.

---

## Three Patterns You've Seen Before

The historical cases make the principle legible. The following scenarios make it recognizable in the organizations most engineers work in today. Each one follows the same script: a structural intervention, an unchanged actual bottleneck, eventual discovery that the change fixed nothing.

**Reporting lines change, budget authority doesn't.** A platform engineering organization is reorganized so that infrastructure teams report to a newly-created Infrastructure VP instead of the CTO. The intent is to give infrastructure more organizational autonomy and reduce the approval bottleneck that slowed investment decisions. Eighteen months later, the same funding debates are happening, with the same outcomes. The Infrastructure VP is now in the meetings the CTO was in before, making the same arguments against the same CFO mental model of infrastructure as a pure cost center. The bottleneck was the budget process and the CFO's model of the business. Neither changed. The root cause is in the incentive layer — the infrastructure team is still measured as a cost center, not as a product with adoption and return — and no new reporting line fixes it.

**The team split that must still coordinate on everything.** A large team is divided to create clearer accountability between two product areas. Both teams continue to share the same underlying platform, the same deployment pipeline, the same on-call rotation, and the same customer segments. Every cross-cutting concern now requires a coordination meeting between two teams with separate managers who have separate performance incentives. The coordination overhead increases. The shared dependencies mean neither team has the autonomy the split was supposed to create. What changed: the team boundary. What didn't change: the technical coupling that determined how much coordination was required. The root cause is in the architecture layer — the split created organizational seams that don't match the system seams — and the fix requires aligning team structure with service ownership, not redrawing the management chart again.

**The center of excellence with no authority.** A reorg creates a new horizontal function to standardize engineering practices across divisions. The function is staffed, given a charter, and asked to produce guidelines and frameworks that will lift practices across the organization. It has no budget authority over the divisions and no role in the hiring or performance review of the engineers it is trying to influence. The divisions continue to make their own decisions. The central function produces documents. The documents are read, occasionally cited in presentations, and then the divisions continue doing what their own incentives and local managers direct them to do. Two years later, the function is quietly absorbed into a different team in the next restructuring. The root cause is in the incentive architecture — divisional engineers are measured on divisional outcomes, not on adherence to company-wide standards — and until that changes, the central function is pushing a rope.

---

## When Structure Actually Is the Problem

The argument so far should not slide into the claim that structure never matters. It does. There are cases where the current structure actively misroutes communication or decision authority in a way that cannot be fixed without changing the boxes. The question is whether yours is one of those cases.

Conway's Law — Mel Conway's 1968 observation that organizations produce systems that mirror their communication structures — provides the clearest diagnostic. If a company built its engineering organization around a monolithic architecture and subsequently migrated to distributed services, the old team structure creates genuine technical friction. Team boundaries that don't correspond to service ownership boundaries produce integration problems: unclear who owns the interface contract, who is responsible for a failing interaction, who should be consulted for changes that cross the boundary. Here, restructuring to align team boundaries with system architecture is load-bearing. The structure is generating the technical problem. Changing the structure can fix the technical problem.

Similarly, when two groups have become so politically toxic that all collaboration has broken down and there is no path to repair within the current structure, a structural change may be the only available intervention — not because it fixes the underlying relationship, but because it separates the parties and removes the structural context in which the conflict regenerated itself.

And when the business model has changed so fundamentally that the old structure is simply wrong — when the company used to sell products and now sells services, when the product has shifted from hardware to software, when the customer relationship has changed from transactional to subscription — structure may genuinely need to follow strategy.

The diagnostic question is: is the current structure actively misrouting communication or decision authority? Not "could we imagine a different structure?" but "is this specific structure producing friction that a different structure would not?" If the answer is yes, and if you can trace the friction directly to the reporting boundaries or decision rights, then structural change is warranted.

The checklist for a load-bearing reorg is short and demanding: Are you changing incentives simultaneously? Are you changing how performance is measured? Are you changing budget authority? Are you changing promotion criteria? If the answer to all of these is no, and you are only moving names on the chart, you are rearranging load-bearing walls while leaving the foundation untouched. The structure will settle back into something resembling the problem you were trying to solve, because the forces that created the problem were never addressed.

---

## The Hard Alternative

If reorgs are not the answer, what is?

The actual work is diagnosing which layer of the iceberg the problem lives in, and then intervening at that layer. This is harder than drawing a new org chart, takes longer, and produces fewer visible signals of action. It is also more likely to work.

**If the problem is incentive misalignment**, change the incentives. This means naming the specific behavior you want, identifying what the current incentive structure rewards instead, and changing the measurement or reward directly. If platform teams are measured on uptime while product teams are measured on feature velocity, the friction between them is predicted by the measurement structure. Change what platform teams are measured on — adoption, developer satisfaction, time-to-onboard — and the behavior changes. This requires political will and access to the performance review process, neither of which is free. But it addresses the cause.

**If the problem is communication breakdown**, address the communication structure directly. This does not mean reorganizing. It means changing who is in which meetings, what decisions require which groups to be consulted, who has explicit decision rights on classes of questions. Decision-rights frameworks — simple written agreements about who decides what in disputed areas — can often resolve the friction that feels like it requires structural change, in a fraction of the time and with far less disruption.

**If the problem is genuine architectural misalignment between team structure and system structure**, then a reorg is warranted — but do the Conway's Law analysis first, and use the checklist from the previous section. Map your communication structure and your system architecture and identify specifically where the mismatch is generating friction. Then restructure to align them, not to create a feeling of change.

**If the problem is culture**, be honest with yourself that you are looking at a multi-year project. Culture changes through sustained changes in what is rewarded and what is penalized in practice, who gets promoted, what leaders model in their own behavior, and what incidents get treated as defining versus forgettable — the postmortem that becomes a case study versus the one that gets quietly filed away. A reorg does not change culture. Culture lags incentive changes by roughly eighteen to thirty-six months because it requires enough instances of the new behavior being rewarded — and the old behavior not being — for the pattern to become internalized as a norm. A sustained and consistent set of incentive changes, made by leaders who personally embody the new expectations, change culture on that timescale. If you need culture to change in six months, you have set an unachievable goal and should revise it.

The common thread is precision. Structural changes are blunt instruments applied to problems that usually have much more specific causes. The question to ask before any restructuring is not "what should the new org look like?" It is "what specific behavior is the current system producing, and why?" The answer to the second question tells you what to change. More often than not, it is not the org chart.

---

## What Changes Monday

**When you're skeptical of a reorg being designed.** Next time you are in a room where one is being designed, ask the specific question: what behavior does this structural change create, and why will that behavior change be durable? If the answer is "clearer ownership," push for specificity. Clearer ownership of what decision, measured how, backed by what budget authority? If those questions cannot be answered, the reorg is theatrical. You don't have to be the one who kills it — that may not be your call — but you can refuse to treat it as the solution to a problem it isn't solving.

**When a reorg is happening anyway and you can't stop it.** Use the window it creates. The social dynamics reset that restructurings produce is real. Informal coalitions are temporarily disrupted, political equilibria are unsettled, and people are in a more open and receptive state than they will be once the dust settles. If there is a behavior change you have been trying to create — a new norm around architecture review, a shift in how on-call is structured, a change in how technical decisions get documented — the post-reorg window is the best time to move on it. The restructuring creates the opening. You close it with the actual change. But you have roughly six to twelve months before the informal structures re-establish around the new boxes. Do not waste the window on process improvements. Use it on the incentive and culture changes that the reorg announcement made briefly possible.

**When you're in a position to change incentives directly.** Start there. Incentive changes are less visible than org changes and more durable. Changing what gets measured in a performance review, what gets praised in a team forum, what gets credited in a promotion decision — these create behavior change that survives the next reorg. They require access and courage, but they work. A reorg without an accompanying incentive change is betting that new names on the chart will change behavior that the old names, under the old incentives, produced. That bet rarely pays off.

**How to run the layer diagnosis.** When you are facing organizational friction — slow decisions, misaligned incentives, coordination overhead, cross-team conflict — resist the reflex to propose a structural solution. Instead, work through four questions:

1. If we changed nothing but the reporting lines, would the behavior change?
2. If we changed what people are measured on, would the behavior change?
3. If we changed who attends which meetings, would the behavior change?
4. If nothing is different a year from now, what specifically hasn't changed — and where in the iceberg does that live?

The answers tell you which layer the problem actually lives in. Question 1 pointing to yes suggests a structural problem. Question 2 pointing to yes suggests an incentive problem. Question 3 pointing to yes suggests a communication or access problem. Question 4 is the honest audit: if you can't name what would be different, and where in the stack the change needs to happen, you don't yet know what the problem is — and any intervention is a guess.

New org charts are easy to draw. The problem is that they mostly describe who the manager of each team is, not who controls the budget, not what gets rewarded, not how the real decisions get made. Those latter things are what actually determine whether your organization works. Change those, and the structure becomes secondary — because the real work was never about the chart.
