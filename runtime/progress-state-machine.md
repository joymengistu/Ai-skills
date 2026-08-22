# Progress and interruption state machine

## States

`planned → running → waiting_for_context → waiting_for_approval → paused → resuming → verifying → completed`

Terminal states are `blocked`, `cancelled`, `failed`, and `completed_with_caveats`.

## Transition rules

| From | To | Required cause or evidence |
|---|---|---|
| `planned` | `running` | Preconditions satisfied and execution begins |
| `running` | `waiting_for_context` | Required evidence or input is missing |
| `running` | `waiting_for_approval` | A proposed action crosses its approval boundary |
| `running` | `verifying` | Planned work has been executed and needs checks |
| `running` | `paused` | User, system, budget, or scheduler pauses the run |
| `waiting_for_context` | `running` | Context arrives and is validated |
| `waiting_for_approval` | `resuming` | Approval or rejection is recorded |
| `paused` | `resuming` | The same run is restored from an integrity-checked checkpoint |
| `resuming` | `running` | Next step is known and safe to continue |
| `verifying` | `completed` | Acceptance criteria pass with evidence |
| `verifying` | `completed_with_caveats` | Outcome is usable but material uncertainty remains |
| `*` | `blocked` | No safe progress is possible without new information or authority |
| `*` | `cancelled` | User or authorized system cancels the run |
| `*` | `failed` | Execution failed and recovery did not succeed |

## Event requirements

Every transition records the run ID, sequence, timestamp, actor, old state, new state, cause, evidence references, pending approvals, checkpoint reference, and next action. User-facing progress should be a concise projection such as “Verifying 3 of 5 deliverables” rather than an internal trace dump.

## Recovery

Persist state before and after side-effect boundaries. On restart, load the latest integrity-checked checkpoint, reconcile any in-flight idempotency keys, and fail closed if the state or external result is ambiguous. Never restart an unverified side effect as if it were new.
