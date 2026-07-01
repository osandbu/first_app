# Research Notes: p1_c3 — Your Mental Model of a Company Is Wrong

## Core Argument

Engineers are trained on systems that behave predictably: given the same inputs, a function returns the same output. Companies do not work this way. They are not machines — they are organisms shaped by incentives, politics, accumulated history, and the identities of the people in them. A company that appears to be making obviously wrong decisions is almost always making decisions that are locally rational for the people making them. Until an engineer internalizes this distinction, organizational behavior will seem not just frustrating but inexplicable. This chapter is the conceptual foundation for Part II.

---

## 1. Historical Parallels

### 1a. From Mechanism to Organism: Morgan's *Images of Organization* (1986)
Gareth Morgan's central contribution was cataloging the metaphors through which people understand organizations — and showing that the metaphor you're using determines what you can see and what you're blind to. The machine metaphor (companies as mechanisms to be optimized) dominated industrial management: Frederick Taylor's scientific management, Henry Ford's assembly lines, the entire tradition of operations research. The machine metaphor is productive when tasks are routine, environments are stable, and people can in fact be treated as interchangeable parts. It becomes actively harmful when the environment is dynamic, when work requires judgment, and when people have identities and interests of their own.

Morgan's organism metaphor treats organizations as living systems that must adapt to their environment to survive. This opens up different questions: what is the organization's environment, what survival pressures is it under, how does it maintain homeostasis? Systems thinking (Beer's Viable System Model, Forrester's system dynamics work at MIT) extended this into the cybernetics tradition — understanding organizations in terms of feedback loops, not flowcharts.

The engineering audience likely encountered systems thinking through its influence on software architecture. The irony: engineers who understand feedback loops in distributed systems often don't apply the same thinking to the organizations they work inside.

### 1b. March and Simon: *Organizations* (1958) and the Limits of Rationality
Herbert Simon's concept of bounded rationality is one of the most important and underused frameworks for understanding organizational behavior. Simon argued (contra classical economics) that decision-makers do not optimize — they satisfice. They do not gather all available information and compute the best answer; they gather enough information to identify an option that clears an acceptable threshold, and then they stop.

This was heretical in 1958. It is now well-established: the cognitive and computational costs of full rationality are prohibitive. People operate under time pressure, with incomplete information, under cognitive load, with competing objectives. The organization as a whole does not make rational decisions — it makes decisions that are rational given the information available to the particular person or coalition making them.

James March extended this into the "garbage can model" of organizational decision-making: problems, solutions, participants, and choice opportunities float around organizations somewhat independently and collide semi-randomly. The solution that gets attached to the problem is often not the best solution — it's the solution that was available when the decision opportunity arose. This feels deeply uncomfortable to engineers trained on optimization. It is also, empirically, how most organizational decisions work.

### 1c. Frederick Winslow Taylor and the Ghost in the Engineering Machine
The machine metaphor of organizations didn't emerge from nowhere: it was explicitly constructed by engineers. Taylor's scientific management (early 1900s) applied industrial engineering principles to human labor — time-motion studies, standardization, the separation of planning (management) from execution (workers). The entire edifice of management science was built by engineers convinced that organizations could be optimized the way manufacturing lines could be optimized.

This legacy lives in how engineers today think about organizations. When an engineer says "we should optimize the process," "we need to fix the system," "the bottleneck is at X" — these are Taylorist metaphors. They are useful in narrow cases and severely misleading in others. The history is worth surfacing because it shows that the machine metaphor wasn't imposed on engineers from outside: engineers built it.

---

## 2. Key Frameworks

### 2a. Morgan's Three Metaphors (Machine / Organism / Political System)
These three are most useful for the chapter's argument:

**Machine**: Organization as a set of processes and roles that produce outputs. Everything should be designed, measurable, controllable. Dysfunction is a malfunction to be repaired. Most engineers' default mental model.

**Organism**: Organization as a living system adapting to its environment. Focus shifts to survival pressures, homeostasis, adaptation. Dysfunction is a response to environmental stress. Explains why "obviously wrong" decisions often make sense when you understand what the organization is responding to.

