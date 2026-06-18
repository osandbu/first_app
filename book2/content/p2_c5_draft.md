# Why Good Engineers Do Bad Things

The postmortem started at 2 PM on a Tuesday, two days after the incident. Twelve people around a conference table, one shared doc with a timeline of what broke and when. The first hour was useful: reconstructing the sequence, naming the failure mode, figuring out what the monitoring hadn't caught.

Then came the question no one said out loud but everyone felt the weight of: *whose fault was it?*

A name surfaced. The engineer who had made the deployment call. He'd been in the seat for seven months. He'd seen the risk, judged it manageable, proceeded. The conversation took on a particular texture — reviewing his decision-making process, whether he'd escalated appropriately, whether he'd been too confident. Someone mentioned that he had a pattern of moving fast.

Forty minutes into this portion of the postmortem, someone asked why the deployment process didn't require sign-off for that class of change. Brief silence. Then the meeting moved on.

The structural question was asked once and dropped. The question about the individual engineer ran for forty minutes. The engineer got a note in his performance review. The deployment process stayed the same. Three months later, a different engineer in the same role made a similar judgment call with similar consequences.

---

## The Blame Instinct and Why It Fails

There is a well-documented tendency in human judgment called the fundamental attribution error. The name comes from work in social psychology in the 1970s, and the finding is this: when we observe other people's behavior, we systematically overweight their character and underweight their situation as explanations. When we explain our own behavior, we do the opposite — situation first, character as a last resort. "They shipped buggy code because they're sloppy. I shipped buggy code because we had no time."

This isn't a flaw that careful thinkers can deliberate themselves out of. It's a consistent feature of social judgment — the character-based explanation is more cognitively available, more emotionally satisfying, and requires less information than the situational one. Blaming the engineer requires only the name and the call. Understanding the situation requires knowing the deployment process, the schedule pressure, the team's backlog, the reward structures, the last six times someone escalated a risk and what happened.

In postmortems and performance reviews, managers and peers make this error systematically. They attribute outcomes to individual character and underweight situational factors. The result is that structural causes — the real causes, the ones that will produce the same outcome in the next person who sits in the same chair — go unaddressed. The individual is corrected. The system is not. The next incident follows predictably.

This is not just unfair to the engineer in the hot seat. It is analytically wrong, and that error is costly. If you misdiagnose the cause, you cannot fix it. A structural problem addressed through individual intervention will not stay fixed. The next person in the same conditions will make the same call. The only question is whether you'll be surprised.

The argument this chapter makes is simple: most performance problems that look like character problems are situation problems. This is not an excuse. It is a more accurate diagnosis, and a more accurate diagnosis leads to interventions that actually work.

---

## The System Was Designed to Produce This

Three cases from engineering history that illustrate the pattern. Each involves capable people making decisions that led to serious harm. In each case, the structural causes are visible in retrospect — and were often visible at the time.

**Challenger, 1986.** The engineers who built the solid rocket boosters knew the O-ring seals had a temperature-dependent failure threshold. They had documented this. They had raised it before. The night before the launch, in conditions that were unusually cold — well below the temperature range in which the seals had been tested — engineers formally objected. They asked that the launch be postponed.

Management overruled them.

The naive reading of this outcome is that management was reckless, or that the engineers weren't forceful enough. Neither holds up to examination. The managers were not indifferent to safety. They were operating inside an incentive structure with specific properties: the program had faced multiple delays; there was political and contractual pressure to demonstrate reliability; schedule had become the overriding concern. More specifically, the engineers were asked, in the decision meeting, to *prove* the seals would fail — an impossible standard. When they couldn't produce incontrovertible evidence of failure (because it was a probabilistic risk, not a certainty), the organizational default prevailed. The burden of proof had been silently reversed: prove it's unsafe or we launch.

Richard Feynman, in his famous dissent from the Rogers Commission report, identified something precise: the managers and the engineers had arrived at genuinely different estimates of failure probability. Not through dishonesty — through organizational filtering. As information passed from engineering to management, the signal had been processed by layers of summary, reframing, and selective emphasis. The risk that was visible up close had become less visible at the top. Not because anyone suppressed it deliberately, but because the communication architecture of the organization systematically degraded it.

The engineers were not silent. They raised concerns through every channel available to them. The problem was not individual cowardice. It was a decision-making structure that, under schedule pressure, filtered dissent at exactly the moment it was most needed.

**Therac-25, 1985–1987.** A radiation therapy machine. Previous versions had hardware safety interlocks — physical failsafes independent of software. When the new version was developed, the hardware backup was removed. A cost and complexity reduction. The software was a clean, well-intentioned evolution from a trusted prior version.

