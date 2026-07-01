# Research Notes: p2_c5 — Why Good Engineers Do Bad Things

## Core Argument

Dysfunctional behavior by capable engineers — cutting corners, deferring maintenance,
over-engineering, hoarding knowledge, failing to communicate risk — is almost always
structurally caused, not characterologically caused. The fundamental attribution error
leads observers (and engineers themselves) to locate the problem in the person rather
than the system. This chapter corrects that. Understanding the structural cause is the
necessary first step to changing either the structure or your own behavior within it.

---

## Historical Parallels

### 1. The Challenger Disaster (1986)

Engineers at the contractor building the solid rocket boosters knew the O-ring seals had
a temperature-dependent failure threshold. They had raised concerns before the launch.
The night before Challenger launched in unusually cold conditions, engineers explicitly
objected. Management overruled them.

The structural mechanism: the engineers were not ignored because management was stupid
or evil. The launch had been delayed multiple times. There was political and contractual
pressure to demonstrate reliability. The engineers were asked to "prove" the seals would
fail — an impossible standard. When they could not produce incontrovertible proof, the
organizational default (launch on schedule) prevailed.

The lesson for this chapter: the engineers did not "go silent" because of cowardice.
They raised concerns through the channels available to them. Those channels had a
structural bias toward the outcome the organization was already committed to. The
problem was not individual silence — it was a communication and decision architecture
that systematically filtered out dissent at the moment it was most needed.

Key detail for the chapter: Richard Feynman's dissent in the Rogers Commission report
was that the managers and the engineers had developed genuinely different estimates of
failure probability — not because the managers were dishonest, but because the
organizational filtering that separates engineering input from executive decision-making
had degraded the signal.

### 2. The Therac-25 (1985–1987)

A radiation therapy machine with a software-controlled safety interlock. Previous
versions had hardware interlocks as a backup. When the software was rewritten for the
new version, the hardware backup was removed — a cost and complexity reduction.

The software had a race condition that, under specific timing conditions, could deliver
a massive radiation overdose. The deaths came in small numbers across multiple hospitals
over two years. Each incident was initially attributed to user error. The software
engineer who maintained the machine worked largely alone; there was no independent code
review; the codebase had grown organically from a trusted prior version.

The structural mechanisms:
- **Schedule pressure** eliminated the independent verification step.
- **Trust inheritance**: the new code was an extension of code that had worked. The
  assumption of correctness transferred.
- **Diffuse responsibility**: each hospital's incident was treated as isolated. No
  feedback loop aggregated the pattern.
- **No redundancy**: removing the hardware backup was locally rational (cost reduction,
  simplification). The systemic risk was not assigned to anyone's budget.

For the chapter: the engineer did not remove the hardware interlock out of malice or
laziness. Under the decision conditions that existed — trusted prior code, schedule
pressure, no mandate for independent review — the decision was locally rational. The
catastrophe was a system property, not a character defect.

### 3. Normal Accident Theory (Perrow, 1984)

Charles Perrow's argument: in complex, tightly coupled systems, accidents are not
anomalies — they are properties of the system. The question is not whether failures
will occur but whether the system's design allows recovery before cascade.

"Tightly coupled" = one failure propagates quickly, there is little buffer or slack.
"Complex" = components interact in ways that are not fully visible or predictable.

The relevance to software engineering organizations:
- Codebases with high coupling and low observability are Perrow-style high-risk systems.
- Organizations with little slack, high coordination overhead, and concentrated expertise
  are tightly coupled sociotechnical systems.
- In such organizations, individual "bad decisions" are often the triggering event of a
  pre-existing accident waiting to happen. The individual is not the cause — they are
  the point of failure that a well-designed system would have been resilient to.

Key concept: **tight coupling eliminates recovery time**. An engineer defers a fix and
plans to return — but the system is so tightly coupled that by the time they return, the
deferred fix has become five entangled issues. The structural condition (no slack, high
coupling) turned a rational deferral into a compounding problem.

---

## Key Frameworks

### Fundamental Attribution Error (Ross, 1977)

