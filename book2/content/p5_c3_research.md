# Research Notes: p5_c3 — What Staff Engineers Actually Do

## Core Argument

The staff engineer title is often treated as a prize for continued technical excellence
rather than as a role with distinct, learnable responsibilities. Engineers who reach it
expecting more of the same senior engineering work are confused and ineffective. The
confusion is not their fault — the role is poorly defined in most organizations and
almost never explicitly taught. This chapter makes the tacit explicit: staff engineering
is not senior engineering amplified. It is a categorically different job whose product
is direction, synthesis, and organizational clarity rather than working code.

---

## 1. Historical Parallels

### 1a. The Fellow track at large research laboratories (Bell Labs, IBM Research)

In the mid-twentieth century, large corporate research laboratories — particularly
those running hundreds of researchers across multiple disciplines — faced a structural
problem: their most technically productive people were terrible managers, and promoting
them into management wasted the thing they were actually good at while producing
mediocre leaders. The problem was recognized explicitly. By the 1960s and 1970s, the
largest of these laboratories had formalized dual-career tracks: a management ladder and
a technical ladder, with titles like "Fellow" or "Distinguished Engineer" reserved for
the most senior individual contributors.

These roles were not staff engineering in the modern software sense, but the structural
logic was identical. The Fellow was not doing the same work as a researcher, just at
higher volume. They were expected to: define research directions that would influence
the institution for decades, mentor and technically guide large clusters of junior
researchers, represent the organization's technical credibility externally, and serve
as the connective tissue across research groups that might otherwise develop in isolation.

The Fellow produced influence, not papers. A Fellow who spent their year writing
two dozen papers was considered to have possibly underperformed — the question was
whether the rest of the laboratory was doing better work because of them.

This is the origin of the modern staff/principal/fellow IC track in software — the
insight that the highest-leverage use of an excellent technical person is often not
to do more excellent technical work, but to raise the ceiling of what everyone around
them can do.

### 1b. Knuth and the influence model of technical leadership

Donald Knuth's career is the most legible case study of technical leadership through
depth rather than authority. He spent decades producing work — *The Art of Computer
Programming*, TeX, literate programming — that did not manage people, did not ship
products in the commercial sense, and did not depend on organizational position.
Yet his influence over how the field thinks about algorithms, typesetting, and program
verification exceeded that of executives running organizations orders of magnitude larger.

The model is not directly transferable — most engineers work inside organizations where
pure independent scholarship isn't the charter. But the mechanism is instructive: deep
technical work, made legible and available to others, accumulates influence through
trust and citation rather than authority and reporting lines. The staff engineer who
writes the architectural RFC that becomes the basis for a thousand decisions over three
years is operating on the same principle: the work's leverage comes from other people
building on it, not from any formal power.

The implication for staff engineers: depth of thinking, expressed clearly in writing,
is a multiplier. It doesn't require a title to exert influence — but it does require
the discipline to do the thinking rigorously and communicate it at a level others can
use.

### 1c. The transition from craftsman to master in pre-industrial guild systems

The medieval European guild distinguished between apprentice, journeyman, and master
not by the quality of their individual output but by the scope of their contribution
to the craft. The master was not the fastest worker or even necessarily the most
skilled at execution. The master's job was to define the standards of the guild,
train the next generation, take on the work that required the most judgment about
novel problems, and represent the craft in dealings with patrons and civic authorities.

The journeyman who remained a journeyman — producing excellent individual work
indefinitely — was valued. The master was a different role. The distinction is
useful for staff engineering: the question is not "are you skilled enough to be a
master?" but "are you doing master work?" Standards, training, judgment on novel
problems, external representation. Most senior engineers are excellent journeymen.
Few have made the transition to thinking about their work in those terms.

---

## 2. Key Frameworks

### The four staff archetypes

Research on how staff engineers actually spend their time (Larson's work, drawing on
surveys of hundreds of staff engineers) identifies four recurring patterns:

**The Tech Lead** is embedded in a team or cluster of teams and provides the ongoing
technical leadership for a specific product or domain. They write significant amounts
of code, are the default decision-maker on architecture within their scope, and
spend meaningful time mentoring the senior engineers around them. The closest to
senior engineering in form — but the scope of judgment extends beyond the immediate
codebase to the product and team strategy.

**The Architect** operates across multiple teams and is responsible for the coherence
of a technical domain across those teams. Less likely to be embedded in a single team.
Spends more time in cross-team design reviews, setting technical standards, and
managing the evolution of shared systems. The job is ensuring the pieces fit together
across an organization that doesn't naturally coordinate.

