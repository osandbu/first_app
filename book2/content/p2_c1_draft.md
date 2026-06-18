# Everyone Is Rational, Given Their Incentives

The meeting had been going for forty minutes when you realized the manager across the table wasn't going to budge. You'd come prepared. The proposal made sense: move two engineers from his team to a new initiative, a high-priority project that had been waiting three months for staffing. His team had capacity. The work was strategic. You'd even offered to make the transfer temporary. He smiled, said he'd have to "check on project commitments," and the conversation circled back to where it started.

You left thinking: what's wrong with him? The choice was obvious. Is he protecting a fiefdom? Does he just not like you? Is he incapable of seeing past his own team?

Probably none of those things. The manager was, in all likelihood, doing exactly what made sense given his situation. The more interesting question — the one that actually helps you — is not "what's wrong with him?" but "what's in it for him to do what I'm asking?"

The answer, almost certainly, was: not much.

---

## What "Rational" Actually Means Here

Before going further, a clarification. Rational, in the way economists use it, doesn't mean "logical" or "admirable." It means: responding to the actual rewards and penalties in your environment. And when those rewards and penalties diverge from what the organization says it cares about, people follow the actual rewards. Every time.

This is not cynicism. It's a description of how systems work. People aren't optimizing for job descriptions. They're optimizing for what they're measured on, what they're praised for, what protects them from risk, and what gives them security. Those things are almost never perfectly described in any formal document.

The principal-agent problem — a concept from economics worth naming here, though we'll spend a full chapter on it later — describes the gap between what an organization wants from someone and what that person has reason to do. The gap is not the result of bad character. It's the result of incomplete contracts, misaligned measurements, and the impossibility of watching everything all the time. No performance review captures everything that matters. No job description specifies every judgment call. In the gaps, people do what they're rewarded for.

The framework that comes out of this is simple to state but surprisingly hard to apply consistently: before you diagnose organizational behavior as dysfunction, map the incentives. Describe what the person doing the behavior is actually rewarded for, afraid of, and measured on. If you do this carefully, the behavior will almost always make sense.

There's an old heuristic called Hanlon's Razor: never attribute to malice what can be explained by incompetence. That's useful as far as it goes. But the organizational version goes one step further: never attribute to malice or incompetence what can be explained by incentives. Most of the time, when something looks wrong, the person doing it isn't bad at their job or acting in bad faith. They're responding accurately to the system they're in.

---

## Canonical Patterns: The Incentive Map in Action

Let's make this concrete. Each of the following scenarios is drawn from patterns that appear across engineering organizations at different scales. In each one, the behavior looks wrong from the outside and rational from the inside.

**The manager who won't share headcount.** In most large organizations, a director's formal influence correlates with team size. Headcount is budget. It's seats at the planning table. It's the organizational signal that someone's work is important enough to require a large team. A director with forty engineers occupies a different organizational weight class than one with fifteen, even if their actual scope of responsibility is similar. Research on organizational behavior in hierarchical firms has documented this pattern: managerial status tracks direct-report count with a consistency that outperforms scope, budget, or results as a predictor of perceived seniority.

Given this, when someone asks a director to give up two engineers, they're asking him to voluntarily shrink his organizational footprint. The formal argument is that the engineers would come back, or that the initiative is important. But the informal calculation is different: the engineers might not come back, and even if they do, there's a period of reduced size and influence. The behavior — resistance, delay, "let me check on project commitments" — is the natural response to being asked to trade a concrete, near-term cost for a diffuse, uncertain benefit.

The fix is not to find directors with more generous personalities. The fix is to stop using headcount as the proxy for importance.

**The team that won't touch the legacy system.** There's a system in nearly every organization that everyone knows needs a rewrite. It's old. It's fragile. The documentation, if it exists at all, describes a version from years ago. The two engineers who understand it are quietly essential because of that understanding, not in spite of it.

The rewrite never happens. Why?