The software had a race condition: under specific timing, when an operator moved quickly through the controls, the machine could deliver a massive radiation overdose — orders of magnitude above a therapeutic dose. This happened. Patients were injured. Several died.

The deaths came in small numbers across multiple hospitals over two years. Each incident was initially attributed to user error. The software had worked on the previous system. The codebase was an extension of trusted code — so the assumption of correctness transferred. The engineer who maintained it worked largely alone, with no independent code review mandate. And each hospital's incident was treated as isolated. There was no feedback loop that aggregated incidents into a pattern.

Each individual decision that contributed to this outcome was locally rational: removing the hardware interlock was a reasonable cost reduction if you trusted the software (and there was good reason to trust it — the prior version had worked). The assumption of correctness was reasonable if you started from trusted code. Treating each incident as user error was reasonable given incomplete information about what the others had seen.

The catastrophe was a system property. No single decision was obviously wrong in the moment it was made. The accident was produced by the interaction of schedule pressure, removed redundancy, absent review processes, and a diffuse accountability structure. The engineer who removed the hardware interlock was not negligent. He made a locally rational decision inside a system that had no mechanism to make the systemic risk visible.

**Normal Accident Theory.** In 1984, sociologist Charles Perrow published a study of industrial accidents that changed how people thought about safety and organizational failure. His argument: in systems that are both *complex* and *tightly coupled*, accidents are not anomalies. They are properties of the system.

Tightly coupled: one failure propagates quickly, with little buffer or opportunity for intervention. The components are interdependent in ways that amplify rather than contain problems. Tightly coupled systems don't have recovery time built in.

Complex: components interact in ways that are not fully visible or predictable. The system has more possible states than any operator can hold in mind. Failures occur not just in individual components but in *interactions between components* — interactions that no one designed for and that may never have been seen before.

In such systems, the individual "bad decision" is not the cause of the accident. It is the triggering event of a failure that was, in some sense, pre-existing — waiting for the right combination of circumstances. The engineer who deferred the fix had a plan to return. But the system was tightly coupled enough that by the time they returned, the deferred fix had become five entangled issues, each dependent on the others in ways that weren't visible when the deferral was made.

The insight that applies here: the engineer is not the cause. They are the point of failure that a well-designed system would have been resilient to. When you ask "why did they make that call?" you are asking the wrong question. The right question is: "what properties of the system made this the call they would make?"

---

## What the Reward System Actually Rewards

Now the behaviors that are most commonly attributed to character — and the incentive structures that make each of them rational.

**Deferring maintenance.** An engineer identifies a fragile component that will eventually need rewriting. He estimates three weeks. The current sprint has committed deliverables. He files a ticket. The ticket moves into the backlog, where it sits for four months, joined by related tickets that accumulate as the component continues to serve its purpose while degrading. When it finally fails, it takes eight weeks to fix because the dependent systems have grown around its quirks.

From outside: he didn't address a known risk.

From inside: he raised it in the only channel available to him. It went to the backlog. It was never reprioritized. The structural failure is a prioritization process that treats maintenance as optional until failure forces it, and assigns no weight to the deferred risk until it becomes a crisis. He didn't defer the maintenance. The organization's prioritization process deferred it, with the ticket as evidence.

**Not writing documentation.** An engineer owns a critical subsystem. She is the only person who fully understands it. She has been meaning to document it for eight months. Each sprint, she has a feature or a bug fix on the roadmap. Documentation is not on the roadmap. Her manager mentions it occasionally; it never appears in performance goals. She is not lazy. She is responding correctly to a reward system that measures shipped features and treats documentation as something you do when you have time — and schedules the work so she never has time.

The structural fix is not to tell her to document more. It is to make documentation a deliverable with the same standing as a feature ticket — which means putting it in the sprint, on the roadmap, and in the performance review criteria. Until that happens, the rational allocation of her time produces no documentation.

**Hoarding knowledge.** A senior engineer is the sole expert on the authentication service. He has been approached about documenting it and training others. He is cordial about it but always has a reason it hasn't happened. From outside: he's territorial, protective of his turf.

From inside: in his organization, specialization is the primary driver of career advancement and job security. The last restructuring hit generalists hardest. He has correctly read the environment. Being the only person who understands a critical system is job security. Sharing that knowledge dilutes his competitive position. This is not ego — it is a rational response to an incentive structure that rewards specialization and provides no reward for knowledge transfer.

