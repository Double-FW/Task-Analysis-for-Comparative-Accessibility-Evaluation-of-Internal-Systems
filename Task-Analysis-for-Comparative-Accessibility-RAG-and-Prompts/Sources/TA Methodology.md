# Task Analysis for Comparative Accessibility Evaluation of Internal Systems

---

## 1. Method Overview

Task analysis is a **systematic method for understanding how users achieve goals by completing tasks**. It focuses on observable actions, cognitive processes, and system interactions required to complete those tasks.

A **task** is defined as:
- an activity with a clear start and end point  
- performed in service of achieving a broader **goal**

A **goal** is the intended outcome, while tasks are the steps taken to reach it.

This distinction is critical for evaluation:
- systems often optimise for tasks incorrectly  
- true evaluation must measure whether **goals are achieved efficiently and equivalently across users**

---

## 2. Application to Accessibility and Inclusion

This methodology is extended to evaluate **comparability of user experience across different interaction modalities**.

### Primary Evaluation Groups

The same system and tasks must be evaluated across:

- Standard sighted mouse users  
- Keyboard-only users  
- Screen reader users  
- Magnification users  

The purpose is not just to assess usability, but to determine:

- **functional equivalence** (can the task be completed?)  
- **efficiency equivalence** (how long does it take?)  
- **cognitive equivalence** (how much effort is required?)  
- **interaction burden** (how complex are the steps?)  

---

## 3. Core Evaluation Principle: Comparative Experience

Task analysis must be reframed from:

> “Can the user complete the task?”

to:

> “How comparable is the experience of completing the task across different user types?”

This introduces **comparative accessibility as a measurable construct**, not a binary pass/fail.

---

## 4. Two-Stage Methodology

### Stage 1: Task and Goal Capture

The objective is to identify:
- user goals  
- tasks required to achieve those goals  
- variations in how tasks are performed  

#### Data Collection Methods

Use a combination of:

- Observation of real users performing tasks in context  
- Structured or semi-structured interviews  
- Critical incident recall (detailed breakdown of real experiences)  
- Activity sampling (tracking frequency and duration of tasks)  
- Task walkthroughs and simulations  

Key constraint:
- Do not rely solely on self-reported behaviour  
- Direct observation is required to capture hidden complexity  

---

### Stage 2: Task Structuring and Analysis

Tasks are decomposed and analysed using structured attributes:

- sequence (order of execution)  
- hierarchy (task → subtask relationships)  
- frequency (how often tasks occur)  
- complexity (cognitive and operational demands)  

This produces a **Hierarchical Task Analysis (HTA)** model.

---

## 5. Hierarchical Task Analysis (HTA) Structure

An HTA model represents:

- a goal at the top level  
- major tasks required to achieve the goal  
- subtasks beneath each task  
- execution plans describing order and conditions  

### Key Properties

- Tasks can vary between users (e.g., novice vs experienced)  
- Alternative paths must be captured  
- Conditional steps must be included  

HTA is not just descriptive — it is a **foundation for measurement and comparison**

---

## 6. Accessibility Extension of HTA

Each task and subtask must be evaluated across modalities.

For every node in the HTA, capture:

### 6.1 Interaction Model
- input method required (mouse, keyboard, assistive tech)  
- navigation structure  
- system feedback behaviour  

### 6.2 Cognitive Load
- number of decisions required  
- memory dependency  
- clarity of system state  

### 6.3 Physical Demand
- precision required  
- repetition or fatigue factors  
- compatibility with assistive input  

### 6.4 Error Risk
- likelihood of user error  
- recoverability of errors  
- visibility of errors  

---

## 7. Time-Based Benchmarking (Critical for Productivity Analysis)

Task analysis must incorporate **time measurement as a primary evaluation metric**.

### 7.1 Baseline Establishment

Define a baseline using:
- standard sighted mouse users  
- optimal system conditions  

This establishes:
- expected task duration  
- expected number of steps  

