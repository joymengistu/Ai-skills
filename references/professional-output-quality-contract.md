# Professional Output-Quality Contract

Professional quality is contextual intentionality under constraints. It is not a fixed aesthetic, a vendor imitation, a high visual score, or a promise of perfection. Judge the output against its users, task, content reality, environment, accessibility needs, and failure cost.

## Quality dimensions

Score only after recording evidence and confidence. Keep blockers separate from averages; a high average cannot cancel a critical failure.

| Dimension | Evidence question | Common blocker |
|---|---|---|
| Outcome clarity | Can the intended user recognize what this helps them do? | Beautiful surface with unclear purpose |
| Hierarchy | Is the next useful action or information obvious? | Competing primary actions |
| Content reality | Does it work with realistic length, density, and edge content? | Placeholder-only quality |
| Interaction clarity | Are affordances, focus, hover, disabled, loading, error, undo, and recovery understandable? | Clickable-looking but inert controls |
| Consistency | Do repeated language, layout, states, and components behave predictably? | Inconsistent patterns that increase learning cost |
| Accessibility | Can people perceive, operate, understand, and recover across relevant inputs and assistive technology? | Contrast, keyboard, semantics, reflow, or focus failure |
| Performance and resilience | Does it remain responsive and recover under expected conditions? | Decorative complexity causing lag or failure |
| Visual craft | Are typography, spacing, alignment, color, density, motion, assets, and proportion intentional? | Ornament competing with task |
| Character | Is distinctiveness purposeful and appropriate to context? | Generic template or novelty without value |
| Trust and transparency | Are system status, permissions, uncertainty, and consequences clear? | Misleading success or hidden commitment |
| Human perception | Does it feel credible, calm, dignified, and easy enough for its users? | User effort or anxiety hidden by polish |

## Review sequence

`context → user outcome → content reality → hierarchy → interaction states → accessibility → performance/resilience → visual craft → character → blind review → repair → re-review`.

For screenshot-only review, label interaction, accessibility, performance, hidden logic, and unseen responsive states `not assessable` unless other evidence exists. For screenshot reconstruction, use fidelity-first rules and do not redesign unusual reference choices without authorization.

## Restraint and differentiation

Remove or quiet an element when it does not improve comprehension, action, feedback, accessibility, trust, recovery, or intentional character. Keep visual density, asymmetry, unusual controls, or ornament when evidence shows that it serves the reference, product identity, information needs, or user task. “Professional” does not mean bland, sparse, rounded, gradient-heavy, or uniform.

## Quality evidence ladder

1. **Intent evidence:** the output matches explicit requirements and audience.
2. **Craft evidence:** visual and structural details are coherent under realistic content.
3. **Usability evidence:** representative users or task tests can complete the intended flow.
4. **Accessibility evidence:** relevant keyboard, focus, contrast, reflow, semantics, and assistive paths are checked.
5. **Resilience evidence:** loading, empty, error, recovery, interruption, and performance cases are observed.
6. **Human-value evidence:** review shows reduced confusion, effort, anxiety, or avoidable friction without manipulation.

Do not infer higher levels from lower levels. A polished screenshot is craft evidence only. A passing build is build-health evidence only. A positive blind review does not prove accessibility or backend correctness.

## Report format

Return the context and definition of professional quality, evidence and confidence by dimension, critical blockers, three highest-leverage repairs, what should remain unchanged, not-assessable properties, and the next validation step. State whether scores are expert judgment, user research, automated checks, or direct runtime observation.

## Boundaries

This contract synthesizes public usability and accessibility guidance with repository policies. It does not create a universal taste metric, replace domain experts or users, or authorize copying another product’s private design language, assets, or tokens.
