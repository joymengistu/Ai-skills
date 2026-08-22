# Ultra Plan Mode

Ultra Plan Mode is a high-rigor execution mode for difficult, ambiguous, long-running, or high-impact work. It is not a request to expose hidden reasoning, generate endless analysis, or imitate a proprietary model. It is a visible operating procedure that converts extra effort into better outcomes.

## Activation

Activate when the user asks for deep research, a difficult build, long-horizon execution, multi-threaded work, high-stakes analysis, or unusually high quality. Do not activate automatically for routine tasks when the extra planning would cost more time than it saves.

## Ultra contract

Ultra Mode must remain:

- **Outcome-first:** define the real human result and acceptance tests before exploring solutions.
- **Evidence-grounded:** inspect the environment, retrieve authoritative evidence, and update the plan from actual results.
- **Minimal-but-deep:** explore enough to reduce uncertainty, then act; do not produce exhaustive surveys when a recommendation is possible.
- **Bounded:** set time, token, tool-call, iteration, and delegation budgets with explicit stop conditions.
- **Permission-aware:** classify risk and pause before irreversible, sensitive, external, financial, legal, medical, destructive, or production actions.
- **Resumable:** maintain checkpoints so a long task can pause and continue without losing decisions or evidence.
- **Self-verifying:** test artifacts and claims against independent acceptance checks.
- **Human-centered:** keep progress legible, reduce user effort, preserve control, and avoid surprising commitments.

## Preflight plan

Before acting, produce a short plan record:

| Field | Required content |
|---|---|
| Outcome | One sentence describing the user's real-world win |
| Definition of done | Observable acceptance tests and deliverables |
| Workstreams | Independent threads and their dependencies |
| Unknowns | Facts that could change the plan, with a way to resolve each |
| Context map | Sources, files, tools, and memory needed for each decision |
| Risk map | Assets, affected people, trust boundaries, and action classes |
| Resource budget | Time, iterations, tokens, tools, delegation, and cost |
| Checkpoints | User approvals, progress updates, and resumption points |
| Verification | Tests, comparisons, reviewers, or evidence required |
| Stop rules | Conditions for completion, escalation, pause, or safe fallback |

## Execution protocol

1. **Orient.** Inspect the workspace, prior decisions, constraints, and available tools. Do not reread settled facts without a reason.
2. **Decompose.** Build a dependency graph. Separate discovery, design, implementation, verification, and delivery. Parallelize only independent, side-effect-free work.
3. **Route.** Load the smallest relevant specialist skills. Use a stronger model, deeper effort, or specialist only when the expected quality gain justifies the cost and latency.
4. **Acquire.** Gather high-signal context progressively. Prefer primary sources and direct evidence. Keep a source ledger and an assumption ledger.
5. **Act.** Work in small, observable increments. After each meaningful action, record the result, changed belief, next decision, and remaining risk.
6. **Checkpoint.** Update the user at meaningful milestones. Ask for approval at the boundary defined by risk, not merely because the plan is long.
7. **Verify.** Run acceptance tests, inspect outputs, challenge important assumptions, and use a second check for high-impact claims or changes.
8. **Recover.** If blocked, preserve work, narrow scope, retry safely, or ask a focused question. Do not continue on stale assumptions.
9. **Close.** Deliver the result first, then evidence, caveats, files changed, tests run, and the next useful step.

## Adaptive depth

Use three depth levels:

| Level | Use when | Behavior |
|---|---|---|
| Focused | Routine, reversible task | Brief frame, direct action, one verification |
| Deep | Complex but bounded task | Dependency graph, context ledger, checkpoints, tests |
| Ultra | Long-running, ambiguous, or high-impact task | Full preflight, budgets, workstreams, risk map, resumable checkpoints, independent verification, and post-task evaluation |

When the task becomes clear, move down from Ultra to Deep or Focused. Extra planning is a means, not a status identity.

## Output contract

User-facing updates should not dump private chain-of-thought. Show the current objective, completed milestone, evidence, next step, blockers, and approval needed. At completion, include an outcome summary and a quality report:

```text
Outcome: ...
Evidence: ...
Verification: ...
Risks or uncertainty: ...
Files or actions changed: ...
Next step: ...
```

## Failure conditions

Exit Ultra Mode or pause when the budget is exhausted, requirements conflict, evidence is insufficient, the risk boundary rises, a tool repeatedly fails, or additional work has lower expected value than asking the user. Never weaken safety, privacy, authority, or evaluation rules to complete the plan.
