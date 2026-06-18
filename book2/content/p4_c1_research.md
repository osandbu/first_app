# Research Notes: p4_c1 — How Decisions Actually Get Made

## Core Argument

Engineers are trained to think of decisions as optimization problems: gather information,
evaluate options against criteria, select the best one. Organizational decisions don't work
that way. They are social processes that produce outputs shaped by power, incomplete
information, reversibility, risk aversion, and timing. The engineer who understands this
is more effective — not because they've abandoned analysis, but because they've stopped
bringing a calculator to a negotiation.

---

## Historical Parallels

### 1. The Cuban Missile Crisis — Allison's Bureaucratic Politics Model

Graham Allison's 1971 analysis of the Cuban Missile Crisis, *Essence of Decision*,
produced three competing models of how governments make decisions. The "rational actor"
model (governments choose the option that best serves national interest) failed to
explain what actually happened. The "organizational process" model (governments execute
standard operating procedures) explained more. The "bureaucratic politics" model explained
the most: what came out of the crisis was a negotiated outcome among senior officials with
different institutional interests, different threat assessments, and different career
incentives — not the output of a rational optimization process.

Key insight for the chapter: the same three models apply in engineering organizations. The
"rational actor" model (engineering leadership makes decisions that optimize for technical
outcomes) is the model most engineers implicitly use. The bureaucratic politics model
is closer to what actually happens. An understanding of how your organization is actually
running its decisions — which stakeholders have power, what their institutional interests
are, which decisions are constrained by prior commitments — is more useful than a cleaner
technical argument.

This also provides the concept of "implementation as negotiation": the Cuban missile
withdrawal involved back-channels, implicit trades, and timing that were separate from
the official decision process. Engineering decisions also have back-channels and implicit
trades that happen separately from the meeting where the decision is nominally made.

### 2. NASA Challenger — Groupthink Under Schedule Pressure

The Challenger disaster is the canonical engineering case study in decision pathology.
The O-ring failure was predicted by engineers at Morton Thiokol. The night before the
launch, those engineers were on a call with NASA managers arguing against the launch.
What happened in that call is essential: the managers essentially asked the engineers
to prove the launch was unsafe (reversing the normal burden of proof: prove it is safe
to launch). The Thiokol management, under schedule pressure and wanting to maintain the
NASA relationship, overruled their own engineers. The decision was made not by analysis
but by institutional hierarchy exercising authority under time pressure.

Key insights for the chapter:
- Decisions made under artificial time pressure are frequently worse decisions. The
  schedule pressure was managerial, not physical — the decision could have been delayed.
- The burden-of-proof flip is a warning sign. When the question changes from "why should
  we do this?" to "prove we shouldn't," the decision has already been made and evidence
  is being collected to ratify it.
- Hierarchy is a decision-making mechanism with failure modes. When the people with
  authority are insulated from the consequences of being wrong, information stops flowing
  upward accurately.

This also connects to Diane Vaughan's concept of "normalization of deviance": the
organization had seen O-ring erosion at lower temperatures before without a catastrophic
failure. Each non-failure normalized the risk a little further. By the time engineers
were raising an alarm, they were fighting against institutional memory that said "we've
done this before and it was fine."

### 3. The Internet Protocol Stack — Distributed Decision-Making That Worked

The TCP/IP stack and the broader architecture of the early internet were not designed by
a committee that made optimal choices. They emerged from a distributed process of rough
consensus and running code, institutionalized in the IETF's working culture. The key
decisions — end-to-end argument, layering, connectionless network design — were
contested. There were alternatives (OSI was backed by government bodies with more
institutional weight than the IETF).

What made it work:
- Decisions were evaluated against running implementations, not just arguments. "Running
  code" forced a reality check that pure standards committees lacked.
- The process was designed to be reversible at multiple layers. You could change
  application protocols without changing the network layer.
- Rough consensus didn't mean unanimity — it meant identifying and overriding minority
  positions that weren't substantive objections.

Key insight: effective distributed decision-making requires structured mechanisms for
integrating information and resolving disagreement. The IETF had one. Most engineering
organizations don't — they have ad hoc email threads and meetings with unclear authority.
The internet also illustrates that reversibility is a design principle, not just a tactical
consideration: building systems that can be changed at one layer without disrupting others
is itself a form of decision architecture.

---

## Key Frameworks

### Klein's Recognition-Primed Decision (RPD) Model

