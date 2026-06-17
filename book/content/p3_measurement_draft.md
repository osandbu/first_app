# Measuring AI Adoption

## The Solow Problem, Revisited

In 1987, the economist Robert Solow made a remark that became one of the most quoted lines in the history of economic commentary: "You can see the computer age everywhere except in the productivity statistics." American businesses had been investing in computing infrastructure for more than a decade, at costs that represented a significant share of capital expenditure. Output per worker wasn't moving.

The quip captured a genuine puzzle. The answer, when it came, was instructive. Productivity gains from computing did arrive — but roughly a decade after the investments, and only after organizations had restructured their workflows, retrained their workers, and redesigned their processes around the technology. The computers themselves were never the unit of measurement that mattered. What mattered was whether the people and processes around them had changed.

The parallel to AI adoption is exact, and the implications are uncomfortable for most organizations currently tracking their AI progress.

Count the AI tools your organization has deployed. Count the employees who have completed AI training. Count the processes that have been augmented or automated. Now ask: are these the right things to count? Are they telling you whether AI is actually improving the decisions that drive your organization's performance? Or are they telling you, with satisfying specificity, that AI is present — while the question of whether it is useful remains unanswered?

Most organizations are counting the wrong things. Not accidentally — the wrong metrics are easier to collect, easier to report upward, and easier to celebrate. They produce numbers that rise predictably over time, that respond to management attention, and that can be reported in board presentations with confidence. They are also systematically misleading. An organization can score perfectly on every common AI adoption metric while remaining fundamentally unreconstructed in how it prioritizes, allocates, and acts on information.

Solow's productivity paradox will repeat for AI, and for exactly the same reason: organizations are measuring inputs rather than outputs, presence rather than integration, activity rather than capability.

---

## Goodhart's Trap

Before introducing better metrics, it is necessary to understand why better metrics are harder to maintain than they are to identify.

Charles Goodhart, a British economist, formulated a principle that has proven more durable than most of his academic work: any measure used as a control target will lose its value as a measure. When a metric becomes the official target of performance management, the people being managed against it will optimize for the metric rather than for the underlying outcome the metric was supposed to proxy.

The principle is not about bad intent. It is about rational behavior in systems where incentives are tied to numbers. The call center manager who knows that customer satisfaction scores determine her team's bonuses will, reasonably, instruct agents to ask for high scores before the call ends. The scores rise; the underlying experience may or may not improve. Net Promoter Score, introduced in the early 2000s as a elegant proxy for customer loyalty, became so thoroughly gameable within a decade that its value as an indicator of actual loyalty eroded substantially in many organizations.

The Goodhart trap is precisely the danger with AI adoption metrics. Consider what happens when utilization rate — the percentage of employees using AI systems in a given week — becomes a performance target. Teams quickly learn to open the AI interface regularly, to route some portion of their work through it, and to document that use for reporting purposes. Utilization rises. The underlying question — whether the organization is making better decisions — remains unanswered.

A global financial services firm that introduced AI systems across its risk management function measured adoption through utilization rates. Utilization was high within months. A subsequent review found that most analysts were using the tools to produce more reports faster, not to ask different questions. The risk committee was receiving three times as much analytical output and making decisions no faster and no differently. The firm had optimized for throughput without defining what throughput was for.

Training completion rates face the same Goodhart dynamic. A professional services firm retrained its workforce on AI tools and tracked training completion as its primary adoption metric. Completion hit 94% within the target window. But when practitioners were surveyed six months after training, fewer than a third reported changing how they actually worked. Training completion measured exposure to a tool, not adoption of a new working method.

The Goodhart lesson for AI adoption measurement: any metric that becomes a target for performance management will be gamed, typically within eighteen to thirty-six months of becoming official. The measurement framework must be designed to resist this — which means focusing on outcomes rather than inputs, and regularly rotating the specific metrics used so that the underlying question (is AI improving our decisions?) remains the target rather than any particular number used to proxy it.

---

## What Actually Matters: A Framework for AI Capability Measurement

The alternative to measuring inputs is measuring capability — the organizational capacity to make better decisions, faster, using AI. This requires three dimensions.

