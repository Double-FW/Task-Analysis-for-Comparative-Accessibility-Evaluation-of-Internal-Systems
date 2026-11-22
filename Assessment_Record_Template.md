---
title: "Illustrative comparative task assessment record"
version: "1.2.0"
updated: "2026-11-22"
owner: "Double FW Ltd"
license: "MIT"
language: "en-GB"
status: "illustrative_blank_template_not_executed_evidence"
---

# Assessment record template

Use this as a drafting aid with [the methodology](TA%20Methodology.md) and [agent safeguards](AGENTS.md). It is not a deployed data model, validated schema, completed assessment or human approval. Empty values are intentionally unassigned. Store actual sensitive evidence only through authorised local arrangements, outside the public repository and public training datasets.

## Study and comparison record

Record the purpose, essential work outcome, scope and exclusions; product/build and interaction contexts; task data and environment; source revisions; voluntary participation/data decisions; familiarity/training/support; timing boundaries and methods; and known limitations. Use actual roles and decision references only when agreed.

## Task and evidence structure

The YAML below is an illustrative blank record. Allowed values are explained in the methodology; they are not enforced by software here. `result` relates to a stated check; `outcome` relates to an actual task attempt. Neither substitutes for a human decision.

```yaml
assessment:
  study_id: null
  source_revision: null
  purpose_and_scope: null
  goal: {id: null, required_outcome: null}
  contexts: [] # Product/AT versions, input/output, configuration, task data,
               # familiarity/training, assistance, environment and exclusions
  hta_nodes: [] # ID, parent, task, start/end, plan/conditions, alternatives,
                # mandatory dependencies, frequency/period, evidence basis
  attempts:
    - attempt_id: null
      task_id: null
      context_id: null
      outcome: null # Only an observed/reported task outcome; no invented completion
      completion_quality: null
      assistance_and_independence: null
      elapsed_seconds: null # Not necessarily a successful completion duration
      completion_seconds: null # Only comparable completed work
      effort_fatigue_privacy_control: null
      evidence_basis: []
      evidence_reference: null # Authorised reference, not personal data
      checks:
        - check_id: null
          requirement_and_scope: null
          method: null
          result: not_tested
          rationale: null
          evidence_reference: null
  comparisons: [] # Reference/comparison IDs, conditions, units, calculation,
                  # applicability, uncertainty and attribution limits
  cumulative_estimates: [] # Non-overlapping terms, frequencies/period,
                           # evidence/assumptions and sensitivity
  impact_conclusions: [] # Task/route scope, conclusion, evidence and limits
  proposed_actions: [] # Interim/permanent options, dependencies and retest
  unresolved_issues_and_decisions: []
  human_decision: null # Actual authority, decision, scope and date if it exists
```

## Interpreting and reviewing the record

Preserve a credible participant report as a report even when direct observation is unavailable. Record failed and abandoned work alongside successful attempts. A blocked mandatory dependency remains visible independently of averages or local timing thresholds. Never infer diagnosis, employee capability or a legal outcome.

Give calculations with units and stated assumptions, and verify each denominator and overlapping component. If needed data is missing, state what cannot be calculated. Keep an author’s proposed recommendation, a human decision and a verified repair as separate events. Retest affected technical behaviour, complete work and repeated burden under recorded conditions.