Gary Klein's naturalistic decision-making research (starting with firefighters, later
extended to many expert domains) found that experienced practitioners under time pressure
don't do comparative option analysis. They pattern-match the situation to prior experience,
generate a single option that seems plausible, mentally simulate it for fatal flaws, and
execute it if no fatal flaw appears. Only if the simulation reveals a problem do they
consider alternatives.

Implications for engineering:
- This is how experienced engineers actually make decisions on familiar problems. It works
  well when the situation matches prior experience and fails badly when it doesn't
  (because the pattern match is wrong).
- Staff engineers and senior managers often make decisions this way — not out of laziness
  but because explicit option comparison is slow and their experience is usually a reliable
  signal. Junior engineers misread this as arbitrary or political.
- The implication: when you need someone to reconsider a decision they've made via RPD,
  you need to disrupt the pattern match — show them something genuinely novel about the
  situation, not just a different analysis of the same features they already processed.

### Kahneman's System 1 / System 2

The dual-process model is relevant here not as an individual psychology observation but
as an organizational one. Organizations under time pressure default to System 1: fast,
heuristic-driven, pattern-matching. The operational environment of most engineering
organizations (quarterly planning, launch pressure, incident response) systematically
produces System 1 decisions on questions that would benefit from System 2 analysis.

The practical implication: the goal isn't to eliminate System 1 decisions (impossible and
counterproductive) but to identify which decisions have sufficient consequence and
reversibility that they warrant slowing down, and to build organizational mechanisms that
force the pause. The pre-mortem is one such mechanism.

### Reversible vs. Irreversible Decisions (Type 1 / Type 2)

The most useful practical framework for calibrating decision effort. Irreversible or
hard-to-reverse decisions (architectural commitments, hiring decisions, vendor contracts,
security models) warrant slow, deliberate, documented processes with explicit
consideration of alternatives. Reversible decisions (feature flags, sprint prioritization,
naming) should be made fast with minimal process — the cost of slow-deliberate processes
applied to reversible decisions is itself a form of organizational dysfunction.

The error engineers most commonly make: treating all decisions as if they were Type 2
(reversible), moving fast, and discovering later that what they thought was reversible
wasn't. The second most common error: treating every decision as Type 1 (irreversible),
creating decision bottlenecks and analysis paralysis.

A useful addition to the basic framework: decisions become harder to reverse over time as
downstream dependencies accumulate. An architectural decision that was reversible at
month 1 may be effectively irreversible at month 18 not because of any technical lock-in
but because teams have built assumptions on top of it. The window for reversal closes
faster than most engineers realize.

### The Pre-Mortem

Developed by Gary Klein, the pre-mortem is a structured technique: before committing to
a decision, assume it has already failed spectacularly, and ask the group to explain why.
This de-anchors the group from the decision they're about to make (making it psychologically
safe to raise concerns) and systematically surfaces the concerns of people who might not
otherwise speak up in a group endorsing a path forward.

The pre-mortem is particularly effective because it reframes objection as participation.
In a normal decision process, raising concerns can feel like obstruction. In a pre-mortem,
raising concerns is the task. The technique converts potential dissenters into
contributors.

For engineering organizations: the pre-mortem is most valuable for irreversible decisions
with significant tail risk — not routine feature work, but architectural pivots, platform
choices, organizational changes.

### The Overton Window for Organizational Decisions

The Overton Window (originally a political science concept) describes the range of
options that are politically viable at a given moment. In organizational settings,
this is the range of decisions that stakeholders will actually support or at least not
actively resist. Technically optimal options outside the window don't get made, no matter
how good the analysis is.

Engineers frequently underestimate how narrow the window is and how to move it. The window
is shaped by: prior decisions and the narrative coherence of reversing them; the political
capital of the person proposing the change; the organizational anxiety about the problem
being solved; and the visibility of the alternative path's failure modes.

Practical implication: sometimes the most effective move is to change the window — to
run a blameless postmortem that makes a problem visible, to build a coalition before
proposing a solution, to let a bad decision accumulate enough consequences that the
window has moved. This is not manipulation; it's understanding that decisions happen
inside social contexts that have their own dynamics.

### DACI/RACI Frameworks

Driver, Approver, Contributor, Informed (DACI) and the older Responsible, Accountable,
Consulted, Informed (RACI) are tools for clarifying decision authority. Their value is
real: many organizational decisions fail not because the analysis was wrong but because
no one knew who actually had authority to make the call, or because authority was
ambiguous enough that everyone expected someone else to decide.

