# Research Notes: p2_c1 — Everyone Is Rational, Given Their Incentives

## Core Argument

Behavior that looks irrational, lazy, or malicious from the outside is almost always
rational from inside the incentive structure of the person doing it. The practical
skill is not judgment — it's mapping. Before diagnosing dysfunction as stupidity or
bad faith, map the incentives. The behavior will usually make sense.

---

## Historical Parallels

### 1. The Challenger Disaster (1986)

The textbook case of incentive suppression in an engineering organization. The O-ring
failure mode was known to engineers at the contractor level for years before the launch.
The night before the launch, engineers explicitly argued against proceeding in cold
temperatures. Their concerns were overridden.

The incentive structure that produced this outcome: NASA was under intense political and
budgetary pressure to demonstrate launch cadence. The shuttle program's continued
funding was, in part, a function of how frequently it could fly. Launch delays were
costly — not just in dollars, but in the organizational narrative that the shuttle was
operational and routine. The managers making the launch decision were not villains
ignoring safety for personal gain; they were people operating in a system where
schedule pressure was concrete and near-term, and where O-ring failure probability
under cold conditions was abstract and uncertain.

The engineers who knew about the O-ring risk faced a different incentive structure:
they were lower in the hierarchy, they had already raised concerns through official
channels, and the organizational norm had established that "prove it's unsafe" was
the burden — not "prove it's safe." That norm inverted the default toward launch and
made dissent structurally costly.

Key lesson: the information existed. The signal was present. The incentive structure
systematically suppressed the signal before it could reach the decision makers who
needed it. This is a structural failure, not a moral one — though the moral consequences
were catastrophic.

Source type: Presidential Commission on the Space Shuttle Challenger Accident (Rogers
Commission, 1986); Diane Vaughan's "The Challenger Launch Decision" (1996) — her
concept of the "normalization of deviance" is the framework here. Vaughan shows that
each small deviation from standard became the new standard, and that this process was
not the result of bad individuals but of organizational processes that made the deviant
normal.

### 2. The Ford Pinto Fuel Tank (1970s)

Ford engineers and executives knew the Pinto's fuel tank design made it vulnerable to
rupture in rear-end collisions. An internal cost-benefit analysis calculated the cost
of litigation from deaths and injuries against the cost of a design fix ($11 per car).
The litigation cost was estimated as lower. Ford proceeded without the fix.

The incentive structure: the company was racing to market to compete with smaller
imported cars. The engineering fix would have delayed launch or added unit cost. The
legal framework at the time made paying out damages cheaper than design changes. The
people involved were operating inside a system where "expected cost" calculations were
standard practice. Every step was, in some sense, locally rational.

The lesson for the chapter: "rational given incentives" does not mean "ethical" or
"correct." The point is not to excuse the outcome — people died — but to understand
that moral condemnation of individuals misses the systemic fix. If the legal environment
had changed the expected cost calculation (as it eventually did with punitive damages),
the incentive to fix the design would have changed too. Incentives determine behavior.
Change the incentives, change the behavior.

### 3. The Space Shuttle Main Engine Turbopump (1970s–1980s)

Less well-known than Challenger but equally illustrative: engineers working on the
turbopump had evidence of fatigue cracks and were under pressure to certify flight
readiness. The program schedule was being driven by political timelines. Engineers who
raised concerns found themselves reassigned or marginalized. The incentive for any
individual engineer to persist in escalating concerns was low: the organizational
consequence was career damage, and the feedback loop was long enough that they could
not observe the outcome.

This is distinct from Challenger in that it was not a single dramatic decision but an
accumulation of small ones, each locally rational. This models the kind of organizational
failure that is invisible until it isn't.

---

## Key Frameworks

### Incentive Theory (Basic Economics)

People respond to incentives. This is not controversial, but the application to
organizations is routinely underestimated. The relevant insight: incentives don't have
to be financial. Status, security, recognition, reduced friction — all function as
incentives. When mapping organizational behavior, the question is not "what are they
paid to do?" but "what are they rewarded for, penalized for, recognized for, and
protected from?"

