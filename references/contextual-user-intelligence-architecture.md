# Contextual user-intelligence architecture

## Purpose

Help an agent infer what the user is probably trying to accomplish without claiming mind-reading. Predictions exist to reduce unnecessary friction and improve relevance; they never override explicit user instructions, safety policy, permissions, or fresh corrections.

## Context separation

| Layer | Retain | Do not mix casually |
|---|---|---|
| Professional context | Projects, tasks, requirements, technical goals, workflows, objectives, artifacts, and decisions. | Personal traits or emotional interpretations. |
| Personal context | Explicitly shared stable collaboration preferences such as format, tone, accessibility, and workflow style. | Sensitive characteristics, diagnoses, secrets, or speculative personality labels. |
| Conversation state | Current objective, recent decisions, active terminology, unresolved questions, immediate task, and recent corrections. | Durable preferences or assumptions that outlive the conversation. |

Each item carries scope, source, freshness, confidence, sensitivity, expiry or review rule, and deletion/correction path.

## Typed predictions

Represent predictions separately rather than treating all guesses as one intent score:

| Type | Question | Default caution |
|---|---|---|
| Intent | What does the user mean? | Preserve literal and contextual alternatives. |
| Output | What form probably satisfies them? | Offer a reversible format when uncertainty matters. |
| Next step | What action may be useful next? | Offer as an invitation, never as a commitment. |
| Correction | What misunderstanding may occur? | Make the response easy to correct. |
| Preference | What presentation style may fit? | Use only demonstrated or explicitly stated preferences. |

Every prediction records `prediction`, `evidence`, `confidence`, `alternatives`, `scope`, `expiry`, and `decision`. Confidence is calibrated by observed outcomes, not by model fluency.

## Ambiguity policy

Consider literal, conversational, project-context, terminology, and likely-action interpretations. Continue naturally with a reversible low-risk interpretation when evidence is strong and correction is easy. Ask one focused question when alternatives change architecture, cost, privacy, safety, external effects, or likely user value. Do not turn a typo or one-off phrase into a universal substitution rule.

## Response-learning loop

`prediction → response → user reaction or correction → actual intent estimate → error cause → scoped lesson → held-out evaluation → authorized promotion`.

Classify errors as insufficient context, ambiguous language, wrong assumption, stale context, overgeneralization, missed correction, or excessive confidence. A lesson must retain evidence and alternatives. Prefer conditional lessons such as: “When objective O and context C are active, response pattern Y may be useful; preserve alternative Z.” Never let a lesson directly rewrite the predictor, safety policy, memory authority, or foundational architecture.

## Quality gates

Measure intent accuracy, unnecessary clarification rate, incorrect-assumption rate, confidence calibration, correction responsiveness, next-step usefulness, user effort, and interruption cost. Optimize the conjunction of high accuracy, good calibration, low unnecessary interruption, and easy correction—not maximum prediction or engagement.

## Failure modes

Block sensitive-trait inference, psychological diagnosis, covert profiling, manipulation, stale-memory authority, confident ambiguity, hidden personalization, and predictions that trigger consequential side effects without explicit authorization. If context conflicts, prefer current explicit instructions and pause when the conflict affects safety, privacy, cost, or external action.

## Architectural boundary

Use the existing foundation, intent preservation, context engineering, memory, human feedback, capability discovery, and skill-forging layers. This document adds a typed prediction and response-learning contract; it is not permission to create a self-modifying autonomous user model.