The tendency to attribute others' behavior to their character or disposition rather than
their situation, while explaining one's own behavior situationally. ("They shipped buggy
code because they're sloppy; I shipped buggy code because we had no time.")

In engineering organizations, this shows up in performance reviews, postmortems, and
incident retrospectives: the individual who made the call is blamed; the conditions that
made the call inevitable are not addressed. This means nothing changes — the next person
in the same conditions makes the same call.

The chapter should be explicit: most performance problems that look like character
problems are situation problems. This is not an excuse — it is a more accurate
diagnosis, and accurate diagnosis leads to interventions that actually work.

### Normal Accident Theory (Perrow)

Covered above. Key terms to use without jargon: tight coupling, complexity, cascade
failure, accident-prone vs. accident-resilient system design.

### Slack Theory (DeMarco, 2001)

Tom DeMarco's argument in *Slack*: organizations operating at full capacity have no
ability to absorb uncertainty, change direction, or improve. Slack — unscheduled time,
organizational bandwidth — is not waste. It is the system's capacity for adaptation.

An engineer with no slack in their schedule cannot:
- Write documentation without slipping a deadline
- Refactor a component before it becomes legacy
- Help a colleague onboard without falling behind on their own work
- Think carefully before making a decision under time pressure

The behaviors that look like character failures (skipping documentation, not helping
with onboarding, cutting corners) are often the direct output of a system running with
no slack. The engineer is making locally rational trades under scarcity.

### Cognitive Overload and Decision Quality

Research on deadline pressure and decision quality consistently shows degradation under
load. Under high cognitive load, decision-making narrows: attention focuses on the
immediate, the near-term, the measurable. Long-term consequences (maintenance burden,
documentation debt, team dependencies) are discounted — not because the engineer doesn't
value them, but because the cognitive bandwidth to hold them in mind simultaneously with
immediate deadline pressure does not exist.

This is a structural condition, not a personal failure. Systems that routinely operate
at the edge of engineer cognitive load will routinely produce decisions that optimize
the immediate at the expense of the long-term.

### Incentive Visibility and Invisible Work

Knowledge transfer, documentation, mentoring, code review quality, postmortem
thoroughness — most of this work is invisible in reward systems that measure shipped
features, closed tickets, or velocity. An engineer rational about their career will
(correctly) observe that time spent on visible output is rewarded, time spent on
invisible output is not. They will allocate accordingly.

This is not cynicism. It is rational response to a reward structure. The organization
that says it values documentation but only measures features has created an incentive
structure that produces engineers who don't write documentation. The fault is not in the
engineer.

---

## Concrete Scenarios

### Scenario 1: The Documentation Deferral

An engineer owns a critical subsystem. It is complex. She is the only person who fully
understands it. She has been meaning to document it for eight months. Each sprint, she
has a feature or a bug fix that is on the roadmap. Documentation is not. Her manager
mentions it occasionally; it never appears in performance goals. She is not lazy. She
is responding correctly to a reward system that measures shipped features and treats
documentation as a nice-to-have.

The structural fix is not to tell her to document more. It is to make documentation a
deliverable with the same first-class status as a shipped feature — which means putting
it in the roadmap, the sprint goals, and the performance review criteria.

### Scenario 2: Knowledge Hoarding as Career Insurance

A senior engineer is the sole expert on the authentication service. He has been
approached about documenting it and training others. He is cordial about it but always
has a reason it hasn't happened. Observers attribute this to protectiveness or ego.

The structural reality: in his organization, specialization is the primary driver of
career advancement and job security. The last round of layoffs hit generalists hardest.
He has correctly read the environment. Being the only person who knows a critical system
is job security. Sharing that knowledge dilutes his competitive position.

The structural fix is to change what the reward system values. Organizations that reward
deep specialization over knowledge transfer will produce knowledge hoarding. The
engineers doing it are being rational.

### Scenario 3: Over-Engineering Under Ambiguity

