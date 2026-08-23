---
name: ui-vision
description: Translate vague visual adjectives into observable UI decisions and review screens for professional hierarchy, minimalism, usability, accessibility, restraint, originality, and interaction quality. Use before designing or reviewing a polished interface, especially when the brief says beautiful, professional, minimal, premium, clean, modern, or polished.
---

# UI Vision

Never design from adjectives alone. Translate each adjective into observable properties, constraints, and tests. “Minimal” may mean fewer visible controls, stronger hierarchy, more proportional whitespace, restrained typography, fewer competing surfaces, progressive disclosure, and contextual actions; it does not mean making everything tiny.

Separate the evaluations. Score beauty, professionalism, usability, accessibility, clarity, and intent alignment independently on a 0–10 scale with evidence. A screen can be attractive but immature, or restrained but unusable. Ask what specifically prevents each score from improving.

Before generating components, establish the user’s current task and the three-level hierarchy: primary action, supporting information and controls, and optional functionality. Assign visual weight deliberately through size, contrast, spacing, position, borders, shadows, and motion. Use a restrained palette, coherent type scale, consistent icon family, proportional control sizes, and borders/cards/shadows only when they communicate meaning.

Apply the review sequence: **reference → observe → decompose → measure → abstract → design → remove → test → polish**. Use first-glance, squint, smaller/quieter, and remove-20-percent tests. Check where the user is, what they are doing, and what they can do next. Remove decorative gradients, glass, blobs, meaningless badges, oversized headings, competing CTAs, inconsistent spacing, and unnecessary animation unless each has a real purpose.

Hide system complexity through progressive disclosure. Sophisticated agents, tools, memory, retrieval, browser automation, code execution, planning, and verification may exist underneath; the interface should remain calm and expose detail when it helps the user decide or recover.

For AI interfaces, avoid giant “thinking” displays, decorative robot imagery, enormous prompts, excessive status panels, and noisy activity surfaces. Show concise progress, useful status, uncertainty, controls, and recovery. Treat screenshots and live products as pattern references, not permission to copy protected assets or exact layouts.

## Screenshot-precision handoff

When the user provides a screenshot and asks for HTML, CSS, JavaScript, or a working reconstruction, route to `skills/screenshot-reconstruction/SKILL.md` and `references/screenshot-reconstruction-architecture.md`. Treat the reference image as the primary specification: measure regions, geometry, typography, assets, density, and visible states before designing. Use UI Vision only to clarify intent, accessibility, and interaction quality after reference fidelity is established. Require same-viewport rendering, objective or structured visual comparison, ordered correction, and explicit observed/inferred/approximated/verified status. Do not redesign or beautify a screenshot unless the user explicitly requests a redesign.

## Operational deepening

Use this Skill to improve **turning visual intent into testable interface decisions**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is hierarchy, tokens, density, states, responsive behavior, accessibility, originality, and live review.

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
