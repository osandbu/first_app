# Metrics Eat Culture

The sprint review was going well. Velocity was up thirty percent over the previous quarter. The team had closed fifty-two story points in the last sprint — a personal best. The engineering director, who'd been pushing for predictable delivery since the reorg, was visibly pleased.

What the velocity chart didn't show: the team had spent four days that sprint in ticket-splitting workshops. The same work that would have been estimated at eight points was now being tracked as three two-point subtasks and two one-point subtasks. The engineering was identical. The estimates had been inflated to match the team's growing sense of what "looked right." And the spike tickets — the exploratory work where nobody really knew how long something would take — had quietly disappeared from the backlog, not because the exploration wasn't needed, but because spikes were hard to point and didn't land cleanly in the closed column.

Nobody was being dishonest. Everyone was responding rationally to what was being measured.

The velocity chart was accurate. The thing it was supposed to represent had quietly decoupled from the numbers on the screen. The velocity number went up. The useful work didn't. That gap is what this chapter is about.

---

## The Correlation Trap

Metrics don't appear from nowhere. They are born from observation: someone notices that teams with property X tend to produce outcome Y. The observation is real, the correlation is real, and tracking property X is a reasonable bet.

A proxy metric is a hypothesis. It says: "we believe this thing we can measure is meaningfully related to this outcome we care about." That's a useful bet to make, especially when the outcome is slow-moving or hard to observe directly. The outcome — whether users retain, whether systems stay reliable, whether products solve real problems — often takes months to confirm. The proxy is observable today.

The trouble begins when the bet becomes a mandate.

Walk through the sequence once and you'll recognize it everywhere. A proxy correlates with an outcome. The proxy is easy to measure. It gets tracked. The team starts reporting it up. Leadership starts including it in quarterly reviews. It gets tied to performance evaluations. It becomes a goal. And at each step, the incentive to optimize the proxy increases — until the proxy is no longer describing what the team is doing; the team is doing things because of the proxy.

This is not a behavior problem. It does not require bad actors, misaligned managers, or cynical engineers. It is a systemic property of complex adaptive systems responding to observation. When you measure something, you change it. When you reward something, you change it faster. The sequence from "useful signal" to "optimization target" can happen to well-intentioned teams running a thoughtful measurement program. It happens to all of them, eventually, if the metric lives long enough.

---

## When Maps Become Territory

The name most associated with this dynamic is Goodhart's Law. Charles Goodhart was a Bank of England economist who observed, during 1970s monetary policy experiments, that when the government began targeting specific monetary aggregates as policy instruments, those aggregates stopped predicting inflation. Financial institutions changed their behavior specifically in response to being measured: shifting funds between categories, creating instruments that straddled definitions, doing whatever was locally rational given the new target. Goodhart's original observation was technical: "any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." The popular modern restatement — "when a measure becomes a target, it ceases to be a good measure" — is a slightly stronger claim, but the mechanism is the same.

The mechanism matters: a proxy metric works because it correlates with an outcome under normal conditions. Once the proxy becomes a target, it decouples from the outcome. Agents optimize the proxy directly, rather than the underlying behavior that created the correlation. The correlation was never a law; it was an observed relationship under a specific set of conditions. Change the conditions — specifically, add a performance incentive to the proxy — and the relationship changes.

Donald Campbell, writing about social policy in 1976, extended this into a broader principle: "the more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor." Campbell added something important over Goodhart: it's not just rational optimization. It's also what people are willing to report, what gets surfaced to leadership, what gets counted. When a metric matters enough, people don't just game it — they change what information flows up the chain about it.

The Vietnam-era body count is the clearest example. Robert McNamara applied operations research discipline to the war: measure everything, track everything, manage to the numbers. The primary progress metric became enemy kill count, because it was measurable and moveable. The downstream effects followed Campbell's Law almost textbook: kill counts were inflated (difficult to verify independently), officers under pressure to show results pressed subordinates, any adult male in a conflict zone was potentially counted as a combatant. The metric was chosen because it was measurable, not because it reliably predicted the actual goal. McNamara's later diagnosis was precise: "the problem was not the measurement, it was the substitution of the measure for the goal." Soviet nail factories, assigned quotas by weight, produced a small number of very heavy nails useless for construction. Same mechanism, different theater.

Campbell's insight applies directly to software organizations. When deployment frequency is a performance indicator, the version of the story that reaches leadership shows frequency going up. What doesn't surface: that reliability is flat, that the deployments are increasingly no-ops, that engineers have quietly stopped talking about the things the metric doesn't capture. Teams under metric pressure don't just optimize the number — they stop surfacing information that would complicate the story the number tells. That's more damaging than gaming, and it is specific to software organizations: the quarterly engineering review becomes a filtered account of what's happening rather than an accurate one, precisely at the moment leadership needs accurate information most.

