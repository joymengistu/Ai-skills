# Professional UI improvement report

**Baseline:** `eb66066`  
**Focus:** Developer-tool interfaces inspired by publicly observable Replit and Vercel patterns.

## Conclusion

The repository should not copy Replit or Vercel. It should extract reusable principles: a stable shell, clear panel ownership, contextual density, strong local action hierarchy, predictable navigation, state-complete controls, responsive collapse, and reusable design tokens.

Public Replit documentation describes distinct workspace roles such as Canvas, Frames, Elements, Chat, Toolbar, and Library panel [1]. Public Vercel documentation describes a resizable/hideable sidebar, consistent team/project tabs, workflow-prioritized ordering, and mobile navigation designed for one-handed use [2]. Public Vercel Geist guidance separates primary, supporting, destructive, loading, disabled, link, and icon-only button behavior [3]. Public Replit design-system guidance emphasizes reusable components, tokens, brand assets, custom instructions, on-demand Skills, consistency, and ongoing maintenance [4]. These are public observations and recommendations, not proof of universal superiority or exact internal tokens.

## Implemented

| Area | Change |
|---|---|
| UI research | Added Replit, Vercel, and Geist observations to `references/professional-taste-research-notes.md` with FACT/EVIDENCE/INFERENCE/HYPOTHESIS/UNKNOWN labels. |
| Reusable patterns | Added `references/professional-ui-patterns.md` with shell geometry, sidebar and panel ranges, button hierarchy, spacing tokens, density rules, responsive behavior, state completeness, and high-information examples. |
| Professional-taste Skill | Added a focused developer-tool shell route that loads the new reference without duplicating the broader taste model. |
| Benchmarks | Added four cases covering oversized/duplicated navigation, unlabeled compact controls, loading/destructive states, and inappropriate exact-vendor copying. |
| Release controls | Updated manifest and repository validation; no new Skill was added. |

## Starting hypotheses, not vendor claims

The reference suggests starting ranges such as a 240–288 px expanded desktop sidebar, 56–72 px collapsed rail, 48–56 px top bar, 32/36–40/44–48 px button-height tiers, and a 4 px base spacing scale with 8 px grouping rhythm. These values are intentionally labeled as hypotheses to test against content, device, accessibility, and task needs. Exact Replit/Vercel production values remain UNKNOWN.

## Quality gate

A professional UI must pass hierarchy, alignment, spacing, typography, density, consistency, restraint, interaction clarity, accessibility, responsive behavior, zoom/reflow, loading, error, recovery, and task-intent checks. Screenshot-only review cannot establish keyboard behavior, actual touch targets, loading/error behavior, performance, or task completion. A polished appearance must not mask a broken action or inaccessible state.

## Validation

The updated repository validates **61 Skills** and **80 evaluation cases**. The professional UI benchmark manifest now contains 12 cases in its professional-and-human-value family, including the four new cases. Existing reference-host, intelligence-kernel, benchmark-runner, and Skill-level checks remain required.

## References

1. [Replit Design components](https://docs.replit.com/design/core-components)
2. [Vercel — New dashboard navigation available](https://vercel.com/changelog/new-dashboard-navigation-available)
3. [Vercel Geist Button](https://vercel.com/geist/button)
4. [Replit — Setting up a Design System](https://docs.replit.com/teams/custom-design-system)
5. [W3C WCAG 2.2 — Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
