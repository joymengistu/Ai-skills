---
name: professional-taste
description: Evaluate and improve professional UI quality by separating beauty, professionalism, usability, accessibility, density, restraint, and interaction clarity. Use for screenshot or live-interface reviews, polished product design, AI-generated UI, design-system decisions, and briefs using beautiful, premium, minimal, modern, clean, or professional.
---

# Professional UI taste

Treat taste as contextual judgment supported by observable evidence, not as a fixed visual style. Extend `skills/ui-vision/SKILL.md`; do not replace it or create a generic UI checklist.

## Define the job first

Identify the product, user, task, device, content reality, primary action, risk, and desired feeling. Professional quality is **intentionality under context**: the interface makes important things clear, gives controls appropriate weight, behaves predictably, and uses visual character without competing with the task.

## Review the eleven dimensions

Score each dimension from 0–10 only after naming evidence and confidence. Keep critical blockers separate from averages.

| Dimension | Ask |
|---|---|
| Hierarchy | Can a person identify what matters first, next, and later? |
| Alignment | Do related elements share meaningful edges, baselines, and rhythm? |
| Spacing | Does distance communicate grouping, separation, and priority? |
| Typography | Are roles, scale, weight, line height, wrapping, and readable width appropriate? |
| Density | Is enough useful information available for this task and device without overload? |
| Consistency | Do repeated components, states, labels, and interactions behave predictably? |
| Restraint | Does every prominent element earn its visual weight and complexity? |
| Interaction clarity | Are affordance, focus, hover, disabled, loading, error, and recovery states clear? |
| Accessibility | Can diverse users perceive, operate, understand, and recover? |
| Character | Is distinctiveness purposeful and suitable rather than decorative noise? |
| Professional perception | Does the whole feel credible, calm, intentional, and appropriate? |

If a screenshot cannot establish interaction, responsive, performance, or accessibility facts, report `not assessable from screenshot` rather than guessing.

## Use the restraint engine

For each large heading, card, border, radius, gradient, shadow, badge, icon, animation, whitespace region, and CTA, ask: what job does this do; what would become harder if it disappeared; can it be smaller, quieter, delayed, or revealed progressively; does it communicate state; and does it compete with the primary action? Keep it when removal harms comprehension, action, feedback, accessibility, or recovery. Reduce or remove it when it signals novelty without helping the user.

Do not ban cards, rounding, gradients, glass, large type, whitespace, or animation. Judge repetition, semantic purpose, proportion, content density, contrast, performance, and product context.

## Separate beautiful from professional

A screen may be visually striking yet confusing, inaccessible, slow, generic, or inappropriate. A restrained screen may be professional yet dull or underdesigned. Evaluate aesthetics, usability, accessibility, intent alignment, and task completion independently. Visual attractiveness can influence perceived usability, so a beautiful surface must not be allowed to mask broken behavior.

## Review sequence

Use:

`brief → task hierarchy → content reality → reference decomposition → visual system → responsive states → micro-states → accessibility → remove/reduce → live interaction → blind review → repair → re-review`.

For live work, test first glance, squint/scan path, smaller/quieter, remove-20-percent, keyboard/focus, touch targets, contrast, reduced motion, zoom/reflow, loading, empty, error, undo, and recovery. Use real content rather than placeholder-only screens.

## Report format

Return: overall judgment with uncertainty; strongest evidence; critical blockers; dimension scores with reasons; anti-patterns with context and user cost; three highest-leverage repairs; and what should remain unchanged. Preserve originality and references without copying another product’s exact layout or assets.

## Developer-tool shell patterns

When the product is a developer tool, dashboard, editor, or agent workspace, read `references/professional-ui-patterns.md`. Use its sidebar, top-bar, docked-panel, button, spacing, density, and state-completeness values as starting hypotheses—not fixed vendor measurements. Treat navigation width, collapse behavior, panel ownership, action hierarchy, and mobile navigation as task-dependent variables. Prefer one primary action per local region, explicit labels, visible focus, stable loading states, and accessible icon-only controls.

Public Replit and Vercel references inform the pattern decomposition, but do not copy their exact layout, assets, or private tokens. Record exact vendor measurements as UNKNOWN unless publicly documented.

## Release gate

Do not call an interface professional merely because it looks polished. A serious accessibility, interaction, content hierarchy, misleading-state, or recovery failure is a blocker. Verify the live artifact when possible and use human blind review for professional perception and taste.
