# AI Agents as Digital Colleagues

## The Admiral's Problem

In the summer of 1690, Admiral Anne Hilarion de Costentin de Tourville commanded a French fleet of seventy-eight warships in the Battle of Beachy Head. Once the engagement began, communication between ships was limited to flag signals visible only in clear weather, readable only at close range, and interpretable only by officers who had memorized the signal book. Tourville could not issue real-time instructions to captains fighting three miles away. He could not correct mistakes as they happened. He could not redirect forces in response to an evolving battlefield.

What Tourville could do was prepare. Before the battle, he instilled doctrine, established formations, and — most critically — communicated his intent clearly enough that captains who could not see the flagship could still act in alignment with it. The French victory at Beachy Head was not the result of superior real-time command. It was the result of subordinates who understood what their commander was trying to accomplish well enough to act without constant instruction.

Military theorists later codified this as Auftragstaktik — mission command. The commander states the desired end state, not a rigid sequence of actions. Subordinates understand the why deeply enough to adapt when circumstances change. The doctrine became the organizing principle of Prussian military success in the nineteenth century and remains the basis of modern Western military doctrine.

It is also, without knowing it, the correct management framework for AI agents.

An AI agent deployed on a multi-hour research task, an autonomous system coordinating supplier relationships across a supply chain, a software system that monitors regulatory filings and drafts compliance responses — these are not tools you operate in real time. Once deployed, they act. The executive's management challenge is not how to watch the agent work; it is how to direct the agent before it starts, how to define success clearly enough that the agent can pursue it faithfully, and how to structure the review that catches the cases where it didn't.

This is one of the oldest management problems in existence, appearing in a new form. The executive who grasps this will deploy agents successfully. The executive who treats agents as sophisticated tools requiring continuous supervision will either underuse them or be perpetually disappointed.

---

## What Agents Are Good At — and Where They Break

The practical question facing every executive deploying AI agents is not "can I use agents?" — that question is already answered — but "what should agents do autonomously, what should they do under close review, and what should they not do at all?"

The answer depends on task characteristics, not on agent capability in the abstract.

Agents perform well — and can be deployed with significant autonomy — when tasks are high-volume, well-defined, and reversible. "High-volume" means the task recurs frequently enough that systematic handling is more efficient than case-by-case human judgment. "Well-defined" means the success criteria are clear, the relevant inputs are available, and the range of situations the agent will encounter has been adequately anticipated. "Reversible" means that errors can be caught and corrected before they cascade into larger harm.

Carrier selection in logistics operations checks all three boxes. The carrier selection decision is made thousands of times a day across a large network; the criteria for a good selection (cost, transit time, reliability, capacity) are well-defined; and a poor selection, once flagged, can typically be corrected before the shipment departs. A global logistics company that deployed agents to manage carrier selection found that agents handled 85% of decisions autonomously, with human planners — now freed from the routine — redirecting their attention to exception handling and carrier relationships. The agents had not replaced the planners; they had changed what the planners did.

Agents require close human review — and should not operate with full autonomy — when tasks involve consequential, low-volume, or novel situations. A compliance failure in a financial services firm illustrates the cost of misclassifying a task as autonomous-ready when it was not. The firm deployed agents to review contracts for regulatory violations, and initial performance was strong. Six months in, a compliance failure occurred in a corner case the agent had never encountered. The post-mortem revealed that the firm had dissolved the human review layer after seeing good average-case performance — it had treated "reliable in typical conditions" as equivalent to "reliable at the edges." They are not equivalent. The edge case is precisely where the agent's training provides no reliable guidance, and where a human with judgment is irreplaceable.

Agents should not operate in any capacity — even advisory — when decisions are irreversible at scale, ethically contested, or genuinely novel. Not because agents cannot contribute useful analysis; they can. But because the accountability for such decisions requires human judgment, and the design of the oversight structure must reflect that requirement from the start.

The executive's job is to develop and maintain clear criteria for which tasks fall into which category — and to resist the temptation, which is real and well-documented, to expand autonomous operation after observing good performance in normal conditions. Normal conditions are not the full distribution.

---

## Accountability Architecture: The Problem with Responsible Without Accountable

When something goes wrong in an AI agent deployment, organizations discover a governance gap they didn't know existed: the agent did the work, but the agent cannot be held accountable. Accountability, in any meaningful governance sense, requires a human who can be questioned, who can be sanctioned, and who has sufficient standing to accept responsibility. AI systems have none of these properties. They can be Responsible for execution — in the RACI sense of performing the work — but they cannot be Accountable.