Their limits are equally real: DACI/RACI frameworks describe intended decision authority,
not actual decision authority. A person with the "Approver" role who lacks the political
capital or organizational standing to enforce the decision is nominally the approver and
functionally a rubber stamp. The framework is only as good as the actual authority
structure behind it.

Use DACI/RACI as a diagnostic tool: when a decision is slow or stuck, asking "who is the
Approver here and do they actually have the authority to approve?" often reveals the
structural problem.

---

## Concrete Scenarios

### Scenario 1: The Technically Correct Decision That Loses
A team proposes migrating from a legacy system to a more maintainable architecture. The
technical case is airtight: lower operational cost, better observability, faster feature
development. The proposal fails. What happened? The team presented to an audience that
included a director whose team had built the legacy system. That system was a significant
career achievement. The migration implied the legacy system was wrong. No one had talked
to the director before the meeting. No one had framed the proposal in terms of what the
director cared about (his team's future, not his past decisions). The technical analysis
was irrelevant to the actual decision being made.

### Scenario 2: The Hallway Decision
A major architectural decision is on the agenda for a Thursday all-hands review meeting.
On Monday, the VP of Engineering runs into the platform team lead in a hallway after a
quarterly business review. They chat for ten minutes. The VP, fresh off a conversation
with the CFO about infrastructure costs, asks whether the proposed approach could be
modified to reduce cloud spend. The platform team lead says yes, with a tweak. The VP
says "let's go with that then." Thursday's meeting happens on schedule. The attendees
discuss the options, raise objections, and are thanked for their input. The decision had
been made on Monday. No one tells the attendees that.

This is not corruption or bad faith — it's how decisions actually get made. The VP had
new information (cost pressure) and a trusted source (the platform lead). The formal
process was theater. The lesson: if you're not in the hallway conversations, you're not
in the decision process, regardless of whether your name is on the meeting invite.

### Scenario 3: The Escalation Trap
A team can't agree on a database schema decision. After three meetings, they escalate
to the engineering director. The director makes a call. Six months later, when the schema
has caused the predicted problems, the team retrospects — and the engineer who raised the
concern earliest says "I told you so." Everyone privately agrees. But because the decision
was escalated and made by the director, no one is willing to say it clearly. The political
cost of documenting that the director was wrong outweighs the organizational benefit of
learning from it. The decision log exists but the decision was never updated with outcomes.

### Scenario 4: The Reversibility Illusion
A team adopts a new service mesh at the encouragement of an infrastructure advocate.
"It's low-risk," the advocate says. "We can always rip it out." Eighteen months later,
every service in the organization has been built with assumptions about the mesh's
capabilities. The on-call rotation includes mesh-specific runbooks. New engineers are
trained on it. It is, in practice, irreversible — not because of technical lock-in but
because of the accumulated organizational weight of the choice. When it causes problems
at scale that weren't visible earlier, no one revisits the original decision; instead
they add layers to work around the limitations. The decision that felt reversible became
a constraint.

### Scenario 5: The Pre-Mortem That Changed a Decision
A cross-functional team is about to commit to a launch date for a major infrastructure
migration. The project lead runs a pre-mortem: "Assume we're six months from now and this
migration failed badly. What happened?" Three people immediately identify the same thing:
the rollback plan assumes a clean state that won't exist in production. Two other people
raise a dependency on a third-party system that has a different maintenance window. The
team doesn't find all the problems, but they find two that would have been showstoppers.
The launch date moves by three weeks. It feels like a setback. Six months later, it's
clear it prevented a significantly worse outcome.

### Scenario 6: Competing Decision Architectures
Two teams are building adjacent systems and need to make a joint architectural decision.
Team A has a flat structure where technical decisions are made by consensus. Team B has
a strong tech lead who makes calls unilaterally. They run three joint meetings. Nothing
gets decided. Team A's process produces a two-page summary of considerations with no
recommendation. Team B's tech lead proposes a direction and asks for Team A's sign-off.
Team A's engineers each have objections. None of them are individually blocking objections
— but the absence of a decision-maker means each objection stalls the process. The
decision finally gets made when a VP gets frustrated and appoints someone from Team A as
the decision-owner, effectively imposing Team B's structure. Team A's engineers are
frustrated. They had legitimate input. But the structural problem wasn't their input —
it was the absence of clear decision authority.

---

## Counter-Arguments

### Counter-Argument 1: Teaching Navigation Normalizes Bad Decision-Making
The objection: "If you teach engineers to navigate organizational politics, you're
teaching them to accept that decisions should be political. You're normalizing dysfunction
instead of fixing it."

This is a serious objection and deserves a direct answer. There are two responses:

First, descriptive and normative claims are different things. This chapter describes how
decisions actually get made, not how they should be made. A cardiologist who explains
how heart disease actually develops is not endorsing it. Understanding the mechanism is
a prerequisite to addressing it.

Second, the alternative — refusing to engage with decision processes as they are while
insisting they should be different — is not a principled position, it's an effective
abdication. Engineers who only operate in the world they want to exist consistently lose
to people who operate in the world that does exist. The goal is to be effective in the
actual environment while working to improve it, not to be ineffective until the
environment becomes ideal.

The chapter should also note where the political dynamics are genuinely dysfunctional
(the Challenger case) and what organizations can do to build better decision processes —
the point isn't just to navigate dysfunction but to contribute to reducing it.

### Counter-Argument 2: Data Should Win, Not Politics
The objection: "You're describing failure modes. The solution is better data and more
rigorous analysis, not adapting to institutional politics."

This conflates two different problems: the quality of the analysis and the adoption of
the analysis. Better data helps with the first problem but is not sufficient for the
second. A technically correct recommendation that fails to account for the organizational
context in which it will be evaluated will fail regardless of the quality of the data.
This is not a bug in organizations; it is a predictable consequence of the fact that
organizations are made of people with legitimate interests that differ.

The chapter's practical tools (pre-mortem, decision log, reversibility assessment) are
not substitutes for rigorous analysis. They are complements: they help good analysis
survive contact with real organizational decision processes.

---

## Data Points and Studies

- Klein's original naturalistic decision-making research (studying firefighters,
  military officers, ICU nurses) consistently found that experts under time pressure use
  RPD, not comparative analysis. The studies span multiple domains. The implication for
  engineering organizations: senior decision-makers are not doing the analysis that junior
  engineers expect them to do.

