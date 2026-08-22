---
name: durable-execution
description: Design and operate long-running AI tasks that survive crashes, delays, approvals, retries, and process restarts without losing state or repeating risky side effects. Use for asynchronous agents, scheduled work, multi-day tasks, or any workflow with external actions.
---

# Durable execution

Treat a long-running agent as a durable record, not a fragile conversation. Persist state at logical boundaries and make the run resumable.

## Required contract

Record the run ID, versioned plan, current state, completed work, pending work, approvals, evidence, tool intents, tool results, budgets, and integrity marker. Emit structured events using `runtime/trace-schema.json` and project visible progress through `runtime/progress-state-machine.md`.

Before a side effect, persist intent with a unique idempotency key. After execution, persist the external result and verification. On retry or restart, reconcile the key and known external state before attempting the action again. Do not assume a failed request had no effect.

Persist approval requests and decisions. A waiting run should consume no unnecessary model or tool work; use durable timers or signals where the host runtime supports them. If approval times out, the reviewer is unavailable, or state integrity is uncertain, fail closed and preserve the checkpoint.

## Recovery test

Simulate process crash before execution, during execution, after execution but before recording the result, while waiting for approval, and during verification. Confirm that recovery neither loses user work nor duplicates a side effect. Report unresolved ambiguity instead of fabricating a result.

This skill specifies behavior; the host runtime must provide durable storage, atomicity, access control, timers, and external reconciliation.