This creates a category problem that standard governance frameworks do not solve. A RACI matrix that assigns "Responsible" to an AI agent leaves the Accountable column empty. Governance structures that assume Responsible and Accountable are naturally coupled — as they usually are when a human does the work — break down when the executor is a system rather than a person.

The solution is an extended accountability architecture that explicitly separates what AI agents do from who answers for it:

**Model selection accountability:** Who chose to deploy this agent for this task, and who accepted the risk that entails? This person is accountable for the initial deployment decision and for ensuring that the agent's capabilities were adequately understood before deployment.

**Ongoing monitoring accountability:** Who is responsible for detecting when agent performance degrades, when edge cases proliferate, or when the agent's operating context has shifted in ways that invalidate its original calibration? This is not a passive role; it requires active tracking and judgment about when to intervene.

**Output review accountability:** Who reviews the agent's work before consequential outputs reach downstream systems or external parties? In many deployments, this role is designed in theory and dissolved in practice — the volume of outputs makes systematic review impractical, so review becomes nominal. The accountability architecture must account for this: either the volume of outputs requiring review must be limited to what humans can genuinely review, or the review scope must be defined precisely enough to be enforceable.

**Incident response accountability:** When something goes wrong — when the agent produces a consequential error — who owns the response? Who communicates externally? Who determines the root cause and decides whether to suspend or redesign the system?

The logistics company that restructured around AI agents found this architecture essential. When the agents produced an unusual routing decision during a regional weather event, the monitoring accountable party recognized the anomaly, the output review team caught it before execution, and the incident response chain activated within hours. The architecture converted what could have been a significant operational failure into a learning event.

---

## The Expertise Pipeline Problem

There is a risk in AI agent deployment that receives far less attention than error rates and accountability structures, and that may be more consequential over the long run: what happens to organizational expertise when agents do the work that used to build it?

In most knowledge-intensive organizations, expertise accumulates through a well-understood pathway. Junior staff perform the routine work that requires careful attention but limited judgment. Over time, pattern recognition develops: the compliance analyst who reviews thousands of contracts comes to recognize the clause structures that signal unusual risk; the credit analyst who underwrites hundreds of loans develops calibrated intuition about the financial ratios that predict trouble. This expertise then becomes the judgment that senior staff apply to the hard cases — the novel situations, the ambiguous decisions, the exceptions that fall outside the range of what routine processes were designed to handle.

When agents absorb the routine work, the developmental pathway breaks. Junior staff no longer build pattern recognition through repetition because the repetitions are now done by systems. The senior staff who currently possess the judgment were trained through a pathway that no longer exists for their successors. Organizations may not notice this for years — the people with judgment are still there, still managing the exceptions. But as they retire or move on, the pipeline is empty.

A retail bank that restructured its fraud operations around AI agents experienced this directly. Human analysts shifted from transaction review to agent oversight — monitoring the agent's decision patterns, identifying drift, and managing escalations. Within a year, experienced analysts described their jobs as fundamentally different: less about fraud judgment, more about system integrity. Several left, finding the new work less engaging. The bank discovered that it had hollowed out the expertise pipeline: junior staff were no longer doing the work that builds pattern recognition, and the senior staff who understood fraud were leaving for organizations where that knowledge still mattered.

A healthcare system's administrative operations group compounded the problem by failing to document institutional knowledge before deploying agents. The people who had done the work being automated carried in their heads a map of the edge cases: the insurers who were slow, the authorization codes routinely rejected, the physicians with unusual preferences. When agents encountered these edge cases, there was no institutional memory to draw on. The system had to invest in retrospective knowledge documentation it hadn't anticipated — at significant cost and delay.

The historical parallel is instructive. When automation arrived on manufacturing assembly lines, the firms that thrived were those that invested in retraining workers to maintain and program the robots, building durable capability around the new technology. Firms that simply reduced headcount found themselves expertise-poor when systems required adaptation. The lesson is not to slow agent deployment but to redesign the expertise pipeline explicitly. If agents do the work that previously built pattern recognition, organizations must create deliberate substitutes: structured simulation of the cases agents handle routinely, adversarial review of agent outputs that requires reviewers to develop deep familiarity with the agent's failure modes, and rotation through exception-handling that exposes developing professionals to the full complexity of the domain.

---

## Trust Calibration

Human beings are not well designed, by default, to supervise automated systems.

