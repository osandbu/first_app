# Research Notes: p5_c4 — The First Ninety Days as a Manager

## Core Argument

The transition from engineer to engineering manager is not a promotion — it is a career
change that happens to share a title with the previous job. The skills that made you
excellent as an engineer (technical depth, individual execution, debugging acuity) do
not transfer. The new job has almost entirely different success criteria. Most new
managers fail, or limp along for years, because nobody tells them this plainly enough
at the moment they take the role.

The central mental model shift: your output is your team's output. Not your code. Not
your architecture. The pull to keep doing what you were good at is strong, rational, and
almost exactly wrong.

---

## Historical Parallels

### 1. Andy Grove at Intel — From Engineer to Manager

Andy Grove trained as a chemical engineer, did his PhD work on fluid dynamics in
semiconductor fabrication, and became Intel's third employee as a technical operator.
The management philosophy he developed — crystallized in *High Output Management* (1983)
— came from working through the actual problem of what changes when you shift from
producing output yourself to producing it through others.

Grove's key insight, stated plainly: a manager's output is the output of the
organizations under their supervision. This seems obvious when stated. It is not obvious
to live. The new manager who is debugging a hard problem because it's interesting, or
writing the architecture because they know it better than anyone, is not being wrong —
they are being a good engineer. But they are failing as a manager. Their individual
output may be high. Their team's output is lower because of their absence from the work
only managers can do.

Grove identified the specific failure mode: the "individual contributor trap," where a
manager produces high personal output while leaving the team's leverage on the table.
The manager is busy and feels productive. The team is less productive than it would be
with a manager who was doing the actual manager job.

Grove's practical tool: manager leverage. Each activity a manager undertakes affects
the output of their team by some multiplier. A one-on-one that unblocks an engineer for
a week has different leverage than writing a feature yourself. Orienting your work around
leverage — not around what you're good at — is the fundamental shift.

### 2. The Player-Coach Problem in Sports

The player-coach is one of the oldest management dilemmas in organized sport. A team's
best player is promoted to player-coach: they continue playing while also managing the
team. The results are almost uniformly bad, and the pattern is well-documented across
professional sports from the 1950s through the present.

The failure mode is structural, not individual. The player-coach:
- Cannot fully evaluate the team from inside it (they are a participant, not an observer)
- Prioritizes their own performance under competitive pressure (which is what they trained
  for) over managing others
- Creates awkward dynamics when the best player is also the evaluator of other players
- Cannot be in two places at once: the critical play and the strategic timeout

The parallel to engineering management is near-perfect. The engineering manager who
stays heavily in the code:
- Cannot observe the team's dynamics while inside them
- Defaults to their own execution under deadline pressure
- Creates uncomfortable ambiguity about code ownership and technical authority
- Cannot be in two places at once: unblocking an engineer and writing the feature

In professional sports, the player-coach largely disappeared from major leagues by the
1980s as the specialization of coaching became recognized. The work of managing a team
became too demanding to be done part-time while playing. Engineering management is
reaching a similar inflection point, with a lag of several decades.

The player-coach parallel resonates with an engineering audience because it strips away
the ideological loading of "manager vs. engineer." No one disputes that Wayne Gretzky
shouldn't also be coaching. The structural logic is clear in sports. It's the same
structural logic in engineering.

### 3. Hewlett and Packard — The Management by Walking Around Philosophy

Bill Hewlett and Dave Packard built a management philosophy that, while not named as
such at the time, anticipated many of the practices now considered foundational to
engineering management. Packard's autobiography *The HP Way* (1995) describes the
principle they called "management by walking around" (MWBA): managers should spend
significant time in direct, informal contact with the people doing the work.

The insight was not sentimental. It was informational. The manager who stays in their
office — or, in the modern engineering context, who stays at their keyboard — is
operating from incomplete information. They know what gets escalated. They don't know
what doesn't get escalated, which is often more important.

Packard's specific observation: decisions that look obvious from an executive's
perspective are often deeply uninformed about what is actually happening in the work.
The gap between what a manager thinks their team is experiencing and what the team is
actually experiencing is typically large and systematically biased toward good news.

For a new engineering manager, this historical parallel provides grounding for
why one-on-ones, informal check-ins, and direct observation of team dynamics are not
soft-skills niceties — they are information collection. They are how you find out what
is actually happening in your organization before it becomes a crisis.

The HP tradition also introduced something relevant to the first ninety days specifically:
the idea that a new manager's first job is to understand the team before trying to
change it. Hewlett and Packard were unusually consistent in their early years about
asking questions rather than arriving with answers. This was a strategic posture, not
a management style preference.

---

## Key Frameworks

### Andy Grove's Manager Leverage

