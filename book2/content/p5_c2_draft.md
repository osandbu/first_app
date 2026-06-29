# The Multiplier Effect

---

You have been, on every team you have joined, one of the best engineers in the room.
This is not vanity — it is just the record. The architecture proposals that unblocked
the team. The debugging sessions that found the problem in an hour that had been
eluding others for a week. The code review comments that caught the failure mode nobody
else saw. These are things you did, with your hands, and they mattered.

Now you are senior. And increasingly you are in meetings, reviewing designs, answering
questions in chat, and explaining things you have already explained. You finish the week
and look at what you produced. A few review comments. A design doc nobody asked you to
write, because someone needed to write it. A conversation that seemed to help. Half a
proposal for something you did not finish.

The feeling is difficult to name exactly, but it is something like: *I am not doing
enough.* You were built for output. Output is legible. Output is the thing that makes
you certain you are still a real engineer and not just someone in the way of actual
engineers doing actual work.

Here is the problem with that feeling: it is measuring the wrong thing.

The most significant transition in an engineering career is not from junior to mid-level,
or from mid-level to senior. It is the transition from producing output to producing
outcomes through other people. These look different. They feel different. They require
you to unlearn most of what made you good at the earlier version of the job.

This chapter is about what the new job actually is, why it is worth doing, and what it
looks like in practice to do it well.

---

## What the Job Actually Is

Let us start with an economic argument, because economic arguments cut through the
discomfort of sounding like you're giving up technical work.

Two engineers. Both excellent. One of them writes good code, ships features, and
produces output directly. The other spends a significant portion of her time in
design reviews, writing guides, giving thoughtful feedback, and explaining her reasoning
rather than just stating her conclusions. At the end of the quarter, the first engineer
has shipped more than the second by any direct measure.

Now zoom out. The second engineer's team has converged on a consistent design vocabulary.
Fewer integration errors. Better first drafts coming into review. Engineers who six months
ago needed her to evaluate every significant design decision are now making those
decisions themselves and arriving at the right answer. Her personal output has been
modest. Her outcome has been substantial.

One engineer whose clarity unblocks three others is worth more to the organization than
two engineers writing excellent code in parallel. This is not philosophy — it is
arithmetic. The question is whether the thing she is producing is legible as a thing.
Usually it is not, which is why the transition is hard.

The framing that helps: the difference between a force multiplier and a force addend.

The term comes from military strategy, where a force multiplier is something that scales
the effectiveness of a force beyond its headcount — better intelligence, better
communications, the capability that makes every other capability work better. A force
addend just makes the number larger. Another rifle is a force addend. Artillery support
is a force multiplier.

In engineering organizations, both matter. But they are not the same, and conflating
them is the source of most of the confusion about what senior engineers should actually
be doing.

A force addend does something useful. It adds to the total. Without it, you have less.
A force multiplier changes the coefficient. It does not just add — it scales. The effort
is bounded; the effect is not.

The test is this: if you were not on this team, would they make the same decision? If
yes, your presence was addition. The output exists without you. If no — not because
they lacked the raw capability, but because your clarity shaped how they reasoned about
the problem — that is multiplication. You did not just add an answer. You installed a
framework.

This distinction matters because the activities that produce multiplication look
different from the activities that produce addition. And if you are optimizing for
output — for the legible, countable artifact — you will almost certainly default to
addition. It is faster. It is more satisfying. It is measurable. And it compounds
nothing.

---

## The History of Leverage

This is not a new problem. The engineers who produced the most lasting work in the
history of computing were, almost without exception, practitioners of the multiplier.

Ken Thompson and Dennis Ritchie worked at Bell Labs through the late 1960s and into
the 1970s with a team of roughly six to eight people. What they produced — Unix — became
the substrate on which the next half century of computing was built. The leverage was
obviously in the technology itself: a system so well-conceived, so composable, so
committed to doing one thing well that it could be extended indefinitely without
collapsing under its own weight.

But the leverage operated at the interpersonal level before it operated at the
technological one. Other researchers at the Labs worked adjacent to Thompson and Ritchie
constantly. They absorbed the mental model. They internalized the design philosophy.
The Unix way of thinking about interfaces, composition, and scope was transmitted through
direct technical mentorship as much as through any formal documentation. Thompson spent
real time helping people understand the system. That time paid back exponentially. Two
engineers did not just produce a product. They created a design vocabulary that other
engineers adopted, and in adopting it, became more productive.