**Political system**: Organization as a coalition of groups with different interests, competing for resources, status, and survival. Decisions are negotiated outcomes. "Rational" from whose perspective? The winning coalition's. Explains why technically superior proposals lose to politically viable ones.

Most organizational behavior requires all three lenses simultaneously. The machine metaphor tells you how work is supposed to flow; the organism metaphor tells you what external pressures are shaping behavior; the political metaphor tells you whose interests are being served by any given decision.

### 2b. Bounded Rationality (Simon)
Every decision-maker in an organization is working with:
- Incomplete information (they don't know what you know; they don't know what they don't know)
- Limited cognitive capacity (attention is finite, complexity is real)
- Time pressure (most decisions are made under deadline)
- Multiple competing objectives (career, team, project, company — these often point in different directions)
- Path dependence (prior commitments, sunk costs, relationships)

The observable output: "satisficing" rather than optimizing. Decisions that are good enough given local constraints. An engineer with full context looking at someone else's decision with the benefit of hindsight will usually be able to identify a better option. That's not evidence of irrationality — it's evidence of information asymmetry.

### 2c. Local Rationality (distinct from bounded rationality)
Local rationality is the concept that behavior is rational given the local incentive structure, even when it produces globally suboptimal outcomes. This is distinct from bounded rationality (which is about cognitive limits) — a person can have full information and still make locally rational choices that hurt the organization.

Classic game-theoretic setup: a manager evaluated on team headcount will hire more people than the work requires. A team evaluated on feature velocity will defer maintenance. A VP evaluated on quarterly metrics will trade long-term reliability for short-term throughput. Each individual is behaving rationally. The aggregate outcome is dysfunctional. The problem is not the people — it's the incentive design. This is the key bridge to Part II.

### 2d. Sensemaking (Weick)
Karl Weick's contribution: organizations don't just process information, they actively construct meaning. "Sensemaking" is the ongoing process by which people explain their situation to themselves and to others. This matters for the chapter because it explains why organizations are resistant to information that doesn't fit their current narrative.

Weick's "enactment" concept: people don't just respond to their environment, they partly create it through the interpretations they project onto it. A team that believes it's shipping a successful product will interpret every ambiguous signal through that lens. A manager who believes they have a strong team will interpret performance problems as external factors. This is not stupidity — it's how cognition works under uncertainty.

Weick's study of the Tenerife airport disaster and the Mann Gulch fire collapse are particularly relevant: in both cases, people died not because they lacked information, but because they couldn't update their mental model fast enough under pressure. The organizational equivalent is slower and less lethal, but structurally similar.

### 2e. Complex Adaptive Systems (Holland, Stacey)
Organizations are not complicated (many parts, but in principle analyzable) — they are complex (emergent behavior that cannot be predicted from the parts). Complex adaptive systems produce behavior that isn't designed by anyone, isn't intended by any individual actor, and can't be controlled by changing any single variable.

This explains why organizational interventions often produce unintended consequences. A reorg intended to improve cross-team collaboration may instead disrupt information flows that were working. A new performance framework intended to align incentives may instead produce gaming behavior nobody anticipated. You're not fixing a machine — you're intervening in an ecology.

The key implication for engineers: your mental model of "find the root cause and fix it" is appropriate for software systems. It is often deeply misleading for human organizations. Organizations don't have root causes the way software does.

---

## 3. Concrete Scenarios

### Scenario A: The Team That Keeps Shipping Features Nobody Uses
A product team ships feature after feature. Adoption is low. From the outside, the obvious question: why don't they talk to users? From the inside: the team is measured on velocity. Their quarterly goals are defined in terms of features shipped, not outcomes achieved. Talking to users takes time and produces ambiguous results. Shipping features produces clear, measurable output. Every engineer on the team knows intellectually that they should do more user research — and every engineer also knows that user research won't appear on their performance review. The locally rational choice is to ship.

The decision isn't wrong because the team is stupid. It's wrong because the measurement system rewards the wrong thing. Fix the measurement, and the behavior changes. Tell the team to "be more user-focused" without changing the measurements, and nothing changes.

### Scenario B: The Legacy System Nobody Will Touch
A codebase has a critical component that everyone knows is fragile, poorly documented, and a major source of production incidents. Everyone avoids working on it. From the outside: obviously the team should refactor it. From the inside: the person who takes on the refactor will spend months in a risky, poorly-scoped project with unclear success criteria, while their peers are shipping features that are visible and attributable to individuals. If the refactor succeeds, it's invisible (nothing broke). If it fails, it's highly visible (things broke). Expected value calculation for the engineer's career: don't touch it. Each engineer is making a locally rational choice. The globally irrational outcome — a fragile system nobody maintains — emerges from individually rational decisions.

### Scenario C: The Reorg That Didn't Fix the Problem
Two teams are in conflict over ownership of a shared service. The conflict produces delays, finger-pointing, and an escalating number of incidents. Leadership decides to reorganize — put both teams under the same manager. The reorg happens. Six months later, the conflict is still there, now expressed as a territorial dispute within a single org rather than across org boundaries. The underlying cause wasn't the reporting structure — it was the ambiguous ownership of the service, the different metrics each team was optimizing for, and the historical mistrust between them. The reorg changed the org chart without addressing any of these. It felt like action. It was organizational theater.

### Scenario D: The VP Who Kills the Better Technical Solution
Two proposed architectures. One is technically superior: better performance, lower operational complexity, more maintainable. The other is familiar to the VP's most trusted team leads and reuses their existing investment. The VP chooses the second one. From the outside: obviously the wrong decision, possibly political. From the inside: the VP is accountable for the outcome. If the technically superior but unfamiliar architecture fails, it's the VP's failure. If the familiar architecture fails, there's more organizational diffusion of blame. The VP is risk-managing their career. The incentive to choose the known quantity is not stupidity — it's a rational response to how accountability is distributed.

### Scenario E: The Team That Never Says No
A team accepts every request that comes in. Their roadmap is a graveyard of half-finished projects. From the outside: dysfunctional prioritization. From the inside: this is a team in a culture where saying no is penalized. The last time the team pushed back on a request, the requestor escalated to the VP, who overruled the team and left everyone with the implicit lesson: say yes, or someone more senior will say yes for you. The locally rational response to that environment is to say yes to everything and manage the consequences later. The dysfunction is in the incentive — the team learned that political capital spent on declining requests has negative expected value.

### Scenario F: The Platform Team Nobody Uses
A platform team builds a "golden path" for all engineering. Eighteen months of work. Low adoption. From the outside: engineers are choosing harder paths when an easier one is available — irrational. From the inside: the platform solves problems the platform team had, not problems the product teams have. The product teams were never consulted. The platform team's success metrics were defined in terms of capabilities shipped, not adoption achieved. The platform team is building what they were incentivized to build. The product teams are avoiding the platform because it doesn't solve their actual problems. Both sides are behaving rationally. The failure is in the design of the system — not in the people.

---

## 4. Counter-Arguments

### Counter-Argument A: "Some decisions really are just dumb."
The local rationality frame can slide into a kind of organizational determinism that excuses bad judgment. Sometimes a decision is simply wrong — not locally rational, just a bad call made by someone who should have known better. Over-applying "everyone is rational" can produce learned helplessness: the dysfunction must be systemic, so there's nothing to be done.

**How to address it**: The chapter should acknowledge this directly. The local rationality frame is a diagnostic tool, not a universal excuse. It tells you to ask "what incentive structure produced this behavior?" before concluding someone is incompetent. In many cases, that question will reveal a structural cause. In some cases, the answer is "no structural cause — this was a genuinely bad decision." Knowing which is which matters. The mistake engineers make is skipping the structural analysis and going straight to "that's just dumb." The local rationality frame corrects that bias; it doesn't replace judgment.

The practical heuristic: if the same type of bad decision recurs across different people in different roles, it's structural. If it's a one-off, it might just be a bad call.

### Counter-Argument B: "This framework is too charitable to leadership."
Telling engineers that confusing organizational behavior is "locally rational" can read as an apologia for bad management — a way to explain away decisions that should be challenged. A cynical reading: the framework tells engineers to accept dysfunction rather than fight it.

**How to address it**: Understanding is not the same as acceptance. The point of diagnosing the incentive structure that produces bad behavior is not to shrug and walk away — it's to understand what would actually need to change for the behavior to change. Telling a team to "be more strategic" when their incentives reward short-term output won't work. Understanding the incentive structure gives you the lever. The chapter should make this explicit: the local rationality frame is a tool for finding the actual problem, not a reason to give up on fixing it.

---

## 5. Data Points and Studies

- Kahneman's work (*Thinking, Fast and Slow*) on cognitive biases: anchoring, availability heuristic, confirmation bias — these operate at the individual level, but organizational decision-making aggregates and sometimes amplifies individual biases rather than averaging them out.

- Studies of organizational decision-making under ambiguity (Cohen, March, Olsen's "garbage can model," 1972): structured empirical evidence that organizational decisions often do not follow a rational problem-solution-choice sequence.

- Research on "normalization of deviance" (Diane Vaughan's analysis of the Challenger decision-making process): how organizations systematically rationalize behaviors that deviate from stated standards, such that what would initially seem like obviously wrong decisions become locally acceptable over time. Highly relevant to the chapter — this is local rationality at its most dangerous.

- March and Simon's original empirical work on satisficing — surveys of actual managerial decision-making showing that the optimization model simply doesn't describe how decisions are made.

- Research on principal-agent problems in organizations (Jensen and Meckling, 1976) — the foundational economics on why individual incentives diverge from organizational incentives, and what it costs to align them.

---

## 6. Suggested Chapter Structure

**Section 1: The Machine Metaphor**
Open with the observation that engineers are trained on deterministic systems. The mental model transferred to organizations: if the system is producing bad outputs, there must be a faulty component. Name this as the machine metaphor, trace its origins briefly (Taylor, scientific management) to show it's a specific historical choice, not an inevitable way of thinking.

**Section 2: The Organism Reality**
Introduce Morgan's organism metaphor as a more accurate model. Organizations are adapting to external pressures: market conditions, regulatory environment, competitive threats, the survival instincts of the people inside them. A decision that looks wrong in the abstract may be the organization's (or a subgroup's) adaptation to something real. Ground with a concrete scenario — e.g., the platform team nobody uses.

**Section 3: Local Rationality**
The core reframe. Every person in an organization is optimizing for something, and it's usually not "the organization's best outcome." It's their career, their team, their relationship with their manager, their need for psychological safety, their accumulated sunk costs. Walk through two or three concrete scenarios where behavior that looks irrational from outside is obviously rational from inside. Introduce bounded rationality here as additional texture — not just wrong incentives, but also limited information and cognitive constraints.

**Section 4: The Political System**
Complete the three-metaphor framework with the political lens. Organizations are coalitions. Decisions are negotiated outcomes. The technically superior proposal that keeps losing isn't losing because decision-makers are stupid — it's losing because it threatens someone's budget, territory, or status. Name this clearly and non-cynically: politics is not a character flaw, it's what happens when rational actors with different interests share limited resources.

**Section 5: The Skeptic's Turn — When It Really Is Just Dumb**
Address the counter-argument directly. The local rationality frame is a diagnostic tool, not a universal excuse. How to tell the difference between structural dysfunction (same bad decision pattern recurring across people and time) and individual bad judgment. Why defaulting to "that's just dumb" is a failure mode, but so is using "local rationality" to avoid naming bad decisions when they occur.

**Section 6: What Changes Monday**
The implications for how you operate. Before attributing dysfunction to incompetence or malice: ask what incentive structure is producing the behavior. Before proposing a fix: ask whether the fix changes the incentive or just addresses the symptom. Before getting frustrated at a decision you think is wrong: map whose local interests are being served by it. Practical tools: the pre-mortem that asks "whose interests would this decision serve?"; the question "what does this person's success look like?" before any major cross-functional interaction.