### Principal-Agent Problem

The classic setup: the principal (organization, manager, employer) delegates to an agent
(employee, vendor, subordinate) whose incentives are not perfectly aligned. The agent
has information the principal lacks and will act on their own interests in the gaps.
The problem is not that agents are dishonest — it's that perfect incentive alignment is
impossible. No employment contract, OKR system, or performance review fully aligns
individual and organizational incentives.

This is covered in depth in p2_c3, so for this chapter, introduce it briefly: the
manager hoarding headcount is doing what the incentive structure rewards. They're not
a bad agent — they're an agent operating exactly as predicted.

### Hanlon's Razor (Inverted)

"Never attribute to malice that which is adequately explained by stupidity." The inversion
for organizational behavior: "Never attribute to malice or stupidity that which is
adequately explained by incentives." This is the chapter's practical slogan.

Hanlon's Razor is useful but stops too early. Organizational dysfunction usually isn't
malice, but it also isn't incompetence — it's structure. The manager who doesn't share
information with another team is not stupid; they're operating in a system where
information is power and sharing it doesn't benefit them. The engineer who won't
document the legacy system isn't lazy; documentation isn't measured, and knowledge
hoarding makes them indispensable.

### Goodhart's Law (introduced here, elaborated in p2_c4)

When a measure becomes a target, it ceases to be a good measure. Brief mention: the
reason people optimize for the metric rather than the outcome is that the metric is what
gets measured — and therefore what gets rewarded. The incentive follows the measurement.

### Local Rationality vs. Global Irrationality

A concept from complex systems: a system can produce globally irrational outcomes
through locally rational individual decisions. Traffic jams. Bank runs. The team that
avoids the shared codebase because touching it has historically led to blame without
reward — locally rational, globally catastrophic. The system-level failure doesn't
require any individual to be irrational.

### Game Theory: Nash Equilibria in Organizations

Organizations are not unified actors — they're collections of agents in a multi-player
game. Each team's optimal strategy depends on what other teams do. Equilibria emerge
that no single actor would design but that every actor is stuck in. The "avoid the
untouchable codebase" pattern is a Nash equilibrium: no team has an individual incentive
to fix it unilaterally (the cost is theirs; the benefit is distributed), so it doesn't
get fixed. This is the organizational version of the prisoner's dilemma.

---

## Concrete Scenarios

### Scenario 1: The Headcount Hoarder

A director of engineering is measured — formally and informally — by team size. In most
large organizations, headcount correlates with budget, influence, and perceived
importance. A director with 40 reports occupies a larger organizational footprint than
one with 15. Their budget is larger, their seat at planning meetings is more secure,
their leverage in cross-team negotiations is greater.

Now consider: a colleague proposes moving two engineers to a new high-visibility project.
From the outside, refusing seems petty. From inside the incentive structure, it's
obvious — reducing headcount reduces power, and the engineers were probably doing
something useful.

The fix is not to hire more empathetic directors. The fix is to change the measurement:
stop using headcount as the proxy for importance or contribution. When organizations
do this (measure impact instead of size), the behavior changes.

### Scenario 2: The Team That Won't Touch the Legacy System

A system is old, fragile, and documented only in the memories of two engineers who have
been around since the beginning. Everyone knows it needs a rewrite. No one does it.

The incentive structure: rewriting the legacy system is a 12-18 month project with
enormous risk, no guaranteed success, and no external visibility. Feature work is
visible, demonstrable, shippable. The two engineers who understand the legacy system
derive significant status and job security from that specialization — a rewrite would
eliminate their monopoly on an important thing.

The team that would theoretically own the rewrite doesn't own the system currently.
If the rewrite goes wrong, they take the blame. If it succeeds, they get some credit
but lose the autonomy of not touching the legacy system.

Locally rational not to touch it. Globally irrational over time: the system accumulates
load until it fails under conditions no one can diagnose.