**Decision quality** is the primary dimension. It is also the hardest to measure, and that difficulty deserves honest acknowledgment rather than workaround. Decisions are hard to evaluate because outcomes are noisy: good decisions sometimes produce bad outcomes through bad luck, and poor decisions sometimes produce good outcomes through good fortune. Context changes. The standards for "quality" in judgment calls are contested.

But decision quality is considerably more measurable than it appears when you focus on process rather than outcome. Process quality metrics — the number of alternatives considered before committing, the degree to which assumptions were made explicit and documented, the quality of dissent recorded in the decision process, the discipline of post-decision review — are not perfect proxies for outcome quality, but they are better proxies than inputs, and they are measurable without waiting for long-term outcomes. A regional bank that defined its primary AI measurement target as "decision quality in credit" — specified as predictive accuracy at twelve months, consistency of decisions across similar risk profiles, and speed from application to approval — found that AI adoption, measured against these anchors, became much clearer: within two years, all three metrics improved measurably. The bank's AI program was considered successful not because its adoption metrics were high, but because its credit outcomes improved in ways directly attributable to changed decision processes.

Portfolio measurement provides a practical path through the measurement difficulty. Track some metrics that are short-cycle outcome measures — approval accuracy, forecast error — alongside process measures (alternatives documented per major decision, override rates for AI-generated recommendations) and some lagging annual measures (decision reversal rates, decision regret rates). Together, they triangulate around decision quality without requiring perfect measurement of any single dimension.

**Decision velocity** is the second dimension. One of the clearest organizational symptoms that AI is not genuinely integrated into decision-making is the persistence of old planning rhythms. A consumer goods conglomerate deployed AI systems across its brand portfolio to accelerate market sensing, and measured adoption by tracking "insights generated per quarter." The number rose steadily. The business case appeared validated. But the metric concealed a critical problem: the firm was generating far more insights than it could act on. Resource allocation decisions were still made annually, in a planning cycle unchanged since the 1990s. The AI was producing real-time intelligence for a batch-processing organization.

When the company redesigned its measurement around "insights acted upon within ninety days," the number was sobering — and clarifying. The real constraint was decision velocity, not analytical capacity. The AI adoption problem was not in the tools or their outputs; it was in the organizational processes that determined what happened to those outputs.

Decision velocity measurement is straightforward in principle: for the categories of decisions most affected by AI adoption, measure the elapsed time from when relevant information became available to when a decision was made and implemented. Persistent long lags are diagnostic of organizational structures, approval processes, or planning rhythms that are incompatible with AI's actual capabilities. Shortening those lags — redesigning the organizational structures to match the speed at which AI can provide information — is a structural challenge, not a technical one.

**The judgment ratio** is the third and most revealing dimension: what proportion of human time is spent on work that requires irreducibly human judgment, versus execution work that AI could handle? This ratio is not about eliminating execution work — some execution will always require humans. It is about tracking whether the shift is happening. An organization where senior professionals spend most of their time on work AI could do as well or better is not capturing the value of AI; it is using AI to produce more of the output that already occupied too much expert time.

The Harvard Business School research finding that senior executives spend less than 30% of their time on decisions that require their unique judgment is simultaneously a diagnosis and a benchmark. AI adoption, if it is working, should shift this ratio over time. Tracking it — even imprecisely, through time studies or manager self-assessment — gives a directional signal about whether AI is genuinely changing how the organization uses its most expensive resource.

---

## Leading Indicators: Measuring Capability Before It Shows Up in Results

Outcome metrics are lagging. By the time poor AI adoption shows up in business performance, the window for cost-effective course correction may be narrow. A set of leading indicators can provide the early warning system that outcome metrics cannot.

**The quality of questions being posed to AI systems.** There is a measurable difference between an organization using AI to answer questions it had already formed and one using AI to identify questions it hadn't thought to ask. The former produces faster versions of existing analysis; the latter produces genuinely new insight. Periodically reviewing what AI systems are actually being asked — not the outputs but the queries — tells you whether the organization's use of AI is expanding its analytical imagination or merely accelerating its existing one.

