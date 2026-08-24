---
name: ultra-planning-mode
description: Build a rigorous, proportionate, verification-first execution plan for complex or high-stakes work. Use when a user explicitly asks for Ultra Planning Mode, wants a detailed plan before execution, or needs requirements analysis, dependency mapping, risk controls, architecture alternatives, evidence needs, test strategy, recovery, and measurable completion criteria. Use alongside fork-one-shot to improve planning quality without granting authority or causing endless planning.
---

# Ultra Planning Mode

Use this Skill to make planning **deeper, clearer, and more testable**—not longer for its own sake. Its output is a decision-ready execution contract that makes later work more accurate.

> **Ultra Planning Mode is successful when it reduces avoidable rework, missing requirements, unsafe actions, and false completion. It fails when it delays useful work with decorative detail or invented certainty.**

## Non-negotiable boundaries

- Do not expose private chain-of-thought. Give concise decisions, assumptions, alternatives, evidence needs, and next actions.
- Do not treat a detailed plan as proof that a task will succeed. Plans must change when observations disagree.
- Do not grant permissions, access external accounts, spend money, publish, deploy, delete data, or perform other consequential actions. Planning can identify such actions; the runtime and user must authorize them.
- Do not fabricate user data, research findings, test outcomes, reviews, or implementation status to make a plan feel complete.
- Match depth to risk and uncertainty. A short reversible task should not receive an enterprise architecture document.

## 1. Decide whether Ultra Planning is warranted

Activate the full mode when **two or more** conditions hold: the task has multiple dependencies; the outcome is ambiguous; external effects, security, privacy, money, or compliance matter; multiple interfaces/data stores are involved; work crosses sessions; correctness must be verifiable; failure would be expensive; or the user explicitly requests detailed planning.

Use a compact planning pass when the task is reversible, familiar, local, and objectively testable in a few steps. State the chosen depth and why.

| Depth | Use for | Minimum output |
|---|---|---|
| **Compact** | Small fixes and reversible edits. | Outcome, 3–7 steps, verification, risks. |
| **Deep** | Multi-part product, research, or engineering work. | Outcome contract, requirements, architecture, plan graph, risks, tests, recovery. |
| **Ultra** | High uncertainty, long horizon, multiple systems, or high impact. | Deep plan plus alternatives, dependency map, authority map, budget/stop rules, failure injection, decision log, and plan-quality gate. |

## 2. Compile the outcome contract

Separate user intent from your interpretation. Record:

| Field | Required content |
|---|---|
| Desired outcome | Observable end state or decision. |
| Explicit requirements | Every user-stated feature, constraint, quality bar, and deliverable. |
| Assumptions | Conservative defaults, each labeled and reversible where possible. |
| Non-goals | What the plan will not solve in this increment. |
| Stakeholders | User, users affected, owners, reviewers, or approvers. |
| Acceptance checks | Evidence that would show the outcome works. |
| Authority | Allowed actions, prohibited actions, and approval-required actions. |
| Limits | Time, budget, compute, access, data, tool, and environment constraints. |

Ask a focused question only when the missing answer materially changes risk, value, architecture, or authority. Otherwise use a visible conservative assumption and keep moving.

## 3. Expand requirements without inventing scope

For each requirement, identify the user-facing behavior, system behavior, data/state, failures, accessibility, security/privacy, verification, and completion evidence. Do not add speculative features merely to make the plan look sophisticated.

Create a requirement ledger with one of four states: `planned`, `satisfied`, `deferred with reason`, or `blocked with reason`. A requirement never disappears silently.

## 4. Compare the smallest viable architecture options

Propose 2–3 genuinely distinct options only when the choice matters. For each, state the fit, trade-offs, cost/complexity, risks, and testability. Select one using explicit criteria rather than popularity or aesthetics.

| Decision lens | Ask |
|---|---|
| Value | Does this materially help the stated outcome? |
| Simplicity | Is there a smaller route that achieves the same verified result? |
| Reliability | How does it fail, recover, and expose uncertainty? |
| Security/authority | What credentials, data, or consequential actions does it introduce? |
| Operability | Can it be monitored, tested, repaired, and evolved? |
| Reversibility | Can the user change course without losing important work? |

## 5. Build a dependency-aware execution plan

Group work into milestones, then implementable nodes. Every node must have an objective, dependencies, inputs, outputs, allowed capability/action class, verification, failure path, and completion evidence.

Prefer a small DAG or ordered milestones over a giant flat checklist. Parallelize only work that is independent, evidence-separable, and safe to merge. Preserve critical-path dependencies.

Read `references/planning-contract.md` for node and decision-record schemas, risk scoring, and the plan-quality gate.

## 6. Add risk, authority, and recovery before execution

Identify the highest-impact failure modes first. For each, record early warning, prevention, detection, recovery, owner, and stop/escalation rule.

| Risk class | Required planning behavior |
|---|---|
| **Low / reversible** | Proceed with normal checks and rollback path. |
| **Medium** | Add explicit preconditions, backup/preview, and targeted verification. |
| **High / consequential** | Require a scoped approval before action; define exact impact and reconciliation. |
| **Unknown** | Reduce scope, gather evidence, sandbox, or ask a material question before acting. |

Use **reconcile before retry** for uncertain mutations. If an external action could have happened, query authoritative state before repeating it.

## 7. Define verification from the start

Every milestone needs verification that matches the claim:

- **Code/product:** type checks, unit tests, integration tests, build, browser/user-flow test, accessibility and responsive checks where relevant.
- **Research:** claim–source alignment, source quality, contradiction search, completeness, and uncertainty labeling.
- **Data:** schema validation, constraints, reconciliation, and sample/aggregate checks.
- **External action:** policy/approval receipt, executor receipt, authoritative environment observation, and impact confirmation.

Do not rely solely on self-review. Prefer an environment test, independent verifier, or human review for important claims.

## 8. Run the plan-quality gate

Before execution, reject or repair a plan that has any of these defects:

- Missing explicit requirement, acceptance check, owner, or terminal condition.
- Ambiguous external action or implicit authority.
- Dependency cycle, impossible precondition, or vague milestone.
- No evidence source or verifier for a claimed outcome.
- No failure/recovery path for high-risk or stateful work.
- Detail that does not change a decision, action, check, or risk control.
- A “do everything” scope with no budget, order, or stop rule.

## 9. Hand off to execution cleanly

When used alone, deliver an **Ultra Plan** containing the outcome contract, depth selection, requirement ledger, chosen architecture, milestone DAG, risks/authority map, verification matrix, budget/stop rules, recovery plan, and the first safe action.

When used with `fork-one-shot`, hand over only the structured plan, assumptions, approval classes, verification gates, and recovery rules. The One-Shot runtime owns task state, tool binding, authority enforcement, evidence storage, and terminal qualification.

## Output contract

Return a concise executive summary followed by a structured plan. Label **facts**, **assumptions**, **open questions**, **risks**, and **not assessable** items separately. End with the first safe action and the exact condition that would cause a pause or user decision.
