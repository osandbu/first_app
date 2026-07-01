# Research Notes: p2_c4 "Metrics Eat Culture"

## Core Thesis / Argument Arc

Metrics are hypotheses about what matters, not facts about what matters. When a metric transitions from measurement tool to target, two things happen simultaneously: people optimize for the metric, and the metric's validity as a proxy degrades. The chapter is not anti-measurement — it's an argument for maintaining the distinction between the map and the territory, and for understanding the organizational dynamics that collapse that distinction.

---

## Historical Parallels

### 1. Goodhart's Law — UK Monetary Policy (1970s)
Charles Goodhart was a Bank of England economist who observed, during the Thatcher-era monetarist experiments, that when the government began targeting specific monetary aggregates (M3, then M1) as policy instruments, those aggregates ceased to reliably predict inflation. Financial institutions changed their behavior specifically in response to being measured — shifting funds between categories, creating instruments that straddled definitions. The original formulation: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." The popular modern restatement — "When a measure becomes a target, it ceases to be a good measure" — is a paraphrase attributed to Marilyn Strathern (1997), not Goodhart himself. The distinction matters: Goodhart was describing a systemic property of complex adaptive systems responding to observation. It's not about bad actors gaming metrics; it's about rational actors responding to incentive structures.

### 2. Soviet Production Quotas
Stalin-era industrial planning provides the clearest large-scale examples of Goodhart's Law in organizational settings. Nail factories given quotas in weight produced a small number of very heavy nails, useless for construction. Quotas shifted to number of nails; factories produced enormous quantities of tiny tacks, equally useless. Glass factories assigned quotas by square area produced dangerously thin panes. By square weight they produced small, thick pieces. Each iteration was "rational" local optimization of the measured variable. The systemic dysfunction was an emergent property of the measurement-target collapse. No individual was acting in bad faith — they were doing exactly what the incentive structure rewarded.

### 3. McNamara's Body Count, Vietnam
Robert McNamara brought operations research and systems analysis from Ford Motor Company to the Pentagon. "Measurement" became doctrine: everything quantified, everything tracked. The primary progress metric became enemy kill count (body count). Downstream effects: soldiers inflated counts (difficult to verify); officers under pressure to show progress pressured subordinates; "kill ratios" became the currency of performance reviews; any adult male in a conflict zone was potentially counted as an enemy combatant. The body count metric was chosen because it was measurable, not because it correlated well with the actual objective (winning the war, securing territory, achieving political outcomes). The metric actively degraded the thing it was meant to measure — progress — by creating incentives that made actual progress harder while the reported metric looked good. McNamara's later admission ("We were wrong, terribly wrong") is often quoted; less quoted is his diagnosis: the problem was not the measurement, it was the substitution of the measure for the goal.

### 4. Cobra Effect (Colonial India)
The British colonial government in Delhi, concerned about the cobra population, offered a bounty for dead cobras. Rational actors began breeding cobras to collect the bounty. When the government discovered this and canceled the bounty, breeders released their now-worthless snakes, increasing the cobra population beyond its original level. The term "cobra effect" now describes any incentive that produces the opposite of the intended outcome. Relevant to engineering: the metric doesn't have to be gamed maliciously. The mere existence of a reward structure redirects effort.

---

## Key Frameworks

### Goodhart's Law
See above. The core mechanism: a proxy metric works because it correlates with an outcome under normal conditions. Once the proxy becomes a target, it decouples from the outcome because agents optimize the proxy directly rather than the underlying behavior that created the correlation.

### Campbell's Law (Donald T. Campbell, 1976)
"The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor." Campbell wrote this about educational testing and social policy, but it maps directly to software engineering metrics. Key addition over Goodhart: Campbell explicitly includes corruption, not just rational optimization. The pressure doesn't just change behavior — it changes what people are willing to do, what they report, and what gets surfaced.

