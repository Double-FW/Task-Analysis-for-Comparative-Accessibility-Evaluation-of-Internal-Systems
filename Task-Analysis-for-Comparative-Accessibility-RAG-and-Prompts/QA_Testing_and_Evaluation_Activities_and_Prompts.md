# Task Analysis for Comparative Accessibility Evaluation of Internal Systems: human-managed QA, testing and evaluation activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `3a9410afd11fc8384decbf2dffe53a735a2270bc`  
**Source:** [Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems](https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems/tree/3a9410afd11fc8384decbf2dffe53a735a2270bc)  
**Audience:** test leads, QA practitioners, researchers, accessibility specialists, engineers, service owners, procurement and HR/employee-experience partners.

## Where the repository is useful

Use the methodology’s two stages—capture goals/tasks, then structure/analyse them through HTA—to examine how workplace systems impose barriers and cumulative burden. Compare functional outcomes, interaction paths, timing, cognitive demands, physical effort and recovery in context. Use the newer employment-impact safeguards to keep independence, privacy, fatigue, opportunity and blocked work visible.

Evaluate systems and work design, not an employee’s capability or worth. The methodology’s mouse baseline, timing bands and scaled profile are proposed approaches, not validated universal acceptability limits or a calibrated score. Its direct-observation requirement and later AGENTS recognition of reported evidence need explicit interpretation, not silent reconciliation. AGENTS is draft pending review and records an older baseline mismatch; source-alignment-dependent claims remain provisional. Do not use this analysis for hiring, dismissal, pay, promotion or diagnosis inference.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI prepares scoped test plans, analytical options and evidence summaries. Testers establish actual results with appropriate competence; researchers involve affected people and preserve the limits of observation and reports. Engineering and service owners repair systems. Accountable humans retain release, procurement, exception, risk and employment decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft test/evaluation aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete test/evaluation artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Evaluation activity | Expected output |
| --- | --- | --- |
| 1. Define role outcomes, scope and participation | Study commissioning and ethical evaluation planning | A study brief, scope map and participation/data decisions. |
| 2. Capture actual goals and task variations | Stage 1: Task and goal capture | A goal/task inventory with provenance and evidence gaps. |
| 3. Build a complete hierarchical task model | Stage 2: HTA structuring and analysis | An HTA with plans, source evidence and uncertain nodes. |
| 4. Design fair comparative conditions | Comparative study and environment design | A comparative protocol and environment/context matrix. |
| 5. Analyse cognitive, physical and interaction demands | Task-demand and recovery analysis | A per-node demand/barrier profile linked to work outcomes. |
| 6. Measure time without hiding blocked work | Comparative timing and interpretation | A timing-analysis plan or checked comparison table with limits. |
| 7. Estimate cumulative workflow burden responsibly | Workload and operational impact analysis | A bounded cumulative-burden model and sensitivity questions. |
| 8. Interpret comparative profiles and employment impact | Evidence synthesis and bounded conclusions | A comparative experience profile and scoped impact statement. |
| 9. Turn barriers into protective and permanent system repairs | Remediation, procurement and organisational follow-up | A system-remediation brief with interim support and verification needs. |
| 10. Retest complete work and report trustworthy learning | Evaluation reporting and continuous improvement | A retest protocol, comparative findings report and learning log. |

## 1. Define role outcomes, scope and participation

**Evaluation activity:** Study commissioning and ethical evaluation planning

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology sections 1–3; AGENTS: Required assessment practice.

### Tasks the repository can support

- Distinguish essential work outcomes from interface-imposed habits.
- Map systems, mandatory workflows, interactions and employment context.
- Plan accessible voluntary participation and minimum necessary evidence.

**Expected output:** A study brief, scope map and participation/data decisions.

**Human review:** The researcher, service owner and appropriate employee/HR representatives agree purpose and safeguards; the study does not decide employment matters.

### Example prompt 1

> Use the attached RAG to scope a comparative evaluation of [internal systems and work role]. Define suitable work outcomes, mandatory/optional workflows, system dependencies, relevant interaction contexts and the decision the study supports. Plan voluntary accessible participation and necessary data only. State explicitly that the subject is system burden, not employee ranking or capability.

### Example prompt 2

> Challenge [study brief] against the RAG. Identify goals confused with interface habits, forced staff observation, unnecessary diagnosis requests and an employee-performance purpose hidden inside accessibility testing. Propose a bounded system-evaluation brief.

## 2. Capture actual goals and task variations

**Evaluation activity:** Stage 1: Task and goal capture

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology section 4; AGENTS: evidence distinctions.

### Tasks the repository can support

- Combine interviews, reported incidents, walkthroughs and observation where available.
- Capture alternatives, enabling tasks and hidden work.
- Preserve participant reports and limits when direct observation is unavailable.

**Expected output:** A goal/task inventory with provenance and evidence gaps.

