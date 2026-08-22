# ULTRIA and FORK integration map

## Integration decision

The attached documents are treated as user-authored design requirements. Their strongest ideas are integrated as modular, inspectable skills and product doctrine. They are not hidden system prompts, do not override safety or authority boundaries, and do not turn every request into maximum-depth execution.

## Requirement mapping

| Attachment requirement | Ai-skills module | Implementation decision |
|---|---|---|
| Define “best” before claiming it | `skills/superlative-analysis` | Compile superlatives into objectives, constraints, alternatives, evidence, uncertainty, and stopping criteria. |
| Intelligence is multidimensional | `skills/superlative-analysis`, `skills/evaluation` | Score reasoning, planning, adaptation, tools, memory, verification, multimodality, and recovery by task. |
| Frontier is not automatically best | `skills/frontier-research` | Separate capability, maturity, evidence quality, cost, safety, and fit. |
| Comprehensive and exhaustive need stopping criteria | `skills/frontier-research` | Record ecosystems searched, dimensions covered, exclusions, diminishing-returns rule, and residual uncertainty. |
| Deep means mechanism, evidence, failure, dependencies, competition, and improvement | `skills/frontier-research` | Use a layered research ladder and failure analysis before synthesis. |
| Maximize useful quality, not word count | `skills/superlative-analysis`, `skills/communication` | Optimize useful intelligence × coverage × reliability under resource limits. |
| Observe → verify → compare → test → synthesize → challenge → select → improve | `skills/superlative-analysis` | Make the ULTRIA loop a repeatable decision protocol. |
| Human satisfaction is broader than correctness | `skills/human-satisfaction` | Add functional, cognitive, emotional, effort, trust, control, progress, discovery, personal, and completion dimensions. |
| Optimal assistance varies by context | `skills/optimal-assistance` | Decide how much the AI should do, ask, explain, suggest, or stop based on user state, risk, urgency, and reversibility. |
| Intelligence means correct useful action | `skills/orchestration`, `skills/evaluation` | Optimize completed outcomes, not impressive conversations. |
| Good autonomy preserves important human decisions | `skills/safety-governance`, `core/action-protocol.md` | Use permissions, checkpoints, escalation, cancellation, undo, and verification. |
| Personalization without creepiness | `skills/memory`, `skills/optimal-assistance` | Use explicit, scoped, editable, inspectable, deletable memory; do not infer sensitive traits by default. |
| Progress, verification, done, and stop engines | `core/ultra-plan-mode.md`, `skills/evaluation`, `skills/optimal-assistance` | Treat progress, completion, stopping, and verification as first-class state machines. |
| What-if, why-not, 10× better, and magic moments | `skills/product-strategy` | Generate alternatives, challenge conventions, search adjacent disciplines, and keep delight tied to useful outcomes. |
| Feature quality bar and anti-feature-bloat | `skills/product-strategy` | Require meaningful user benefit, clarity, control, safe failure, measurability, and maintainability. |
| Research → define → question → ideate → prototype → test → measure → critique → improve | `skills/product-strategy`, `skills/frontier-research` | Use as a product discovery loop with evidence and held-out tests. |

## Resulting modules

The integration adds six modules:

1. `superlative-analysis`: turns words such as “best,” “maximum,” “frontier,” “deep,” and “optimal” into measurable decision criteria.
2. `frontier-research`: runs systematic research across mature and emerging alternatives while separating evidence from hypothesis.
3. `optimal-assistance`: chooses the right balance of AI initiative, human work, explanation, silence, suggestion, and stopping.
4. `product-strategy`: applies the What-if, Why-not, 10×, magic-moment, quality-bar, and anti-bloat engines.
5. `human-satisfaction`: expands the current skill with completion satisfaction and the user's broader Fork dimensions.
6. `outcome-completion`: verifies that a task is genuinely done and knows when further work is no longer useful.

## Guardrails

The modules must not treat “go to your limit” as permission to generate unlimited text, take unlimited actions, or bypass approvals. They must not treat “find all” as a literal guarantee of completeness. They must not present product hypotheses or psychological claims as established facts without evidence. They must not imitate protected competitor internals or use leaked prompts. They must preserve the user's authority, privacy, safety, and ability to stop or undo consequential work.
