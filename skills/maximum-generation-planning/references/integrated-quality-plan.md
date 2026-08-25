# Integrated Quality Plan

## Plan before polish, not instead of building

An integrated quality plan should make a product’s creative promise testable early. It is not a lengthy description of a future masterpiece. Every plan detail must change a milestone, dependency, observation, verifier, risk control, or stop decision.

| Plan element | Required question |
|---|---|
| Experience promise | What should a real person feel, understand, or remember? |
| First observable slice | What small working artifact lets us test that promise soon? |
| Quality dependencies | Which functional, visual, interaction, asset, performance, or accessibility prerequisites must exist first? |
| Evidence | What screenshot, interaction, test, log, comparison, or human response could assess the claim? |
| Iteration budget | How many meaningful review-and-repair passes are warranted before diminishing returns? |
| Replan trigger | What observation would prove the current plan wrong? |
| Stop rule | What evidence is sufficient to stop honestly? |

## Quality-aware milestone schema

| Field | Record |
|---|---|
| Milestone and user outcome | |
| Experience intent | |
| Dependencies and preconditions | |
| Smallest observable slice | |
| Relevant quality dimensions | |
| Acceptance checks and verifier | |
| Likely quality debt | |
| Repair/replan trigger | |
| Budget and terminal rule | |

## Good and bad planning distinction

| Pattern | Example |
|---|---|
| Good | “Before adding an inventory, make one playable exploration loop where the landmark, movement feedback, and first objective can be observed and scored.” |
| Bad | “Add trees, shaders, music, particles, inventory, quests, enemies, and polish.” |
| Borderline | “Add particles for atmosphere.” It becomes useful only when the missing atmosphere is observed and particles are the smallest credible repair. |

## Planning depth guard

Choose Compact for a bounded observable surface with few dependencies. Choose Deep when quality depends on multiple systems, assets, or responsive states. Choose Ultra only when the project is uncertain, high impact, cross-session, or contains consequential interfaces. Reduce plan depth once its details stop changing decisions.
