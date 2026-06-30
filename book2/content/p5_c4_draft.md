# The First Ninety Days as a Manager

You are sitting at your keyboard on Monday morning. The calendar has eight meetings on it, several of which you did not schedule and could not explain if asked. Your editor is open. There is a pull request that you know exactly how to fix — you wrote the code it touches, you understand the tradeoff, you could have it merged before lunch. Instead, you have a one-on-one in twenty minutes with an engineer you have managed for three days.

You close the pull request tab. Or you don't.

That choice — seemingly trivial, made dozens of times in the first few weeks — determines whether you make the transition successfully or spend the next two years fragmented between two jobs, doing neither well.

Here is the thing nobody says plainly enough at the moment of promotion: this is not a step up from engineering. It is a different job that happens to share a building with the old one. The skills that earned you this role — technical depth, individual execution, the ability to debug your way out of anything — are necessary but no longer sufficient. Some of them are actively counterproductive. The faster you accept that, the better the next ninety days will go.

The player-coach parallel is useful here because it strips away the ideological freight that tends to accumulate around conversations about "engineering versus management." Nobody argues that the best player should also be coaching. The logic is structural: you cannot evaluate the team from inside it, you cannot be in two places at once, and competitive pressure will always pull you back to playing. The same structural logic applies in engineering management. Not because management is more important than engineering — it isn't — but because the work is different and the failure modes are predictable.

Studies of first-time managers who receive no structured support — no formal onboarding, no mentorship, no deliberate transition — find failure rates estimated between 40 and 60 percent within the first two years. "Failure" here means performing poorly by organizational metrics or reverting to individual contributor behavior and being moved back. This is not a number about bad people. It is a number about an unannounced career change.

---

## The Career Change Nobody Announces

The player-coach problem is structural. It is not a question of effort or commitment or even self-awareness. The player-coach who tries genuinely to do both jobs still runs into the same four walls.

First, you cannot evaluate a team you are embedded in. A player-coach is a participant, not an observer. The dynamics they can see are the dynamics they are producing. The engineer who is intimidated by the technical lead — now the manager — will not reveal that in a code review. The pair who always agrees with each other because they've worked together for three years will not surface that tendency while the manager is contributing to the same codebase.

Second, under competitive pressure, you will default to what you trained for. Deadline approaching, a hard bug to fix, the codebase on fire — every engineer in the room will write code, including the one with "manager" in their title. This is not a character flaw. It is an optimized response to the situation. The problem is that the manager's absence from the actual manager work — unblocking the team, making decisions, running interference with stakeholders — has a compounding cost that does not show up immediately.

Third, when the best player is also the evaluator of other players, you create an asymmetry that people feel but rarely name. An engineer being reviewed by someone they are also competing with technically is navigating an uncomfortable ambiguity. Who owns this code? Whose architectural judgment is final? Are my ideas being assessed on their merits or filtered through our technical history together?

Fourth, you cannot be in two places at once. The critical feature and the strategic conversation with the adjacent team about the dependency they are blocking you on both need attention simultaneously. In the first case, the work gets done. In the second, the team stays blocked. Andy Grove put the logic plainly: a manager's output is the output of the organization they supervise. Not their own output. The individual contributor trap is the manager who produces high personal output while leaving the team's leverage untouched.

This framework matters because it reframes the problem. The engineer who keeps writing code after taking a management role is not lazy about management or insufficiently committed to growing into the new job. They are being a good engineer. The habits were rewarded for years. The pull is completely rational. The transition requires noticing the pull, understanding why it is strong, and redirecting it — not suppressing it through force of will.

---

## The First Week: Listen Before You Fix

The most common error new managers make in the first week is acting like managers. They arrive with a diagnosis — the team is slow because of X, the process is broken because of Y — and start fixing things. This is a mistake for the same reason that a doctor who skips the examination and goes straight to the prescription is a bad doctor. Your priors are incomplete. Act on them anyway and you will be wrong, expensively.

The first week is primarily a listening exercise. This is not a soft-skills suggestion. It is strategic.

