---
name: staged-execution
description: Execute complex builds in fast, observable stages with a vertical slice, bounded parallel work, integration checkpoints, budgets, and explicit release gates. Use for long-horizon coding, game creation, product development, or multi-agent implementation.
---

# Staged execution

Run the work as waves: brief compilation, architecture, vertical slice, independent feature increments, integration, dynamic verification, repair, and release. Each stage has an entry condition, output, verifier, budget, and stop condition.

Build one thin end-to-end path first. Parallelize only independent, side-effect-free work such as research, asset preparation, test authoring, or isolated modules. Assign one integration owner for shared state and fragile files. Every handoff includes assumptions, artifacts, evidence, failures, and unresolved decisions.

At each checkpoint compare the running artifact to the requirement ledger and capability map. If the vertical slice fails, repair it before adding breadth. If a stage exceeds its budget or reveals an architecture mismatch, pause, re-plan, and preserve the current working state.

Make progress visible without flooding the user. Report what is usable now, what is being built, what is unverified, and what decision or approval is required.

## Operational deepening

Use this Skill to improve **wave-based work with clear entry and exit gates**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is brief, architecture, vertical slice, integration, dynamic verification, repair, and release.

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