Grace Hopper's contribution is an even starker example. Before compilers, programming
meant assembling machine instructions by hand. The cognitive load was immense. The
expertise required was narrow, hard to acquire, and nearly impossible to transfer.
Hopper's work on early compilers — particularly her insistence that programming languages
could and should be closer to natural language — was leverage at civilizational scale.
One person's careful abstraction enabled thousands, eventually millions, of subsequent
programmers to be effective without needing the low-level expertise she possessed.

The insight in Hopper's case is that she did not choose between producing technical
work and enabling others. She understood that at sufficient scale, these collapse into
the same question. The compiler was not a departure from serious engineering. It was
serious engineering whose output happened to multiply the effectiveness of everyone who
came after her.

Bell Labs at its peak was one of the most productive research institutions in history —
the transistor, information theory, Unix, C, the laser — relative to its size, an
extraordinary run. The reason is not mysterious. The institution understood that senior
researchers were expected to be teachers, and structured itself accordingly. Time spent
in hallway conversations, in reviewing others' work, in explaining the reasoning behind
a design choice — this was not considered a distraction from real work. It was real work.

Claude Shannon's information theory papers were preceded by years of hallway
conversations at the Labs that shaped how other researchers thought about signal, noise,
and transmission. His ideas multiplied through the organization before they were
published, because the institution created space for that kind of transmission. A
senior researcher who developed five junior researchers into excellent ones was credited
— socially, culturally, and to some extent structurally — for the output of those five.

The contrast with organizations that measure only personal output is sharp. In those
environments, the incentive is to produce. Teaching, reviewing, explaining — these are
costs with diffuse returns. The result, over time, is exactly what you would predict:
knowledge silos, repeated mistakes, junior engineers who stay junior, and senior engineers
who are excellent but whose excellence dies with their tenure.

The Bell Labs model produced something compounding. The individual-output model produces
something linear at best.

---

## Force Multiplier vs. Force Addend

Enough history. What does this actually look like in practice?

Here is a pattern that is common enough to be almost a type: the senior engineer who
writes the first draft of every design proposal before circulating it to the team. She
does this because she is good at it. Her drafts are clear, well-reasoned, correctly
scoped. The team iterates from a strong starting point, and the resulting designs are
better than they would otherwise be.

Two years later, nothing has changed. The team still cannot write a strong first draft
without her. Every new initiative, she is in the critical path. She cannot take a week
off without a queue forming. She is excellent. She is also, structurally, a quality
gateway — everything flows through her — rather than a force multiplier.

The alternative looks like this. She writes a guide on how to write a good design
proposal: the structure, the reasoning, the failure modes to avoid. She runs two working
sessions. She reviews three early drafts carefully, explaining her thinking as she edits
rather than just editing. Then she steps back. Within a quarter, five engineers on the
team write solid first drafts independently. Her output has declined; her leverage has
grown. The team she leaves behind — when she goes on vacation, when she gets promoted,
when she moves to the next problem — is different from the one she joined.

That is the distinction. The RFC factory produces excellent output. The guide, the
workshops, the annotated feedback — these produce capability. Capability compounds.
Output does not.

The design review scenario is even cleaner. A staff engineer who sits in on design
reviews not to approve or reject, but to ask three questions: What are you optimizing
for? What did you rule out and why? What would change your mind?

These are not trick questions. They are the questions that force a design to reveal
whether it is actually reasoning or performing reasoning. She asks them consistently,
across a dozen reviews per quarter, regardless of the domain.

Eighteen months later, engineers are answering those questions preemptively in their
design documents, before anyone asks. The quality of designs coming into review has
improved — not because she reviewed more, but because her questions have become the
team's internal monologue. She has installed a reasoning framework into a dozen
engineers. Her output for the year: no code shipped, no systems built. Her outcome:
the team's design quality has compounded significantly.

Attribution is impossible. Measurement is hard. The leverage is real.

The underlying principle: there is a difference between evaluative feedback and
capability-building feedback, and only one of them compounds.

Evaluative feedback tells a person whether their work is good or bad. It is necessary
but low-leverage. "This architecture decision is wrong because of X" addresses the
artifact. It does not change the person's capacity to make better decisions next time.
They will need you to evaluate the next one too.

Capability-building feedback explains the reasoning, makes the principle explicit, and
invites the person to apply it themselves. "What tradeoff were you trying to optimize
for? Let me show you how I think through this class of decision." This takes longer.
It also produces an engineer who does not need you to evaluate the next design, because
they have internalized the reasoning.