The "new manager" frame gives you a window that closes. Questions that would seem naïve or politically fraught in month three are legitimate in week one. You can ask an engineer why a decision was made without the question implying you are challenging it. You can ask why a process exists without the question reading as a threat. You can learn that two people on the team stopped trusting each other eighteen months ago without that information appearing to be gossip. The window is real. Use it.

Start the first round of one-on-ones as soon as you have the role. The format matters: ask more than you direct. What are you working on? What is going well? What is frustrating you? What do you wish the team did differently? What do you need from a manager that you are not currently getting? Write down what you hear, not just the content but the texture — who speaks easily, who hedges, who has clearly wanted to say something for a long time, who seems to be testing you.

Separately, map the team's actual working relationships. Not the org chart. The org chart shows reporting lines. What you need to understand is who talks to whom, who unblocks whom, which cross-team relationships are strong and which are strained, where work actually flows between people. This takes several sessions and will produce surprises.

In one common case, a manager taking over a six-engineer team discovers that three of those engineers do their most important daily collaboration with engineers on a different team — a team whose members do not report to them. The org chart suggested two parallel independent groups. The actual working structure was one integrated group with an administrative boundary through the middle. Every decision the new manager was about to make about process, on-call rotation, and project assignment would have been wrong, because they were designed for a team that did not exist.

HP's management-by-walking-around philosophy is not a sentimental artifact of a different era. Packard's insight was informational, not relational: the manager who stays at their desk operates from incomplete information. They know what gets escalated. They do not know what doesn't get escalated, which is often more important. The modern equivalent of walking around is being genuinely available in one-on-ones and paying close attention to what engineers do not say directly, as well as what they do.

In the first week, also identify the organizational debt you have inherited. Every team carries it. Unresolved interpersonal tensions that everyone has learned to work around. Implicit understandings about who owns which piece of the system that have never been written down. Compensation inequities that calcified years ago. Technical commitments made to other teams that the previous manager agreed to and nobody documented. Engineers who have been building toward departures that have not happened yet.

This debt is now yours. Not because you created it, but because you have the authority to address it and the new manager frame gives you cover to ask about it. After month three, the organizational debt is simply your debt. The window to ask "can you help me understand how this situation developed?" closes as you become more established, because the implied follow-up becomes "and why haven't you fixed it."

Make as few changes as possible in the first week. The one exception: things that are clearly urgent and clearly yours to address. Everything else — process changes, team structure, communication patterns — should wait until you understand what you have.

---

## The First Month: Establish the Operating System

By the start of week two, you should be running one-on-ones consistently. Set a cadence and hold it. Weekly for each direct report in the first ninety days. This is the most important investment of the first month, and it is also the most commonly sacrificed when delivery pressure rises.

Long-running research on management quality and team engagement finds that management quality is the primary variable in team engagement — more predictive than compensation or work content. The mechanism is not abstract. It runs directly through the one-on-one. An engineer whose manager is consistently present, genuinely listening, and visibly acting on what they hear develops a fundamentally different relationship with their work and their organization than one whose manager cancels frequently and treats the meeting as a status update to be expedited.

The pattern of canceling one-on-ones under delivery pressure is so strongly correlated with team attrition that it functions almost as a leading indicator. Engineers interpret cancellations as signal about how the manager values the relationship — regardless of what the manager says the reason is. "Things are just really busy" is heard as "you are not my priority when things matter." This is not an irrational reading.

The first round of one-on-ones will surface information you were not expecting. A well-run initial listening round with a team of eight will typically reveal: at least one person who is interviewing elsewhere or actively thinking about it, at least one person who has been frustrated by a specific recurring situation for longer than a year and has never said so through official channels, at least one person whose career progression has stalled on a decision that the previous manager never made, and at least one person who is doing work significantly above their current level without recognition or title to match. None of this will be in any handoff document. All of it is load-bearing.

The manager who skips or shortchanges this initial listening period begins managing a team they do not actually understand. They make decisions — about who gets the interesting project, about how to handle the next delivery crunch, about what feedback to give in the first review cycle — with a systematically distorted picture of what they have.

