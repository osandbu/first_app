# AI Agents as Digital Colleagues

## The Admiral's Problem

In the summer of 1690, Admiral Anne Hilarion de Costentin de Tourville commanded a French fleet of seventy-eight warships in the Battle of Beachy Head. Once the engagement began, communication between ships was limited to flag signals visible only in clear weather, readable only at close range. Tourville could not issue real-time instructions to captains fighting three miles away. He could not correct mistakes as they happened.

What Tourville could do was prepare. Before the battle, he instilled doctrine, established formations, and — most critically — communicated his intent clearly enough that captains who could not see the flagship could still act in alignment with it. The French victory at Beachy Head was not the result of superior real-time command. It was the result of subordinates who understood what their commander was trying to accomplish well enough to act without constant instruction.

Military theorists later codified this as Auftragstaktik — mission command. The commander states the desired end state, not a rigid sequence of actions. Subordinates understand the why deeply enough to adapt when circumstances change. The doctrine became the organizing principle of Prussian military success in the nineteenth century and remains the basis of modern Western military doctrine.

It is also, without knowing it, the correct management framework for AI agents.

An AI agent deployed on a multi-hour research task, an autonomous system coordinating supplier relationships across a supply chain, a software system that monitors regulatory filings and drafts compliance responses — these are not tools you operate in real time. Once deployed, they act. The executive's management challenge is not how to watch the agent work; it is how to direct the agent before it starts, how to define success clearly enough that the agent can pursue it faithfully, and how to structure the review that catches the cases where it didn't.

This is one of the oldest management problems in existence, appearing in a new form. The executive who grasps this will deploy agents successfully. The executive who treats agents as sophisticated tools requiring continuous supervision will either underuse them or be perpetually disappointed.

---

## What Agents Are Good At — and Where They Break

The practical question facing every executive deploying AI agents is not "can I use agents?" but "what should agents do autonomously, what should they do under close review, and what should they not do at all?"

The answer depends on task characteristics, not on agent capability in the abstract.

Agents perform well — and can be deployed with significant autonomy — when tasks are high-volume, well-defined, and reversible. High-volume means the task recurs frequently enough that systematic handling is more efficient than case-by-case human judgment. Well-defined means the success criteria are clear, the relevant inputs are available, and the range of situations the agent will encounter has been adequately anticipated. Reversible means that errors can be caught and corrected before they cascade into larger harm.

Carrier selection in logistics operations checks all three boxes. The selection is made thousands of times a day; the criteria — cost, transit time, reliability, capacity — are well-defined; and a poor selection can typically be corrected before a shipment departs. A global logistics company that deployed agents to manage carrier selection found that agents handled 85% of decisions autonomously, with human planners redirecting their attention to exception handling and carrier relationships. The agents had not replaced the planners; they had changed what the planners did.

Agents require close human review when tasks involve consequential, low-volume, or novel situations. A compliance failure in a financial services firm illustrates the cost of misclassifying a task as autonomous-ready. The firm deployed agents to review contracts for regulatory violations, and initial performance was strong. Six months in, a compliance failure occurred in a corner case the agent had never encountered. The post-mortem revealed that the firm had dissolved the human review layer after seeing good average-case performance — it had treated "reliable in typical conditions" as equivalent to "reliable at the edges." They are not equivalent. The edge case is precisely where the agent's training provides no reliable guidance, and where human judgment is irreplaceable.

The practical implication: executives must develop and maintain clear criteria for which tasks fall into which category — and resist the temptation, which is real and well-documented, to expand autonomous operation after observing good performance in normal conditions. Normal conditions are not the full distribution. As agent capabilities evolve, the criteria for what qualifies as autonomous-ready will shift, which is exactly why maintaining the criteria as a living framework — rather than a fixed deployment decision — is essential.

---

## Accountability Architecture: The Problem with Responsible Without Accountable

When something goes wrong in an AI agent deployment, organizations discover a governance gap they didn't know existed: the agent did the work, but the agent cannot be held accountable. Accountability, in any meaningful governance sense, requires a human who can be questioned, sanctioned, and who has sufficient standing to accept responsibility. AI systems have none of these properties. They can be Responsible for execution — in the RACI sense of performing the work — but they cannot be Accountable.