A team builds a new service. The requirements are vague — "needs to scale." No specific
targets. No user numbers. The team builds a distributed, event-driven architecture that
could handle ten times the anticipated load. It takes twice as long. The product launches
late and the scale never materializes.

This looks like gold-plating or technical excess. The structural cause: under ambiguous
requirements, engineers default to the technically interesting solution that demonstrates
skill and creates optionality. The organization failed to provide constraints. Ambiguity
+ technically capable people + no feedback on cost = over-engineering. Not a character
failure. A requirements and product discipline failure.

### Scenario 4: The Deferred Maintenance Spiral

An engineer identifies a fragile component that will eventually need rewriting. He
estimates three weeks. The current sprint has committed deliverables. He files a ticket.
The ticket lives in the backlog for four months, joined by related tickets. When the
component finally fails, it now takes eight weeks to fix because the dependent systems
have grown around its quirks. He is blamed for "not raising it sooner."

He raised it. In the only channel available to him. The structural failure is a
prioritization process that treats maintenance as optional until failure forces it, and
a culture that files blame at the point of failure rather than the point of systemic
misalignment.

### Scenario 5: The Silent Engineer in the Room

A team is about to make an architectural decision that a senior engineer believes is
wrong. She doesn't speak up clearly. Later, the consequences she predicted arrive. Her
manager is frustrated: "Why didn't you say anything?"

What happened: she raised concerns in a meeting. They were acknowledged but overruled.
She read the room — her manager was committed to the decision, raising objections further
would be read as not being a team player, the culture historically punished persistent
dissent. She did a rational calculation about the personal cost of speaking up versus
the organizational benefit, and stayed quiet.

This is Amy Edmondson's psychological safety research made concrete: people withhold
dissent not because they are cowardly but because the environment has signaled, through
past responses, that dissent carries personal cost. The structural fix is not to tell
engineers to "speak up more" — it is to change what happens when they do.

### Scenario 6: The Corner-Cutting Deadline Push

A team is ten days from a hard launch deadline. There are two known stability risks in
the codebase. Fixing them would take a week each. The team lead makes the call to ship
and monitor. Post-launch, one of the risks materializes into a two-day outage.

From the outside: they shipped known risks. From the inside: they made a judgment call
under severe time pressure with the information available. They were working from an
incentive structure where missing the launch date had a certain, visible, immediate cost,
and the risk of the known issues was probabilistic, deferred, and uncertain. Classic
hyperbolic discounting. The structure — the hard deadline, the no-slack schedule, the
absence of a formal risk-sign-off process — made this outcome predictable. Not the
character of the lead.

---

## Counter-Arguments

### Counter-argument 1: Structural Explanations Become Excuses

The strongest objection: if every bad outcome is structural, engineers are absolved of
responsibility. This can become a learned helplessness in which nothing is anyone's
fault. At some point, individual judgment and courage matter. The engineer who knew the
O-rings would fail and stayed silent anyway bears some responsibility, regardless of the
structural pressure.

How to address: the chapter is not arguing that structural conditions remove individual
responsibility. It is arguing that structural conditions change the realistic range of
expected behavior and that intervention at the structural level is more effective than
intervention at the individual level. When five engineers in a row make the same bad
call under the same conditions, the diagnosis should be the conditions, not the
engineers. Individual accountability still matters — but it is insufficient as an
explanation and ineffective as the primary lever for change.

The practical version: blaming the individual without changing the structure guarantees
the next person in that role makes the same call. You can hold people accountable and
fix structures simultaneously. They are not mutually exclusive.

### Counter-argument 2: Some Engineers Really Are Just Difficult

Not every case of knowledge hoarding is structural. Some engineers are territorial by
temperament. Not every over-engineered system is ambiguity-driven — some engineers
over-engineer because they find the technical problem more interesting than the business
problem.

How to address: true. The chapter is not claiming structural causes are the only causes.
It is claiming they are systematically underweighted. The diagnostic question is not
"is this a structural problem or a character problem?" — it is "if I change the
structure, does the behavior change?" If you fix the incentive structure and the
knowledge hoarding stops, it was structural. If you fix the incentive structure and one
person still hoards, you have isolated a different problem. Start with structure because
structure scales and because wrongly attributing a structural problem to character
produces the worst outcome: you replace the person and nothing changes.

