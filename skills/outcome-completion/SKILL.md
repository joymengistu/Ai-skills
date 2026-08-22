---
name: outcome-completion
description: Determine whether an AI task is genuinely complete, useful, verified, and ready for delivery rather than merely producing an impressive conversation. Use before declaring work done, especially for multi-step or tool-using tasks.
---

# Outcome completion

A task is done when the user's defined outcome is achieved and the evidence supports that conclusion. A polished draft, plausible answer, or completed conversation is not proof of completion.

## Completion gate

Check:

1. **Outcome:** Did the real-world goal happen?
2. **Acceptance:** Are all must-have criteria satisfied?
3. **Evidence:** What artifact, test, tool result, source, or user confirmation proves it?
4. **Quality:** Is it correct, complete enough, clear, and fit for use?
5. **Safety:** Were permissions, privacy, approvals, and boundaries respected?
6. **Recovery:** Can the user correct, undo, resume, or recover if needed?
7. **Human experience:** Did the work reduce effort, preserve control, and avoid unnecessary friction?
8. **Next step:** Is there a useful follow-up, or should the system stop?

Use a status such as `complete`, `complete_with_caveats`, `blocked`, `needs_review`, or `not_started`. Never use “done” to hide unresolved risks or missing evidence.

## Done engine

For long work, maintain a checklist of deliverables, tests, unresolved questions, and approvals. Verify important outputs independently. If more work would not materially improve the outcome, stop and explain why. If the user must decide, present the decision clearly instead of silently choosing.

## Stop engine

Stop when acceptance criteria are met, the budget is exhausted, evidence is insufficient, risk increases, the task is blocked, or additional work has diminishing value. Preserve checkpoints and state what would restart the work.

Read `contributions/FORK-original.txt` for the user's completion and stop-engine concepts.
