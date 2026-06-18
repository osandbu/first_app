# Research Notes: p1_c1 — "Nobody Told You This Was the Job"

## Core Argument to Anchor

The chapter's thesis: the skills that get engineers promoted (clean architecture, fast
debugging, reliable delivery) are necessary but not sufficient past a certain level.
Once you cross that threshold, the problems multiplying on your desk are organizational —
misaligned incentives, communication structures that distort signal, decisions made for
reasons that have nothing to do with technical merit. Nobody explained this transition.
Most engineers discover it by running into it hard.

---

## 1. Historical Parallels

### 1a. Frederick Brooks and the Tar Pit (The Mythical Man-Month, 1975)

Brooks documented a specific species of the same problem: programming projects weren't
failing because the engineers were bad at programming. They were failing because the
organizational structures around the programming work were broken — estimates ignored
systemic complexity, adding people to late projects made them later, and the coordination
overhead of large teams was invisible in the planning models everyone used.

What makes Brooks useful here: he was writing from inside the engineering tradition.
He was not a management consultant telling engineers to be better communicators. He was
a program manager observing that the non-technical forces were more determinative than
the technical ones, and that nobody had a vocabulary for them. That's exactly the
register this chapter wants to hit. The reader's situation in 2025 is structurally
identical to what Brooks described fifty years ago.

Specific hook: Brooks's wry observation that "adding manpower to a late software project
makes it later" was so counterintuitive to managers at the time that it needed a whole
chapter to defend. It didn't fit the mental model. This chapter is doing the same thing
for the organizational environment more broadly — the reader has a mental model that
doesn't match reality, and the book's job is to update it.

### 1b. The Peter Principle and Its Engineering Flavor

Laurence Peter's observation (1969) that people are promoted to the level of their
incompetence is usually cited as a joke. But in engineering it has a specific and
non-comedic form: engineers are promoted for technical output, then deposited into a
role that primarily requires organizational navigation. The incompetence isn't personal
— it's the absence of training in a different set of skills. Nobody told them the job
had changed.

Peter's original formulation is about hierarchical promotion in general. The engineering
version is more specific: the criteria for promotion and the criteria for success in the
post-promotion role are almost entirely different, and this is rarely made explicit.
The engineer finds out through the experience of failing at things that seemed like
they should be easy, or winning the wrong battles, or being blindsided by political
decisions that invalidated months of technical work.

### 1c. Dijkstra on the Social Structure of Computing

Dijkstra wrote extensively (EWD manuscripts) that the separation between what computers
do and what the organizations around computers do was the central unsolved problem of
computing. His famous complaint that computing was treated as a discipline concerned with
machines rather than with the symbolic and social structures built on top of machines.

Less commonly cited: Dijkstra's observation that most of the failures he witnessed in
computing weren't technical — they were failures of how humans organized themselves
around technical systems. He saw organizational dysfunction as a first-class technical
problem, not a separate concern.

This is a credible historical anchor: if Dijkstra, whose technical credentials were
unimpeachable, considered organizational behavior part of the core problem, then senior
engineers who feel the same thing are in good company.

---

## 2. Key Frameworks

### The Individual Contributor / Organizational Influence Transition

The clearest framework: at the IC level, you create value directly through technical
output. At the senior/tech lead level, you create value through organizational influence
— by shaping what problems get solved, how they get framed, which proposals win, and
how a team functions. The input-output relationship changes completely, but the
performance review system usually hasn't caught up, and the engineer's own self-image
often hasn't either.

Will Larson's engineering levels framework (from *An Elegant Puzzle*) is directly
relevant: his description of the shift from "getting things done" to "making the
organization around you more effective" maps exactly onto what this chapter is about.

### The Organizational Behavior Lens