---

## Data Points and Studies

- Research on deadline pressure and quality: studies of software project deadline
  compression consistently show increased defect rates, reduced test coverage, and
  higher technical debt accumulation. The causal mechanism is cognitive — under time
  pressure, engineers shortcut the activities (testing, code review, documentation)
  that have delayed returns.

- Attribution research: studies of team performance reviews show that managers
  systematically over-attribute outcomes to individual character and under-attribute them
  to situational factors — consistent with the fundamental attribution error. This means
  postmortems and performance reviews that focus on individual behavior without examining
  structural conditions are both analytically weak and organizationally harmful.

- Knowledge hoarding in organizations: organizational behavior research shows knowledge
  hoarding increases in environments with high internal competition, uncertain job
  security, and individual rather than collective reward structures. Hoarding is not a
  personality trait distributed across individuals — it is a response to incentive
  conditions, and it rises and falls with those conditions.

- DeMarco's slack data: in *Slack* (2001) and earlier in *Peopleware* (with Lister),
  DeMarco documents the relationship between schedule pressure and quality outcomes.
  Teams consistently underestimate the cost of running at capacity; organizations
  persistently demand it despite evidence of degraded output.

- Perrow's Normal Accident Theory: the original empirical basis was industrial accidents
  (nuclear, petrochemical, aviation). Subsequent applications to software and
  sociotechnical systems have found consistent support: organizational accidents follow
  from system properties, not individual failures.

---

## Suggested Chapter Structure

### Section 1: The Blame Instinct and Why It Fails
Introduce with a postmortem scene — after an incident, attention goes to who made the
call rather than what conditions produced it. Frame the fundamental attribution error.
Argue that blame is not only unfair but analytically wrong: it misdiagnoses and
therefore fails to fix.

### Section 2: The System Was Designed to Produce This
Three historical examples compressed: Challenger (structural silencing of dissent),
Therac-25 (schedule pressure + removed redundancy + diffuse accountability), and the
general argument from Normal Accident Theory. The pattern: capable people, bad
outcomes, structural causes.

### Section 3: What the Reward System Actually Rewards
The incentive-visibility gap. Walk through five common behaviors (deferring maintenance,
not writing documentation, hoarding knowledge, over-engineering, staying silent) and
show the incentive structure that makes each rational. The engineer is not broken.
The reward system is.

### Section 4: Slack Is Not Waste
DeMarco's argument applied to engineering organizations. An organization with no slack
has no capacity for improvement, error correction, or deliberate quality investment. The
behaviors that look like laziness (skipping documentation, cutting corners) are often
the direct output of a system running at full capacity. Make the argument that building
in slack is a performance investment, not a cost.

### Section 5: The Skeptic's Turn — Structure Isn't Everything
Address the counter-arguments directly. Structure doesn't remove individual
responsibility. Some people really are difficult. How to hold both — and why starting
with structure is the more effective diagnostic even when individual factors are present.

### Section 6: What Changes Monday
Diagnostic questions the reader can use immediately: Before attributing a team behavior
to character, can you describe the structural condition that produces it? What would
change if the reward structure changed? Where is your system running with no slack?
What invisible work is your team doing that gets no credit?

---

## Connections to Adjacent Chapters

- **p2_c4 (Metrics Eat Culture)**: Goodhart's Law is one mechanism by which reward
  structures produce bad behavior. The engineer optimizing for the metric is behaving
  exactly as this chapter predicts.
- **p2_c1 (Everyone Is Rational)**: The same rational-within-incentive-structure
  argument, applied specifically to engineer behavior rather than organizational
  behavior.
- **p3_c1 (Conway's Law)**: Silent engineers producing poorly communicated systems is
  the human-layer equivalent of Conway's Law — communication structure shapes output.
- **p5_c6 (The Feedback Nobody Wants to Give)**: The structural causes of silence
  connect directly to why feedback gets withheld.
