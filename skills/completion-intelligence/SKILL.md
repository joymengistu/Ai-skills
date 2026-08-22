---
name: completion-intelligence
description: Decide whether a task is genuinely complete rather than merely producing an output, using requirements, tests, runtime behavior, edge cases, quality, safety, and user-goal evidence. Use before declaring any complex task done.
---

# Completion intelligence

Distinguish `output_generated` from `task_complete`. Generated output means files, text, or a demo exist. Completion means the result satisfies the requirement ledger and user goal, passes relevant tests, works through the real journey, handles important states and failures, meets safety and accessibility gates, and is ready for the stated context.

Before closing, inspect explicit requirements, justified inferences, acceptance criteria, dependencies, known edge cases, and deferred work. Verify the running artifact when possible. Record evidence for each material claim and label items as verified, partially verified, unverified, deferred, blocked, or rejected with reason.

Do not mark a feature complete because it compiles, renders, looks impressive, or passed one happy path. Check integration, persistence, errors, loading, empty states, permissions, recovery, responsive behavior, and operational readiness when relevant.

Close with a concise completion report: what works, evidence, what remains, risks, and the next useful action. If the work is not complete, say so and propose the smallest path to completion.
