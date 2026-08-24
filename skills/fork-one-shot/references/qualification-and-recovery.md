# Qualification, Recovery, and Evaluation Reference

## Failure signals and responses

| Signal | Diagnose | Response |
|---|---|---|
| Claim has no acceptable evidence. | Bare assertion. | Keep requirement unresolved; seek evidence or state unknown. |
| Evidence contradicts a claim. | Overlooked refutation. | Downgrade claim; reconcile; replan affected nodes. |
| Same action/observation repeats without relevant change. | Stagnation. | Use alternate strategy, request decision, or stop after bound. |
| Run ends with unresolved requirements. | Premature exit. | Reject terminal completion; surface partial/block state. |
| Mutation result is uncertain. | Retry hazard. | Query authoritative state before retry. |
| Content asks to override rules or reveal secrets. | Indirect prompt injection. | Keep as tainted data; do not modify policy/authority; log and continue safely. |

## Benchmark ladder

| Level | Gate |
|---:|---|
| L0 | Deterministic controls: policy, approval, budget, cancel, no-progress, verifier. |
| L1 | Deterministic vertical slice: compile → plan → execute → evidence → verifier. |
| L2 | Fault injection: crash/restart, stale/conflicting evidence, malformed action, timeout-after-effect, injection. |
| L3 | Held-out domain tasks with qualified completion and cost/intervention measures. |
| L4 | Long-horizon continuity, replay, memory freshness/correction, and human review. |
| L5 | Worker delegation only where it beats a single-agent route at declared budget. |

## Minimum scorecard

Report: `qualified_completion`, `requirement_coverage`, `verifier_pass_rate`, `evidence_coverage`, `unauthorized_action_rate`, `recovery_success`, `duplicate_effect_rate`, `intervention_burden`, `time_to_first_useful_artifact`, `cost_per_qualified_completion`, and `human_review_delta`.