The research literature on human-automation interaction — studied most carefully in aviation, where the stakes of miscalibration are highest — documents two reliable failure modes. The first is automation bias: when an automated system has provided an assessment, humans are significantly less likely to notice contradicting evidence than they would be if they had formed the judgment themselves. The automated assessment anchors their attention. In aviation, crews have missed instrument anomalies, overlooked visible contradictions, and failed to catch system malfunctions because the automation told them things were fine.

The second failure mode is automation disuse: after a visible automation error — even a single, non-representative failure — humans abandon the automated system entirely, or require such extensive human review that the automation's benefits disappear. Neither automation bias nor automation disuse represents a calibrated response to the system's actual reliability. Both are predictable consequences of deploying automation into human cognitive environments without designing for the interaction.

A healthcare system's diagnostic support tool illustrated automation bias in an organizational context. Clinicians were told the tool was advisory. A study of actual usage patterns found that when the tool flagged a case as low-priority, physicians almost never overrode it — even in cases where clinical intuition might have prompted a second look. The tool's recommendations had effectively become decisions, despite the governance structure treating them as suggestions. The gap between formal oversight structure and actual human behavior under cognitive load was complete.

The organizational implication is that "humans in the loop" as a structural requirement is not the same as "humans in the loop" as an effective governance mechanism. Designing genuine human oversight — oversight that is not merely nominal — requires attending to the cognitive conditions under which that oversight occurs.

Calibrated trust requires active management: creating conditions where humans are expected to disagree with agents, where disagreements are documented and reviewed, where the base rate of AI errors is made visible to the humans overseeing the system rather than absorbed silently into aggregate metrics. Organizations should measure override rates — the frequency with which human reviewers reject or modify agent outputs — and treat a sustained override rate of near zero not as a success but as a warning sign that human review may have become nominal.

The professional services firm that embedded agents in its client delivery workflow learned this through a costly miscalibration in the opposite direction. Junior consultants who previously handled client check-ins had been replaced by automated summaries, and clients felt the relationship had thinned. The agents had operated autonomously in a space where the relationship capital they were eroding was invisible to any metric the firm was tracking. When client satisfaction fell, the root cause traced back to agents being trusted with relationship-maintenance tasks they were not equipped to perform. The firm learned that the boundary between agent-appropriate and human-necessary work is not always defined by task complexity; sometimes it is defined by what the work means to the people on the receiving end.

---

## Designing the Agent-Integrated Team

The organizations that will get the most from AI agents are not those that deploy the most agents, or the most capable agents. They are the ones that most deliberately redesign their teams around the characteristics of human-agent collaboration.

What does such a team look like?

It has clearly assigned accountability for agent outputs. Every agent in production has a named human who owns monitoring, a named human who owns output review, and a named human who owns incident response. These may be the same person for small-scale deployments; they require explicit assignment at any meaningful scale.

It has designed expertise pathways that survive agent deployment. The team's learning infrastructure does not assume that junior staff will build expertise through doing the routine work agents now handle. It invests explicitly in simulation, adversarial review, and exception-handling rotations that substitute for the learning that routine work previously provided.

It actively manages trust calibration. Override rates are tracked and discussed. Anomalies in agent behavior are surfaced and reviewed, not just logged. The team develops a working mental model of the agent's failure modes — the conditions under which its outputs are least reliable — and applies heightened scrutiny under those conditions rather than extending uniform trust across all agent outputs.

It preserves human relationship capital in customer-facing work. The consumer goods manufacturer that embedded agents in new product development found that creative output from the human team improved — agents had moved the team up the value chain, freeing people for the divergent thinking that generated genuinely novel ideas. But the professional services firm found that clients experienced relationship thinning when human touchpoints were replaced by automated summaries. The difference lies in distinguishing between the work that agents improve by doing it and the work that agents degrade by doing it. That distinction requires judgment, and it requires teams organized to make it continuously rather than once at deployment.

The admiral who prepared his captains at Beachy Head and then trusted them to act could do so because he had selected capable captains, instilled clear doctrine, and designed a fleet organization that functioned in the absence of real-time command. The same design challenge faces every executive deploying AI agents: the preparation that happens before deployment determines the quality of what happens after.

Define intent. Select capable teams to oversee. Establish doctrine — the criteria for autonomous action, the triggers for escalation, the standards for review. Then trust the system — not blindly, but verifiably, through the monitoring and calibration that reveals whether the trust is warranted.

That is still the work. It has always been the work. The agents are new. The management challenge is not.