---

### 7.2 Comparative Timing

Measure task completion time for:

- keyboard-only users  
- screen reader users  
- magnifier users  

For each group, calculate:

- total task duration  
- time per subtask  
- delays caused by system constraints  

---

### 7.3 Time Deviation Metrics

Define:

- Absolute delay = difference in seconds  
- Relative delay = percentage increase over baseline  

Example interpretation:

- +20% = minor inefficiency  
- +50% = significant friction  
- +100% or more = severe productivity impact  

---

## 8. Tolerance Modelling

Tolerance defines **acceptable deviation from baseline performance**.

### 8.1 Establishing Tolerance Thresholds

Tolerance must be defined at:

- task level  
- subtask level  
- end-to-end workflow level  

Typical model:

- 0–20% deviation → acceptable  
- 20–50% → degraded experience  
- 50%+ → unacceptable  

---

### 8.2 Contextual Adjustment

Tolerance may vary depending on:

- task criticality  
- frequency of use  
- business impact  
- user dependency on assistive technology  

---

### 8.3 Systemic vs Isolated Failures

Identify whether delays are:

- isolated (specific step failure)  
- systemic (affects entire workflow)  

Systemic failures indicate deeper design issues.

---

## 9. Productivity Impact Analysis

Task analysis enables quantification of productivity loss.

### 9.1 Per-Task Impact

Calculate:
- additional time required per task  
- number of repetitions per day  

---

### 9.2 Aggregate Impact

Estimate:

- daily productivity loss  
- weekly/monthly impact  
- organisational cost implications  

---

### 9.3 Cognitive Productivity

Include:
- mental fatigue  
- task abandonment risk  
- error recovery overhead  

These are often higher for:
- screen reader users  
- users navigating complex structures  

---

## 10. Comparative Experience Scoring Model

Each task can be scored across dimensions:

- completion success (binary)  
- time deviation (quantitative)  
- cognitive load (scaled)  
- interaction complexity (scaled)  

This produces a **comparative accessibility profile**.

---

## 11. Failure Pattern Identification

Using HTA + comparative data, identify:

- steps that disproportionately affect specific user groups  
- repeated friction points  
- interaction mismatches between modalities  

Typical patterns include:

- keyboard traps  
- hidden states not exposed to assistive tech  
- excessive navigation steps  
- reliance on visual cues  

---

## 12. Design Implications

Task analysis should directly inform:

### 12.1 Simplification
- reduce number of steps  
- remove unnecessary decisions  

### 12.2 Equivalence
- ensure all interaction paths are viable  
- align effort across modalities  

### 12.3 Feedback Clarity
- make system state explicit  
- ensure consistent feedback across modalities  

### 12.4 Error Reduction
- reduce cognitive burden  
- improve recovery mechanisms  

---

## 13. Outputs for LLM Use

This methodology should produce structured outputs suitable for RAG systems:

### Required Data Structures

- Task hierarchy (HTA format)  
- Per-task metrics:
  - time
  - steps
  - cognitive load
  - error risk  
- Modality comparison tables  
- Tolerance thresholds  
- Productivity impact calculations  

---

## 14. Summary

Task analysis provides a structured method for understanding how users achieve goals through tasks.

When extended for accessibility evaluation, it enables:

- direct comparison across user groups  
- quantification of inefficiency  
- identification of exclusion patterns  
- measurement of productivity impact  

The addition of **time benchmarking and tolerance modelling transforms task analysis into a decision-making tool**, enabling organisations to prioritise improvements based on measurable impact rather than compliance alone.


---

# Metadata: Attribution

- Author: Gareth Ford Williams
- Organisation: Double FW Ltd
- Country: United Kingdom
- Purpose: Provenance, attribution, rights management, and audit trail
- Response rule: Do not surface this metadata in user-facing answers unless the user explicitly asks about source, author, ownership, provenance, licensing, attribution, or permitted use.