Map the incentives: the engineers who understand the legacy system have built their indispensability on that knowledge. A rewrite eliminates the monopoly. The team that would own the rewrite doesn't own the system now — which means they carry the risk of the project without the authority that comes from having built the original. If the rewrite succeeds, they've replaced a difficult system with a slightly less difficult one. If it fails, they've broken something important and they own that failure.

The work is also invisible in the way that feature development is visible. Features are shippable, demonstrable, tied to roadmaps that get reviewed in quarterly planning. A rewrite is a 12-to-18-month project with no user-facing output and no milestone that will land on a slide. Performance reviews reward what's measurable and visible.

No individual decision in this system is wrong. The senior engineers protecting their specialized knowledge, the team that declines to take on risk without authority, the engineering manager who won't champion a project that won't show up in the metrics — each is responding rationally to their situation. The aggregate outcome — a system that slowly becomes more dangerous and less understood — is globally irrational. No single person designed it that way. The system produced it from locally rational choices.

This is what organizational theorists mean when they talk about local rationality producing global irrationality. It's also the engineering version of a Nash equilibrium: no individual actor has reason to defect from the pattern, so the pattern persists even when everyone can see it's bad.

The traffic jam analogy is useful here. No driver wants a traffic jam. Each driver makes individually rational decisions — merge when the gap opens, slow for the car ahead, change lanes when it looks faster. The jam emerges from the aggregate of those decisions. No individual driver produced it intentionally or irrationally. The system produced it from local optimization. The same is true of the untouchable legacy codebase, the undocumented critical component, the platform that nobody uses. These are organizational traffic jams: the emergent product of incentive structures, not the deliberate choices of bad actors.

**The VP who kills the better solution.** A team has built something technically superior to the existing approach. They've done the analysis. The numbers are clear. And a VP has decided the organization will continue with the existing system.

The explanation that engineers usually reach for is politics, or ego, or not-invented-here syndrome. Sometimes that's right. More often, the incentive map tells a different story.

The VP built their reputation on the existing system. It is, in some meaningful way, their legacy. The new approach was developed by a different team. If the new system is adopted and succeeds, the VP's team gets credit for stepping aside gracefully — which is not the same as credit for winning. If the new system is adopted and struggles during migration, the VP's team takes blame for the transition pain. If the existing system is maintained and continues to have problems, those problems are known and managed.

More concretely: the VP's performance is measured in the near term. The new approach requires real investment in migration, training, and a period of lower velocity before the benefits materialize. Those costs are front-loaded and certain. The benefits are back-loaded and probabilistic. A rational near-term calculation often points toward continuing with what works well enough.

This isn't weakness or corruption. It's how individual incentive horizons interact with investment decisions that have long payoff periods. Organizations that want different outcomes need to change the horizon, not the VP.

**The engineer who won't document.** Documentation is a form of public goods: everyone benefits, and the person who produces it pays the full cost. In a system where performance reviews measure individual output — commits, shipped features, resolved tickets — documentation appears nowhere on the ledger. It takes time. It makes the author more replaceable. It transfers knowledge to others who will benefit from it without any mechanism for the author to receive credit.

The engineer who doesn't document isn't lazy or unkind. They're operating in a system that genuinely doesn't reward the thing you're asking them to do. Change the measurement — make knowledge transfer visible, reward it, include it explicitly in how people are evaluated — and the behavior changes. The person doesn't change. The incentive does.

**The platform team that serves itself.** An internal platform team builds something technically impressive — a unified deployment pipeline, a shared data layer, an internal developer tooling suite. The engineers who built it are proud of it. But the product teams who were supposed to use it have quietly developed workarounds, local scripts, and informal processes that bypass it entirely.

The platform team can't understand the rejection. They're offering something genuinely capable. But map their incentives: the platform team is measured on what they ship, not on whether downstream teams adopt it or succeed with it. There is no feedback loop that makes low adoption costly to the platform team. There is no mechanism by which a product team's struggle with the platform translates into a cost on the platform team's metrics. So the platform team optimizes for the sophistication of what they build, because that's what they're judged on. The product teams, who are judged on shipping their own work, do whatever is fastest — which increasingly means going around the platform.