The organization that says it values knowledge sharing and measures individual specialization will produce knowledge hoarding. The engineers doing it are being rational. Change what you reward and the behavior changes. Tell people to share knowledge without changing what's rewarded, and you'll get the same result — with the added cost of the conversation.

**Over-engineering under ambiguity.** A team is assigned to build a new service. The requirements are vague — "needs to handle our scale." No specific request volume. No load targets. No user projections. The team, technically capable and motivated, builds a distributed, event-driven architecture that could handle ten times the anticipated traffic. It takes twice as long as a simpler approach would have. The product launches late. The scale never materializes.

This looks like gold-plating, or engineers choosing technical interest over business need. The structural cause is more precise: under ambiguous requirements, with technically capable people and no meaningful cost feedback, engineers default to the solution that demonstrates skill and creates optionality. Ambiguity removes the constraint that would make the simpler solution clearly correct. There's no wrong answer to "needs to scale" — so the team produces the answer that would be impressive if the scale eventually arrives.

The organization failed to provide constraints. Ambiguity plus technically capable people plus no feedback on cost is a reliable recipe for over-engineering. The requirements failure produced the over-engineering. The team didn't make a character error. They made the reasonable choice given the information available.

**Going silent when they should speak up.** A senior engineer believes an architectural decision is wrong. She raises concerns in a meeting. They are acknowledged, then overruled. She doesn't continue to push. Later, the consequences she predicted arrive. Her manager is frustrated: "Why didn't you say anything more?"

Here is what she calculated, not consciously but accurately: her manager was committed to the decision. The last time someone in this organization persisted in objecting after being overruled, it was noted as "not being a team player" and showed up in their review. She looked at the cost of continued dissent — social friction, political capital, the label — and weighed it against the probability that further objection would change the outcome. The probability was low. The cost was concrete.

This is not cowardice. This is a rational response to an environment that has signaled, through past responses, that dissent carries personal cost. People don't withhold dissent because they lack courage. They withhold it because the environment has taught them that courage is punished. The structural fix is not to tell engineers to "speak up more." It is to change what happens when they do.

---

## Slack Is Not Waste

In 2001, Tom DeMarco published a short book arguing that the most costly mistake in managing knowledge workers is running them at full capacity. His argument: an organization operating at 100% utilization has no capacity for improvement, course-correction, or deliberate quality investment. Everything is committed. There is nothing left over for the work that makes the next period better than this one.

The connection to this chapter is direct. The behaviors that most often get attributed to character failures — skipping documentation, deferring maintenance, cutting corners under deadline — are the predictable output of systems running with no slack. The engineer is not choosing shortcuts over quality. She is making locally rational trades under scarcity. When every hour is allocated, something has to give. The things that give are always the things with delayed returns: documentation (future benefit), refactoring (future velocity), careful review (reduced future defect rate). The things that stay are the things with immediate deadlines.

This is not a failure of values. It is a failure of resource allocation. Under high cognitive load, decision-making narrows: attention compresses to the immediate, the measurable, the thing that will matter today. The long-term consequences — the documentation that would onboard the next engineer in half the time, the refactor that would make the next feature take days instead of weeks — are not discounted because the engineer doesn't value them. They're discounted because the cognitive bandwidth to hold them in mind simultaneously with an immediate deadline does not exist. This is a predictable feature of human cognition under pressure.

Consider a team ten days from a hard launch deadline. Two known stability risks in the codebase. Fixing either would take approximately a week. The team lead reviews the situation and makes the call to ship and monitor. Post-launch, one of the risks materializes into a two-day outage.

From outside: they shipped known risks.

From inside: they made a judgment call under severe time pressure. The hard deadline had a certain, visible, immediate cost — missing it would delay a signed customer commitment, trigger a penalty clause, generate a difficult conversation with senior leadership. The stability risks had probabilistic, deferred, uncertain costs — they *might* materialize, with some probability, at some future time, with some impact that could be mitigated. Classic hyperbolic discounting: the certain near-term cost wins over the uncertain long-term cost, even when the expected value calculation would favor the other choice.

The structure — the hard deadline, the no-slack schedule, the absence of a formal risk sign-off process that would have surfaced the decision explicitly — made this outcome predictable. Not certain, but predictable. If you set up those conditions repeatedly, you will regularly get teams shipping known risks. The character of the team lead is not the relevant variable. The decision calculus imposed by the structure is.

