---
name: agent-max
description: Universal single-entry command and Skill router for invoking the Ai-skills capability library through one button, a slash command, or a short natural-language request. Use when the user says Agent Max, asks Manus to use AI Skills on itself, clicks an Agent Max action, types `/agent-max`, or wants the system to choose and load only the Skills needed for a build, research, screenshot, or verification task.
---

# Agent Max

Use Agent Max as the **single universal entry point** for the Ai-skills library, not as a second library of instructions. The user should not need to know or name downstream Skills. Translate a button action, `/agent-max` slash command, `Agent Max` message, or natural-language request into the smallest sufficient ordered bundle of existing Skills in the Ai-skills package. For complex or consequential routing, use `references/agent-max-governed-routing.md` to record route purpose, selected Skills, handoffs, conflicts, permissions, fallback, execution state, verification, and uncertainty.

## Universal invocation

Expose one user-facing action wherever the host supports custom Skills or commands:

| Surface | Canonical invocation | Meaning |
|---|---|---|
| Button | `Agent Max` | Route the attached request automatically |
| Slash command | `/agent-max <request>` | Use Agent Max for the request |
| Short message | `Agent Max: <request>` | Use Agent Max for the request |
| Empty invocation | `/agent-max` | Ask for the user’s goal, then route it |

The host may bind the button or slash command to `agent-max.auto`. The Skill itself supplies the routing contract; it does not register a platform button, alter Manus’s immutable core, or create permissions. After installation, the user invokes only Agent Max, while Agent Max internally loads the referenced Skills as needed.

## Core contract

1. Identify the user’s outcome, artifact, constraints, reference inputs, and authority boundary.
2. Create a route record when complexity or consequence warrants it; select one preset or compose the smallest relevant Skills from the routing map below. Do not load all Skills by default.
3. Load the named `SKILL.md` files from the current Ai-skills installation, normally `/home/ubuntu/skills/ai-skills/skills/<skill-name>/SKILL.md`. In a repository checkout, use `skills/<skill-name>/SKILL.md`.
4. Preserve explicit requirements. Treat inferred choices as reversible and label unknowns.
5. Return the selected route before execution when the task is complex, consequential, or ambiguous.
6. Execute with the selected Skills, verify the real outcome, repair focused failures, and report evidence and remaining limits. Reconcile the planned route with the Skills actually loaded, artifacts produced, checks run, and fallbacks used.

Agent Max routes work; it does not grant permissions, bypass approvals, invent tools, expose private reasoning, or declare success without evidence. Runtime controls and the host system remain authoritative.

## Manus self-use mode

When the user says “use AI Skills on yourself,” “update the Skill,” “run Agent Max on this task,” or equivalent, interpret it as **apply the installed routing and evidence contracts to the current task**, not as permission to rewrite Manus’s hidden system prompt, immutable host behavior, model weights, native UI, or authorization controls. Use command ID `agent-max.self` for this mode.

1. Inspect the current request, relevant artifact, available Skills, host capabilities, constraints, and authority boundary.
2. Select the smallest sufficient route and load only the relevant installed Skills. Prefer `/home/ubuntu/skills/ai-skills/skills/<skill-name>/SKILL.md`; if unavailable, use the repository checkout or report a reduced route.
3. For a consequential or multi-step update, show a compact route preview, preserve the user’s explicit requirements, and use bounded planning, checkpoints, repair, and regression verification.
4. Apply the selected contracts to Manus’s current work: intent, evidence, tools, memory, safety, human value, artifact quality, and completion status as relevant. Do not create a self-referential loop merely to appear more capable.
5. Report what was applied, what actually changed, checks performed, remaining uncertainty, and host-level limits. A loaded Skill is guidance, not proof that Manus changed internally.

## Short commands and button IDs

These stable commands are suitable for chat prompts, command palettes, or buttons. A UI may display one universal **Agent Max** label and submit the corresponding command ID; the user does not need to select a downstream Skill.

| Button label | Command ID | Ordered route |
|---|---|---|
| Agent Max | `agent-max.auto` | Select the smallest sufficient route from the request, then verify the outcome |
| Load Ai-skills | `agent-max.catalog` | Load the umbrella router and list relevant Skills; do not load the full catalog blindly |
| Use on Manus | `agent-max.self` | Apply the minimal relevant AI Skills route to the current Manus task; do not claim hidden self-modification |
| Screenshot precision | `agent-max.screenshot` | `screenshot-reconstruction` → `requirement-compiler` if functional scope exists → `product-completeness` → `dynamic-verification` → `accessibility`; `professional-taste` is secondary |
| Build complete product | `agent-max.product` | `intent-preservation` → `requirement-compiler` → `product-completeness` → domain/build Skill → `dynamic-verification` → `outcome-completion` |
| One-shot build | `agent-max.oneshot` | `task-framing` → `planning` → `requirement-compiler` → `build-recipes` → `staged-execution` → `dynamic-verification` → `repair-loop` → `completion-intelligence` |
| Research deeply | `agent-max.research` | `task-framing` → `frontier-research` → `evidence-ledger` → `evaluation` → `communication` |
| Verify and repair | `agent-max.verify` | `dynamic-verification` → `evidence-ledger` → `repair-loop` → `outcome-completion` |
| Find a Skill | `agent-max.find <name-or-goal>` | Search the catalog and return matching Skill paths, triggers, conflicts, and a recommended minimal bundle |

Button IDs are routing vocabulary, not executable APIs. The surrounding host or application must bind a button to a prompt or action and enforce permissions.

## Routing rules

