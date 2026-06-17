# Measuring AI Adoption

## The Solow Problem, Revisited

In 1987, the economist Robert Solow made a remark that became one of the most quoted lines in the history of economic commentary: "You can see the computer age everywhere except in the productivity statistics." American businesses had been investing in computing infrastructure for more than a decade. Output per worker wasn't moving.

The answer, when it came, was instructive. Productivity gains from computing did arrive — but roughly a decade after the investments, and only after organizations had restructured their workflows, retrained their workers, and redesigned their processes around the technology. The computers themselves were never the unit of measurement that mattered. What mattered was whether the people and processes around them had changed.

The parallel to AI adoption is exact. Count the AI tools your organization has deployed. Count the employees who have completed AI training. Count the processes that have been augmented or automated. Now ask: are these the right things to count? Are they telling you whether AI is actually improving the decisions that drive your organization's performance? Or are they telling you, with satisfying specificity, that AI is present — while the question of whether it is useful remains unanswered?

Most organizations are counting the wrong things. Not accidentally — the wrong metrics are easier to collect, easier to report upward, and easier to celebrate. They produce numbers that rise predictably over time. They are also systematically misleading. An organization can score perfectly on every common AI adoption metric while remaining fundamentally unreconstructed in how it prioritizes, allocates, and acts on information.

Solow's productivity paradox will repeat for AI, for exactly the same reason: organizations are measuring inputs rather than outputs, presence rather than integration, activity rather than capability.

---

## Goodhart's Trap

Before introducing better metrics, it is necessary to understand why better metrics are harder to maintain than they are to identify.

Charles Goodhart, a British economist, formulated a principle that has proven more durable than most of his academic work: any measure used as a control target will lose its value as a measure. When a metric becomes the official target of performance management, people will optimize for the metric rather than for the underlying outcome it was supposed to proxy. This is not about bad intent. It is about rational behavior in systems where incentives are tied to numbers.

The trap is precisely the danger with AI adoption metrics. Consider what happens when utilization rate — the percentage of employees using AI systems in a given week — becomes a performance target. Teams quickly learn to open the AI interface regularly, to route some portion of their work through it, and to document that use for reporting purposes. Utilization rises. The underlying question — whether the organization is making better decisions — remains unanswered.

A global financial services firm that introduced AI systems across its risk management function measured adoption through utilization rates. Utilization was high within months. A subsequent review found that most analysts were using the tools to produce more reports faster, not to ask different questions. The risk committee was receiving three times as much analytical output and making decisions no faster and no differently. The firm had optimized for throughput without defining what throughput was for.

Training completion rates face the same dynamic. A professional services firm retrained its workforce on AI tools and tracked training completion as its primary adoption metric. Completion hit 94% within the target window. When practitioners were surveyed six months after training, fewer than a third reported changing how they actually worked. Training completion measured exposure to a tool, not adoption of a new working method.

Goodhart's Law suggests that any AI adoption metric that becomes a performance management target will be gamed — typically within two or three years of becoming official. The measurement framework must be designed to resist this by focusing on outcomes rather than inputs, and by regularly reassessing whether the specific metrics in use are still measuring the underlying capability or have become targets divorced from it.

---

## What Actually Matters: A Framework for AI Capability Measurement

The alternative to measuring inputs is measuring capability — the organizational capacity to make better decisions, faster, using AI. This requires three dimensions.

**Decision quality** is the primary dimension. It is also the hardest to measure, and that difficulty deserves honest acknowledgment. Decisions are hard to evaluate because outcomes are noisy: good decisions sometimes produce bad outcomes through bad luck, and poor decisions sometimes produce good outcomes through good fortune.

But decision quality is considerably more measurable than it appears when you focus on process rather than outcome. Process quality metrics — the number of alternatives considered before committing, the degree to which assumptions were made explicit and documented, the quality of dissent recorded, the discipline of post-decision review — are meaningful proxies for outcome quality, and they are measurable without waiting for long-term outcomes. Portfolio measurement provides a practical path: track some short-cycle outcome measures (approval accuracy, forecast error), alongside process measures (alternatives documented per major decision, override rates for AI-generated recommendations), and some lagging annual measures (decision reversal rates). Together, they triangulate around decision quality without requiring perfect measurement of any single dimension.

A regional bank that defined its primary AI measurement target as "decision quality in credit" — specified as predictive accuracy at twelve months, consistency across similar risk profiles, and speed from application to approval — found that AI adoption measured against these anchors became clear: within two years, all three metrics improved measurably. The bank's AI program was considered successful not because its adoption metrics were high, but because its credit outcomes improved in ways directly attributable to changed decision processes.

**Decision velocity** is the second dimension: the elapsed time between when relevant information becomes available and when a decision is made and acted upon. A consumer goods conglomerate deployed AI systems across its brand portfolio to accelerate market sensing, and measured adoption by tracking "insights generated per quarter." The number rose steadily. But the metric concealed a critical problem: the firm was generating far more insights than it could act on. Resource allocation decisions were still made annually, in a planning cycle unchanged since the 1990s. The AI was producing real-time intelligence for a batch-processing organization. When the company redesigned its measurement around "insights acted upon within ninety days," the number was sobering — and clarifying. The real constraint was decision velocity, not analytical capacity.