In month one, also establish clarity on how decisions are made. Not an elaborate governance document — that's overkill and signals anxiety. A simple, communicated understanding of which decisions the team makes autonomously, which require input from the manager, and which the manager reserves. Engineers who do not have this clarity will either over-escalate (interrupting you with decisions they could make themselves) or under-escalate (making decisions that should have had your input and creating work to unwind later). Both failure modes are expensive.

Identify one or two process changes that are clearly high-leverage and make only those. The instinct to fix everything visible is strong in month one, when you can see the dysfunction clearly and your energy is high. The manager who restructures the sprint cadence, changes the on-call rotation, introduces a new approach to code review, and starts a weekly architecture session — all in month one — is not wrong about any individual change. The aggregate effect is organizational whiplash. The team's cognitive bandwidth is spent adapting to new processes instead of delivering. Engineers who were already close to leaving now have a concrete new reason. The instinct to act decisively is understandable and should be applied surgically.

Paul Graham's distinction between the maker's schedule and the manager's schedule is load-bearing here. The maker's schedule is organized around large uninterrupted blocks, because a context switch costs an hour of setup and recovery. The manager's schedule is organized around one-hour chunks, because meetings are the work, not an interruption to it. Most new engineering managers try to hold both simultaneously. They block deep-work mornings to write code and attend afternoon meetings and end each day feeling fragmented and effective at nothing.

The transition requires accepting one schedule and releasing the other. This is psychologically costly. It is also necessary. You cannot optimize for deep engineering work and management work at the same time. The attempt to do so will leave you bad at both.

---

## The Mental Model Shift

The pull to keep writing code is not weakness. This needs to be said clearly, because the discourse around the engineering-to-management transition often implies that engineers who struggle are failing some character test. They are not. The pull is rational.

You were rewarded for writing code for years. You are good at it. It produces visible, measurable, immediate output — you can see it in the pull request, in the test suite, in the feature that works. Management output is indirect, delayed, and often invisible. You unblock an engineer and they ship the feature; you are not in the commit log. You run a good one-on-one and the engineer stays another year; nobody attributes the retention to that conversation. You make a decision in week two that prevents a significant architectural mistake; the mistake never happens, so nobody knows what was avoided.

This invisibility is real, and it is not fixed by anyone telling you that your work matters. It requires a genuine mental model shift about what "productive" means.

Research on first-time managers finds consistently that they underestimate in advance the interpersonal and emotional demands of the role. The learning curve is longer than most new managers or their organizations expect — typically twelve to eighteen months before a new manager feels genuinely competent. The engineers who make this transition successfully tend to be the ones who allow themselves to acknowledge the difficulty instead of performing confidence while privately feeling adrift.

The identity loss is real. The engineer who becomes a manager has given up a professional identity that was built over many years and was the basis for the promotion itself. That loss is not compensated immediately by the new identity. There is a period — usually several months — of operating in the new role without yet having internalized it. The manager still thinks of themselves as an engineer who is currently doing management. The shift to thinking of themselves as a manager who maintains technical engagement happens later, unevenly, often without a clear moment of arrival.

Andy Grove's leverage framework is the practical tool here. The question is not "am I being productive?" — which the engineer's brain will answer by pointing at the code they just wrote. The question is "is this activity producing leverage on my team's output?" A one-on-one that surfaces a three-week blockage and enables you to resolve it in a thirty-minute cross-team conversation has dramatically different leverage than writing the same feature yourself. Orienting daily decisions around leverage rather than personal output is the core shift. It does not happen automatically, and it is not maintained without deliberate attention.

Grove's formulation is also useful for engineering managers who feel guilty about not writing code: the measure of a manager is not how much they personally produced. It is the output of the organization they run. A manager whose team ships well, whose engineers are growing, whose technical direction is coherent — that manager is doing the job well, regardless of how many pull requests they authored.

---

## The Skeptic's Turn: You Need to Stay Technical

The objection deserves a serious answer, not a dismissal.

Engineers are pattern-matching constantly on whether their manager understands the work. A manager who cannot read a diff, who consistently misestimates complexity, who cannot hold a real conversation about architectural tradeoffs — that manager loses credibility in ways that permanently impair their effectiveness. The team begins filtering information upward differently. They stop consulting the manager on technical decisions. The manager becomes a bureaucratic layer rather than a contributing voice. This is a real failure mode and it happens to people who overcorrect on the "stop writing code" advice.