**Human review:** The researcher checks validity and access; unavailable direct observation does not erase a credible reported barrier.

### Example prompt 1

> Using the RAG, plan Stage 1 capture for [workflows]. Combine interviews/critical incidents, walkthroughs and authorised observation where feasible, recording alternatives, assistance, workarounds and enabling steps. Distinguish direct observations, reports and unknowns. Explain the source tension about mandatory observation and preserve reported evidence with limits rather than rejecting it.

### Example prompt 2

> Review [task capture notes] against the RAG. Find missing recovery or handoffs, reported barriers treated as untrue because not observed and assumptions presented as timings. Produce a source-qualified task inventory and triangulation plan.

## 3. Build a complete hierarchical task model

**Evaluation activity:** Stage 2: HTA structuring and analysis

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001).

**Relevant source sections:** Methodology sections 4–6.

### Tasks the repository can support

- Decompose goals into tasks/subtasks with meaningful start/end conditions.
- Record sequence, conditional branches, alternatives and dependencies.
- Include interruptions, failure, recovery and handoffs.

**Expected output:** An HTA with plans, source evidence and uncertain nodes.

**Human review:** The analyst and people doing the work review whether the model represents actual goals and routes.

### Example prompt 1

> Use the RAG’s Stage 2 method to build an HTA from [task evidence]. Record goals, tasks, subtasks, execution plans, conditions, alternatives, frequency and system/handoff dependencies. Include enabling, interrupted, failed and recovery paths; mark unsupported nodes instead of inventing an ideal workflow.

### Example prompt 2

> Challenge [HTA] using the RAG. Identify omitted authentication/support work, an unnecessary interface path treated as the goal and branches hidden in a linear list. Propose a corrected hierarchy and questions for validation.

## 4. Design fair comparative conditions

**Evaluation activity:** Comparative study and environment design

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology sections 2, 6 and 7; AGENTS: comparison safeguards.

### Tasks the repository can support

- Compare equivalent goals across relevant interaction routes.
- Record versions, configuration, task data, experience and conditions.
- Control or disclose practice, training, support and reference-condition limits.

**Expected output:** A comparative protocol and environment/context matrix.

**Human review:** The researcher reviews fairness and alternative explanations; a sighted mouse route is a reference, not universal ability.

### Example prompt 1

> Using the RAG, design comparison of [equivalent work tasks] across relevant mouse, keyboard, screen-reader and magnification contexts, plus other routes the actual work requires. Record product/AT versions, configuration, task data, familiarity, training, assistance and environment. Treat the source mouse baseline as one reference condition, not the standard of employee worth.

### Example prompt 2

> Review [comparison protocol] against the RAG. Find unmatched task complexity, practice effects, different system versions or assisted versus independent routes being compared without explanation. Propose controls, transparent limits and alternative reference designs.

## 5. Analyse cognitive, physical and interaction demands

**Evaluation activity:** Task-demand and recovery analysis

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology section 6; sections 10–12; AGENTS: outcomes.

### Tasks the repository can support

- Inspect decisions, retained context, state visibility and input demands.
- Record observed errors, recovery, fatigue and assistance alongside reports.
- Distinguish interface demand indicators from measured mental capacity.

**Expected output:** A per-node demand/barrier profile linked to work outcomes.

**Human review:** Researchers and affected users interpret effort and fatigue; UI counts do not diagnose cognition or capacity.

### Example prompt 1

> Use the RAG to analyse [HTA and observations] for memory dependencies, decisions, state clarity, precision, repetition, errors and recovery. Link each demand to evidence, relevant interaction context and task consequence. Distinguish observed behaviour, reported effort and inferred interface demand; do not turn steps or decisions into a clinical cognitive-load score.

### Example prompt 2

> Challenge [demand profile] with the RAG. Identify diagnosis-based explanations, mental fatigue asserted without evidence and an assisted route labelled independent. Propose more precise observations and system-design hypotheses.

## 6. Measure time without hiding blocked work

**Evaluation activity:** Comparative timing and interpretation

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology sections 7–8; AGENTS: blocked, abandoned and untested tasks.

### Tasks the repository can support

- Define timing boundaries, task outcomes and assistance conditions.
- Calculate delays with units and valid reference denominators.
- Keep blocked, abandoned and untested cases separate from successful timing.

**Expected output:** A timing-analysis plan or checked comparison table with limits.

**Human review:** The analyst checks calculations and contextual interpretation; percentage bands do not determine universal acceptability.

### Example prompt 1

> Using the RAG and [supplied task timings], compare equivalent outcomes with stated start/end events, units, assistance and context. Calculate absolute and relative delays only where the reference is valid and nonzero. Keep blocked/abandoned/untested tasks visible, never assign them zero time, and do not apply the source example bands as validated thresholds.

### Example prompt 2