- Research on escalation of commitment (often called the "sunk cost fallacy" in
  organizational contexts) shows that groups exhibit stronger sunk-cost effects than
  individuals — organizations are more susceptible to doubling down on failing projects
  than the individuals within them, because the social cost of admitting a group decision
  was wrong is distributed and therefore politically costly.

- Studies of hospital decision-making and aviation crew resource management (both
  safety-critical domains with extensive post-hoc analysis) consistently find that
  information suppression happens not through active deception but through social
  hierarchies that make it difficult for junior personnel to contradict senior ones.
  The Challenger pattern reappears in medical errors and aviation incidents: the person
  with the information was not the person with the authority.

- Organizational behavior research on "decision velocity" (how quickly organizations
  move from identifying a decision to making it) finds that most organizations confuse
  decision quality with decision thoroughness. High-quality decisions in most
  organizational contexts do not require complete information — they require enough
  information to distinguish the best available option from the alternatives, plus a
  clear owner and a defined timeline.

---

## Suggested Chapter Structure

1. **The Decision You Thought You Were Making** — Open with a scenario (hallway
   conversation scenario above). Establish the gap between the model and the reality.
   Name the gap: decisions are social processes, not optimization problems.

2. **How Experienced People Actually Decide** — Klein's RPD model. Kahneman's system
   framing. The key implication: when you present an analysis to an experienced
   decision-maker, you're not giving them inputs for a calculation — you're providing
   information that may or may not update a pattern match they've already made.

3. **The Reversibility Principle** — Type 1 / Type 2 framework. The reversibility
   illusion scenario. The practical discipline: before investing decision effort, ask
   whether this choice can be revisited. The discipline applies in both directions —
   don't slow-walk reversible decisions, don't fast-track irreversible ones.

4. **The Pre-Mortem and the Decision Log** — Two concrete tools. Pre-mortem: how to
   run one, when to use it (irreversible decisions with tail risk). Decision log:
   what to record (context, options considered, decision, owner, expected outcome).
   Why the log matters — not for accountability theater but for organizational learning.
   The retrospective that can only happen if you wrote down what you expected.

5. **The Political Context Is Not Separate from the Decision** — Allison's models.
   The Overton Window. The technically correct decision that loses (Scenario 1).
   Address Counter-Argument 1 directly: this is not about normalizing politics but
   about operating effectively in a social environment.

6. **What Changes Monday** — Concrete second-person actions: before the next
   significant decision, identify who the actual decision-maker is (vs. who is nominally
   the decision-maker). Run a pre-mortem on one high-stakes decision this quarter.
   Keep a decision log for the next major architectural choice. In the hallway
   conversation you're about to have, ask yourself whether you're in the actual
   decision process or the formal one.