Standard governance frameworks do not solve this. A RACI matrix that assigns "Responsible" to an AI agent leaves the Accountable column empty. The solution is an extended accountability architecture that explicitly separates what AI agents do from who answers for it.

**Model selection accountability** answers: who chose to deploy this agent for this task, and who accepted the risk that entails? This person is accountable for the initial deployment decision and for ensuring the agent's capabilities were adequately understood.

**Ongoing monitoring accountability** answers: who is responsible for detecting when agent performance degrades, when edge cases proliferate, or when the operating context has shifted in ways that invalidate the agent's original calibration? This is an active role, not a passive one; it requires regular judgment about when to intervene.

**Output review accountability** answers: who reviews the agent's work before consequential outputs reach downstream systems or external parties? In many deployments, this role exists in theory and dissolves in practice — the volume of outputs makes systematic review impractical, so review becomes nominal. The accountability architecture must address this directly: either the volume of outputs requiring review must be limited to what humans can genuinely process, or the review scope must be defined precisely enough to remain enforceable.

**Incident response accountability** answers: when something goes wrong, who owns the response? Who communicates externally? Who determines root cause and decides whether to suspend or redesign the system?

The logistics company that restructured around AI agents found this architecture essential. When agents produced an unusual routing decision during a regional weather event, the monitoring accountable party recognized the anomaly, the output review team caught it before execution, and the incident response chain activated within hours. The architecture converted what could have been a significant operational failure into a learning event.

---

## The Expertise Pipeline Problem

There is a risk in AI agent deployment that receives far less attention than error rates and accountability structures, and that may be more consequential over the long run: what happens to organizational expertise when agents do the work that used to build it?

In most knowledge-intensive organizations, expertise accumulates through a well-understood pathway. Junior staff perform the routine work that requires careful attention but limited judgment. Over time, pattern recognition develops: the compliance analyst who reviews thousands of contracts comes to recognize the clause structures that signal unusual risk; the credit analyst who underwrites hundreds of loans develops calibrated intuition about the financial ratios that predict trouble. This expertise then becomes the judgment that senior staff apply to the hard cases — the novel situations, the ambiguous decisions, the exceptions that fall outside what routine processes were designed to handle.

When agents absorb the routine work, the developmental pathway breaks. Junior staff no longer build pattern recognition through repetition. The senior staff who currently possess judgment were trained through a pathway that no longer exists for their successors. Organizations may not notice this for years — the people with judgment are still there, still managing the exceptions. But as they retire or move on, the pipeline is empty.

A retail bank that restructured its fraud operations around AI agents experienced this directly. Human analysts shifted from transaction review to agent oversight — monitoring decision patterns, identifying drift, managing escalations. Within a year, experienced analysts described their jobs as fundamentally different. Several left, finding the new work less engaging. The bank discovered that it had hollowed out the expertise pipeline: junior staff were no longer doing the work that builds pattern recognition, and senior staff who understood fraud deeply were leaving for organizations where that knowledge still mattered.

A healthcare system's administrative operations group compounded the problem by failing to document institutional knowledge before deploying agents. The people who had done the work being automated carried in their heads a map of the edge cases: insurers who were slow, authorization codes routinely rejected, physicians with unusual preferences. When agents encountered these cases, there was no institutional memory to draw on.

The historical parallel is instructive. When automation arrived on manufacturing assembly lines, firms that invested in retraining workers to maintain and program robots built durable capability around the new technology. Firms that simply reduced headcount found themselves expertise-poor when systems required adaptation. The lesson is not to slow agent deployment but to redesign the expertise pipeline explicitly. If agents do the work that previously built pattern recognition, organizations must create deliberate substitutes: structured simulation of the cases agents handle routinely, adversarial review of agent outputs that requires reviewers to develop deep familiarity with the agent's failure modes, and rotation through exception-handling that exposes developing professionals to the full complexity of the domain.

---

## Trust, Relationship Capital, and the Invisible Erosion

Human beings are not well designed, by default, to supervise automated systems.