The same dynamic plays out in any relationship between a supporting team and the teams it serves when there is no measurement connecting the provider's incentives to the consumer's outcomes. The information that the platform isn't working doesn't arrive. The frustration accumulates on one side of the relationship while the other side reports success.

---

## When the Signal Never Arrives

Everything so far has been frustrating but manageable. Incentive misalignment produces inefficiency, friction, and organizational drag. Those are real costs. But there's a category where the same dynamic produces not just inefficiency but catastrophe, and understanding it changes the stakes of the whole framework.

In January 1986, engineers at a NASA contractor spent the night before a shuttle launch arguing against the launch. They had data on O-ring performance in cold temperatures. They had reason to believe the seals would not perform reliably in the conditions forecast for launch day. They argued, formally, through official channels.

The launch proceeded. The shuttle broke apart 73 seconds after liftoff.

This is not a story about villains. The managers who overrode the engineers were not indifferent to safety. They were operating inside a system with a specific incentive structure: the shuttle program's continued funding was tied, in part, to launch cadence. Launch delays were costly — not abstractly costly, but costly in terms of budget, narrative, and political survival. Schedule pressure was concrete and near-term. The risk from O-ring failure at low temperatures was probabilistic and uncertain.

The engineers who raised concerns faced a different incentive structure. They had already gone through official channels. The organizational norm had established — through a gradual process that sociologist Diane Vaughan later called the normalization of deviance — that the burden of proof was on the person arguing against launch. "Prove it's unsafe" rather than "prove it's safe." Each prior flight that succeeded in spite of concerns about the O-rings reinforced the pattern: the concern was raised, the launch proceeded, nothing happened. The deviance became normal. The concerns became noise.

The signal was present. The information existed. The incentive structure systematically degraded that signal before it could influence the decision. This is a structural failure — one that didn't require any individual to be negligent or dishonest. Every step made sense from the inside. The outcome was catastrophic.

The same pattern, at lower stakes, plays out constantly in engineering organizations. The engineer who doesn't escalate the architecture concern because the last three times they raised it nothing changed. The team that stops reporting schedule risk because it got them additional scrutiny without additional help. The manager who tells leadership that things are on track because the last person who delivered bad news got cut from the meeting list. Each of these is a small, locally rational suppression of signal. Accumulated across an organization, they produce the conditions where the information that could prevent serious failures doesn't arrive at the people who need it.

---

## The Skeptic's Objection: What About Bad Actors?

If every organizational dysfunction is explained by incentives, does this framework become an alibi? Someone wrongs you and the response is: "well, their incentives made them do it." That's not accountability. That's learned helplessness with intellectual camouflage.

This objection is legitimate, and the framework needs to answer it directly.

Incentive mapping is a diagnostic tool, not a verdict. The purpose of starting with incentives is not to excuse behavior — it's to identify the most durable lever for changing it. If the incentive structure explains the behavior, then the most effective intervention is structural: change what people are measured on, change what gets rewarded, change the cost of the behavior you want to reduce. That intervention works across everyone in the role, not just the current occupant. It's also more durable than individual correction, which depends on the current person staying in the role and taking the feedback to heart.

But — and this matters — structural explanation does not preclude individual accountability when it's warranted. The sequence is: exhaust the structural explanation first. If the incentive structure explains the behavior and you can change the structure, do that. If the behavior persists after you've changed the incentives, or if the behavior is genuinely harmful and the person is choosing it despite correct incentives, then individual accountability is appropriate.

There are genuinely malicious actors and genuinely negligent ones. The framework doesn't deny this. It says: treat individual character as the residual explanation, not the first one. Most of the time, when you map the incentives honestly, the behavior makes sense and the right intervention is structural. Some of the time — in cases of persistent, harmful behavior where the structural explanation doesn't hold — individual accountability is the right tool.

Starting with incentives also protects you from a specific and common mistake: confronting someone over behavior that is the predictable output of their environment, producing a difficult conversation, generating resentment, and changing nothing. If the incentive is still there, the behavior will come back, in this person or the next one who sits in the same seat. The hard conversation was a cost with no durable benefit.

---