Weick's concept of "sensemaking" — that organizations are not rational machines but
collections of people constructing coherent narratives about ambiguous situations — is
the backdrop. Most engineers were trained to think of organizations as machines with
inputs and outputs. Weick (and the organizational behavior tradition more broadly)
argues they are much more like organisms: adaptive, politics-laden, shaped by history
and identity, locally rational in ways that don't add up to global rationality.

This framework matters for the chapter because it reframes the experience the reader
is having. When the organization makes a decision that seems irrational from a purely
technical perspective, the engineer's first instinct is "these people are stupid." The
organizational behavior lens says: they're not stupid, they're operating in a different
system of incentives and information than you are. Understanding that shift is the
precondition for everything else in the book.

### Herbert Simon: Bounded Rationality and Satisficing

Simon's observation that organizations don't optimize — they satisfice. They look for
solutions that are "good enough" given the constraints of time, information, and
cognitive load. This is disorienting for engineers trained to find optimal solutions.
The organization that keeps a suboptimal system because "it works well enough" and
the political cost of migration is too high is not being irrational. It is satisficing
in a perfectly Simonian way.

Practical payoff: once engineers understand satisficing, they can work with it rather
than against it. Proposals that acknowledge the organizational switching cost will
outperform proposals that are technically superior but politically unworkable.

### Dunning-Kruger Adjacent: The Competence Inversion

Not Dunning-Kruger exactly, but related: the experience of being excellent at one thing
and discovering you're a beginner at an adjacent thing. Engineers who become tech leads
often experience a sudden, sharp drop in the feedback signal that told them they were
competent. The compiler told them when they were wrong. Tests told them when they broke
something. Now the feedback loop is months long and the signal is noisy. This is
disorienting in a way that needs to be named directly.

---

## 3. Concrete Scenarios

### Scenario A: The Technical Decision That Wasn't

A tech lead at a mid-size SaaS company spends three weeks on a detailed architectural
proposal — database design, migration path, scaling analysis. They're confident it's
correct. In the review meeting, the decision goes a different direction. Not because
anyone had a better technical argument. Because the VP sponsoring the alternative
approach had more organizational capital, and the migration timeline conflicted with
a sales commitment that the tech lead didn't know about. Nobody explained this in the
meeting. It was settled in conversations the tech lead wasn't in.

The tech lead walks out thinking the decision was wrong. Maybe it was. But they also
didn't understand what they were playing. They brought technical reasoning to a
negotiation that had already been partially conducted through other channels.

### Scenario B: The First Performance Review Surprise

An engineer is promoted to senior based on architectural output and delivery track record.
Eighteen months later, their first senior-level performance review comes back with
feedback they didn't expect: "needs to develop stronger cross-team relationships,"
"could do more to raise visibility of the team's work," "decisions sometimes bypass
stakeholders." None of these things were in the criteria they were promoted against.
Nobody told them the criteria had changed.

The engineer, reasonably, interprets this as the organization being inconsistent. In
one sense it is. But the inconsistency has a structure: the criteria for performing
well as a senior engineer are genuinely different from the criteria for being promoted
to senior engineer. The gap between them is what this book is about.

### Scenario C: The Good-Enough Wins

A team inherits a system with a well-understood architectural flaw. The correct fix is
obvious to anyone who looks at it closely. The team proposes a rewrite. The proposal
is technically unimpeachable. It gets deprioritized — not because anyone disagreed
with the diagnosis, but because the business unit that relies on the system is in the
middle of a product push, the VP doesn't want to touch working infrastructure during
a critical quarter, and the memory of a failed migration two years ago is still fresh.

The "obviously right" technical decision doesn't get made. Not because of bad
engineering judgment. Because of risk aversion, organizational memory, and timing. The
engineers on the team interpret this as the organization being broken. The right
interpretation is: the organization is making a locally rational decision given its
context, and the proposal didn't account for that context.

### Scenario D: Consensus That Isn't

