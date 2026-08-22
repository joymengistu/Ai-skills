# Peak upgrade design

## Design thesis

The project has reached a strong instruction layer. The next leap is to make the operating model observable, durable, testable, and resistant to repeated side effects. The upgrade should add runtime contracts without pretending that Markdown skills alone enforce them.

## Upgrade package

| Upgrade | Purpose | Primary artifact |
|---|---|---|
| Event and trace contract | Make every meaningful decision and side effect inspectable | `runtime/trace-schema.json` |
| Durable execution | Resume after crashes, delays, approvals, and tool failures | `skills/durable-execution/SKILL.md` |
| Idempotent actions | Prevent retries from duplicating side effects | `core/action-protocol.md` extension |
| Capability-risk gates | Couple usefulness, reliability, safety, control, and recoverability | `governance/capability-risk-matrix.md` |
| Evidence ledger | Track claim provenance, confidence, contradictions, and freshness | `skills/evidence-ledger/SKILL.md` |
| Human feedback loop | Convert corrections into scoped, consent-aware learning | `skills/human-feedback/SKILL.md` |
| Progress and interruption states | Make long work understandable and resumable | `runtime/progress-state-machine.md` |
| Peak regression suite | Detect overclaiming, unsafe retries, lost approvals, and false completion | `evals/cases.jsonl` and `scripts/validate_repo.py` |

## Runtime event contract

Every run can emit events such as `run_started`, `plan_created`, `context_acquired`, `decision_proposed`, `approval_requested`, `approval_received`, `tool_started`, `tool_completed`, `tool_failed`, `checkpoint_saved`, `verification_completed`, `run_paused`, `run_resumed`, `run_completed`, and `run_stopped`.

Each event should include a run ID, monotonic sequence, timestamp, actor, event type, payload, risk class, evidence references, and schema version. Sensitive payloads should be redacted or referenced by secure identifiers. A trace is an audit and debugging record, not a chain-of-thought dump.

## Durable execution contract

Persist after every logical step that changes state or crosses a side-effect boundary. Use idempotency keys for external actions, record intent before execution and result after execution, and make retries distinguishable from new actions. Approval state must survive process restarts and timeouts. If state is missing or integrity is uncertain, fail closed and request review.

## Capability-risk gate

A capability may ship only when it has a named user outcome, acceptance tests, evidence of reliability, a threat model, permission boundaries, recovery behavior, observability, and a human-value measurement plan. The release gate is conjunctive for critical dimensions: a high capability score cannot compensate for an unacceptable safety, privacy, or control score.

## Evidence ledger

Represent claims separately from conclusions. A claim record should include claim ID, text, source or observation, source authority, date, freshness, confidence, counterevidence, dependent decisions, and review status. A conclusion should link to the claims that support it and clearly label inference or hypothesis.

## Human feedback contract

Collect explicit correction, preference, and satisfaction feedback only for a stated purpose. Separate “the answer was wrong” from “the answer was right but hard to use.” Let users inspect, correct, export, and delete learned preferences. Do not silently convert one-off behavior into a permanent profile.

## Progress state machine

Use states `planned → running → waiting_for_context → waiting_for_approval → paused → resuming → verifying → completed`, with terminal `blocked`, `cancelled`, `failed`, and `completed_with_caveats`. Every transition has a cause, actor, timestamp, and next action. Users should see a concise human-readable projection of the state.

## Non-goals

Do not add a feature marketplace, multi-agent swarm, or automatic self-modification merely because they sound advanced. Add them only when a defined user outcome, measurable benefit, safe control model, and maintenance owner exist.