### Scenario 3: The VP Who Kills the Technically Superior Project

A VP blocks adoption of a technically better approach in favor of continuing investment
in an existing system. Engineers are frustrated — the existing system has obvious
limitations, the new approach demonstrably solves them.

The incentive structure: the VP built their reputation on the existing system. It is,
at some level, their legacy. The new approach was championed by a different team.
Killing the new approach is not necessarily about ego — it may be about organizational
risk. If the new system fails, the VP's team carries the blame for the failure. If it
succeeds, the VP's team gets credit for stepping out of the way — a reputational wash
at best.

More concretely: the VP's performance is measured in the near term. The new approach
would require investment in migration, training, and a period of reduced velocity.
The existing system, for all its flaws, is known to work well enough. The cost of
changing is real and near-term; the benefit is diffuse and future.

### Scenario 4: The Engineer Who Won't Document

A senior engineer is the only person who understands how a critical component works.
Others have asked for documentation. It hasn't appeared.

The incentive structure: documentation takes time and produces nothing measurable.
It makes the engineer more replaceable. In a culture where performance reviews reward
individual output, writing documentation is a cost to the individual with a benefit
to the team. The engineer is not malicious — they're responding to a system that
doesn't reward knowledge transfer.

### Scenario 5: The Team That Over-Engineers

A team consistently builds solutions more complex than the problem requires. Abstractions
proliferate. Every feature ships with a framework that could serve ten use cases the
team will never encounter.

The incentive structure: complexity can justify headcount, extend timelines, and
increase perceived importance. It can also reflect genuine craft — engineers often
build for elegance because that's what they find rewarding, even when it doesn't serve
the current need. In performance reviews, "built a system that handles X, Y, and Z
cases" sounds better than "built the simplest possible thing." The incentive system
rewards sophistication over adequacy.

### Scenario 6: The Platform Team That Doesn't Serve Its Customers

An internal platform team has built something technically impressive. The engineers
who built it are proud of it. The teams who are supposed to use it don't, or use it as
little as possible.

The incentive structure: the platform team is measured on platform capabilities, not
on adoption or on the outcomes of the teams using it. They're rewarded for building,
not for the platform's usefulness. There's no feedback loop that makes customer failure
costly to the platform team. Absent that feedback loop, the platform serves the people
who build it, not the people who use it.

---

## Counter-Arguments

### Counter-argument 1: Sometimes people really are malicious or incompetent

Incentive mapping can become an excuse for tolerating bad behavior. Not everything is
structural. Some managers are genuinely abusive, some engineers are genuinely negligent,
some decisions are genuinely corrupt. The incentive-first lens can produce a kind of
learned helplessness: "the structure made them do it," followed by nothing changing.

**How to address:** The framework has two uses — diagnostic and corrective. For
diagnosis, starting with incentives is almost always correct because it prevents
misattribution and reduces wasteful confrontation. For correction, structural intervention
is usually more durable than individual correction (change the incentive, change the
behavior across all people in that role — not just the current occupant). But structural
intervention doesn't preclude individual accountability when the behavior is genuinely
harmful, persistent, or intentional in spite of correct incentives.

The practical guidance: exhaust the structural explanation first. If the incentive
structure explains the behavior, fix the structure. If the behavior persists after
incentive alignment, then individual accountability is appropriate.

### Counter-argument 2: This makes change seem impossible

If everyone is rationally responding to incentives, then changing the behavior requires
changing the incentive structure, which is a systems problem. Individual engineers
reading this may conclude: "I can't change the incentive structure, so this framework
is interesting but not useful."

**How to address:** The framework is useful even if you can't change the incentives,
because it changes how you respond. If you understand that a colleague's behavior is
incentive-driven rather than malicious, you stop trying to convince them with the
better argument and start asking what you'd need to change about the situation to shift
the incentive. Sometimes that's within your control (you can offer credit, remove risk,
provide cover). Sometimes it isn't — but knowing that saves you the energy of
attributing bad faith where there is none.

