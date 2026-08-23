---
name: outcome-completion
description: Determine whether an AI task is genuinely complete, useful, verified, and ready for delivery rather than merely producing an impressive conversation. Use before declaring work done, especially for multi-step or tool-using tasks.
---

# Outcome completion

A task is done when the user's defined outcome is achieved and the evidence supports that conclusion. A polished draft, plausible answer, or completed conversation is not proof of completion.

## Completion gate

Use `references/completion-contract.md` for the canonical completion record and status vocabulary. Check:

1. **Outcome:** Did the real-world goal happen?
2. **Acceptance:** Are all must-have criteria satisfied?
3. **Evidence:** What artifact, test, tool result, source, or user confirmation proves it?
4. **Quality:** Is it correct, complete enough, clear, and fit for use?
5. **Safety:** Were permissions, privacy, approvals, and boundaries respected?
6. **Recovery:** Can the user correct, undo, resume, or recover if needed?
7. **Human experience:** Did the work reduce effort, preserve control, and avoid unnecessary friction?
8. **Next step:** Is there a useful follow-up, or should the system stop?

Use the contract statuses `complete`, `complete_with_caveats`, `blocked`, `needs_review`, or `not_started`. Keep outcome, acceptance, evidence, quality, safety, recovery, and human-value gates separate. Never use “done” to hide unresolved risks or missing evidence.

## Done engine

For long work, maintain a checklist of deliverables, tests, unresolved questions, and approvals. Verify important outputs independently. If more work would not materially improve the outcome, stop and explain why. If the user must decide, present the decision clearly instead of silently choosing.

## Stop engine

Stop when acceptance criteria are met, the budget is exhausted, evidence is insufficient, risk increases, the task is blocked, or additional work has diminishing value. Preserve checkpoints and state what would restart the work. Report what passed, what failed, what remains unknown, and what would restart or resolve the work.

Read `contributions/FORK-original.txt` for the user's completion and stop-engine concepts.

## Operational deepening

Use this Skill to improve **closing work only when the outcome is evidenced**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is acceptance, artifact state, quality, safety, recovery, human experience, and status vocabulary.

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
