# Task Classification and Proportionality Contract

Use this contract before selecting planning depth, Skill breadth, tool access, or verification effort. Classification is a routing aid, not an authority grant. A high score increases care and evidence; it never permits unsafe or unauthorized action.

## Classification record

```yaml
task_classification:
  outcome: "The real-world result"
  dimensions:
    ambiguity: 0        # unclear intent, competing interpretations
    consequence: 0      # harm if wrong
    irreversibility: 0  # difficulty of undoing the result
    dependency_depth: 0 # number of coupled workstreams or systems
    artifact_complexity: 0
    evidence_burden: 0  # difficulty of proving the result
    external_effect: 0  # impact on external systems or people
    sensitivity: 0      # privacy, credentials, regulated or personal data
  planning_level: focused|deep|ultra
  approval_required: false
  verification_set: []
  budget: {}
  stop_rules: []
  rationale: "Short observable explanation"
```

## Dimension scale

| Score | Meaning |
|---:|---|
| **0** | Clear, low-risk, reversible, local, and easy to verify |
| **1** | Some uncertainty or coupling, but a safe reversible default exists |
| **2** | Material ambiguity, consequence, coupling, evidence burden, external effect, or sensitivity |
| **3** | High-impact, hard to undo, safety/privacy-sensitive, production-facing, or difficult to verify |

Score each dimension independently. Do not hide a critical dimension inside an average.

## Routing algorithm

1. Identify the outcome, artifact, explicit requirements, unknowns, and authority boundary.
2. Score all eight dimensions from 0 to 3 and record the reason for each nonzero score.
3. Set `approval_required: true` whenever consequence, irreversibility, external effect, or sensitivity is 2 or 3, then apply the host’s approval policy before the side effect.
4. Use **Focused** for a routine, reversible task when ambiguity, dependency depth, artifact complexity, and evidence burden are all 0–1 and no critical risk dimension exceeds 1.
5. Use **Deep** when the combined planning dimensions are material, the artifact has coupled parts, or the user requests a robust result; produce a dependency map, context/assumption ledger, checkpoints, and targeted verification.
6. Use **Ultra** when any critical risk dimension is 3, when several dimensions are 2, or when the work is long-running, high-impact, multi-threaded, or hard to verify; add a full preflight, budgets, independent verification, recovery, and resumable state.
7. If the risk is high but the user’s authority or required evidence is missing, pause or narrow the task instead of compensating with more planning.
8. Reduce depth when the task becomes clear or when additional planning costs more than it is likely to save. Record why the level changed.

## Proportional verification

| Planning level | Minimum verification |
|---|---|
| Focused | Direct output check or one smoke test |
| Deep | Acceptance checks for must-haves, high-risk edge states, and one independent or rendered check where relevant |
| Ultra | Full acceptance set, safety/privacy/authority gates, recovery or interruption check, independent critique or comparison, and explicit unresolved-unknowns report |

Verification depth must follow evidence burden and consequence, not the user’s adjective alone. A short request can require Ultra controls; a long but reversible draft may remain Focused.

## Examples

| Task | Classification | Why |
|---|---|---|
| Reformat a local note | Focused | Clear, local, reversible, and easy to inspect |
| Build a working storefront from a brief | Deep | Multiple states, data, errors, persistence, accessibility, and runtime verification |
| Reconstruct a UI from screenshots and make it production-ready | Deep or Ultra | Visual evidence, responsive inference, functional behavior, and separate fidelity/accessibility gates |
| Publish a change to production | Ultra or pause | External effect and irreversibility require authorization, rollback, reconciliation, and live evidence |
| Research a current high-impact medical or financial decision | Ultra or bounded information only | High consequence and evidence burden; personal action requires appropriate safeguards and professional boundaries |

## Anti-patterns

Do not choose Ultra merely to sound capable. Do not choose Focused merely because the prompt is short. Do not average away a high consequence or privacy score. Do not treat planning depth as permission. Do not load every Skill because the task is “maximum.” Do not claim that a route is proportional without recording the dimensions, rationale, budget, verification, and stop rule.

## Human-value check

Classification must include user effort and interruption cost. If two routes achieve comparable verified quality, prefer the route that is clearer, faster, easier to correct, less surprising, and more controllable. Ask one focused question when it prevents expensive rework; otherwise choose a reversible default and state it.