Done once, the difference is small. Done consistently over a year, it transforms a
team's baseline. The team that received evaluative feedback is still bringing decisions
to the senior engineer. The team that received capability-building feedback is making
those decisions themselves and arriving at good answers.

The same distinction applies to the difference between directing and coaching. Directing
tells someone what to do and how to do it. It is efficient in the short run and produces
zero capability transfer. The same conversation will happen again the next time the same
situation arises. Coaching helps someone reason through a problem. Lower short-term
efficiency; high long-term capability transfer. The conversation installs a framework,
not just an answer.

Neither is universally correct. Directing is right when stakes are high, time is short,
and the skill gap is too large to bridge in the moment. Coaching is right when there is
time, the person has the capacity to reach the answer, and developing their judgment
matters more than reaching the answer quickly.

Senior engineers who default to directing — because they are faster, because they are
confident in their answers, because the organization rewards speed — create the
bottleneck where all judgment flows through them. Coaching is the investment that makes
the bottleneck unnecessary.

---

## Feedback That Changes Trajectories

Consider the case of a strong mid-level engineer who consistently ships solid code and
repeatedly causes integration problems downstream. Not because she is careless — she is
not. Because she has never developed the habit of thinking about the blast radius of a
change before making it. Her work is technically excellent in the local sense and
disruptive in the system sense.

She has received this feedback twice in formal performance reviews. It was clear.
She heard it. Nothing changed.

Then a tech lead does something different. Not "you need to think more about
dependencies" — she has already received that evaluation. Instead: "I want to show you
how I map out the blast radius of a change before I make it. Let me walk you through the
last design I did this way." Three sessions. The engineer sees the framework concretely.
She watches the senior engineer do the thing, not just hear that she should do the thing.

Six months later, she is the person on the team who most reliably surfaces integration
risks early. She will do this at her next job, and the one after that.

The performance reviews told her she was getting something wrong. The three sessions
transferred the knowledge of how to get it right. These are different interventions.
The first kept the judgment with the reviewer. The second moved it to the engineer.

Delegation works the same way, and most senior engineers get it wrong in a predictable
direction.

Two versions. A senior engineer, overloaded, hands off an incident review: "I don't have
time for this. You handle it." The engineer receiving this has a task without context.
She completes it adequately. Nothing was learned about how the senior engineer approaches
this class of problem. The quality is lower than it would have been. Neither person is
better positioned for next time.

The alternative: "I want you to lead this incident review. Here is what I focus on —
the first three questions I ask, the documents I pull, the order in which I look for
contributing factors. I will be there for the first thirty minutes and then hand it to
you. Afterward, let us compare notes on what we found."

Same task. Similar time investment in the short run. The first approach produces a
completed incident review. The second produces a completed incident review and an
engineer who can lead incident reviews.

Over a year, the compounding difference between those two engineers — the one who
received thoughtful delegation and the one who received task dumping — is a career.

The senior engineer who gives evaluative feedback keeps every decision flowing through
them. The one who explains the reasoning distributes the judgment. These are not just
different tactics. They are different careers. One of them produces an engineer who is
irreplaceable because they cannot be replaced. The other produces an engineer who can
leave and leave the team more capable than they found it.

---

## The Skeptic's Turn

Two objections, both serious enough to deserve honest answers.

The first: if you spend half your time reviewing and mentoring, your technical skills
atrophy. You lose touch with what it actually takes to ship. Your advice becomes
abstract and increasingly disconnected from reality. Eventually you are the person who
gives confident-sounding guidance that does not work in practice.

This is a real risk. Not a strawman. Engineers who move entirely into advisory roles
without maintaining technical currency do lose calibration. Their pattern-matching stays
sharp — they have seen more failure modes than almost anyone — but their sense of what
is hard and what is tractable degrades. The advice drifts toward the theoretical. Junior
engineers stop trusting it. Rightly.

The resolution is not to choose between technical work and multiplier work. It is to
be selective about which technical work you do. Maintain direct technical involvement
in the hardest problems — not the routine ones, the hard ones. The debugging session
no one else can crack. The architecture decision with the most unknowns. The performance
problem that requires understanding several layers simultaneously.

Do this work visibly. Narrate your reasoning as you go. The investigation becomes both
technical contribution and capability transfer at once. You stay current. The people
working alongside you absorb how you think. This is what Thompson did at Bell Labs. The
technical work was real; the pedagogical effect was a byproduct of doing it in proximity
to others.