**The discipline of post-decision review.** Research from decision science consistently shows that organizations with structured post-decision review practices make measurably better decisions over time, independent of the quality of the initial decision. The review creates the feedback loop that converts experience into learning. For AI-augmented organizations, post-decision review has an additional dimension: did the AI input improve the decision, degrade it, or neither? Tracking this — even informally — builds organizational intelligence about where AI judgment is reliable and where it is not.

**The rate at which AI-generated insights are translated into acted-upon decisions.** Not insights generated (a Goodhart-vulnerable input metric) but insights-to-action conversion: what fraction of AI-surfaced insights result in organizational action within a relevant time window? Low conversion is diagnostic of an insight production process disconnected from the decision-making processes that could use it. A large hospital network that measured the proportion of clinical decisions supported by AI-generated data summaries found that adoption rates looked excellent — but a later audit showed that a significant proportion of AI recommendations were being ignored without documentation. The override-documentation-rate, once tracked, revealed that the system was creating the appearance of AI-augmented care without the substance.

**Learning velocity.** When one team discovers an effective AI application, how long does it take before comparable teams are using it? Rapid diffusion indicates a healthy learning culture. Slow diffusion indicates organizational silos that prevent knowledge from traveling. In organizations that track learning velocity over time, the trend line tells you whether the organizational learning infrastructure — communities of practice, knowledge-sharing processes, cross-team experimentation — is working.

---

## Building the Measurement System

Identifying the right metrics is the easier half of the measurement challenge. The harder half is building the organizational discipline to track them honestly, and the governance to ensure the measurement framework itself evolves as AI capabilities change.

**Ownership and independence.** AI adoption measurement should not sit entirely inside the AI function, where incentives favor self-report and positive framing. The function that owns AI deployment has an incentive to demonstrate progress; the function that measures AI adoption effectiveness should have an incentive to identify gaps. In practice, this suggests that measurement should involve both the AI function and a more independent organizational capability: a strategy function, an internal audit group, or an operations team. The Balanced Scorecard approach, adapted for AI, recommends a measurement portfolio rather than a single metric owner: financial outcomes tracked by finance, decision process quality tracked by operations, learning velocity tracked by a strategy or transformation function.

**Evolution.** Measurement frameworks that were right in year one will be wrong in year three as AI capabilities change, as organizations develop more sophisticated use, and as the initial round of Goodhart gaming renders early metrics unreliable. The discipline of regularly asking "are we measuring the right things?" — not just "are our numbers improving?" — is itself an organizational capability. Organizations that have developed this discipline are rare and valuable. They are also the ones most likely to maintain measurement integrity as competitive pressures mount to report progress rather than diagnose reality.

**The executive AI audit.** A practical discipline for converting measurement into action: the executive conducts a regular audit of the organization's relationship with AI through four diagnostic questions. Is the time my organization spends on high-judgment work growing or shrinking, and do I have evidence? Can I name a decision we made differently — better — because of AI, with a specific example? What is the elapsed time between when AI surfaces an insight and when we act on it, in the decisions that matter most? And: where are our AI systems making us faster at the wrong things?

The last question is the most important and the least often asked. Speed at the wrong things is not a neutral outcome; it is a compounding disadvantage. An organization that uses AI to produce more reports that no one acts on, to generate more insights that never reach decision processes, to train more employees who don't change how they work — such an organization is paying the full cost of AI adoption and capturing little of its value, while becoming progressively harder to restructure as the investments accumulate.

The organizations that will win the AI era are those that figure out, before their competitors, what they are actually trying to measure. Not the presence of AI. Not the activity it generates. The quality, speed, and distribution of the judgment it enables.

That clarity is not automatic. It is a choice — a leadership decision about what questions the organization is trying to answer and what it is willing to hear when the honest answer is that the AI adoption is proceeding but the organizational capability is not. The Solow problem did not resolve itself. It resolved when organizations redesigned themselves around what computing made possible, rather than counting the computers they had acquired. The measurement framework is not a reporting exercise. It is the instrument that tells you whether the redesign is working.
