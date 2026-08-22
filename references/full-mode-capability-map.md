# Full-mode capability map

## Design goal

Move Ai-skills from a strong instruction library toward a portable agent operating specification with a skill lifecycle, runtime contracts, evidence discipline, and human-centered control. Add capabilities only when they improve a defined user outcome and can be evaluated safely.

## Capability layers

| Layer | Capability family | Full-mode addition |
|---|---|---|
| Meaning | Intent, superlatives, outcome framing | `superlative-analysis`, `task-framing`, `outcome-completion` |
| Strategy | Planning, orchestration, product thinking | `ultra-plan`, `product-strategy`, `orchestration` |
| Knowledge | Research, context, evidence, memory | `frontier-research`, `evidence-ledger`, `context-engineering`, `memory` |
| Action | Tools, code, data, creative work | Existing domain skills plus tool contracts |
| Runtime | State, progress, cancellation, durability | Trace schema, progress state machine, durable execution |
| Human layer | Optimal assistance, feedback, interaction, accessibility | `optimal-assistance`, `human-feedback`, `human-satisfaction`, `interaction-design` |
| Governance | Safety, privacy, risk, release | Safety skill plus capability-risk matrix |
| Evolution | Skill creation, evaluation, self-improvement | `skill-forging`, `evaluation`, `self-improvement` |
| Portability | Resources, prompts, tools, discovery | Capability manifest and MCP-compatible boundary guidance |

## Skill-forging lifecycle

**Discover gap → frame user outcome → design trigger and scope → choose progressive disclosure → write skill → add resources → define permissions and risks → create representative and adversarial tests → validate metadata → package/version → observe usage → improve or retire.**

A skill is not complete when its Markdown is eloquent. It is complete when another agent can discover it, know when to use it, follow its bounded workflow, fail safely, and be evaluated against a measurable outcome.

## “Skill for anything” rule

Do not create an unbounded skill that claims to cover everything. Create a routing or meta-skill that can forge specialized skills for new domains. Keep universal behavior in the operating contract; keep domain-specific procedures in focused packages; keep large references outside the core skill body.

## Full-mode release rule

A release can add breadth only if it also adds discoverability, scope boundaries, tests, human-value criteria, safety controls, and maintenance ownership. Prefer a smaller set of composable, reliable skills over a catalog that no agent can navigate.