A tech lead runs what they believe is a consensus-building process. They circulate a
design doc. They get async comments. Several people say "LGTM." The proposal is
ratified. Two sprints in, they discover that two of the engineers who said LGTM
actually had significant reservations — they didn't voice them because the culture
didn't feel safe for that, or because they assumed someone more senior would raise
them, or because they were optimistic about finding solutions later. The "consensus"
was performative. The tech lead never learned how to tell the difference.

### Scenario E: The Manager Who Absorbs Credit

A senior engineer does the foundational technical work on a project that becomes
successful. In the post-mortems, the retrospectives, and the promotion cycles, the
work is described in terms of decisions made at the management layer. This isn't
necessarily malicious — it's a feature of how organizational narrative works. Managers
present to managers; they summarize; the individual contributor's work becomes context
for the decision, not the decision itself. The engineer who doesn't understand this
mechanism will be mystified by promotion cycles. The one who understands it will manage
their visibility deliberately.

### Scenario F: The New Tech Lead Who Keeps Coding

An excellent individual contributor is promoted to tech lead. For the first six months,
they do exactly what they were doing before, but with a new title. They continue to
produce most of the significant code. They are proud of this — it's the evidence they
can "still do the job." Meanwhile, the things the team actually needs from a tech lead
are not getting done: nobody is managing the cross-team dependency that's creating risk,
the roadmap document is out of date, the two junior engineers on the team are floundering
without guidance, and the product manager doesn't know what's coming in the next quarter.
The tech lead is performing their old job excellently and their new job poorly, without
knowing the new job exists.

---

## 4. Counter-Arguments

### Counter-Argument 1: "This Is Just Management. Technical People Should Stay Technical."

The strongest objection: the cure is worse than the disease. If engineers have to learn
organizational politics to be effective, the solution is to keep technical people in
technical roles and let managers handle the organizational side. The organizational
layer exists precisely so that engineers don't have to deal with it.

**How to address it:** This objection misunderstands the claim. The book is not arguing
that engineers should become managers. It's arguing that engineers who want to have
significant technical influence above a certain level have to understand the environment
they're operating in. The most damaging technical decisions in most organizations are
made by engineers who didn't understand the organizational context, not by executives
ignoring technical input. The engineer who can translate between technical and
organizational logic is not doing management's job — they are doing theirs more
effectively.

Also: the "stay technical" opt-out is only available if someone else is managing the
organizational dynamics well. In most organizations, nobody is. The engineers who
avoid organizational understanding often end up on the receiving end of decisions they
don't understand and can't influence.

### Counter-Argument 2: "The Organizations Are Just Broken. Fix the Org, Don't Ask Engineers to Adapt."

A more sophisticated objection: this book is asking engineers to work around broken
organizational structures rather than fix them. The principal-agent problems, the
misaligned incentives, the political decision-making — these are real dysfunctions. The
right response is to reform organizations, not to train individuals to navigate the
pathology.

**How to address it:** True, and the book doesn't disagree that organizations are often
broken in these ways. But two things are simultaneously true: the organizations are
structurally broken, and engineers who understand the dysfunction are more effective
at changing it than engineers who don't. You cannot fix a system you don't understand.
The chapters on incentives, Conway's Law, and decision-making are all aimed at helping
engineers diagnose what's actually wrong — which is the precondition for changing it.
The goal is not learned helplessness. It's legibility as a precondition for leverage.

---

## 5. Data Points and Studies

- Studies of software project failure rates (Standish Group Chaos Reports, various
  years): consistently show that technical factors account for a minority of project
  failures. Organizational, communication, and requirements failures dominate. This
  data point is useful precisely because the audience finds it counterintuitive.

- Research on managerial derailment (Morgan McCall and Michael Lombardo, Center for
  Creative Leadership, 1983 and follow-on studies): high-performing individual
  contributors who fail after promotion overwhelmingly fail on interpersonal and
  organizational dimensions, not technical ones. The failure mode is remarkably
  consistent: people who succeeded in technical roles applied technical-style thinking
  to organizational problems.

