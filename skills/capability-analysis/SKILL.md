---
name: capability-analysis
description: Analyze an agent capability by separating model contribution, harness contribution, tool contribution, state and memory contribution, and unknown or unsupported claims. Use for vendor comparisons, research synthesis, and architecture decisions.
---

# Capability analysis

For each claimed behavior identify the observable result, the model capabilities it may require, the host controls and workflow that may enable it, the tools and data it depends on, the state or memory it needs, and plausible alternative explanations. Label evidence as `confirmed`, `supported`, `inferred`, `speculative`, `unsupported`, or `unknown`.

Do not turn a vendor claim into a universal fact. Distinguish a public product description, a controlled benchmark, an anecdotal demonstration, and a reproducible result. Record source, date, task distribution, missing variables, and confidence. Do not seek or reproduce leaked, private, or hidden prompts or reasoning.

Translate findings into portable contracts: what any capable hosted model can attempt, what the runtime must enforce, what tools must provide, what evaluators must measure, and what remains dependent on model quality. Recommend experiments that isolate one factor at a time and report cost, latency, safety, user effort, and verified outcome quality.

## Operational deepening

Use this Skill to improve **fairly separating model, harness, tools, state, and evaluator effects**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is source quality, confounders, matched tasks, unknown mechanisms, and cautious conclusions.

### Execute

1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.
2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.
3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.
4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.

### Evidence and boundaries

Treat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |
| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |
| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |
| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |
| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |

### Composition and stopping rule

Declare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.
