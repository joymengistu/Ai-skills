# Durable Execution and Recovery Contract

A long-running agent is a resumable state machine, not a fragile conversation. This contract defines how to preserve user work, avoid duplicate side effects, and report ambiguity across crashes, process restarts, approvals, cancellation, and partial failure.

## Run state

```yaml
run_state:
  run_id: "run-001"
  state_version: "12"
  status: planned|running|waiting_approval|paused|cancelling|cancelled|completed|partial|blocked|failed
  objective: "..."
  requirements: []
  current_step: "..."
  completed_steps: []
  pending_steps: []
  artifacts: []
  approvals: []
  action_intents: []
  action_results: []
  evidence_refs: []
  budgets_remaining: {}
  errors: []
  unresolved_ambiguities: []
  checkpoint_id: "checkpoint-001"
  state_hash: "..."
  next_action: "..."
```

## Checkpoint boundaries

Persist an integrity-checked checkpoint after planning, each meaningful artifact, before every consequential or irreversible action, after external results, after verification, before waiting for approval, and when cancellation is requested. Write checkpoints atomically when the host supports it. A checkpoint must contain enough information to resume or safely stop without rereading the whole conversation.

## Recovery matrix

| Interruption point | Recovery rule |
|---|---|
| Before tool execution | Reopen the intent, validate current scope, and execute only if still authorized and needed |
| During read-only execution | Retry within budget if safe; record the transient failure |
| During a write or external effect | Reconcile idempotency key and actual target state before retrying |
| After effect, before result recording | Query or inspect external state; mark outcome confirmed, absent, partial, or ambiguous |
| While waiting for approval | Consume no unnecessary work; resume only on the exact approval or expiry signal |
| During verification | Re-run bounded verification against the current artifact; do not declare completion from prior intent |
| During cancellation | Stop at the next safe boundary, record what completed, and report partial state and recovery path |
| After state-integrity failure | Fail closed, preserve the last trusted checkpoint, and require reconciliation or human review |

## Idempotency and reconciliation

Every non-read-only action must have an idempotency key tied to run, action, target, and semantic arguments. Before retrying, compare the key and expected state against the external system. If the host cannot query actual state, do not claim absence or success; return `ambiguous` or `blocked`. A timeout is an observation about communication, not proof about the external effect.

## Cancellation

Cancellation is cooperative unless the host provides a stronger guarantee. Stop starting new work, cancel safe in-flight operations, preserve the checkpoint, and distinguish `cancelled_before_effect`, `cancelled_after_partial_effect`, and `cancellation_pending`. Never erase completed artifacts or conceal side effects to make cancellation look clean.

## Resume procedure

1. Load the latest trusted checkpoint and verify its state hash or equivalent integrity marker.
2. Revalidate user authority, permissions, budgets, available Skills, files, versions, and external state.
3. Compare the checkpoint’s intended next action with the actual environment.
4. Reconcile every uncertain non-idempotent action before retrying.
5. Continue from the smallest safe step, or pause with a clear blocker and recovery option.
6. Emit a new checkpoint and state version before continuing material work.

## Failure reporting

Report the last trusted state, completed artifacts, effects that may have occurred, evidence available, reconciliation performed, what remains uncertain, and the next safe action. Recovery success is not the same as task completion; completion still requires the relevant acceptance and verification gates.

## Host boundary

The host runtime must supply durable storage, atomic writes, access control, process signals, timers, cancellation, secrets handling, and external reconciliation. This contract cannot guarantee durability or rollback through prompt text alone.