**The Solver** is deployed into hard, ambiguous technical problems that the organization
doesn't know how to approach. Often working alone or with a small group. The value
is in the depth of investigation and the clarity of the solution or recommendation
that comes out. Not primarily about multiplying others — about going deep where depth
is needed.

**The Right Hand** operates in close partnership with an executive (typically an
engineering VP or CTO) as a technical force multiplier for that leader's scope.
Often involved in org design, hiring strategy, and the hardest cross-cutting technical
decisions. The most management-adjacent of the archetypes without being management.

These archetypes are not mutually exclusive and most staff engineers blend them, but
the rough categorization is useful because it predicts where someone should spend their
time. A Tech Lead who is spending most of their time doing Architect work is probably
leaving their team under-led. A Solver who is being asked to do Right Hand work is
probably miserable.

### The scope model: depth, breadth, and impact horizon

Senior engineering operates at the team scope — your impact is your team's output.
Staff engineering operates at the organization scope — your impact is multiple teams'
output, often over a longer time horizon. Principal engineering operates at the
company scope, often with a 3-5 year impact horizon.

This is the cleanest diagnostic: what is the largest unit whose success is materially
affected by your work? If the honest answer is still your immediate team, you are
doing senior engineering at a staff title. If the answer is three teams, you are
doing staff work. If the answer is the whole engineering organization or the company's
technical trajectory, you are doing principal-level work.

The corollary: the scope model explains why writing code does not disqualify staff
work, but purely individual code contribution is usually inconsistent with it.
Code can be staff-level work if it is architecting something that will be built on
by many teams, or demonstrating a technical direction that others will follow.
Code is not staff-level work if it is just shipping features within the scope of
one team.

### The glue work problem

Tanya Reilly's observation about "glue work" is essential here. Glue work is the
category of work that is necessary for teams to function — clarifying requirements,
writing documentation, running design reviews, onboarding new engineers, managing
cross-team dependencies, synthesizing information across silos — but that is invisible
in most performance evaluation systems because it doesn't ship code.

The glue work problem intersects staff engineering in two ways. First, a significant
portion of staff engineering *is* glue work at organizational scale: writing the ADR
that prevents five teams from making divergent choices, doing the cross-team alignment
that would otherwise take six months of confusion, synthesizing the incident postmortem
into a coherent technical risk picture. If these are not explicitly recognized as
high-value work, staff engineers doing them will not be recognized for it.

Second, the glue work dynamic is a trap for people *trying* to grow to staff level.
Senior engineers can accumulate enormous amounts of organizational glue work — much of
it genuinely valuable — without developing the technical depth and direction-setting
capability that distinguishes staff engineering. The observation is that glue work
without technical substance is often rewarded with gratitude and informally, but not
with a staff title or the organizational authority that comes with it.

---

## 3. Concrete Scenarios

### 3a. The canonical staff week

A staff engineer's week at a mid-size technology organization might look like:
Monday: a two-hour cross-team architectural review where three teams are making
decisions about a shared data model; the staff engineer has read all three proposals
in advance, synthesizes the conflicts, and helps the three teams converge on an
approach none of them had proposed individually. Tuesday: three design document
reviews — one thorough written review of a significant proposed service decomposition,
one quick async comment on a smaller change, one thirty-minute conversation with a
senior engineer whose proposal needs to be substantially rethought before it goes
broader. Wednesday: a half-day deep investigation into an incident that exposed
a latent architectural flaw — not running the incident response, but doing the
technical analysis that determines whether the flaw is local or systemic and what
class of remediation is warranted. Thursday: a product roadmap meeting where the
staff engineer is the technical voice helping the product team understand what
is feasible in what timeframe and what dependencies will be created by different
sequencing choices. Friday: writing — finishing the investigation writeup, sketching
an RFC on the architectural direction suggested by the incident, and a weekly
technical context email to the engineering leadership team.

Note what is not in this week: writing production code. Note what is hard to
measure: almost all of it.

### 3b. The senior engineer mistaking staff work for more senior engineering

An engineer promoted to staff level continues doing what made them a great senior
engineer: deep individual technical work, high-quality code, careful architecture
within their team's scope. A year later, they are technically excellent and are
producing good output. They are not operating at the staff level.

The diagnosis: they have not shifted the scope of their investment. Their impact is
still primarily felt by their immediate team. The cross-team design reviews go poorly
when they attend because they are thinking about the problem from their team's
perspective rather than from the organization's perspective. They have not developed
the practice of synthesizing technical context across teams — they are still
optimizing their own work.

This is not a failure of capability. It is a failure of model. The engineer knows
how to do excellent senior engineering. They have not been told — clearly and
concretely — that the job has changed.