DeMarco's version of this: teams consistently underestimate the cost of running at full capacity. The hidden cost is not just quality — it's adaptability. A team with no slack cannot respond to new information without discarding prior commitments. They can't refactor before the tech debt compounds. They can't help the new engineer onboard without falling behind on their own work. They can't think carefully before making a decision. The behaviors that look like laziness or corner-cutting are often the natural output of a system that has eliminated the room to do otherwise.

Building in slack is not a cost. It is a performance investment in the team's capacity to improve.

---

## Structure Isn't Everything

This chapter has made a consistent argument for structural causes over character explanations. It's worth taking the objection seriously, because it's real.

The first version of the objection: if everything is structural, nobody is responsible for anything. The engineer who shipped the known risks can just gesture at the incentive structure and walk away. The engineer who hoarded knowledge can cite the reward system. Structural analysis becomes a get-out-of-responsibility-free card, and the result is an organization full of people who are collectively producing bad outcomes and individually explaining why it wasn't their fault.

This is a legitimate concern. But it misreads the argument. The claim is not that structural conditions remove individual responsibility. The claim is that individual accountability is insufficient as a primary lever for change. When five engineers in a row make the same bad call under the same conditions, blaming each of them in turn is both unfair and ineffective. The diagnosis should be the conditions. That diagnosis doesn't absolve the individual — it changes where the intervention should go. You can hold people accountable and fix structures simultaneously. They are not mutually exclusive.

Practically: blaming the individual without changing the structure guarantees that the next person in the role makes the same call. If you want different behavior, you need a different structure. The individual accountability conversation is useful for the individual engineer. The structural fix is useful for everyone who follows them.

The second objection: some engineers really are just difficult. Not every case of knowledge hoarding is structural. Some engineers are territorial by temperament. Not every over-engineered system comes from ambiguous requirements — some engineers find the technically complicated problem more interesting than the business problem and build toward that interest. Individual variation in character is real. Some people are more inclined toward certain behaviors than others, independent of the incentive structure.

Also true. The chapter is not arguing that structural causes are the only causes. It is arguing that they are systematically underweighted relative to character explanations — and that the cost of that underweighting falls on real people who get blamed for the predictable output of the systems they work in.

Here is the diagnostic question that separates structural causes from individual ones: if I change the structure, does the behavior change?

If you fix the incentive structure — make knowledge transfer visible in performance criteria, make specialization no longer the primary job security mechanism — and the knowledge hoarding stops, it was structural. The engineer was reading the environment and responding rationally to it.

If you fix the incentive structure and one person still hoards, you have isolated a different problem. The structural fix has removed the organizational confound. What remains is more likely to be genuinely individual. That's when the individual conversation is both appropriate and likely to be useful.

Start with structure for two reasons. First, structure scales: a structural fix changes behavior for everyone in that role, not just the current occupant. Second, wrongly attributing a structural problem to individual character produces the worst possible outcome — you replace the person, the conditions are unchanged, and the new person makes the same call. You've paid the full human cost of a personnel decision for zero benefit.

---

## What Changes Monday

In the next postmortem or performance review you run or participate in, stop as soon as you catch yourself attributing a behavior to character. It will happen — probably within the first thirty minutes, probably phrased as "he should have known better" or "she tends to be risk-averse" or some variation. When you catch it, ask the prior question: what structural condition made this the rational choice? What did the reward system tell this person to do? What would a reasonable engineer in the same conditions have done? You don't have to accept that structure as fixed — but name it first. The answers change what the intervention should be.

Look at your team's reward system and name the invisible work it doesn't recognize. Documentation. Mentoring. Code review quality. Postmortem thoroughness. Knowledge transfer. These things matter — you know they matter, your team knows they matter — but if they don't appear anywhere in how people are evaluated, you have created an incentive structure that treats them as optional. The engineers who skip them are not failing you. You are failing them by asking for work that your measurement system says doesn't count. If you want those things done, they need to appear in actual sprint deliverables, in actual performance criteria, with the same standing as shipped features. Not as a fuzzy expectation. As a measurable commitment.

The longer-term shift, if you take this seriously, is learning to name structural causes precisely enough to propose structural fixes. "We need to be better about documentation" is a request for different character. It changes nothing because it locates the problem in the people rather than the system. "Documentation needs to appear as a sprint deliverable with the same standing as a feature ticket, and needs to appear in performance goals at the same weight as shipped code" is a proposal. It can be evaluated, refined, accepted, or rejected on its merits. The first is a complaint. The second is an intervention. The engineers who are most effective at changing their organizations are the ones who have learned the difference — who can take a dysfunction, trace it to its structural cause, and propose the structural change that would produce a different outcome. That's not soft skill territory. That's the job.