Use `agent-max.auto` as the default route for every request that enters through the universal button or `/agent-max`; use `agent-max.self` when the user explicitly asks Manus to apply AI Skills to itself or update the Skill. Do not ask the user to choose a downstream Skill unless the user explicitly wants to inspect the catalog. Load `references/task-classification-contract.md` to score ambiguity, consequence, irreversibility, dependency depth, artifact complexity, evidence burden, external effect, and sensitivity; use the result to choose Focused, Deep, or Ultra planning and the appropriate approvals. Add `task-framing` and `intent-preservation` for ambiguous or high-value requests. Add `requirement-compiler` before complex builds. Add `product-completeness` when the user asks for a working app, game, store, tool, or backend-backed experience. Add `dynamic-verification` whenever runtime behavior matters.

For a supplied screenshot or reference image, use `agent-max.screenshot`. Load `screenshot-reconstruction` first and treat the reference as the visual specification. Measure geometry, typography, assets, regions, density, and viewport; render at the same viewport; compare or diff; repair in priority order; and record observed, inferred, approximated, verified, and not-assessable claims. Never let Professional UI Taste redesign an unusual reference unless redesign is explicitly requested.

For research, keep facts, evidence, inferences, hypotheses, and unknowns distinct. For actions affecting external systems, load the relevant safety and approval Skills and stop for required user confirmation. For accessibility or human-facing output, add `accessibility` and the relevant communication or human-value Skill. When the request uses “best,” “maximum,” “top tier,” “perfect,” “go to your limit,” or similar language, load `references/quality-vocabulary.md` and convert the intensifier into a target, scope, constraints, evidence standard, budget, and stopping rule. Never interpret it as unlimited resources or authority.

## Button-action output contract

For every button or command, produce a compact route preview:

```text
Agent Max route
Command: agent-max.screenshot
Goal: faithful screenshot-driven working interface
Skills: screenshot-reconstruction → requirement-compiler → product-completeness → dynamic-verification → accessibility
Checks: same-viewport visual diff; functional journey; state/error behavior; accessibility path
Unknowns: hidden interactions and unseen responsive states require separate evidence
```

Then execute only after required inputs and permissions are available. At completion, report the route used, artifacts produced, checks passed or failed, repairs made, and unresolved uncertainty.

## Direct invocation examples

Use prompts such as:

> Click **Agent Max** and use this reference to reconstruct the interface faithfully. Do not redesign it.

> `/agent-max Build this product from the brief and choose the right Skills automatically.`

> Run `agent-max.product` on this flower-pot shop brief. Preserve every explicit requirement and build a working vertical slice with states, persistence, accessibility, and verification.

> Run `agent-max.find screenshot precision` and show me the minimum Skills and their file paths.

> Run `agent-max.verify` on the current artifact. Do not equate a successful build or attractive screenshot with a verified product.

> Use AI Skills on yourself for this task. Apply the minimal route, show what changed, and state what remains outside the Skill’s authority.

## Failure and fallback

If a requested Skill or path is unavailable, report the missing capability and continue only with a clearly labeled reduced route. Do not pretend that a route loaded. If the request matches multiple presets, choose the narrowest one and explain the choice. If the user asks to load everything, first offer the catalog route and load only the Skills needed for the stated outcome unless the user explicitly needs a full audit.

## Catalog pointers

- Umbrella router: `/home/ubuntu/skills/ai-skills/SKILL.md`
- Manifest: `/home/ubuntu/skills/ai-skills/manifest.yaml`
- Skill directory: `/home/ubuntu/skills/ai-skills/skills/`
- Screenshot route: `/home/ubuntu/skills/ai-skills/skills/screenshot-reconstruction/SKILL.md`
- Repository source: `https://github.com/joymengistu/Ai-skills` (private)

Keep this Skill small. Detailed domain behavior belongs in the referenced Skills, not in Agent Max.

## Operational deepening

Use this Skill to improve **short-command routing into reliable, composable workflows**. Load it when a user invokes Agent Max, a command ID, a command palette action, or asks which Ai-skills to use. The main review surface is route selection, minimal loading, typed handoff, permission boundaries, verification, and honest fallback.

### Execute

1. Parse the command and request; identify the outcome, required artifact, inputs, constraints, and authority boundary.
2. Select the narrowest preset or Skill bundle; show the route preview for complex or consequential work.
3. Load only the referenced Skills, preserve explicit requirements, and keep visual, functional, accessibility, and safety acceptance distinct.
4. Verify the real outcome, repair focused failures, and record missing Skills, uncertainty, and evidence.
5. In `agent-max.self` mode, report applied Skills and contracts, actual changes, validation evidence, and immutable host limits; never report internal Manus modification unless the host provides explicit evidence.

### Evidence and boundaries

Treat a route preview as a plan, not proof of execution. Do not claim a button created behavior unless the host actually bound and ran it. Do not grant permissions, bypass approvals, load confidential material, or replace the host runtime’s safety and authorization controls.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Map `agent-max.screenshot` to the dedicated reconstruction Skill first, then add only the functional and accessibility checks the request requires. |
| BAD EXAMPLE | Load all Skills for every button, or claim that a command ID is an executable API without a host binding. |
| BORDERLINE EXAMPLE | A broad preset seems helpful but duplicates domain guidance; prefer the narrower route and add a Skill only when its acceptance check is relevant. |
| EXCEPTION | For `agent-max.find`, return catalog paths and triggers without loading or executing the matched Skills. |
| TRANSFORMATION | Convert “make it max” into a named route, selected Skills, expected checks, permissions, fallback, and completion evidence. |

### Composition and stopping rule

Declare the selected route, expected handoff, conflicts, permissions, and evidence before execution when risk or ambiguity warrants it. Stop when the requested route is selected, the relevant acceptance checks pass, or the host reports that a binding, input, permission, or Skill is unavailable.
