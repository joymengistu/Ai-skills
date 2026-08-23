---
name: ultra-plan
description: Run high-rigor, long-horizon planning for difficult, ambiguous, multi-threaded, or high-impact tasks with dependency mapping, context budgeting, risk gates, checkpoints, verification, and resumable execution. Use when the user asks for deep planning or unusually high quality.
---

# Ultra Plan Mode

Use Ultra Plan Mode when extra planning is likely to improve the user's outcome. It is not a command to overthink, reveal private chain-of-thought, or copy a proprietary model. It is a bounded execution protocol.

## Activate selectively

Activate for long-running builds, deep research, ambiguous goals, many dependencies, high-impact decisions, or tasks requiring independent verification. Use Focused or Deep mode for routine reversible work. Deactivate or reduce depth when the task becomes clear.

## Build the preflight

Before acting, record the outcome, definition of done, workstreams, dependencies, unknowns, context map, risk map, resource budget, checkpoints, verification plan, and stop rules. Use `references/task-classification-contract.md` to score ambiguity, consequence, irreversibility, dependency depth, artifact complexity, evidence burden, external effect, and sensitivity before selecting Focused, Deep, or Ultra. Use `references/adaptive-planning-contract.md` to bind the level to budgets, checkpoint fields, escalation/downgrade triggers, recovery, and stop rules. Give the user a concise plan; do not dump private reasoning.

## Run the loop

1. Inspect the workspace and existing decisions.
2. Build a dependency graph and separate discovery, design, execution, verification, and delivery.
3. Route work to the smallest relevant skills and tools.
4. Gather high-signal context progressively and maintain source and assumption ledgers.
5. Act in observable, reversible increments.
6. Ground each next step in actual tool results.
7. Update the user at meaningful milestones and ask at risk-based approval boundaries.
8. Verify outputs with acceptance tests and an independent check for high-impact work.
9. Preserve checkpoints, recover safely from blockers, and close with evidence, uncertainty, changes, tests, and next steps.

## Control overplanning

Use a time, iteration, token, tool-call, delegation, and cost budget. Save checkpoints after planning, meaningful artifacts, before consequential actions, and verification; on resumption reconcile state and external effects before continuing. Prefer a recommendation over an exhaustive survey when the decision is clear. Do not re-derive settled facts, add features beyond scope, or create abstractions for hypothetical requirements. When enough information exists to act safely, act. A high consequence, irreversibility, external-effect, or sensitivity score can require Ultra controls even when the request is short; planning depth never grants permission.

## Safety and human value

Do not cross irreversible, destructive, privacy-sensitive, financial, legal, medical, security-sensitive, production, or external-communication boundaries without the required permission. Keep progress legible, preserve user control, and make recovery possible. Never relax safety or privacy constraints to finish faster or improve a benchmark.

## One-shot execution path

When the user asks for a one-shot, first-pass, or maximum-quality result, read `references/one-shot-execution-prompt.md`. Use it as a transparent execution contract: compile the brief, preserve explicit requirements, choose proportional planning depth, build a thin complete slice, verify the real result, repair the smallest cause, and report verified versus unverified work. One-shot does not mean blind guessing, hidden chain-of-thought, infinite planning, or universal perfection. For simple reversible work, use the focused exception rather than activating the entire Ultra protocol.

## Completion report

Use this compact report:

```text
Outcome: ...
Evidence: ...
Verification: ...
Risks or uncertainty: ...
Files or actions changed: ...
Next step: ...
```

Read `core/ultra-plan-mode.md` for the full protocol and depth-level guidance.

## Operational deepening

Use this Skill to improve **high-rigor but proportional planning**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is preflight, dependencies, context budget, risk, checkpoints, verification, stop rules, and one-shot path.

### Execute

1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.
2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.
3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.
4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.

### Evidence and boundaries

Treat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |
| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |
| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |
| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |
| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |

### Composition and stopping rule

Declare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.
