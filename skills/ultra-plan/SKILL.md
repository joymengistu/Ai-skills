---
name: ultra-plan
description: Run high-rigor, long-horizon planning for difficult, ambiguous, multi-threaded, or high-impact tasks with dependency mapping, context budgeting, risk gates, checkpoints, verification, and resumable execution. Use when the user asks for deep planning or unusually high quality.
---

# Ultra Plan Mode

Use Ultra Plan Mode when extra planning is likely to improve the user's outcome. It is not a command to overthink, reveal private chain-of-thought, or copy a proprietary model. It is a bounded execution protocol.

## Activate selectively

Activate for long-running builds, deep research, ambiguous goals, many dependencies, high-impact decisions, or tasks requiring independent verification. Use Focused or Deep mode for routine reversible work. Deactivate or reduce depth when the task becomes clear.

## Build the preflight

Before acting, record the outcome, definition of done, workstreams, dependencies, unknowns, context map, risk map, resource budget, checkpoints, verification plan, and stop rules. Give the user a concise plan; do not dump private reasoning.

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

Use a time, iteration, token, tool-call, delegation, and cost budget. Prefer a recommendation over an exhaustive survey when the decision is clear. Do not re-derive settled facts, add features beyond scope, or create abstractions for hypothetical requirements. When enough information exists to act safely, act.

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
