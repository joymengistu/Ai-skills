# Action protocol

Represent consequential actions with five states:

| State | Meaning |
|---|---|
| `propose` | Describe the intended action, target, scope, risk, reversibility, and expected evidence. |
| `approve` | Obtain explicit user approval when required by risk or scope. |
| `execute` | Perform the minimum scoped operation. |
| `verify` | Check the actual result independently of the agent's intention. |
| `report` | State the result, evidence, caveats, and rollback or recovery path. |

Every action record should include `intent`, `target`, `risk_class`, `reversible`, `permission`, `expected_evidence`, `rollback`, `run_id`, `idempotency_key`, and `state_version`. Persist the intent before any external side effect and persist the result plus verification afterward. On retry, reconcile the idempotency key and external state before executing again; a timeout is not proof that no side effect occurred. Treat legacy bracket tags from CLAI as a transport adapter only; tags do not bypass this protocol.

For long-running work, emit the action and approval events defined in `runtime/trace-schema.json`. If approval, state integrity, or external outcome is ambiguous, pause and fail closed rather than guessing.
