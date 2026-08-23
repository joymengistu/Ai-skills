# Professional UI taste architecture

## Purpose

Professional UI taste is the ability to make context-appropriate visual and interaction decisions that help people understand, act, recover, and trust. It is not a fixed aesthetic, a collection of fashionable tokens, or a guarantee that restrained screens are usable.

## Evidence boundary

Apple, Material Design, and WCAG provide public principles and measurable accessibility guidance, while HCI research suggests that visual aesthetics can influence perceived usability but does not imply that visual beauty equals task usability.[1] [2] [3] [4] Therefore the evaluator must separate perceived polish from actual task success, accessibility, interaction clarity, and intent alignment.

## Professional taste model

| Dimension | Question | Evidence |
|---|---|---|
| Purpose | What is the user here to accomplish? | Primary task and expected next action. |
| Hierarchy | Can the user identify what matters first, second, and later? | First-glance test, scan path, focus order. |
| Proportion | Do sizes, spacing, and surfaces fit the content and input method? | Measured relationships, responsive states, content samples. |
| Consistency | Do repeated patterns behave and look predictably? | Component/state comparison, keyboard and touch behavior. |
| Density | Is enough useful information visible without overload? | Task completion, scan time, viewport/context, device size. |
| Typography | Does type establish hierarchy and preserve reading flow? | Role usage, line length, wrapping, contrast, zoom/reflow. |
| Restraint | Does each visual element earn its attention and complexity? | Remove-one-element, smaller/quieter, remove-20-percent tests. |
| Interaction clarity | Do controls communicate affordance, state, feedback, and recovery? | Hover/focus/disabled/loading/error/undo states. |
| Accessibility | Can diverse users perceive, operate, understand, and recover? | WCAG checks, keyboard, contrast, reduced motion, screen reader review. |
| Character | Is the interface memorable in a way that serves the product? | Distinctive but purposeful details, not decoration for its own sake. |
| Professional perception | Does the whole feel intentional, credible, calm, and appropriate? | Blind human comparison plus reasons; never a screenshot-only fact. |

## Contextual restraint engine

For every prominent element, ask: what job does it perform; what would become harder if it disappeared; can it be smaller, quieter, or revealed later; does its color communicate state; does its motion convey information; does its container clarify grouping; and does it compete with the primary task? Keep an element when removing it harms comprehension, action, feedback, accessibility, or recovery. Remove or reduce it when it only signals novelty, status, or decorative effort.

## Anti-pattern reasoning

Cards, rounded corners, gradients, glass, shadows, large headings, whitespace, badges, and animation are not inherently amateurish. They become warning signals when they repeat without semantic roles, compete with task hierarchy, reduce usable density, harm contrast or performance, or substitute visual novelty for product clarity. Record the observed symptom, context, user cost, and smallest repair instead of banning a style.

## Review sequence

`brief → task hierarchy → content reality → reference decomposition → tokens → responsive states → micro-states → accessibility → remove/reduce → live interaction → blind review → repair → re-review`.

A screenshot can support hierarchy and surface review, but only a live artifact can establish keyboard behavior, loading/error/recovery states, responsive layout, performance, and actual interaction quality.

## Scoring discipline

Use 0–10 scores for hierarchy, alignment, spacing, typography, density, consistency, restraint, interaction clarity, visual noise, character, accessibility, and professional perception. Every score requires an observable reason and confidence. Report critical blockers separately; never average away a keyboard failure, unreadable text, broken action, or misleading state. Include “not assessable from screenshot” where appropriate.

## References

[1]: https://developer.apple.com/design/human-interface-guidelines/design-principles "Apple Human Interface Guidelines — Design principles"
[2]: https://m3.material.io/styles/typography/applying-type "Material Design 3 — Applying type"
[3]: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html "W3C WCAG 2.2 — Contrast minimum"
[4]: https://www.sciencedirect.com/science/article/pii/S1071581922000647 "Visual aesthetics and user experience: A multiple-session experiment"