The point of these examples is not that your sprint velocity is equivalent to atrocity. The point is that this is a structural pattern, not a local dysfunction. It emerges at scale in monetary policy, industrial planning, military operations, educational testing, and software engineering teams. The mechanism is the same. The conditions that trigger it — measurement, reporting, performance linkage — are present in nearly every engineering organization.

---

## A Tour of the Usual Suspects

Let's be specific. The following are engineering metrics that began as reasonable proxies and are now, in most organizations that use them as targets, primarily measuring their own optimization.

**Story point velocity.** The original insight was sound: teams doing relative estimation learn to size work consistently, and that consistency makes near-term delivery more predictable. Story points were never meant to measure absolute throughput or compare across teams. When velocity becomes a performance indicator — when managers track it, report it up, and use it in evaluations — the behavior shifts in predictable ways. Estimates drift upward. Tickets get split not because the engineering requires it but because smaller closed tickets look better in the chart. Spikes and research work disappear because they're hard to estimate and generate no closed points. Velocity goes up. The actual throughput of meaningful work stays flat or declines, because the overhead of the ticket management theater has increased and the planning conversations that used to happen organically are now replaced by estimation ceremonies focused on hitting the number.

**Code coverage.** The original insight: if you measure what fraction of your codebase is exercised by tests, you can find entirely untested code. That's useful. The degraded behavior when a coverage percentage becomes a hard requirement is now well-documented in any team that has maintained a large test suite: tests are written to cover lines, not behaviors. A function that calculates whether a financial transaction should be rejected gets tests that call it and verify it returns something — not tests that verify it returns the right thing under boundary conditions, after numeric overflow, when the inputs are adversarially constructed. Coverage hits the required percentage. The defect rate for covered code is unchanged, because the tests don't catch logic regressions — they catch only "the function exists and doesn't throw." The coverage number creates false confidence, which is worse than acknowledged uncertainty.

**Deployment frequency.** Research on software delivery performance found that high-performing teams deploy more frequently than low-performing ones. The correlation is real and the research methodology is sound. The degraded behavior when deployment frequency becomes a target: teams begin deploying smaller changes — good — but also deploying documentation updates, config no-ops, and comment-only changes as separate deployments — not good, or at least not the point. Frequency goes up. Mean time to restore, which is harder to game, stays flat. The team has improved one measured number without improving the system. Worse: the focus on deployment counts redirects attention from the post-incident reviews that would actually improve reliability. The other metrics in the cluster, which exist precisely to catch this substitution, get less attention because they don't have a target attached.

**Performance goals with synthetic measurements.** A product team sets a key result: reduce page load time below two seconds, measured by a synthetic test runner. This is not a bad goal. The degraded behavior: teams optimize for the measurement condition rather than the user experience. They cache the specific pages the runner tests. They implement performance hints that only fire on the URL pattern the runner uses. They reduce image quality on assets the runner doesn't load. The synthetic test hits 1.8 seconds. Real user experience is unchanged. The measurement condition was a proxy for user experience, and the team, under performance pressure, optimized the proxy directly. This is Campbell's Law in a single sprint.

**On-call alert volume.** A reliability team tracks mean time between alerts as a health indicator — high alert volume means something is wrong with the system or the alerting hygiene. When reducing alert volume becomes a target, some teams resolve the measurement by raising alert thresholds rather than fixing the underlying issues. Alert volume drops. Elevated error rates, rising latency, and degraded performance — the things that were generating alerts — are now invisible to the on-call rotation. The system is quieter. It is not healthier. The silence is broken only when the accumulated degradation reaches outage scale.

In each case, notice the structure: the metric was a reasonable proxy for something valuable. Someone attached a target to it. Rational actors optimized the target. The proxy decoupled from the outcome. The dashboard looks better. The thing the dashboard was supposed to reflect has not improved.

---

## Why This Keeps Happening

The proxy-to-target pipeline is not an accident or a management failure. It's the output of a set of structural forces that are present in most engineering organizations, and understanding them is the only way to interrupt the pattern.

Metrics are visible; outcomes are slow. A proxy metric moves immediately — you can see velocity change sprint over sprint, coverage percentage on every PR, deployment frequency in a weekly digest. The outcome the proxy is meant to predict may take a full quarter or more to confirm. In a world of quarterly planning and monthly reporting, the feedback loop between proxy and outcome is often too slow to catch the decoupling before the proxy has already become entrenched as a target.

