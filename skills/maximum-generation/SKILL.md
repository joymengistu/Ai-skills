---
name: maximum-generation
description: Orchestrate evidence-led creative and experiential quality improvement for AI-built products and artifacts. Use when a user asks for an exceptional, memorable, polished, immersive, or non-generic result in a game, website, interface, creative tool, visual product, prototype, or other experience where runtime observation and focused iteration can materially improve the outcome.
---

# Maximum Generation

Use this Skill to improve the **experienced quality** of a real artifact, not merely to make an implementation larger or more decorative. It turns “make it exceptional” into a bounded loop: **generate → observe → critique → score → improve → re-observe → qualify**.

Maximum Generation is a quality-orchestration layer. It does not replace domain Skills, grant authority, generate assets by itself, or prove that a subjective result is universally “best.” It keeps a capable build from stopping at technically functional but generic.

## When to use and when to skip

Use it when a project has enough creative or experiential surface for focused iteration to matter: a game, product UI, visual tool, interactive prototype, world, landing experience, or a high-value artifact that must feel intentional.

Skip it for a small reversible fix, a purely mechanical conversion, an emergency repair, or a task where no artifact can be observed. Use the smallest capable route; do not force a creative-quality loop onto work that has no relevant quality surface.

## Inputs and boundaries

Establish a concise quality brief before building. Capture the outcome, audience/context, desired feeling, primary remembered moment, required functionality, relevant quality dimensions, available observation methods, resources, authority limits, budget, and stop condition. Label a missing material input as an assumption; do not invent a visual identity or claim a user preference.

Treat generated output and self-critique as candidates, not proof. Runtime screenshots, interactions, tests, logs, asset provenance, and human feedback are evidence. The Skill cannot access accounts, spend funds, publish, or create permissions. Do not claim a “10” or exceptional quality without correspondingly strong evidence and, when preference matters, human review.

## Compose the smallest quality route

Choose only the Skills that own a needed capability. Use `skill-composition` or Agent Max to record the route when it is complex.

| Surface | Typical companion route |
|---|---|
| Web product or interface | `ui-ux-pro-max` → `micro-ui` when compact tool UI is relevant → runtime verification. |
| Game or interactive world | `game-dev` → relevant asset/audio tools → runtime verification. |
| Visual or media-heavy artifact | `imagegen` or the relevant media Skill → visual observation. |
| Long, ambiguous, or high-risk build | `ultra-planning-mode` → `fork-one-shot` → focused domain Skill → verification. |
| Qualitative evaluation | `quality-judgment` for criteria/evidence discipline; keep human preference separate. |

Agent Max should consider this Skill when the request includes terms such as **exceptional**, **memorable**, **immersive**, **polished**, **creative**, **visual quality**, **atmosphere**, **wow moment**, or **avoid generic AI output**. It is an optional layer, not a default route for every build.

## 1. Set creative direction before feature work

Write a short direction record. State the intended feeling, remembered moment, distinctive constraint, focal point, visual/interaction language, first-seconds experience, and what to deliberately leave out. Translate noun lists into an experience hypothesis.

Read `references/creative-direction-and-composition.md` before designing a visual surface, environment, world, or interaction-heavy experience.

## 2. Produce an observable first slice

Build the smallest real vertical slice that can be observed. A screenshot, running screen, playable loop, generated asset comparison, browser flow, or tested interaction is stronger than source code or a design claim alone. Do not spend the entire budget planning a perfect result.

## 3. Review quality with evidence

Choose only relevant dimensions and score them individually from 1–10. Record an observation, confidence, and evidence source beside each score. Hard functional, accessibility, safety, and explicit-requirement failures block qualification regardless of a pleasant appearance.

Read `references/quality-review.md` for the scorecard, thresholds, anti-generic signals, and regeneration decisions. Use `templates/quality-loop-record.md` to capture the review.

## 4. Improve the weakest meaningful cause

First remove generic patterns, unclear hierarchy, repetition, lifeless composition, missing feedback, inconsistent visual language, or an absent focal moment. Then make the smallest change that plausibly addresses the observed weakness. Regenerate a component, layout, asset, interaction, or scene only when targeted repair is not enough.

Do not add decoration, features, motion, assets, or agents just to appear sophisticated. Preserve accessibility, performance, user intent, and project constraints while improving quality.

## 5. Re-observe and decide honestly

Repeat the review after a meaningful change. Stop when required checks pass, important relevant dimensions meet the stated threshold, remaining gains are small, or the budget/risk limit is reached. If the artifact cannot be observed or a required dimension remains weak, report a partial result rather than declaring a polished success.

Read `references/iteration-and-stop-rules.md` when deciding whether to repair, regenerate, defer, or stop.

## Completion report

Report the creative direction, route used, initial observation, quality dimensions selected, evidence and scores, targeted improvements, re-observation, terminal decision, and remaining limits. Do not expose hidden reasoning. State plainly whether the result is verified, partial, blocked, or requires human review.

## Non-negotiables

Do not equate feature count, code volume, a successful build, or a self-written compliment with quality. Do not use a universal magic score, repeat empty “make it beautiful” advice, run unlimited loops, or optimize toward a particular game, brand, or competitor. A smaller experience with deliberate composition and satisfying feedback can be superior to a broad but empty one.
