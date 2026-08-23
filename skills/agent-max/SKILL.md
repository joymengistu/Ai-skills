---
name: agent-max
description: Universal single-entry command and Skill router for invoking the Ai-skills capability library through one button, a slash command, or a short natural-language request. Use when the user says Agent Max, clicks an Agent Max action, types `/agent-max`, or wants the system to choose and load only the Skills needed for a build, research, screenshot, or verification task.
---

# Agent Max

Use Agent Max as the **single universal entry point** for the Ai-skills library, not as a second library of instructions. The user should not need to know or name downstream Skills. Translate a button action, `/agent-max` slash command, `Agent Max` message, or natural-language request into the smallest sufficient ordered bundle of existing Skills in the Ai-skills package.

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
2. Select one preset or compose the smallest relevant Skills from the routing map below. Do not load all Skills by default.
3. Load the named `SKILL.md` files from the current Ai-skills installation, normally `/home/ubuntu/skills/ai-skills/skills/<skill-name>/SKILL.md`. In a repository checkout, use `skills/<skill-name>/SKILL.md`.
4. Preserve explicit requirements. Treat inferred choices as reversible and label unknowns.
5. Return the selected route before execution when the task is complex, consequential, or ambiguous.
6. Execute with the selected Skills, verify the real outcome, repair focused failures, and report evidence and remaining limits.

Agent Max routes work; it does not grant permissions, bypass approvals, invent tools, expose private reasoning, or declare success without evidence. Runtime controls and the host system remain authoritative.

## Short commands and button IDs

These stable commands are suitable for chat prompts, command palettes, or buttons. A UI may display one universal **Agent Max** label and submit the corresponding command ID; the user does not need to select a downstream Skill.

| Button label | Command ID | Ordered route |
|---|---|---|
| Agent Max | `agent-max.auto` | Select the smallest sufficient route from the request, then verify the outcome |
| Load Ai-skills | `agent-max.catalog` | Load the umbrella router and list relevant Skills; do not load the full catalog blindly |
| Screenshot precision | `agent-max.screenshot` | `screenshot-reconstruction` → `requirement-compiler` if functional scope exists → `product-completeness` → `dynamic-verification` → `accessibility`; `professional-taste` is secondary |
| Build complete product | `agent-max.product` | `intent-preservation` → `requirement-compiler` → `product-completeness` → domain/build Skill → `dynamic-verification` → `outcome-completion` |
| One-shot build | `agent-max.oneshot` | `task-framing` → `planning` → `requirement-compiler` → `build-recipes` → `staged-execution` → `dynamic-verification` → `repair-loop` → `completion-intelligence` |
| Research deeply | `agent-max.research` | `task-framing` → `frontier-research` → `evidence-ledger` → `evaluation` → `communication` |
| Verify and repair | `agent-max.verify` | `dynamic-verification` → `evidence-ledger` → `repair-loop` → `outcome-completion` |
| Find a Skill | `agent-max.find <name-or-goal>` | Search the catalog and return matching Skill paths, triggers, conflicts, and a recommended minimal bundle |

Button IDs are routing vocabulary, not executable APIs. The surrounding host or application must bind a button to a prompt or action and enforce permissions.

## Routing rules

Use `agent-max.auto` as the default route for every request that enters through the universal button or `/agent-max`. Do not ask the user to choose a downstream Skill unless the user explicitly wants to inspect the catalog. Add `task-framing` and `intent-preservation` for ambiguous or high-value requests. Add `requirement-compiler` before complex builds. Add `product-completeness` when the user asks for a working app, game, store, tool, or backend-backed experience. Add `dynamic-verification` whenever runtime behavior matters.

For a supplied screenshot or reference image, use `agent-max.screenshot`. Load `screenshot-reconstruction` first and treat the reference as the visual specification. Measure geometry, typography, assets, regions, density, and viewport; render at the same viewport; compare or diff; repair in priority order; and record observed, inferred, approximated, verified, and not-assessable claims. Never let Professional UI Taste redesign an unusual reference unless redesign is explicitly requested.

For research, keep facts, evidence, inferences, hypotheses, and unknowns distinct. For actions affecting external systems, load the relevant safety and approval Skills and stop for required user confirmation. For accessibility or human-facing output, add `accessibility` and the relevant communication or human-value Skill.

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
