---
name: repair-loop
description: Repair incomplete or failing agent-built artifacts through observed reproduction, root-cause classification, minimal patches, focused reruns, regression tests, and safe escalation. Use after build failures, broken interactions, missing requirements, tool errors, or verification failures.
---

# Repair loop

Repair from evidence, not from guesswork. Use `references/verification-repair-report-contract.md` for completion gates, status, repair convergence, and stopping. Observe the failure in the running artifact, trace, test, or user report; preserve the original state; and classify the cause as requirement, architecture, context, implementation, dependency, tool, environment, permission, or verification.

Reproduce with the smallest useful test. Patch the smallest cause that explains the failure. Rerun the focused test, the affected requirement checks, and the relevant regression suite. Update the trace, requirement ledger, evidence, and incident record when the failure is material.

Do not hide missing requirements by weakening tests. Do not repeatedly retry a side effect whose outcome is uncertain; reconcile it through the durable action protocol first. Escalate when repairs reveal a wrong architecture, missing host capability, unsafe permission, or repeated non-convergence.

A repair is complete only when the original failure is gone, related behavior still works, the requirement is verified, and the user-facing status is honest. Stop when the repair converges, the budget ends, the same failure repeats without a new hypothesis, risk rises, or a missing permission, capability, or user decision blocks safe progress.

## Operational deepening

Use this Skill to improve **smallest-cause failure recovery**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is reproduction, classification, patch scope, focused tests, regression tests, evidence, and escalation.

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
