# Action protocol

Represent consequential actions with five states:

| State | Meaning |
|---|---|
| `propose` | Describe the intended action, target, scope, risk, reversibility, and expected evidence. |
| `approve` | Obtain explicit user approval when required by risk or scope. |
| `execute` | Perform the minimum scoped operation. |
| `verify` | Check the actual result independently of the agent's intention. |
| `report` | State the result, evidence, caveats, and rollback or recovery path. |

Every action record should include `intent`, `target`, `risk_class`, `reversible`, `permission`, `expected_evidence`, and `rollback`. Treat legacy bracket tags from CLAI as a transport adapter only; tags do not bypass this protocol.