Decision velocity measurement is practical: for the categories of decisions most affected by AI adoption, track the elapsed time from when relevant information became available to when a decision was made and implemented. Persistent long lags are diagnostic of organizational structures, approval processes, or planning rhythms that are incompatible with AI's capabilities. Shortening those lags is a structural challenge, not a technical one, and measurement makes it visible.

**The judgment ratio** is the third and most revealing dimension: what proportion of human time is spent on work that requires irreducibly human judgment, versus execution work that AI could handle? If senior professionals are spending most of their time on work AI could do as well or better, the organization is not capturing AI's value — it is using AI to produce more of the output that already occupied too much expert time.

This ratio is more tractable to measure than it appears. A practical approach, used by several organizations to establish a baseline: ask managers across functions to estimate — over a representative two-week period — what fraction of their direct reports' time is spent on work where human judgment is genuinely essential versus work that is principally execution, synthesis, or routine analysis. The estimates will be imprecise. They will also be directionally consistent, and the direction is diagnostic. One professional services firm that ran this exercise found that senior consultants estimated only about 35% of their time was spent on work where their judgment, versus their labor, was what clients were actually paying for. That number became the benchmark against which subsequent AI adoption was measured. Within eighteen months, the firm's self-assessment had moved the estimate to approximately 55% — a meaningful shift attributed directly to AI-assisted research and drafting that freed consultant attention for the genuinely judgment-intensive client interaction.

---

## Leading Indicators: Measuring Capability Before It Shows Up in Results

Outcome metrics are lagging. By the time poor AI adoption shows up in business performance, the window for cost-effective course correction may be narrow. Four leading indicators provide the early warning system that outcome metrics cannot.

**The quality of questions posed to AI systems.** There is a measurable difference between an organization using AI to answer questions it had already formed and one using AI to identify questions it hadn't thought to ask. Periodically reviewing what AI systems are actually being asked — not the outputs but the queries — tells you whether AI is expanding the organization's analytical imagination or merely accelerating its existing one.

**The discipline of post-decision review.** Research from decision science shows that organizations with structured post-decision review practices make measurably better decisions over time, independent of the quality of the initial decision. For AI-augmented decisions, the review has an additional dimension: did the AI input improve the decision, degrade it, or neither? Tracking this — even informally — builds organizational intelligence about where AI judgment is reliable and where it is not.

**The rate at which AI-generated insights are translated into action.** A large hospital network that measured the proportion of clinical decisions supported by AI-generated summaries found that adoption rates looked excellent — but a later audit showed that a significant proportion of AI recommendations were being ignored without documentation. The override-documentation-rate, once tracked, revealed that the system was creating the appearance of AI-augmented care without the substance. The metric: not insights generated, but the fraction of AI-surfaced insights that result in documented organizational action within a relevant time window.

**Learning velocity.** When one team discovers an effective AI application, how long before comparable teams are using it? Rapid diffusion indicates a healthy learning culture with functioning knowledge-sharing infrastructure. Slow diffusion indicates organizational silos that prevent learning from traveling. Tracking this over time tells you whether the organizational learning infrastructure is working — and whether it is improving.

---

## The Executive AI Audit

The hardest half of the measurement challenge is not identifying the right metrics. It is building the discipline to track them honestly over time, and maintaining the organizational willingness to ask whether the metrics themselves are still pointing at the right thing.

A practical discipline for converting measurement into action: the executive AI audit, conducted regularly — quarterly or semi-annually — against four diagnostic questions.

**Is the time my organization spends on high-judgment work growing or shrinking, and do I have evidence?** The judgment ratio should be moving in one direction over time if AI adoption is working. If you cannot answer this question with any data, you are not measuring what matters most.

**Can I name a decision we made differently — better — because of AI, with a specific example?** The inability to name one is diagnostic. It does not necessarily mean AI isn't working; it may mean the organization is not developing the practice of attributing decision quality to process inputs, including AI. That attribution practice is itself a cultural signal.

**What is the elapsed time between when AI surfaces an insight and when we act on it, in the decisions that matter most?** If you don't know this number, you are not measuring decision velocity. If the number is weeks or months, the constraint is organizational, not analytical.

**Where are our AI systems making us faster at the wrong things?** This is the most important question and the least often asked. Speed at the wrong things is a compounding disadvantage: it directs organizational attention, accumulates investment, and makes restructuring progressively harder. The AI deployment that produces more reports no one acts on, more insights that never reach decision processes, more trained employees who don't change how they work — that deployment is paying the full cost of adoption while capturing little of its value.

The organizations that will win the AI era are those that figure out, before their competitors, what they are actually trying to measure. Not the presence of AI. Not the activity it generates. The quality, speed, and distribution of the judgment it enables.

Solow's paradox didn't resolve itself. It resolved when organizations stopped counting computers and started redesigning around what computers made possible. The measurement framework is the instrument that tells you whether that redesign is actually happening — or whether the organization is simply acquiring a more expensive version of the technology it already had, counting the new tools where it once counted servers, and waiting, as a generation of managers waited before it, for the productivity statistics to move.