> Review [timing report] against the RAG. Find failed tasks removed from the denominator, favourable averages hiding mandatory blockers and uncertain times treated as exact. Return corrected calculations or explain what cannot be calculated, with scope and alternative explanations.

## 7. Estimate cumulative workflow burden responsibly

**Evaluation activity:** Workload and operational impact analysis

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology section 9; AGENTS: cumulative effects and extrapolation.

### Tasks the repository can support

- Combine repetition and additional work across realistic workflows.
- Avoid overlapping time and explain frequencies/periods.
- Report blockers, fatigue, privacy and lost opportunity beyond time averages.

**Expected output:** A bounded cumulative-burden model and sensitivity questions.

**Human review:** The analyst and work/service owners review assumptions with employees; estimated time is not proof of cost or lost capacity.

### Example prompt 1

> Use the RAG and [task observations, frequencies and work-period context] to estimate cumulative system burden. Separate measured time from extrapolation, state units/periods, prevent overlapping-time double counts and show uncertainty in frequency. Report mandatory blockers, fatigue, assistance, privacy and opportunity separately; do not multiply uncertain success rates as independent probabilities.

### Example prompt 2

> Challenge [productivity-impact calculation] against the RAG. Identify invented repetition, overlapping recovery time, extrapolated delays presented as measured loss and employee cost claims unsupported by evidence. Produce corrected estimates and the data needed for a defensible conclusion.

## 8. Interpret comparative profiles and employment impact

**Evaluation activity:** Evidence synthesis and bounded conclusions

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology sections 8, 10–11; AGENTS: conclusion categories.

### Tasks the repository can support

- Keep completion, time, effort, complexity and independence separate.
- Expose uncertainty, sample limits and alternative explanations.
- Trace system barriers to demonstrated or plausible work consequences.

**Expected output:** A comparative experience profile and scoped impact statement.

**Human review:** Qualified reviewers and affected people assess interpretation; conclusions do not establish legal liability or individual capability.

### Example prompt 1

> Using the RAG and [evidence], create a comparative experience profile without an invented weighted score. Separate completion quality, independence, time, cognitive/physical demands, errors, recovery and privacy. State whether evidence supports demonstrated exclusion, credible risk, material burden without demonstrated exclusion, no material impact observed within scope or insufficient evidence, with reasons and limits.

### Example prompt 2

> Audit [employment impact conclusion] against the RAG. Identify a small timing difference treated as proof of exclusion, compliance used to dismiss burden and a failed mandatory workflow averaged away. Produce an appropriately bounded statement and remaining evidence questions.

## 9. Turn barriers into protective and permanent system repairs

**Evaluation activity:** Remediation, procurement and organisational follow-up

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology section 12; AGENTS: recommendations and human authority.

### Tasks the repository can support

- Trace a system/process behaviour to task and workflow consequences.
- Compare interim access and permanent redesign alternatives.
- Prepare human follow-up without deciding employment outcomes or claiming escalation.

**Expected output:** A system-remediation brief with interim support and verification needs.

**Human review:** The actual service, HR, procurement and technical owners decide within remit; support should not depend on blaming the employee.

### Example prompt 1

> Use the RAG and [barrier evidence] to prepare system/process remediation options. State the affected goal, mechanism, observed or anticipated consequence, interim access, permanent repair, dependencies and verification plan. Preserve privacy and independence; identify the human decision role to confirm without claiming to assign work, send a referral or decide employment matters.

### Example prompt 2

> Review [workaround or procurement response] with the RAG. Identify assistance that removes confidentiality, training proposed for a system defect and a funding dispute leaving essential work blocked. Propose less burdensome alternatives and an evidence-based human follow-up brief.

## 10. Retest complete work and report trustworthy learning

**Evaluation activity:** Evaluation reporting and continuous improvement

**Retrieve:** [S001 — TA Methodology.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Methodology sections 11–14; AGENTS: reporting and review.

### Tasks the repository can support

- Compare repaired tasks and full workflows under stated conditions.
- Revisit cumulative burden, assistance and human outcomes.
- Retain provenance and avoid unsupported closure, approval or baseline claims.

**Expected output:** A retest protocol, comparative findings report and learning log.

**Human review:** The study/service owner reviews actual evidence with affected users where feasible; technical repair alone is not verified employment access.

### Example prompt 1

> Using the RAG, plan retest of [system repairs and prior evidence]. Reuse equivalent work goals and record changed versions, experience, task data and support conditions. Evaluate individual tasks, complete workflows and repeated burden, including independence, fatigue and privacy. Produce a report structure with actual evidence or Not tested and human review needed.

### Example prompt 2

> Audit [comparative study report] against the RAG. Find methodology baseline metadata treated as confirmed compatibility, a closed ticket treated as restored access and reported findings labelled direct observation. Return corrections, unresolved limits and next evaluation actions.

## Evaluation evidence and decision record

For each adopted result, record the project/task, source revision and sections used, observed test/evaluation question, barrier or outcome, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