From *High Output Management*: a manager's output = the sum of the output of their
organization. Manager activities vary in their leverage — the ratio of team output
produced to manager time invested. High-leverage activities: setting clear goals,
running effective one-on-ones, making decisions that unblock multiple people, training
an engineer in a skill they'll use repeatedly. Low-leverage activities: doing the work
yourself, attending meetings where your presence has no decision impact.

The new manager's error: confusing high personal activity with high leverage. Writing
code feels productive. It may have negative leverage — consuming time better spent on
high-leverage management activities, and reducing ownership and autonomy for the
engineers who should be doing it.

### Manager's Schedule vs. Maker's Schedule (Paul Graham)

Paul Graham's 2009 essay distinguishes two fundamentally different time structures.
The maker's schedule: large uninterrupted blocks of time, because the cost of a context
switch is an hour of recovery and setup. The manager's schedule: one-hour chunks, because
a meeting at 2pm is not disruptive in the same way — meetings are the work, not an
interruption to it.

The new engineering manager faces a transition between these two schedules. Their
previous identity was entirely on the maker's schedule — and with good reason, because
deep work produces engineering output. The new job is on the manager's schedule. This
is not a degradation; it is a restructuring of what "productive" means.

The mistake: trying to hold both schedules simultaneously. Blocking deep-work mornings
to write code, then attending afternoon meetings, then feeling fragmentary and
ineffective in both modes. The manager's schedule requires accepting the loss of the
maker's schedule, which is psychologically costly and often unaddressed.

### The Structure and Purpose of One-on-Ones