- Organizational research on the "sycophancy trap" in team decision-making: teams
  where the most senior technical voice dominates produce worse decisions than teams
  where dissent is structurally enabled. Relevant to Scenario D above; also useful for
  establishing that the problem isn't unique to any one organization.

- Engineering education research: surveys of what CS curricula cover vs. what
  practitioners identify as the most important skills. The gap between "what school
  taught" and "what the job requires" in the organizational and communication domains
  is consistently cited as one of the largest single gaps in industry surveys.

---

## 6. Suggested Chapter Sections

### Section 1: The Moment It Stops Being Technical (Opening)

Scene-based opening. The experience of hitting the first problem that didn't have a
technical solution — a decision overridden, a proposal ignored, a piece of work
rendered irrelevant by something that happened in a room the engineer wasn't in. The
visceral experience of a rule change nobody announced. This section's job is to be
immediately recognizable. Every reader who has hit senior engineer or tech lead will
have a version of this moment.

### Section 2: What the Promotion Was Actually For

Unpack the promotion criteria discontinuity. The skills measured in a promotion to
senior or tech lead are necessarily backward-looking: they reflect what the person did
well as a junior or mid-level engineer. But the job that comes after the promotion is
measuring something different. This section names the mismatch directly and without
sympathy for the organization (it is a real failure) while being clear that the
mismatch is structural and predictable, not a personal betrayal.

### Section 3: The New Problems Don't Look Like Problems

The organizational problems that land on a senior engineer's desk often don't announce
themselves as problems at all. They look like technical decisions that happen to have
weird constraints. They look like stakeholder communication. They look like roadmap
uncertainty. This section is about developing the recognition that these are the actual
work — not the overhead before the actual work.

Reference Brooks: the managers in his stories didn't see the coordination overhead as
the problem. They saw the programming schedule as the problem. The overhead was
invisible until it was catastrophic.

### Section 4: The Skeptic's Turn — "Just Do the Technical Work"

Address the strongest objection directly. The "stay technical" instinct is not wrong —
technical excellence remains necessary. The argument here is that it's not sufficient,
and that pretending otherwise is not a defense of craft, it's an avoidance of
responsibility. The engineers with the most enduring technical influence in any
organization are almost never the ones who optimized purely for technical output.

### Section 5: What This Book Is (and What It Isn't)

Explicit orientation for the reader. Not a management book. Not an argument for
becoming a manager. Not a claim that organizational concerns should override technical
judgment. A claim that organizational forces are as real and as learnable as technical
ones — and that understanding them is part of doing the technical job at a high level.

Preview the book's structure briefly: incentives, organizational structure, decision-
making, communication, leadership. Not as soft skills, but as the engineering of human
systems.

### Section 6: What Changes Monday

Tight, direct, second-person close. The one immediate shift: start noticing when a
problem you're working on is organizational rather than technical, and stop trying to
solve it with technical tools. Name a specific type of situation (a proposal that isn't
gaining traction, a decision that went a direction you didn't expect) and suggest the
question to ask: what are the incentives and constraints of the people involved, and
do I understand them?

---

## Tone Notes for Draft

- The opening should be slightly rueful, not bitter. The experience this chapter
  describes is annoying but it's not a tragedy. The reader is smart enough to have
  noticed it; they just haven't had a framework for it.
- Avoid making the organization the villain. Organizations aren't breaking a contract
  with engineers — they just never made the contract explicit. The frustration is real;
  the frame of "betrayal" is not useful.
- The strongest move: acknowledge that the reader is already dealing with this. They
  didn't pick up a book called "Engineering Beyond Code" because everything was going
  smoothly. The chapter can assume the reader is already mid-experience, not being
  warned about something in their future.
- Historical parallels (Brooks, Dijkstra) should feel like recognizing something the
  reader already suspected, not like citations in a paper.
