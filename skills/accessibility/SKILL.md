---
name: accessibility
description: Design and evaluate AI outputs, interfaces, and workflows for accessibility across sensory, motor, cognitive, linguistic, device, bandwidth, and stress conditions. Use whenever a human-facing result must be broadly usable.
---

# Accessibility

Treat accessibility as part of correctness, not a cosmetic enhancement. Identify users, modalities, assistive technologies, language needs, device constraints, cognitive load, and failure consequences.

Provide equivalent information in appropriate formats: structured text, meaningful headings, captions or transcripts, alt text, keyboard paths, readable contrast, clear labels, predictable focus, plain language, and non-visual or non-audio alternatives. Avoid relying on color, motion, tiny text, timing alone, or unexplained jargon.

For AI interactions, make status, uncertainty, permissions, errors, cancellation, and next actions understandable. Preserve user input and provide recovery. Test with realistic interruptions, slow networks, screen readers, keyboard-only use, zoom, and varied comprehension. Do not infer disability or lower user autonomy because the user requests simplicity.

## Operational deepening

Use this Skill to improve **perception, operation, understanding, and recovery**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is keyboard order, focus visibility, names/roles, contrast, zoom/reflow, reduced motion, and assistive technology paths.

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