### Proxy Metrics vs. Outcome Metrics
- Outcome metrics measure the thing you actually care about (user retention, system reliability, revenue per customer).
- Proxy metrics measure something correlated with the outcome that is easier to observe or faster to move (code coverage, story points, deployment frequency).
- Proxies are useful tools. The dysfunction begins when proxies are treated as outcomes. A team that improves deployment frequency without improving reliability has moved the proxy without moving the outcome.

### Leading vs. Lagging Indicators
Lagging indicators (defect rate, revenue) measure outcomes but report them after the fact — too slow for operational decisions. Leading indicators (PR cycle time, test coverage trends) predict future outcomes. The danger: the correlation between leading and lagging indicators is probabilistic and context-dependent. It holds until you start managing to it.

### The Balanced Scorecard (Kaplan and Norton, 1992)
An explicit attempt to address single-metric dysfunction by forcing measurement across multiple dimensions (financial, customer, internal processes, learning and growth). The insight: optimizing any one dimension degrades the others; measuring all of them creates visible trade-offs. Critique: in practice, balanced scorecards tend to get reduced back to a single weighted composite score, or the financial dimension dominates. The mechanism of dysfunction reasserts itself at the level of the composite.

---

## Engineering-Specific Scenarios

### 1. Story Point Velocity Inflation
A team reports story point velocity each sprint. Leadership begins treating velocity as a performance indicator. Rational response: point estimates drift upward. Tickets get split into subtasks not for engineering reasons but to make completion counts look good. "Spikes" (open-ended research tasks) disappear because they're hard to point and easy to not count. The velocity number increases. The actual throughput of meaningful work stays flat or declines, because the overhead of ticket management has increased and the planning conversations that used to happen in estimation meetings now don't happen because everyone's focused on keeping the numbers up.

### 2. Code Coverage Theater
A codebase is required to maintain 90% line coverage. Coverage is checked in CI. The natural response: tests are written to cover lines, not behaviors. A function that calculates whether a transaction should be rejected gets tests that call it and verify it returns something — not tests that verify it returns the right thing given boundary conditions. The coverage metric hits 90%. The actual defect rate for the covered code is unchanged because the tests don't catch regressions in logic, only regressions in "the function exists and doesn't throw." The coverage number provides false confidence.

### 3. DORA Metrics as Checkbox
Deployment frequency is a DORA metric correlated with high-performing teams. A team under pressure begins deploying more frequently to improve the metric. They do this by deploying smaller changes, which is good — but they also begin deploying documentation changes, config no-ops, and comment updates as separate deployments. Deployment frequency goes up. Mean time to restore (another DORA metric) is harder to game so it stays flat. The team has improved one metric without improving the system. Worse: because they're now focused on deployment counts, they're less focused on the post-incident reviews that would actually improve MTTR.

### 4. NPS Score Management
Net Promoter Score is a reasonable aggregate proxy for customer satisfaction. When it becomes a target, customer-facing teams learn to time the survey request immediately after a positive interaction, to coach customers on the scoring system ("a 9 or 10 is considered a success"), and to avoid sending surveys to customers who just had a bad experience. The NPS score goes up. The actual customer satisfaction it was meant to measure may be unchanged or declining.

### 5. OKR Key Result Gaming
A product team sets an OKR with a key result of "reduce average page load time to under 2 seconds." The metric is measured by a synthetic test runner against a controlled environment. Teams optimize for the synthetic test: they cache the specific pages the test runner hits, implement resource hints that only fire on the exact URL pattern the runner uses, and reduce image quality on assets the runner doesn't load. The synthetic test hits 1.8 seconds. Real user experience is unchanged. The problem here is partially the proxy (synthetic test vs. real user monitoring) and partially the incentive (the KR is tied to team performance ratings).

### 6. On-Call Alert Volume
A reliability team tracks mean time between alerts as a health metric for the paging system. High alert volume = bad. When this becomes a target, some teams begin raising the threshold for what triggers an alert rather than fixing the underlying issue that generates alerts. Alert volume drops. The underlying degraded behavior — elevated error rates, slow queries, rising latency — is now invisible to the on-call rotation until it escalates to an outage.

---

## Counter-Arguments