Metrics are legible to management; outcomes require context. Anyone can read a dashboard. Knowing whether the dashboard reflects reality requires understanding that most managers two or three levels up don't have: what's actually in the tickets being closed, whether the test suite is behavioral or structural, whether the deployments are real changes or paperwork. The metric is not just easier to measure — it's easier to communicate up the chain. This is not a flaw in management; it's the nature of information compression across organizational layers. The compression loses the context that would tell you whether the metric is still tracking the outcome.

Metrics get embedded in performance reviews, which means they're now worth gaming. The moment a proxy touches compensation or promotion decisions, every rational actor in the organization optimizes it. This is not cynicism — it's a completely predictable response to an incentive structure. The performance review creates a new optimization target, and that target is the metric, not the outcome the metric was meant to represent.

W. Edwards Deming, who spent decades thinking about quality systems in manufacturing, captured the result precisely: "Management by use of visible figures only... leaves a company with little room to grow." He was not arguing against measurement. He was arguing that the visible figure and the underlying reality are not the same thing, and managing as if they were is a category error.

The organizational result is an intelligence failure that happens at exactly the wrong moment. The organization cares most about its metrics when they're attached to targets. And at that point, the metrics are telling the most optimized story possible — which is the story least correlated with the underlying reality. Leadership is getting the cleanest-looking information at precisely the moment the information is most distorted.

---

## The Case for Measurement

Before going further, this argument needs to address its own skeptics directly, because the wrong takeaway from everything above is that metrics are bad.

The first objection: "if you don't measure it, you can't improve it." The underlying claim is correct. Without feedback, you cannot distinguish improvement from regression. Without some form of measurement, engineering decisions reduce to opinion. And opinion-driven systems get dominated by engineering decisions driven by whoever has the most authority in the room rather than the most relevant data. That's also not a reliable proxy for good judgment.

The refutation of Goodhart's Law is not "stop measuring." The answer is a three-part alternative to attaching a single proxy to a performance target:

1. **Measure multiple correlated proxies rather than one.** It is harder to simultaneously game all of them — if velocity goes up but release quality goes down and customer-reported issues rise, the optimized velocity is visible against a backdrop of other signals.
2. **Hold the proxy loosely, treating it as a signal that merits investigation rather than a verdict that closes inquiry.** A metric moving in the right direction is a question, not an answer.
3. **Track the outcome directly — slowly, imperfectly — and check whether proxy movements are actually predicting it.** This is the step almost no team does. The outcome data may take weeks to arrive. That delay is not a reason to ignore it; it's exactly why you need to instrument it deliberately.

Pure qualitative assessments are vulnerable to recency bias, availability bias, and the natural human tendency to remember evidence that confirms existing beliefs. The answer to Goodhart's Law is not to stop measuring — it's to measure in ways that resist capture.

The right framing is this: use metrics to surface questions, not to answer them. When deployment frequency goes up, ask: did reliability improve? When coverage hits the required percentage, ask: are we catching more regressions? When velocity increases, ask: did we ship more meaningful work, or did our estimates get looser? The metric opens an inquiry. It does not close one. The moment a metric is allowed to close an inquiry — to substitute for investigation rather than trigger it — the map has replaced the territory.

This is a real distinction in practice, and it requires discipline to maintain. The pressure to let metrics close inquiries is high: the quarterly review is in three days, the metric is good, the discussion about whether the metric reflects reality is uncomfortable and takes time. But the organization that consistently treats metric improvement as a question rather than an answer has a structural advantage: it catches decoupling before it becomes entrenched.

---

## Practical Counter-Patterns

If the answer isn't "stop measuring," what is it? There are specific practices that maintain the distinction between the map and the territory, and they are each directly in tension with the organizational forces that collapse that distinction.

**Outcome laddering.** For every proxy metric you track, write down explicitly what outcome you believe it predicts, and describe how you would know if that belief is wrong. "We track deployment frequency because we believe it correlates with system reliability. We verify this by also tracking mean time to restore and change failure rate. If frequency goes up but reliability doesn't move, the proxy has decoupled and we treat that as a signal, not a success." This sounds obvious. Almost no team does it. Writing it down forces the question of whether the proxy-to-outcome link is actually being observed, or just assumed.

When you find the decoupling, the right response in a review isn't "the metric is wrong" — it's "velocity went up, here's the outcome data that should be moving with it, and here's why it isn't yet." That framing keeps the conversation investigative rather than defensive. In a review, frame it as: "This number moved — before we call it success or failure, can we spend five minutes on what behavior produced the movement?"

