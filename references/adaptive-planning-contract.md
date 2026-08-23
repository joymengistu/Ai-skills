# Adaptive Planning, Budget, and Checkpoint Contract

Use this contract to turn planning depth into a bounded execution policy. Planning must adapt to risk, uncertainty, evidence burden, user urgency, and observed results. A long mission is not automatically a better mission.

## Planning record

```yaml
planning_record:
  run_id: "run-001"
  classification_ref: "classification-001"
  level: focused|deep|ultra
  outcome: "Real-world result"
  definition_of_done: []
  budgets:
    time_minutes: null
    model_calls: null
    tool_calls: null
    iterations: null
    delegation_units: null
    cost_limit: null
  workstreams: []
  dependencies: []
  context_sources: []
  assumptions: []
  risk_gates: []
  checkpoints: []
  verification_plan: []
  stop_rules: []
  escalation_triggers: []
  downgrade_triggers: []
```

## Level defaults

| Level | Plan | Budget | Checkpoints | Verification |
|---|---|---|---|---|
| **Focused** | Outcome, one or two steps, one risk note | Small explicit bound | Completion checkpoint | Direct check or smoke test |
| **Deep** | Dependencies, context/assumption ledger, vertical slice, failure states | Time, iteration, tool, and cost bounds appropriate to task | Before implementation, after thin slice, before delivery | Must-haves, high-risk edges, and targeted independent check |
| **Ultra** | Full preflight, workstreams, risk map, authority boundaries, recovery plan | Explicit time, model, tool, iteration, delegation, and cost limits | Meaningful milestone and user approval checkpoints | Full acceptance, safety/privacy/authority gates, independent critique, recovery/interruption check |

These are defaults, not universal quotas. Set a lower or higher bound only with a rationale.

## Adaptive control loop

1. Start with the task classification and select the smallest sufficient level.
2. Set budgets before expensive exploration. If the user gives no budget, use conservative host limits and state that they are defaults.
3. Save a checkpoint after planning, after each meaningful artifact, before a consequential action, and after verification.
4. Escalate from Focused to Deep or Ultra when ambiguity, risk, dependency, evidence burden, or failure cost rises; preserve the reason and remaining budget.
5. Downgrade from Ultra to Deep or Focused when the task becomes clear, the high-risk branch is removed, or further planning has diminishing value; do not downgrade away required safety or verification gates.
6. Pause when a required permission, input, source, tool, or decision is missing. A checkpoint is a safe pause, not permission to continue.
7. On resumption, verify the checkpoint hash or state version, reconcile changed files and external state, and do not repeat ambiguous non-idempotent effects.
8. Stop when acceptance passes, the authorized budget ends, evidence is sufficient, risk rises, the user must decide, or expected value becomes low.

## Checkpoint record

```yaml
checkpoint:
  checkpoint_id: "checkpoint-001"
  run_id: "run-001"
  state_version: "7"
  timestamp: "..."
  objective: "..."
  requirements: []
  completed_steps: []
  active_step: "..."
  artifacts: []
  approvals: []
  tool_results: []
  evidence_refs: []
  unresolved_unknowns: []
  failures_and_repairs: []
  budgets_remaining: {}
  next_action: "..."
  stop_conditions: []
  state_hash: "..."
```

## Human-value constraints

Checkpoints must reduce restart cost without flooding the user. Show concise milestone, evidence, blocker, next step, and approval-needed updates. Ask at risk boundaries, not simply because a plan is long. Preserve user control when a route changes scope, cost, privacy, or likely outcome.

## Anti-patterns

Do not silently consume unbounded tools or retries. Do not use “Ultra” as a status identity. Do not create checkpoints that cannot resume safely. Do not claim a checkpoint proves the artifact is complete. Do not downgrade because the budget is inconvenient if a required safety or verification gate remains. Do not keep planning after the decision is clear merely to appear rigorous.