## The Incentive Map as a Practical Tool

Given all of this, what does it actually look like to map incentives before diagnosing dysfunction?

The next time you're frustrated by something an organization is doing — a team that won't collaborate, a manager who's blocking a decision, a process that produces the wrong output — stop before you attribute it to character. Work through these questions:

What is this person or team actually measured on? Not what their job description says. What shows up in their performance review? What do they report on to leadership? What metric, when it moves, makes their quarter better or worse?

What are they afraid of? What outcome would cause them serious professional pain? Visible failure, losing a resource, being blamed for something outside their control, having a project cancelled?

What would they have to sacrifice to do the thing I'm asking? Time, political capital, team capacity, a relationship, their current metrics?

What do they get if they help me? Not what I'm offering — what do they actually receive in their incentive system if they cooperate?

If you work through these questions honestly, the behavior almost always makes sense. The manager who blocked you for forty minutes wasn't being irrational. He was being precisely rational given a system that treats headcount as organizational importance. The team that won't touch the legacy system isn't being cowardly. They're declining to take on risk without reward in a system where the reward for fixing invisible problems is invisible.

This is clarifying, not defeating. Understanding the incentive structure tells you where to apply pressure. If you want the manager to agree to the transfer, you need to address the thing he's actually losing — not just make the case for why it's good for the organization. If you want the team to take on the legacy rewrite, you need to change the reward structure for that work — not just explain why it needs to happen.

The incentive map is the difference between trying to push someone up a hill and figuring out why the hill exists.

There's a related skill that comes with practice: distinguishing between the things that look like friction and are actually immovable given the current structure, versus the things that look immovable but have a lever you haven't found yet. A tech lead who understands incentives can tell the difference between "this will never change because the measurement won't change and I can't change the measurement" and "this will change if I offer the right thing, because the block is a specific fear I can address." That distinction determines where to spend political capital. Spending it on the first category is expensive and fruitless. Spending it on the second is often more effective than expected, because most people are genuinely relieved when someone understands their actual constraints rather than just repeating the case for why the thing they want is a good idea.

Behavioral economists have documented a related dynamic at the individual level: people respond to actual rewards, not intended ones. Introducing an external reward for something people were doing intrinsically can actually reduce the behavior, because the extrinsic reward changes the nature of the activity. This is sometimes called the crowding-out of intrinsic motivation. The practical implication for engineering organizations: when you change how something is measured, you don't just add a signal — you sometimes change how people relate to the underlying work. Incentive design is not neutral. It shapes what people care about, not just what they do.

---

## What Changes Monday

Stop explaining organizational behavior you don't like as stupidity or bad faith. This is not primarily a moral reframe — it's a practical one. If the cause of the behavior is character, the intervention is individual. If the cause is structure, the intervention is structural. Structural interventions are almost always more durable and more likely to actually change things. When you misdiagnose a structural problem as a character problem, you spend energy on confrontation that changes nothing and generates resentment.

Before your next frustrating organizational interaction — the meeting that isn't going the way it should, the decision that seems obviously wrong, the behavior that keeps repeating — write down what you think the other person's actual incentives are. Not what their role says. What they're measured on. What they're afraid of. What they'd have to give up to do what you're asking. Now ask: is the behavior still irrational? Usually it isn't.

Start doing this: when you want to change behavior, ask what you'd need to change about the incentive structure rather than what you'd need to change about the person. Sometimes — more often than you might expect — you have leverage over the structure. You can offer credit, remove risk, provide cover, surface the incentive misalignment to someone who can change it. Other times you can't change the structure, but knowing that the behavior is structural tells you something important: the energy you'd spend on confrontation or persuasion is unlikely to produce durable change.

The longer-term shift, if you take this seriously, is that organizational life becomes less frustrating and more legible. Not because organizations get better — many of them don't — but because the behavior stops being random. Every pattern that used to look like politics or stupidity starts to have a structure underneath it. You can see the incentive producing the behavior. That doesn't mean you can always fix it. But it means you stop wasting energy on misattribution, and the energy you do spend is directed at what can actually change.