### 3c. The staff engineer who operates primarily through other engineers

A staff engineer at a large organization has not made a significant individual
technical contribution to the codebase in eight months. What they have done: helped
three senior engineers work through a re-architecture of a critical shared library,
each of whom produced better work for the engagement. Caught a systemic security
assumption embedded in the way five teams were handling a particular class of request
— not by auditing the code themselves, but by recognizing the pattern in three
separate design docs and connecting the dots. Written a technical strategy document
that clarified the organization's approach to a category of infrastructure decisions
for two years, eliminating a class of recurring debates.

The resulting output is enormous, and none of it has their name on the commit.
The question of whether this person is being evaluated correctly by a system that
tracks code contribution is a separate and important one — but the point is that
this is recognizably and legitimately staff-level work.

### 3d. The staff engineer as the organization's institutional memory

An organization loses three senior engineers in a six-month period. The staff engineer
becomes, effectively, the repository of context that would otherwise be lost: why
the authentication system is the way it is, what the failure mode is of the design
choice made two years ago, which of the current architectural debts were accepted
knowingly and which accumulated by accident.

This is valuable, but it is also a trap. An organization that relies on a single
staff engineer as its institutional memory has not built the systems (documentation,
architectural decision records, design reviews with written summaries) that would
distribute that knowledge. The staff engineer who accepts this role uncritically
has made themselves a bottleneck rather than a multiplier. The correct response is
to use that context to build better systems for capturing and distributing it.

### 3e. The staff engineer who cannot get out of the weeds

A staff engineer is technically brilliant and highly trusted, but every major
decision ends up at their desk because they are the person most likely to have
the right answer. They are always in the critical path. They work long hours.
The teams around them are not growing because the staff engineer keeps solving the
problems the teams should be developing the capacity to solve themselves.

This is a common failure mode for technically excellent engineers at the staff level.
The instinct is to help — and they are helping, in the immediate transaction. But
the behavior has a hidden cost: it is not transferring capability, so it does not
compound. The same questions come back next month. The staff engineer's leverage
stays constant rather than growing.

The shift required: from "I can solve this problem" to "how do I make it so this
class of problem gets solved without me?" This requires deliberately building the
capacity of the senior engineers around them — which is slower in the short term and
higher leverage in the long term.

### 3f. The staff engineer who loses technical credibility

A staff engineer who has been primarily doing coordination, mentoring, and
organizational work for two years is asked to weigh in on a significant architectural
decision. Their read of the problem is two years out of date. They make a strong
recommendation. The senior engineers who have been living with the system push back.
The staff engineer holds the position based on experience. The decision made is
suboptimal.

Technical credibility at the staff level requires enough continued technical
engagement to maintain current, accurate intuitions about the systems the organization
is building. This does not mean writing significant amounts of code — it means doing
enough hands-on work and close technical engagement to stay calibrated. The exact
form varies by archetype: a Solver must stay deeply technical; an Architect can
maintain credibility through close design review; a Right Hand can operate somewhat
further from the technical frontier. But all of them require some minimum technical
engagement to stay credible.

---

## 4. Counter-Arguments

### 4a. "Staff engineer is a made-up title with no consistent meaning"

This objection is factually correct and structurally irrelevant. The title is
inconsistent across organizations. At some companies it is one level above senior
and common. At others it is a rare designation for the technically elite. At some
places it comes with organizational authority; at others it is purely peer influence.
"Staff engineer" does not reliably describe a consistent job.

But the underlying role exists regardless of what it is called, and this is the
substantive response. Every organization of sufficient scale has a need for people
who operate at a scope larger than a single team, maintain technical credibility,
set direction across teams, and manage the technical coherence of the organization.
In some places, this person is called a staff engineer. In others, they are called
a principal engineer, an architect, or a senior engineer with unusual scope.
The title is not the thing — the thing is the thing.

The chapter is not about how to get the title. It is about what the role requires
and how to do it well. Engineers who spend energy on the title question rather than
the role question are optimizing for the map rather than the territory.

### 4b. "Staff engineers just do politics and don't build anything"

This objection is the bitterness version of the previous one, and it points at a
real failure mode rather than a false premise. There are staff engineers who have
effectively stopped doing technical work and are primarily doing organizational
navigation. They are influential but technically stale. They speak with authority
they no longer have the technical depth to back up. They produce process and
meetings rather than clarity and direction.

This is a real failure mode, not a definition. The response is to name it as such:
a staff engineer who has lost technical credibility is not doing the job. The
solution is not to conclude that the role is pointless — it is to understand what
makes the role valuable (technical synthesis, credible direction-setting, multiplying
others) and recognize that the political version is a degraded form that no longer
delivers the value.

