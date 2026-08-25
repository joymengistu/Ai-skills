---
name: prompt-architect
description: Turn a user’s goal into a clear, bounded, reusable prompt with explicit inputs, constraints, output contract, quality checks, and a concise refinement pass. Use when a user asks to make, improve, shorten, structure, or test a prompt for an AI, agent, workflow, creative tool, research task, product build, or repeatable task.
---

# Prompt Architect

Create prompts that reliably communicate an outcome without turning every request into a giant pseudo-system prompt. A strong prompt is a **usable task contract**: it preserves the user’s goal, supplies only relevant context, names constraints, requests an observable output, and says how uncertainty or failure should be handled.

This Skill authors prompt artifacts. It does not modify a host platform’s hidden instructions, grant permissions, reveal private reasoning, guarantee model behavior, or replace runtime safety and verification.

## Choose the prompt depth

| Need | Produce |
|---|---|
| One-off, clear request | A compact prompt with outcome, inputs, constraints, and output format. |
| Ambiguous or multi-step request | A structured prompt with assumptions, acceptance checks, and a focused clarification policy. |
| Reusable agent/workflow prompt | A versioned prompt contract with authority boundaries, evidence needs, failure handling, and test cases. |
| Quality-sensitive build | Compose with `maximum-generation` or `maximum-generation-planning`; do not duplicate their quality loop. |
| Complex product or execution plan | Compose with `requirement-compiler`, `ultra-planning-mode`, or `fork-one-shot`; do not turn the prompt into the runtime. |

## Inputs and boundaries

Capture the intended outcome, target user/audience if relevant, source inputs, non-negotiable requirements, constraints, requested format, available capabilities, and evidence standard. Keep facts, user-provided context, assumptions, optional ideas, and unknowns distinct.

Ask one focused question only when the answer materially changes value, safety, privacy, authority, cost, architecture, or the requested deliverable. Otherwise state a conservative, reversible assumption inside the prompt. Do not fabricate credentials, sources, user data, tool access, completed actions, or test results.

Read `references/prompt-contract.md` when drafting a prompt. Use `templates/prompt-brief.md` for reusable or high-value requests.

## Author the prompt

Write in this order when relevant:

1. **Role and operating stance:** State only the expertise or behavior that changes the work.
2. **Outcome:** Name the observable artifact, decision, or state to produce.
3. **Inputs and context:** Include source material and facts needed for the next decision; omit irrelevant history.
4. **Requirements and constraints:** Preserve explicit needs, non-goals, authority limits, quality bar, budget, and time boundaries.
5. **Process:** Specify only critical steps, checkpoints, or tool/evidence rules; leave valid judgment flexible.
6. **Output contract:** Request the format, sections, files, schema, or decision record the user needs.
7. **Verification and honesty:** Require matching evidence, uncertainty labels, failure handling, and a next safe action.

Do not use a long role-play introduction, repeat the same instruction in several forms, claim the model can do unavailable work, or force hidden chain-of-thought. Prefer short, precise directives over “be amazing,” “think very hard,” or “do everything.”

## Run one critique-and-refinement pass

Before delivering the final prompt, inspect it for intent loss, conflicting instructions, unnecessary length, missing inputs, implicit authority, non-observable success criteria, and vague output. Repair only material defects; do not endlessly rewrite a clear prompt.

Read `references/prompt-review.md` for the rubric and failure patterns. Include an optional compact “why this works” note only when the user would benefit; otherwise return the ready-to-use prompt first.

## Prompt testing

For reusable prompts, add two to five representative test cases: a normal input, a boundary/ambiguous input, and a failure or missing-information input. Specify what a good response should preserve and what it must not claim. Test output quality with real runs when the environment supports it; do not call a prompt proven merely because its wording seems plausible.

Read `references/behavior-tests.md` when building a reusable prompt or prompt library.

## Composition

| Concern | Use alongside | Boundary |
|---|---|---|
| Context selection and compression | `context-engineering` | It controls runtime context budget; Prompt Architect writes the task prompt. |
| Requirements and product scope | `requirement-compiler` | It compiles the full brief; Prompt Architect turns the relevant result into a usable instruction artifact. |
| Complex execution | `ultra-planning-mode` and `fork-one-shot` | They own planning/execution contracts; Prompt Architect does not promise autonomous completion. |
| Experiential quality | `maximum-generation` | It owns observed quality iteration; Prompt Architect expresses the desired task clearly. |

## Completion report

Deliver the final prompt, labeled assumptions if any, the selected prompt depth, and a concise note on what remains unknown or needs testing. For a reusable prompt, provide its test cases and version label. Do not claim that a prompt alone guarantees correctness, access, execution, or exceptional quality.