**Proxy rotation.** Any proxy that has been in use for a year has been gamed for a year. The gaming may be subtle — slightly inflated estimates, slightly lower-risk deployments, slightly easier-to-reach tests — but it's happening. Periodically rotating which proxy you track resets the optimization target before it becomes entrenched. Treat any single metric with a time horizon: "We will use this proxy for two quarters, then reassess whether it's still tracking the outcome, and consider rotating to a different proxy that captures a different facet of the same outcome."

**Dashboards without targets.** You can observe a metric without making it a target. The moment you attach a threshold — "deployment frequency must exceed X," "coverage must stay above Y" — you have changed the incentive structure. The metric is no longer a signal; it's a pass/fail criterion. For metrics that you want to use as operational signals — "is this trend concerning or not?" — consider removing the hard threshold and replacing it with a directional trend and a range. Targets convert observations into games. Not everything you want to observe needs to be gamed.

If the target was set before you arrived and you're not in a position to remove it, the next best move is to add a countervailing signal: one that would move in the wrong direction if someone is optimizing the primary metric rather than the underlying outcome. "Can we also track X?" is a much easier conversation than "we should stop tracking Y." You can propose the second metric without proposing to remove the first.

**Investigation mode versus accountability mode.** These are two different things, and the confusion between them is a large fraction of the Goodhart problem. When a metric moves, the first question should be investigative: what explains this movement? Velocity went up — is that real throughput, estimate drift, ticket-splitting, or scope reduction? Coverage increased — did we add behavioral tests, or did we add structural tests against already-covered paths? Deployment frequency rose — are we shipping more real changes, or are we deploying more no-ops? The investigation may conclude that the metric movement is real and good. It may also reveal the decoupling. If you skip the investigation and go straight to accountability — "velocity is up, the team is performing" — you've turned a signal into a verdict.

In a review setting, hold investigation mode by framing it explicitly: "The metric is moving in the right direction — before we call this a success, let me share what I'd want to see over the next two weeks to know whether this is real throughput or proxy optimization." That framing acknowledges the good-looking metric, signals the right disposition, and creates a short, bounded window for investigation rather than demanding the review stay open indefinitely.

**The capturability test.** Once you understand why proxy capture is structural — metrics are visible, performance-attached, and faster than outcomes — the diagnostic becomes: is this metric capturable without moving the underlying outcome?

For any metric you are currently using as a target, ask: what behavior would improve this metric without improving the underlying outcome? If the answer comes easily — if you can describe in ten seconds how someone would game the metric — then the metric is capturable, and it will be captured. Either don't use it as a target, add a countervailing metric that catches the gaming, or accept that you're measuring the metric's optimization, not the underlying outcome. The capturability test doesn't change the structural forces that will convert your proxies to targets — the quarterly review pressure, the legibility requirement for leadership, the performance linkage. What it does is help you know in advance which metrics will degrade fastest, so you can either add countervailing measures or decide not to attach targets to them at all.

The capturability test is uncomfortable because it often reveals that your most-used metrics have easy answers. That discomfort is information.

The meta-competency underneath all of these practices is the same: permanent, structured skepticism about any metric's relationship to the thing you actually care about. Not cynicism — cynicism produces paralysis, and "therefore nothing matters" is a failure mode just as surely as "the dashboard is good therefore things are good." Structured skepticism means building the question "is this proxy still tracking the outcome?" into your operating rhythm, rather than assuming the relationship holds indefinitely.

---

## What Changes Monday

For each metric currently in your team's performance goals, do one thing before this week's planning meeting: write down in one sentence what behavior would improve it without improving the underlying outcome. If the answer comes easily — if the gaming strategy is obvious — treat the metric as already gamed. It may not be gamed yet, but it will be, probably faster than you expect. For each metric where the gaming strategy is not obvious, you have a stronger proxy; hold it loosely anyway, because the difficulty of gaming now doesn't mean it stays difficult as people orient to it. Add a countervailing measure for any metric where you can easily describe the gaming strategy: something that would move in the wrong direction if someone is optimizing the proxy rather than the outcome.

The longer-term shift is to build measurement systems that surface questions rather than produce verdicts. This means instrumenting the outcome directly — slowly, imperfectly, even if the data takes weeks to arrive — and making the relationship between proxy and outcome visible over time. It means running investigation mode consistently when metrics move, rather than defaulting to the accountability interpretation. And it means being willing to say, in a quarterly review, "this metric went up, but we don't yet know whether it's tracking real improvement — here is what we would need to see to be confident." That's more honest than the alternative, and it keeps the map from replacing the territory.
