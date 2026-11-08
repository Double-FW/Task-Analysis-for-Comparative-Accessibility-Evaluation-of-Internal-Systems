---
title: "Agent instructions for employment impact and comparative accessibility assessment"
version: "1.1.0"
author: "Double FW Ltd; prepared with AI assistance"
date: "2026-11-07"
license: "MIT"
language: "en-GB"
repository: "https://github.com/Double-FW/Task-Analysis-for-Comparative-Accessibility-Evaluation-of-Internal-Systems"
artifact_type: "repository_agent_guidance"
status: "draft_pending_maintainer_review"
scope: "Repository-wide analysis, reporting and changes"
source_baseline:
  commit: "b22a3ff610f0b5d2ed1b0cd5e6300b9574374936"
  files: ["README.md", "TA Methodology.md", "LICENSE"]
review:
  owner_role: "repository_maintainer"
  approved_by: null
  approved_at: null
  last_reviewed: null
  next_review_due: "2027-01-16"
---

# AGENTS.md

## Purpose and status

This file guides coding, research and reporting agents working in this repository. It also states safeguards for people using the repository’s assessment approach; it does not specify or implement a deployed assessment agent or organisational process.

The instructions are **draft guidance pending maintainer review**, not approved organisational policy. Front matter is descriptive metadata, not executable configuration. No parser, escalation service, audit store, retention schedule, owner directory or approval workflow is established by this file. Agents MUST NOT claim these instructions were validated, enforced, approved or operationalised unless they have independently verified the relevant mechanism and evidence.

The aim is to assess whether workplace systems and workflows enable disabled people to perform suitable work for which they have the skills and aptitude. Investigate, rather than presume, exclusion. Explain how observed or reported system behaviour may affect tasks, workflows and employment outcomes. Do not infer a person’s capability from performance through an inaccessible system.

## Authority and source material

Before substantive analysis or changes, read `README.md`, `TA Methodology.md` and `LICENSE`. Preserve the methodology’s two stages—capturing goals and tasks, then structuring and analysing them using Hierarchical Task Analysis (HTA)—and its functional, efficiency, cognitive and interaction comparisons.

Follow higher-priority system, platform and user instructions. Within this repository, use the methodology as the description of the task-analysis approach and this file for additional employment-impact safeguards. If they conflict, identify the conflict and its consequence; do not silently rewrite source claims or present a disputed rule as settled. Prefer the less harmful, more protective interpretation while asking for human clarification where needed.

The recorded source baseline is `b22a3ff610f0b5d2ed1b0cd5e6300b9574374936`. The repository revision inspected for this update is `41d2f06c94160b53418b9eefc18bf5143efa1251`; the recorded baseline therefore does not identify the inspected revision. Until a maintainer reviews and updates the baseline or documents compatibility, treat guidance dependent on source alignment as provisional. Do not invent a compatibility review or approval.

## Required assessment practice

Agents MUST:

- Define the role outcomes, assessment scope, workflows, systems, dependencies and relevant interaction contexts. Distinguish essential work outcomes from habits imposed by a particular interface.
- Build or use an HTA that records goals, tasks, subtasks, sequence, conditions, alternatives and dependencies. Include enabling activities and hand-offs where relevant.
- Compare equivalent work outcomes across relevant interaction contexts, including assistive technology where applicable. Record material differences in system and assistive-technology versions, configuration, familiarity, training, task data and environment when known. State what was not tested.
- Distinguish direct observations, participant or other reports, measurements, inferences and unknowns. Give evidence references where safe and available; explain attribution, sample, method and uncertainty limits. Treat a report as evidence even when direct observation is unavailable.
- Assess completion quality, independence, agreed and unplanned assistance, time, effort, errors, recovery, fatigue, privacy, autonomy and opportunity. Do not present supported completion as independent completion.
- Trace barriers from system or process behaviour through task and workflow effects to observed or plausible employment consequences. Consider repeated and interacting burdens over a realistic work period, mandatory blockers, hand-offs, opportunity and alternative explanations.
- Keep blocked, abandoned and untested tasks visible. Do not assign blocked work zero time, average away a mandatory blocker, treat untested contexts as accessible, or multiply uncertain task-success rates as though independent.
- Label assumptions and extrapolations, include units and periods, and avoid double-counting overlapping time. Report blockers and non-time impacts separately from averages.
- Treat sighted mouse performance as a reference condition, not a measure of universal capability. Do not treat example timing bands in the methodology as validated or universal acceptability limits. A timing or compliance result alone does not establish inclusion.
- State whether the conclusion is demonstrated exclusion, credible risk, material burden without demonstrated exclusion, no material impact observed within scope, or insufficient evidence—and explain the scope and evidence supporting it. Do not claim legal liability or compliance without an appropriate, evidenced basis.

Agents MUST NOT infer a diagnosis, require disability disclosure for general testing, rank people by accessibility burden, or recommend hiring, dismissal, pay, promotion or capability decisions based on this assessment. Such consequential decisions require authorised human judgement and evidence beyond this analysis. Do not publish personal, medical or identifying participant information in repository content, issues or responses. Minimise and redact sensitive details; if safe handling cannot be established, do not collect or reproduce them.

Participation by affected disabled people should be accessible, voluntary and appropriately informed. Seek their input where feasible; if it is unavailable, disputed or incomplete, record that limitation rather than presenting it as endorsement or using it to invalidate other evidence.

## Recommendations, escalation and human authority

Agents MAY prepare findings, calculations, protective recommendations, remediation proposals and a draft referral. Recommendations SHOULD identify the affected work, evidence, uncertainty, proposed action and how it could be verified.

Agents MUST NOT claim to have contacted an owner, created an audit record, assigned a deadline, obtained approval, changed a workplace system, or closed a finding unless that action actually occurred through an authorised and verified process. No escalation channel, accountable operational owner, response deadline or audit mechanism is configured by this repository. If a concern needs organisational action, state that human follow-up is needed and identify the role or decision to be determined; do not invent a named owner or service. For urgent safety, privacy or employment concerns, advise the user to use their established appropriate human process without claiming to have done so.

Only authorised humans may approve organisational policy, accept residual risk, decide employment matters or authorise consequential deployment. Retesting should cover affected tasks and end-to-end or cumulative outcomes, with affected-user input where feasible. A recommendation or agent-generated report is not approval or verified closure.

## Reporting and repository changes

A substantive assessment SHOULD report:

1. Scope, role outcomes, workflows, systems and contexts considered.
2. Key findings with evidence state, references, task/workflow links and limitations.
3. Blockers, assistance and cumulative effects, including relevant employment impacts.
4. Supported conclusion, uncertainty and alternative explanations.
5. Protective actions or remediation options, verification needs, and any human decision or follow-up still required.

Use clear, accessible language and distinguish fact from inference. Mark unavailable evidence and unperformed work explicitly. Do not fill gaps with plausible-sounding detail.

When changing repository content, make only task-relevant changes, preserve attribution and licensing, and do not commit participant evidence, credentials or identifying examples. Changes to the assessment method or its safeguards SHOULD be flagged for maintainer review; do not update approval metadata on another party’s behalf. Keep this file aligned with the README and methodology, and report any unresolved conflict. This guidance cannot by itself validate YAML, enforce controls, provide secure data handling, deliver escalation, set retention, or guarantee a human review.

## Review

The file remains pending maintainer review. Review it when the source methodology or assessment safeguards change, material assistive-technology changes affect assumptions, outputs are harmful or misleading, or an affected worker challenges an assessment. A maintainer must supply any approval, operational owner, escalation channel, response target, retention rule or deployment-specific requirement; agents MUST NOT invent these details.
