---
name: maximum-generation-planning
description: Plan ambitious creative or experiential builds so quality goals, dependencies, evidence, iteration budget, and stop rules reinforce one another. Use when a user asks for Maximum Generation with integrated planning, or when a quality-sensitive game, product, interface, visual tool, world, or prototype has enough uncertainty or dependencies that planning should shape the build before the quality loop begins.
---

# Maximum Generation Planning

Use this companion when a quality-sensitive outcome needs more than a post-build polish pass. It joins **proportionate planning** to **evidence-led creative iteration**:

> direction → quality plan → observable slice → review → focused improvement → replan only where evidence requires it → qualified stop.

It does not replace `maximum-generation`, `ultra-planning-mode`, or `fork-one-shot`. It makes their handoff explicit: planning decides what must be true before an experience can be judged; Maximum Generation improves the observed artifact; One-Shot owns execution state, authority, evidence, and terminal qualification.

## Activate proportionately

Use this Skill when both are true: the outcome has a meaningful creative or experiential quality bar, **and** dependencies/uncertainty make an unplanned build likely to waste effort. Typical cases include an original game, a design-heavy app, a rich creative tool, an interactive world, or a high-value prototype.

Skip it for a small visual tweak, a mechanical conversion, a bug fix with clear reproduction, or a task where the artifact cannot be observed. Use `maximum-generation` alone when the build is already simple and the main need is an observed quality loop. Use `ultra-planning-mode` alone when the risk is primarily security, architecture, or external consequence rather than experienced quality.

## Inputs and boundaries

Record the user outcome, explicit requirements, audience/context, experience promise, remembered moment, constraints, authority limits, available observation methods, quality dimensions, budget, and terminal condition. Keep assumptions visible and reversible.

Plans do not prove quality. A Skill does not grant permissions, make external actions safe, access tools, or establish user preference. Treat screenshots, runtime behavior, tests, logs, asset provenance, and human feedback as evidence; treat a plan and self-critique as hypotheses.

## 1. Select planning depth and quality budget

Choose Compact, Deep, or Ultra depth using `ultra-planning-mode`; choose the smallest depth that changes a decision or reduces a real risk. Then reserve an explicit iteration budget: at least one observable slice, one quality review, and one focused repair for work that claims a strong creative outcome. Do not reserve unlimited polish passes.

Read `references/integrated-quality-plan.md` before planning a new build. Use `templates/quality-execution-plan.md` to record the handoff.

## 2. Build a quality-aware milestone graph

For every milestone, define the user-facing experience intent, functional output, quality dependency, observation method, verifier, failure path, and completion evidence. Make visual identity, composition, interaction feedback, performance, accessibility, and asset generation dependencies explicit only when they materially affect the intended experience.

Build the smallest observable vertical slice early. A feature cannot be considered “polish-ready” until the person can actually see, use, or otherwise experience it.

## 3. Track quality debt separately from feature debt

Maintain a small quality-debt ledger. Quality debt is an observed gap between the experience promise and what a person can currently perceive—for example, an empty focal route, generic hierarchy, repetitive generation, weak feedback, or unclear first seconds. It is not a list of speculative decoration.

Prioritize debt by user impact, evidence strength, dependency criticality, reversibility, and cost. Repair the smallest meaningful cause before adding new features.

Read `references/quality-debt-and-replanning.md` when evidence requires a plan change.

## 4. Execute the quality loop within the plan

After each meaningful slice, hand the artifact to `maximum-generation`: observe, select relevant dimensions, score with evidence, identify the weakest meaningful cause, make a focused improvement, and re-observe. Replan only affected milestones and descendants when evidence exposes a wrong dependency, failed verifier, changed constraint, or high-value quality debt.

Do not use qualitative ambition as a reason to discard requirements, create a generic agent swarm, or redo a working artifact without an observed cause.

## 5. Gate progress and stop honestly

A milestone advances only when its functional acceptance checks pass, the required observation exists, no hard quality/accessibility/reliability blocker remains, and its residual quality debt is explicitly dispositioned. Stop when the experience promise is supported by evidence, the declared quality threshold is met in relevant dimensions, or further work has diminishing value or violates budget/risk limits.

Report **verified**, **partial**, **blocked**, or **deferred**; never use a detailed plan or a self-score as proof of completion.

## Composition

| Need | Owner | Handoff from this companion |
|---|---|---|
| Deep requirements, risks, authority, alternatives | `ultra-planning-mode` | Quality-aware milestone priorities and observable slice requirements. |
| Runtime state, approvals, tools, durable evidence, completion | `fork-one-shot` | Plan graph, quality gates, iteration budget, and replan triggers. |
| Creative direction, critique, scoring, targeted improvement | `maximum-generation` | Observable artifact, selected dimensions, quality debt, and evidence needs. |
| Domain implementation | Relevant game, UI, media, frontend, or product Skill | A bounded milestone with acceptance checks and quality intent. |
| Human preference | User or qualified reviewer | Feedback with context; never substitute model confidence. |

## Completion report

State planning depth, creative direction, selected route, quality-aware milestones, observed slices, evidence and scores, repairs/replans, residual debt, terminal label, and next safe action. Do not expose private reasoning.