The research literature on human-automation interaction documents two reliable failure modes. Automation bias: when an automated system has provided an assessment, humans are significantly less likely to notice contradicting evidence than they would be if they had formed the judgment themselves. The automated assessment anchors their attention. In aviation, crews have missed instrument anomalies and overlooked visible contradictions because the automation told them things were fine. Automation disuse: after a visible automation error, humans abandon the automated system entirely, or require such extensive human review that the automation's benefits disappear.

Neither represents a calibrated response to the system's actual reliability. Both are predictable consequences of deploying automation into human cognitive environments without designing for the interaction.

A healthcare system's diagnostic support tool illustrated automation bias in an organizational context. Clinicians were told the tool was advisory. A study of actual usage patterns found that when the tool flagged a case as low-priority, physicians almost never overrode it — even in cases where clinical intuition might have prompted a second look. The tool's recommendations had effectively become decisions. The gap between formal oversight structure and actual human behavior under cognitive load was complete.

The implication is that "humans in the loop" as a structural requirement is not the same as "humans in the loop" as an effective governance mechanism. Designing genuine oversight requires attending to the cognitive conditions under which that oversight occurs. Organizations should track override rates — the frequency with which human reviewers reject or modify agent outputs — and treat a sustained override rate near zero not as a success but as a warning sign that review has become nominal.

A second dimension of invisible erosion is more subtle: relationship capital. A professional services firm that embedded agents in its client delivery workflow found that junior consultants who previously handled client check-ins had been replaced by automated summaries. Client satisfaction scores fell — not because the summaries were inaccurate, but because clients experienced the relationship as thinning. The agents had operated autonomously in a space where the relationship capital they were eroding was invisible to any metric the firm was tracking. When the cause was eventually traced to agent deployment, the firm discovered it had no way to measure relationship depth in real time — it had only been measuring deliverable quality.

The lesson generalizes: agent deployment can erode dimensions of organizational value that standard performance metrics don't capture. Before deploying agents in any customer-facing or relationship-dependent context, executives must identify what relationship capital currently exists in that work — what the human presence provides that is not captured in the deliverable — and design explicit safeguards for it. This is not an argument against agent deployment in relationship contexts; it is an argument for knowing what you are trading when you deploy there.

---

## What the Admiral Does Before the Battle

The closing question is not "should we deploy agents?" That question is settled. It is: what must an executive do — before, during, and after deployment — to make agent integration genuinely productive rather than superficially efficient?

Before deployment, the work is preparation in the Tourville sense. Define intent precisely: what is the agent supposed to accomplish, and what constraints bound its operation? Establish the accountability architecture before the agent is active — the four accountability roles (model selection, monitoring, output review, incident response) must be assigned and understood before the first autonomous decision is made. Design the expertise pathway that will sustain human judgment in the domain the agent is entering: identify what knowledge must be actively preserved and how.

During deployment, the work is active calibration. Track override rates and treat anomalies in either direction as signals. Maintain honest visibility into edge case accumulation — the conditions the agent has never encountered, or encounters poorly. Review the agent's output not just for correctness but for the second-order effects: is it eroding relationship capital? Is it degrading dimensions of value that metrics don't capture?

After a period of deployment, the work is structural learning. What did the agent reveal about the work it was doing? The consumer goods manufacturer that embedded agents in new product development found something unexpected: creative output from the human team improved. Freed from synthesis work, engineers and brand managers spent more time in divergent-thinking sessions. The agent had moved the team up the value chain. That outcome was not designed; it was discovered. Executives should expect to discover similar shifts — places where agent deployment surfaces higher-value human activity that was previously crowded out — and redesign deliberately around what they find.

The admiral who prepared his captains at Beachy Head and then trusted them to act could do so because he had selected capable captains, instilled clear doctrine, and designed a fleet organization that functioned in the absence of real-time command. The same design challenge faces every executive deploying AI agents.

Define intent. Assign accountability. Build the expertise pathway. Then trust the system — not blindly, but verifiably, through the monitoring and calibration that reveals whether the trust is warranted.

That is still the work. It has always been the work. The agents are new. The management challenge is not.
