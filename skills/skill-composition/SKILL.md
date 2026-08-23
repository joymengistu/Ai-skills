---
name: skill-composition
description: Compose a minimal compatible bundle of skills for a goal by checking inputs, outputs, dependencies, ordering, permissions, side effects, evidence flow, and failure recovery. Use when an agent needs multiple capabilities or must build a reusable workflow.
---

# Skill composition

Treat a skill as a contract, not a keyword. For each candidate identify the artifact it consumes, the artifact it produces, required state, dependencies, permissions, risk, verification evidence, and safe failure behavior.

Build a directed workflow. Use sequential composition when later work depends on shared mutable state or previous observations. Use parallel composition only for independent, side-effect-free work with mergeable outputs. Reject bundles with incompatible ports, unresolved dependencies, conflicting permissions, unbounded side effects, duplicate authority, or no recovery path.

Prefer the smallest bundle that covers the requirement ledger. Preserve provenance and version for each component. Pass evidence and uncertainty between skills, not just raw outputs. Keep one owner for shared files, external mutations, contradictions, and final completion judgment.

Before execution, report selected skills, why each is needed, ordering, assumptions, risks, budget, and fallback. After execution, evaluate the composition as a whole; a collection of individually valid skills can still fail through interface mismatch or orchestration overhead.

## Operational deepening

Use this Skill to improve **composing Skills without hidden conflicts**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is typed interfaces, ordering, dependencies, permissions, evidence flow, parallelism, and fallback.

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