The resolution is not zero technical participation. It is a different mode of technical participation.

Staying technical as a manager means: reading code, regularly enough to maintain genuine understanding of what the team is building and how. It means participating in architecture discussions with real opinions, not performative deference. It means having enough technical judgment to know when a proposal has a flaw and enough skill to name it clearly. It means being the person who can talk to the adjacent team's architects as an equal, not as a liaison.

Staying technical as a manager does not mean: owning implementation. Booking mornings for deep coding work. Being the fallback for hard technical problems that the team should be solving. Inserting yourself into the design of a feature because it's technically interesting to you.

The player-coach who watches game film, runs practice, and develops players is different from the player-coach who plays every shift. Both are involved with the technical work. Only one is doing the manager job.

One pattern to watch for: the manager who overcorrects stops contributing technical opinions in code review, stops pushing back in architecture discussions, stops being a genuine technical voice in design conversations. The team notices. Some engineers interpret this as lack of engagement. Others, correctly identifying that the technical guidance is absent, start making decisions without it — including decisions the manager would have redirected. The manager who stepped back too far has not avoided the player-coach problem. They have produced a different version of it.

The practical calibration depends on team size. A manager of three engineers in an early-stage environment with fluid roles may write code regularly and manage well — the organizational structure supports it, the team is small enough that management overhead is low, and the contribution is genuinely needed. A manager of eight who spends their time writing features is almost certainly failing at the management job. The overhead of eight people's one-on-ones, context, career development, and unblocking is a near-full-time job by itself. The chapter's argument is primarily addressed to that case.

What changes is not the amount of code — it is the nature of the engagement. The manager participates as a senior technical voice, not as an individual contributor. The distinction is ownership. A manager can give strong opinions on architecture without owning the implementation. They can push back on a proposal without writing the alternative. They can be technically credible without being technically occupied.

---

## What Changes Monday

Three things. Not ten. Three.

**Stop writing the code.** Not forever, not completely, but stop treating the editor as your default response to available time. If you have twenty minutes between meetings and your instinct is to open a pull request, redirect that instinct. Use the time to respond to the question you have been putting off, or to think about what one of your engineers needs that they have not asked for yet. The editor will still be there. The window to build the management relationships that your team's output depends on is shorter than you think.

**Make the one-on-one the non-negotiable event on the calendar.** Not the one that gets rescheduled when a production incident lands, not the one that becomes a Slack message when delivery pressure spikes. The one that happens because you decided in advance that it happens. Schedule it and hold it. The research here is clear: teams whose managers cancel one-on-ones under pressure interpret that as signal — correctly — about how the manager prioritizes the relationship. Consistency under pressure is almost the whole message. The content of the conversation matters, but the consistency matters more.

The first round of one-on-ones has a specific shape. Ask what is going well. Ask what is frustrating. Ask what they need from a manager that they are not currently getting. Do not come with an agenda. Write down what you hear. Come back to it. Show through actions that you were listening — not by immediately acting on everything, but by following up on specific things weeks later in a way that demonstrates you retained them. This is not complicated. It is also not automatic.

**Measure yourself by your team's output.** This shift takes longer than ninety days. Most managers who make it successfully look back and identify a specific moment — usually six to twelve months in — when they realized they had stopped mentally tracking their own code contributions as a measure of professional worth and started tracking what the team shipped, who was growing, what got unblocked. That moment does not happen without intention. You can accelerate it by being deliberate: at the end of each week, ask yourself not "what did I produce?" but "what is my team able to do now that they could not do at the start of the week?" The second question takes longer to answer. It is also the right question.

The first ninety days are not the whole transition. They are the window in which the patterns get established — patterns that are much harder to change six months later when they have become the team's expectations of how you operate. The manager who establishes a consistent one-on-one cadence, who listens before acting, who resists the pull to stay in the code while remaining genuinely technically engaged — that manager has not finished the transition. But they have started it correctly.

That's the job. It is harder than the previous one in most of the ways that matter, and it produces a different kind of satisfaction. Give it ninety days of genuine attention before you decide whether you like it.