The activities to reduce are not technical work in general. They are routine technical
tasks that you could do quickly but that teach nothing and could be done by someone who
needs the experience. These are the tasks where your doing it quickly is actually the
problem — not a virtue.

The second objection is harder: this only works if your organization rewards it.

In most engineering organizations, impact is measured by shipped features. The engineer
who takes time to develop others will be rated below the engineer who ships more
personally — even if the team outcomes are better. A rational engineer optimizing for
their own performance review will produce less teaching and more direct output. The
incentive structure punishes the multiplier investment.

This is also substantially true. If you are in an organization where individual
line-item credit is everything, operating as a pure multiplier is irrational in the
short term. You will do more for other people's careers than for your own. That is a
real cost.

The reply to this has two parts. First, it is worth naming clearly that this is an
organizational failure. Institutions that reward only personal output will produce
exactly the outcome you would predict: knowledge silos, fragile teams, staff engineers
who are irreplaceable because nothing was ever transferred. The Bell Labs model was
not accidental — it required deliberate institutional support. Most organizations have
not built that support. If yours has not, you should understand the constraint clearly.

Second, the career arc argument. Multiplier behavior, even where under-rewarded in the
immediate term, is the activity that produces staff and principal engineer careers.
The engineer who is visibly making the people around them more capable is — in
functional organizations, eventually, with patience — the one being considered for
senior technical leadership. The alternative is also a career: being an excellent
individual contributor whom others depend on rather than learn from. That career has a
ceiling. You are valuable, but you are not someone the organization can build around,
because nothing compounds when you are away.

The choice is not between getting credit now and investing in the longer arc. It is
between a career that tops out when your personal output does, and one that grows as
the people around you grow.

Take the medium-term bet. Accept some short-term friction. Make the arc.

---

## What Changes Monday

Here is the metric that matters. Six months from now, which decisions can your team
make without you that they could not make six months ago? Write it down. Track it.
That is the ledger for multiplier work — not code shipped, not reviews completed, not
documents written. The capability that exists in the team now that did not exist before.

This is the thing that will not show up in your performance review in any direct form.
Your job is to make it legible anyway — to name it in conversations with your manager,
to point to the engineer who now leads incident reviews without you, to note the design
proposals that would have been escalated eighteen months ago and are now decided at the
team level. The output of multiplier work is other people's output. Your job is to
make that visible, because the organization will not do it for you.

There are three activities to shift toward starting this week.

First, when you give feedback on a design or a piece of code, practice explaining the
reasoning rather than just the verdict. This takes longer. It is worth it. The goal is
not to evaluate the artifact but to transfer the principle. "The reason I would change
this is that it conflates two concerns that will want to diverge — here is how I usually
think about where to draw that boundary." The next design they bring you should need
less of this. If it does not, something is not transferring.

Second, in design reviews, ask questions rather than give answers. The three questions
in Scenario B are a reasonable starting point: what are you optimizing for, what did
you rule out and why, what would change your mind. Ask them consistently, across domains.
After six months, notice whether engineers are answering them preemptively. That is the
signal.

Third, when you delegate, add thirty minutes of context. Not a wall of documentation —
a conversation about how you would approach the thing, the first three questions you
would ask, the document you would pull, the failure mode you would look for first. Then
hand it over. Do this consistently and the engineering knowledge that currently lives
only in you will, over a year, live in five other people as well.

There are two things to stop.

Stop being the quality gateway. If you are the person who must review every significant
decision before it proceeds, you have created a bottleneck where a force multiplier
should be. The goal is not to be in the critical path of every important decision. The
goal is to have shaped the reasoning so well that your presence in the critical path
is no longer necessary.

Stop doing quickly things that someone else should be learning slowly. This is the
hardest one. You are faster. The team is watching. Doing it yourself is clearly the
right call in the moment. And it is exactly the wrong call in the medium term, because
it protects the other engineer from the learning they need and protects you from the
discomfort of watching someone struggle toward something you could resolve in ten minutes.

The discomfort of that watching is the actual work.

The engineer who cannot stop helping — who answers every question directly, who writes
the first draft because theirs will be better, who jumps into every hard problem before
someone else can get traction — is not failing at the multiplier. They are succeeding
at the wrong metric. Fast answers produce gratitude and stasis. The harder contribution
is to let someone reach the answer, guide them when they are lost, and then watch them
carry that capability forward without you.

That is the job. It is less legible than the old one. It is more important.