The weekly one-on-one is the most important recurring activity of an engineering manager.
Not a status update (that information can come in other forms). Not a performance
conversation (that's a specific event, not weekly). The one-on-one serves several
functions simultaneously:

- **Information gathering**: What is actually happening in this engineer's work? What
  is blocked? What is frustrating? What is exciting? This is the most reliable source
  of ground-truth information about the team.
- **Relationship investment**: Trust is built through regular, consistent attention. An
  engineer who trusts their manager escalates early and honestly. One who doesn't will
  manage their manager, filtering bad news upward.
- **Career development context**: What does this person want? What are they working
  toward? What feedback do they need? This can't be stored in quarterly reviews — it
  requires ongoing attention.

Research on one-on-one effectiveness (from studies of management practices in engineering
organizations, notably documented in the work of Camille Fournier and others building
on Drucker) consistently finds that the most common one-on-one failure mode is not
doing them at all during busy periods. This is precisely backwards: one-on-ones are most
valuable when the team is under stress, which is when they're most likely to be canceled.

The cadence: weekly for direct reports, particularly in the first ninety days. Bi-weekly
once patterns are established is acceptable, but monthly is insufficient for a healthy
management relationship.

### Skip-Level Meetings

A skip-level meeting is a meeting between a manager and the direct reports of their
direct reports. The purpose is calibration: the manager hears directly from the people
doing the work, without the filtering of an intermediate layer. It is not designed to
undermine the direct report — it is designed to give the manager signal about whether
their picture of the team's experience matches the ground-level reality.

For a new manager, skip-levels in the first ninety days are primarily listening tools.
They are not appropriate for the first few weeks (too disruptive before the manager
has established credibility with their direct reports), but in weeks six through twelve
they provide invaluable calibration.

### Organizational Debt Inherited by New Managers

A new manager inherits the organizational debt of their predecessor and the team's
history. This includes: unresolved interpersonal tensions, implicit understandings about
who owns what, compensation inequities that have calcified over years, technical
commitments made to other teams that nobody has documented, engineers who have been
building toward departures that haven't happened yet.

The new manager who assumes they're starting fresh is already behind. Organizational
debt must be surfaced and acknowledged before it can be addressed. The first ninety days
are the best window to do this: the "new manager" frame gives permission to ask questions
that would seem naïve later. "I'm still learning the context" is a legitimate and useful
opening for three months. After that, the organizational debt becomes the new manager's
debt.

---

## Concrete Scenarios

### Scenario 1: The Engineer Who Keeps Engineering

A new engineering manager spends the first six weeks doing what they're good at: writing
code. They're the strongest technical person on the team. The codebase needs help. They
feel productive. Their team makes decisions without them — because they're not available
to be consulted, and because the engineers correctly conclude that the manager's
bandwidth is occupied. By week eight, the team has made two significant architectural
decisions that the manager would have redirected. Correcting them now requires undoing
work and addressing the implicit message that the decisions were wrong. The manager
discovers that staying in the code was not neutral — it was actively disruptive to the
team's decision-making coherence.

### Scenario 2: The Blocked Engineer Who Never Escalated

A manager doing their monthly review of team velocity discovers that one engineer has
been blocked on an external dependency for three weeks. The dependency is held by
another team. No escalation has happened. The engineer didn't escalate because: the
previous manager handled these situations without being asked, the engineer didn't want
to look incapable, the team culture didn't reward escalation, and the new manager had
not yet established that they wanted to know about blocks. Three weeks of an engineer's
time lost, and a cross-team relationship that has quietly degraded. The lesson is not
that the engineer failed to escalate — it is that the manager had not yet done the work
to establish the conditions for escalation to happen.

### Scenario 3: The First One-on-One Reveals Everything

A new manager's first round of one-on-ones, done properly — mostly listening, few
directives — surfaces within three weeks: one engineer is interviewing elsewhere, one
has been frustrated with a specific recurring process for eighteen months and has never
said so officially, one is blocked on a career level decision they've been waiting two
years for, and one has been doing the work of a staff engineer without the title. None
of this was in any handoff document from the previous manager. All of it is load-bearing
context. The manager who skips or shortchanges this initial listening period begins
managing a team they do not actually understand.

### Scenario 4: The Manager Who Tries to Fix Everything in Month One

A new manager arrives with high energy and a clear diagnosis: the team is slow because
the process is bad. In the first month, they restructure the sprint cadence, change the
on-call rotation, introduce a new approach to code review, and start a weekly
architecture session. Each individual change is reasonable. The aggregate effect is
organizational whiplash: the team's cognitive bandwidth is consumed by adapting to new
processes instead of delivering. Two good engineers, who were already close to leaving,
now have a concrete new reason. The manager conflated "having legitimate opinions" with
"being effective immediately." The first ninety days are primarily for listening and
targeted intervention, not comprehensive reform.

### Scenario 5: The Technical Credibility Trap

A manager who used to be the team's strongest engineer stops writing code as advised.
In code review, they hold back. In architecture discussions, they defer more than they
should. The team notices. Some interpret it as lack of engagement. Some start ignoring
technical guidance that is actually sound, because the manager has withdrawn from
technical participation. The manager overcorrected. The right balance is not zero
technical participation — it is participating in the mode of a senior technical voice,
not as an individual contributor. The distinction is ownership: a manager can give
strong technical opinions in architecture discussions without owning the implementation.

### Scenario 6: The Team Mapping Session

In their third week, a new manager spends two sessions mapping the team's context:
who works with whom, what projects are active, what cross-team dependencies exist, what
technical risks are known. They discover that three of their six engineers do their most
important collaboration with members of a different team — the org chart implied two
parallel independent teams; the actual working structure is one integrated group
with an administrative boundary through the middle. This changes every decision the
manager was about to make about team process, on-call, and project assignment.

---

## Counter-Arguments

### Counter-argument 1: "A Manager Who Can't Code Loses Technical Credibility"

This is a real concern, not a straw man. Engineers are pattern-matching constantly on
whether their manager understands the work. A manager who hasn't written production code
in two years, who can't read a diff, who misestimates complexity consistently — that
manager loses credibility in ways that permanently impair their effectiveness. The
team filters information up to them differently. They stop being consulted on technical
decisions. They become a bureaucratic layer rather than a contributing voice.

The response: this is a legitimate risk that must be managed, not dismissed. The
resolution is not "keep writing the code." It is: maintain enough technical engagement
to stay legible to engineers — reading code, participating meaningfully in architecture
discussions, understanding the technical complexity of what the team is doing — without
taking on individual contribution ownership. The manager who attends design reviews and
asks good questions is different from the manager who books out their mornings to write
features. Both are engaged technically. Only one is doing the manager job.

The specific calibration: in the first ninety days, the new manager should probably be
pair-reviewing code, asking questions in architecture discussions, and spending a small
amount of time on clearly bounded technical tasks if that helps maintain credibility.
But the arc should be toward less individual contribution, not maintenance of the old
pattern.

### Counter-argument 2: "Most Management Advice Is for Large Companies — Small Teams Are Different"

On a team of three, the manager probably should be writing code. On a team of five
in an early-stage organization with no process and everyone shipping, rigid separation
of manager and individual contributor may be a luxury. The Paul Graham essay on "maker's
schedule vs. manager's schedule" was written for a context with enough organizational
structure to support specialization. Early-stage teams often don't have that structure.

The response: this is true, and should be stated explicitly in the chapter. The
player-coach model is not always wrong — it is wrong as a permanent state for most
medium-to-large teams. For small teams, the practical calibration is different. A
manager of three may write code regularly and manage well. A manager of eight who spends
their time writing code is almost certainly failing at the management job. The chapter
is primarily addressed to the latter case.

The more fundamental point: even on small teams, the mental model shift matters. The
manager of three who understands that their job is to make the team productive —
not to be the most productive engineer themselves — will make different decisions about
what to work on than the manager who hasn't made that shift. The model applies at any
scale; the practice scales with team size.

---

## Data Points and Studies

- Studies of new manager transitions consistently identify the first year as the highest-
  risk period for management failure. Research across large engineering organizations
  finds that first-time managers who receive no structured support (formal onboarding,
  mentorship, or management training) fail at rates estimated between 40–60% within the
  first two years. "Failure" here means either performing poorly by organizational
  metrics, or reverting to individual contributor behavior and being moved back.

- Gallup's long-running research on employee engagement identifies management quality
  as the primary variable in team engagement — more predictive than compensation, work
  content, or work environment. The mechanism: team members' experience of their manager
  in one-on-ones and day-to-day interactions is the dominant factor in whether they
  feel informed, valued, and unblocked. This places outsized weight on exactly the
  activities new managers most often skip (the one-on-one, the informal check-in) when
  under pressure.

- Research by Linda Hill (Harvard Business School) on first-time managers, documented
  in *Becoming a Manager* (1992), found that new managers underestimate in advance and
  discover in practice that: (a) the interpersonal and emotional demands of management
  far exceed what they expected, (b) the loss of individual contributor identity is
  genuinely painful and underacknowledged, and (c) the learning curve is longer than
  most new managers or their organizations assume. The average new manager in Hill's
  study took 12–18 months to feel genuinely competent in the role.

- Studies of one-on-one effectiveness in engineering organizations (informed by Drucker's
  foundational work and developed in engineering-specific contexts by Fournier, Larson,
  and others) find that inconsistent one-on-ones — especially the pattern of canceling
  them during periods of high delivery pressure — are strongly correlated with team
  attrition. Engineers interpret canceled one-on-ones as signal about how the manager
  values the relationship, regardless of stated reasons.

- Research on the "player-coach" problem in professional services (consulting, law,
  medicine) finds that the highest performers in individual contributor roles show the
  worst transition outcomes when promoted to management, in part because their identity
  investment in individual performance is highest. The engineer who was the best individual
  contributor is, counterintuitively, at elevated risk as a new manager — not because
  of any deficiency, but because the identity gap is larger.

---

## Suggested Chapter Sections

**Section 1: The Career Change Nobody Announces**
Open with the experience of the first week: the new manager sitting at their keyboard,
the pull to open their editor, the unfamiliar discomfort of a calendar full of meetings.
State the core argument plainly: this is not a promotion. The job has changed. The skills
that earned the promotion are insufficient and occasionally counterproductive in the new
role. Introduce the player-coach parallel to frame the structural problem.

**Section 2: The First Week — Listen Before You Fix**
Practical guidance for days one through seven. The first round of one-on-ones is primarily
a listening exercise. Map the team's actual working relationships (not the org chart).
Learn what is in flight, what is blocked, what dependencies exist with other teams.
Identify the organizational debt you've inherited. Resist the urge to make any changes
except those that are clearly urgent. HP's management-by-walking-around philosophy as
grounding: you cannot understand what you have not yet observed.

**Section 3: The First Month — Establish the Operating System**
Weeks two through four. Set the one-on-one cadence and run them consistently, even as
things get busy. Understand what each person on your team needs to do their best work —
this varies by engineer and cannot be assumed. Establish clarity on how decisions get
made and how the team communicates. Identify the one or two highest-leverage process
changes and make those only. Grove's leverage framework: orient activities by impact on
team output, not personal output.

**Section 4: The Mental Model Shift**
This section addresses the psychological core of the transition. The pull to keep writing
code is not weakness — it is rational. You were rewarded for it. You are good at it. It
produces visible, measurable output. The manager's output is indirect, delayed, and often
invisible. An engineer you unblocked ships the feature; you do not see yourself in the
git log. Address the identity loss directly. This is real and it takes time. The engineers
who make this transition well are usually the ones who allow themselves to acknowledge it.
Paul Graham's maker's/manager's schedule distinction here.

**Section 5: The Skeptic's Turn — You Need to Stay Technical**
Address the credibility argument directly. The resolution is not zero technical
participation — it is a different mode of technical participation. Define what staying
technical means when you are a manager: reading code, maintaining genuine technical
judgment, being a useful voice in architecture discussions. Define what it does not mean:
owning implementation, booking your mornings for deep coding work, being the fallback for
hard technical problems your team should be solving. The player-coach who watches game
film and runs practice is different from the player-coach who plays every shift.

**Section 6: The First Quarter — Calibrate and Commit**
Months two and three. By now, one-on-ones have surfaced real information. You know who
is considering leaving. You know where the organizational debt is. You know what
process changes are actually needed vs. what you were tempted to change in week one.
Run your first skip-levels. Have a direct conversation with your manager about how things
are going. Begin to make deliberate choices about where to invest management attention
based on leverage rather than urgency. This section closes with "What Changes Monday":
stop writing the code, start making the one-on-one the non-negotiable. The longer-term
shift: measure yourself by your team's output, not your own.