### "If you don't measure it, you can't improve it"
This is often attributed to Drucker but appears to be a paraphrase. The underlying claim is correct: without feedback, you can't distinguish improvement from regression. The refutation isn't "don't measure." It's: (1) measure multiple correlated proxies, not one, because it's harder to simultaneously game all of them; (2) hold the proxy loosely — treat it as a signal that merits investigation, not a verdict; (3) rotate metrics periodically to prevent entrenchment; (4) instrument the outcome directly even when it's slow, and check whether your proxy movements are tracking it.

### "Engineering intuition without data is just HiPPO rule"
(HiPPO = Highest Paid Person's Opinion.) Valid. Pure qualitative judgment is vulnerable to bias, politics, and recency effects. The chapter's argument isn't that metrics are bad but that metrics divorced from outcomes are dangerous. The right framing is: use metrics to surface questions, not to answer them. When deployment frequency goes up, ask: did reliability improve? When coverage hits target, ask: are we catching more regressions? The metric opens an inquiry; it doesn't close one.

---

## Data Points and Research

- Donald T. Campbell's 1976 paper "Assessing the Impact of Planned Social Change" is the primary academic source for Campbell's Law.
- Marilyn Strathern's 1997 paper "Improving Ratings: Audit in the British University System" contains the modern Goodhart's Law formulation.
- Research on standardized testing and Campbell's Law is extensive in education literature: schools consistently improve test scores without improving underlying learning outcomes when tests become accountability mechanisms.
- DORA (DevOps Research and Assessment) metrics were developed by the DORA research program (now part of Google Cloud) from large-scale surveys of software delivery performance. The four metrics: deployment frequency, lead time for changes, change failure rate, mean time to restore. Key caveat from DORA's own documentation: these metrics work as a cluster. Optimizing one in isolation without moving the others is a signal of gaming, not improvement. The DORA team themselves have noted that the metrics are most useful as diagnostic signals rather than targets.
- Volkswagen emissions scandal (2015): a canonical real-world example of Goodhart's Law in engineering — the ECU detected test conditions and activated emissions controls only during testing. Omitting company name per guidelines, but the mechanism is worth describing in abstract: a system designed to meet a measurement condition rather than to satisfy the underlying regulatory intent. Worth noting the mechanism is identical to "test only what the CI checks."
- W. Edwards Deming's critique of management by numerical goal (Out of the Crisis, 1982): "Management by use of visible figures only... leaves a company with little room to grow." Deming was arguing against what we'd now call proxy-metric management from a quality systems perspective.

---

## Suggested Chapter Structure

1. **The Correlation Trap** — How metrics are born: someone observes a correlation between a measurable proxy and a valuable outcome. The proxy is a reasonable bet. The trouble begins when the bet becomes a mandate.

2. **When Maps Become Territory** — Goodhart's Law, Campbell's Law, the historical examples. The argument that this is a systemic property, not a behavior problem. It happens to well-intentioned teams with good metrics.

3. **A Tour of the Usual Suspects** — Engineering-specific walk-through: velocity, coverage, DORA, OKRs, NPS. For each: the original insight behind the metric, how it gets co-opted, what the degraded behavior looks like on the ground.

4. **The Anatomy of Metric Capture** — Why it happens mechanically: metrics are visible, outcomes are slow; metrics are legible to management, outcomes require context; metrics get embedded in performance reviews, which means they're now worth gaming. The organizational pathway from "useful signal" to "target."

5. **Measuring Without Capturing** — Practical counter-patterns: outcome laddering (connect every proxy to an outcome explicitly), proxy rotation, dashboards without targets, investigation mode vs. accountability mode, separating diagnostic metrics from performance metrics.

6. **The Meta-Skill: Holding Metrics Loosely** — The disposition that survives the chapter. Not skepticism of measurement but permanent skepticism of any single metric. Ask what behavior the metric is incenting. Ask whether that behavior produces the underlying outcome. Ask what behavior would improve the metric without improving the outcome. If the answer is easy, the metric is probably capturable.