The corrective is also practical: the engineers making this critique usually have
a specific person in mind. The question is whether that person's technical judgment
is actually worse than the people around them, or whether it is just different in
form (high-level synthesis vs. implementation detail). Both are possible. The
diagnostic is whether acting on their technical guidance produces better or worse
technical outcomes.

---

## 5. Data Points and Studies

- Staff engineer surveys (e.g., Teal Unicorn's and similar) consistently find that
  the distribution of time at the staff level skews heavily toward communication,
  review, and coordination relative to senior engineers — typically 50–70% of
  reported time versus under 30% for senior engineers. The gap is often invisible
  to the people managing staff engineers because the outputs are not in a tracking
  system.

- Research on expertise transfer in organizations finds that tacit knowledge (the
  kind of knowledge that cannot be easily written down) is most effectively transferred
  through close working relationships over extended periods. This is the empirical
  basis for the "mentorship" function of staff engineering — it is not just nice
  to have, it is the primary mechanism by which hard-won technical judgment propagates
  through an organization.

- Studies on the effectiveness of technical review processes in large organizations
  find that design reviews conducted by engineers with cross-team context catch
  significantly more systemic issues than reviews conducted by engineers with only
  local context. This is the quantifiable version of the "staff engineer synthesizes
  context across initiatives" claim.

- Research on the "glue work" problem (Reilly, and subsequent empirical work by others)
  finds that the category of work is disproportionately performed by women and
  engineers from underrepresented groups, and is systematically undervalued in
  performance systems. This is not primarily a social justice argument in this
  context — it is evidence that the work category is real, widespread, and
  systematically underaccounted for, which is directly relevant to how staff engineers
  should think about making their work legible.

- Work on the "scope creep" failure mode in senior IC roles finds that the most common
  failure of engineers newly promoted to staff level is not technical inadequacy but
  insufficient scope shift — continuing to operate at the senior engineer level while
  holding a staff title. The estimate from multiple practitioner accounts is that this
  describes the majority of newly-promoted staff engineers in the first 6–12 months,
  with a substantial fraction never fully making the transition.

---

## 6. Suggested Chapter Sections

1. **The Job Changed When You Weren't Looking** — Open with the engineer who earned
   the staff title through excellent senior engineering and spends the first year
   doing excellent senior engineering, confused about why the promotion doesn't feel
   different. Frame the transition: staff is not senior amplified. It is a different
   job with a different scope, a different product, and different success criteria.

2. **What the Role Actually Is** — Walk through the four archetypes as a diagnostic
   tool, not a taxonomy. The key question: which description of the week resonates
   with the kind of work your organization actually needs from you? Then introduce the
   scope model: what is the largest unit whose success is materially affected by your
   work? If the honest answer is still your team, the scope isn't there yet.

3. **The Work That Doesn't Show Up in the Commit Log** — The glue work section.
   Name the specific categories of high-leverage staff work that are invisible in
   standard engineering metrics: synthesis across initiatives, pre-alignment
   conversations that prevent month-long debates, design reviews that catch systemic
   issues, written direction that eliminates a recurring decision. Address the
   corollary: if you are doing a lot of glue work without technical direction-setting,
   you are not yet at the staff level — you are a highly effective organizational
   contributor, which is valuable but different.

4. **Staying Technical Without Getting Stuck in the Code** — Address the credibility
   problem directly. How much technical engagement does a staff engineer actually need?
   The answer varies by archetype but the floor is real. The failure modes in both
   directions: the staff engineer who codes too much and starves the organizational
   work; the staff engineer who codes too little and loses the technical credibility
   that makes their organizational work valuable.

5. **The Skeptic's Turn: When "Staff Engineer" Is Just a Senior Engineer With Delusions**
   — Address the legitimate failure mode: the staff engineer who has stopped doing
   technical work, produces process and meetings, and coasts on a title. Name this
   as a real failure, not a description of the role. Give the diagnostic: is your
   technical judgment still current and accurate? Are teams producing better outcomes
   because of your engagement? Is there work that could only have happened with you
   involved? If the honest answer to all three is no, the objection is correct about
   you specifically.

6. **What Changes Monday** — Concrete, second-person. For the senior engineer who
   wants to grow toward this: what to start doing (scope your thinking beyond your
   team's immediate work, practice written synthesis of technical context, ask to
   be included in cross-team design reviews). For the newly-promoted staff engineer
   who hasn't made the transition: the one thing to stop doing (treating the title
   as a reward for continuing to do senior engineering). For the established staff
   engineer: the audit question — over the last month, what work happened only
   because you existed, and what would have happened anyway?
