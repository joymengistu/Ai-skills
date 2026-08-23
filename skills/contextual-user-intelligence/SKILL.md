---
name: contextual-user-intelligence
description: Make evidence-based contextual predictions about what a user is trying to accomplish without claiming mind-reading. Use for ambiguity resolution, intent preservation, scoped personalization, context management, communication learning, and adaptive agent workflows.
---

# Contextual user intelligence

Use prediction to reduce friction, not to override the person. Explicit current instructions, safety policy, permissions, and fresh corrections always outrank inference or memory.

## Separate context

Keep three layers distinct:

- **Professional context:** projects, tasks, requirements, objectives, workflows, artifacts, and decisions.
- **Personal context:** explicitly shared stable collaboration preferences such as format, tone, accessibility, and workflow style.
- **Conversation state:** the current objective, recent decisions, active terminology, unresolved questions, immediate task, and recent corrections.

Attach scope, source, freshness, confidence, sensitivity, expiry/review, and correction/deletion paths. Do not mix project facts with personal traits or temporary state with durable preferences.

## Type the prediction

Before adapting, distinguish:

| Prediction | Question |
|---|---|
| Intent | What does the user mean? |
| Output | What form of answer probably helps? |
| Next step | What action may be useful next? |
| Correction | What misunderstanding may occur? |
| Preference | What presentation style may fit? |

For each, keep `prediction`, `evidence`, `confidence`, `alternatives`, `scope`, `expiry`, and `decision`. Model fluency is not evidence of confidence.

## Resolve ambiguity

Consider the literal wording, conversational meaning, active project context, prior terminology, and likely action. Continue with a reversible low-risk interpretation when evidence is strong and correction is easy. Ask one focused question when alternatives change architecture, cost, privacy, safety, external effects, or likely user value. If the user corrects the interpretation, acknowledge it, update only the scoped conversation state, and do not defend the old guess.

Never turn a typo or one-off phrase into a universal substitution. Never infer sensitive characteristics, diagnose psychology, covertly profile, or use an inferred state to pressure engagement.

## Learn from responses safely

Use `prediction → response → reaction/correction → actual-intent estimate → error cause → conditional lesson → held-out evaluation → authorized promotion`. Classify errors as insufficient context, ambiguous language, wrong assumption, stale context, overgeneralization, missed correction, or excessive confidence.

Store lessons only when evidence justifies them. Prefer: “When objective O and context C are active, response Y may help; preserve alternative Z.” Do not let a lesson grant permissions, rewrite foundational behavior, silently promote memory, or directly modify the predictor without review and evaluation.

## Measure quality

Track intent accuracy, unnecessary clarification rate, incorrect-assumption rate, confidence calibration, correction responsiveness, next-step usefulness, user effort, and interruption cost. Optimize high accuracy plus good calibration plus low unnecessary interruption plus easy correction. Do not optimize maximum prediction or message engagement.

## Verification

Before acting on a prediction, check whether the action is consequential, surprising, privacy-sensitive, external, costly, or irreversible. Predictions may shape a draft or offer, but they cannot authorize side effects. Explain meaningful assumptions and make correction easy. Use the reference architecture in `references/contextual-user-intelligence-architecture.md` when the task needs the full contract.

## Operational deepening

Use this Skill to improve **scoped, correctable predictions about user intent and preferences**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is evidence, alternatives, confidence, expiry, correction, sensitivity boundaries, and no authorization.

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
