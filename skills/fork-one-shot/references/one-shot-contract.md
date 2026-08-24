# One-Shot Contract Reference

## Required records

| Record | Minimum fields |
|---|---|
| Task | `schemaVersion`, ID, outcome, requirements, acceptance checks, authority envelope, budgets, plan revision, state. |
| Milestone node | ID, objective, dependencies, preconditions, capability allowlist, expected outputs, verifier, recovery policy, state. |
| Event | Version, ID, task/node IDs, actor, transition, timestamp, budget delta, causal reference. |
| Evidence | Version, ID, linked claim IDs, origin, source reference, observed time, scope, freshness, integrity, sensitivity. |
| Approval | ID, action digest, proposed effect, scope, destination, risk, expiry, user decision, policy version. |
| Capability | ID/version, input/output schemas, risk class, executor binding, verifier, policy tags, idempotency/reconcile rule. |

## Run states

`received → framing → planned → executing → verifying → repairing/planned → terminal`

Supporting states: `needs_clarification`, `waiting_approval`, and `paused`.

Terminal states: `completed`, `partial`, `blocked`, `cancelled`, `budget_exhausted`.

Only the orchestrator accepts transitions. The model may propose a transition; it may not rewrite events, grant authority, or self-certify `completed`.

## Policy decision sequence

1. Validate task/node state and action schema.
2. Confirm capability is allowlisted for the node and tenant/user scope.
3. Validate action against budget, risk, environment, and semantic policy.
4. Require an action-bound approval if policy says so.
5. Execute through a scoped binding; write a receipt/observation.
6. Reconcile unknown mutation results before retrying.
7. Link evidence to claims; run verifier; advance only after required gates pass.