Additionally: senior engineers and tech leads often have more leverage over incentive
structures than they realize. The engineer who can clearly explain "this team isn't
documenting because we don't measure or reward it" has surfaced a structural problem
that management can act on. Naming the incentive is the first step to changing it.

---

## Data Points and Studies

- **Behavioral economics on performance incentives:** Research by Ariely et al. has
  shown that adding external rewards for work people find intrinsically motivating can
  reduce performance — the "crowding out" of intrinsic motivation. Relevant here:
  the engineer who is proud of their craft is sometimes harmed by a bonus structure
  that incentivizes quantity over quality.

- **Organizational behavior on information suppression:** Research in organizational
  behavior (Milliken & Morrison, 2000 — "employee silence") shows that employees
  consistently withhold information from supervisors when they expect negative
  consequences. The Challenger analogy: the incentive to not be the bearer of bad news
  is pervasive and well-documented.

- **Principal-agent studies in professional services:** Research on the advisory
  professions — medicine, law, consulting — consistently shows that advice tracks
  the advisor's financial interest even when advisors have professional obligations
  otherwise. This is not fraud; it is incentive alignment at work.

- **Goodhart's Law in practice:** Studies of software project metrics (lines of code,
  bug counts, velocity) consistently show that measurement of a proxy drives optimization
  of the proxy at the expense of the underlying goal. This has been documented in
  healthcare (readmission rates), education (test scores), and financial services
  (risk metrics before 2008).

- **Headcount as power proxy:** Studies of organizational behavior in hierarchical firms
  document that managerial status correlates strongly with direct report count,
  independent of scope of responsibility. This is the structural explanation for
  headcount hoarding.

---

## Suggested Chapter Sections

1. **The Manager Who Was Doing Everything Right**
   Open with a scene: an engineer or tech lead who has just had a frustrating conversation
   with a manager who blocked something sensible. Introduce the attribution error: the
   instinct is to conclude the manager is incompetent or political. Propose the reframe.

2. **What "Rational" Actually Means**
   Clarify: rational here means responding to actual incentives, not formal job
   descriptions. Introduce the core framework. Brief primer on principal-agent dynamics
   and local vs. global rationality.

3. **Canonical Patterns: The Incentive Map in Action**
   Walk through 3-4 of the concrete scenarios above. For each: describe the behavior,
   then reveal the incentive structure. The reader should feel the "oh" of recognition.

4. **When the Signal Never Arrives: Historical Cases**
   The Challenger-level cases: where incentive structures don't just produce suboptimal
   behavior but suppress the information that could prevent catastrophe. Makes the stakes
   legible. Normalizes the idea that this isn't abstract — it's how good organizations
   fail.

5. **The Skeptic's Objection: What About Bad Actors?**
   Direct engagement with the counter-argument. Incentive mapping is not an alibi.
   Individual accountability is appropriate in some cases. The diagnostic sequence:
   incentives first, character second.

6. **What Changes Monday: The Incentive Audit**
   Practical tool: before your next frustrating organizational interaction, write down
   what you think the other person's incentives are. Not their formal job description —
   their actual incentives. What are they measured on? What are they afraid of? What
   would they have to sacrifice to do the thing you're asking? Now ask whether the
   behavior still looks irrational.

---

## Notes on Voice and Framing

- Avoid the word "incentivize" — it's jargon. Use "rewarded for," "measured by,"
  "penalized for."
- The chapter's tone should be *clarifying*, not cynical. The point is not that
  organizations are corrupt or that people are only motivated by money. The point is
  that understanding the actual incentive structure is more useful than assuming
  dysfunction is random or personal.
- The Challenger example is familiar to a technical audience and carries weight. Use
  it as the serious anchor. The organizational examples (headcount hoarding, etc.) are
  the accessible everyday translation.
- Avoid the implication that incentives are destiny. The chapter ends with agency:
  you can change the structure, you can change how you interact with the structure, you
  can at least stop spending energy on misattribution.
