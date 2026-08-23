---
name: self-improvement
description: Diagnose agent failures from traces, feedback, and evaluations, then propose bounded, reversible, evidence-backed improvements. Use after observed failures or during controlled optimization.
---

# Self-improvement

Collect a failure example, classify the cause, identify the smallest intervention, predict side effects, and test on held-out cases. Record lessons through `references/memory-lifecycle-contract.md`: keep them conditional, scoped, provenance-linked, reviewable, expiry-aware, and removable rather than treating a single observation as permanent truth. Common causes include poor task framing, missing context, ambiguous tools, stale memory, bad routing, weak verification, unsafe permissions, and communication mismatch.

Prefer changes in this order: improve data/context, clarify tool contracts, adjust routing, add a verifier, refine the skill, then revise the core prompt. Keep a changelog, baseline metrics, confidence, affected cases, rollback, lesson status, promotion evidence, and demotion/forgetting trigger. Do not optimize only for aggregate scores; inspect distributional harm and user experience.

The agent may propose changes, generate patches, or run sandboxed experiments. A human or authorized release process must approve changes to safety, privacy, authority, or evaluation policy.

## Operational deepening

Use this Skill to improve **evidence-backed reversible capability improvement**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is baseline, smallest change, paired tests, regressions, lesson, authorization, and rollback.

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
