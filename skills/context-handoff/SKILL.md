---
name: context-handoff
description: Preserve the state needed for a fresh agent or context window to continue long-running work without guessing, repeating, or declaring completion early. Use across sessions, model switches, worker handoffs, resets, and compaction.
---

# Context handoff

At the end of each stage, write a compact handoff containing the objective, current status, requirement ledger, decisions, assumptions, artifacts, tests, evidence, failures, unresolved questions, next step, and stop conditions. Keep it in durable storage outside the model context window and outside a disposable worker.

Prefer a clean context reset with a high-signal handoff when the current context is bloated, confused, or showing premature wrap-up. Use compaction only when its transformations are recoverable and preserve the material state. Retrieve context by need rather than dumping the entire history.

Use source control, checkpoints, progress files, and artifact indexes to make work reversible. The next worker must inspect the handoff and current artifact, then verify reality before editing. Never treat a memory note as authorization, a plan as proof of completion, or a prior worker's claim as evidence without checking.

Keep handoffs concise enough to load reliably, but complete enough to prevent loss of goals, constraints, and test status.
