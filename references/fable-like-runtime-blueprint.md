# Portable Fable-like runtime blueprint

## Core idea

The “one-shot” experience is not one prompt. It is a coordinated system: a strong model, a host runtime, tools, reusable skills and templates, a structured requirement compiler, staged execution, persistent state, self-testing, dynamic inspection, and repair. The prompt should make this process reliable and visible, not pretend that the prompt itself contains the whole runtime.

## Fast-detail pipeline

| Stage | Goal | Output | Speed mechanism |
|---|---|---|---|
| 1. Brief compiler | Turn a short idea into explicit requirements, justified inferences, constraints, and unknowns | Requirement ledger and acceptance matrix | Reusable domain schemas and learned patterns |
| 2. Architecture pass | Choose stack, data, state, backend, tools, permissions, and vertical slice | Product/system map | Templates and capability discovery |
| 3. Vertical slice | Implement one end-to-end path | Runnable thin product | Proves integration early |
| 4. Staged expansion | Add independent features in bounded waves | Feature increments | Parallelize only side-effect-free work |
| 5. Dynamic verification | Run the artifact and test intent, usability, build health, and operations | Evidence-linked test report | Automated checks and focused probes |
| 6. Repair loop | Classify failures, patch the smallest cause, rerun affected tests, and prevent regression | Verified repair or escalation | Failure signatures, local context, and targeted retries |
| 7. Release gate | Confirm completeness, safety, accessibility, user value, and rollback | Release decision | Hard gates and explicit caveats |

## Requirement compiler

Every brief becomes a graph of `requirement -> interpretation -> dependency -> artifact -> test -> evidence -> status`. Explicit requirements are mandatory unless rejected with a reason. Inferences are labeled and reversible. Unknowns that change architecture, cost, risk, or user experience become questions or conservative defaults.

## Staged execution

Use waves: discovery, architecture, core slice, independent features, integration, dynamic verification, repair, and release. Keep the integration owner responsible for the source of truth. Do not let parallel agents edit the same fragile files without coordination. Every handoff includes assumptions, evidence, failures, and unresolved decisions.

## Repair loop

1. Observe the failure in the running artifact or evaluator.
2. Classify it as requirement, design, context, implementation, dependency, tool, environment, permission, or verification failure.
3. Reproduce with the smallest useful test.
4. Patch the smallest cause, not the entire project.
5. Rerun the focused test and the relevant regression suite.
6. Update the requirement ledger, trace, and incident record if needed.
7. Escalate when repeated repairs suggest a wrong architecture or insufficient tool/runtime capability.

## Low-cost host blueprint

A practical portable host can start with a local process, filesystem or SQLite state, a model adapter, a tool registry with permission scopes, a skill loader, a JSONL event trace, a simple approval queue, and a test runner. Add durable queues, sandboxing, browser execution, visual evaluation, and distributed workers only when the workload requires them. Keep provider access and user accounts separate from the skill package.

## Product truth

A fast first pass is valuable only when it is a strong first slice, not when it hides omissions. Optimize for time-to-first-usable-result and time-to-verified-complete-result separately. A polished demo can be an excellent prototype; it is not automatically a production system.
