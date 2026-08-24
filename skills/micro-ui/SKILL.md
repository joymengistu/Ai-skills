---
name: micro-ui
description: Design and review compact, precise, professional interfaces with small-but-usable controls, calm hierarchy, high information efficiency, and accessible responsive behavior. Use when building or refining toolbars, buttons, sidebars, tabs, dropdowns, forms, dashboards, command palettes, or dense productivity UI; apply alongside UI/UX Pro Max for broad UX decisions.
---

# Micro UI

Make an interface feel like a capable tool: **small controls, generous whitespace, clear hierarchy, and no decorative noise**. The goal is not maximum density. It is high information efficiency without making a person squint, hunt, or mis-tap.

## Scope and boundaries

Use Micro UI for application surfaces, not as a universal visual style. It is especially useful for workspaces, editors, dashboards, libraries, developer tools, project lists, and command-driven products.

Apply it together with `ui-ux-pro-max` for product-level UX, accessibility, responsive behavior, and stack guidance. Use `human-value-design` to ensure compactness removes friction rather than hiding needed explanation. Follow an existing approved brand or design system; Micro UI refines control density and interaction hierarchy, not the brand identity.

Do not use compactness to excuse poor touch targets, hidden critical actions, vague iconography, or inaccessible contrast. Never treat a visual control’s size as its interactive hit area.

## Workflow

### 1. Orient the surface

Identify the person’s primary outcome, the one action that deserves emphasis, the likely device, and the density that the work actually requires. Before adding a control, ask whether it is needed, whether its label can be shorter, whether it belongs in the current location, and what happens after it is used.

Read `references/compact-controls.md` before designing toolbars, navigation, buttons, tabs, menus, or icon controls.

### 2. Establish restrained hierarchy

Make the primary action recognizable without turning it into advertising. Prefer short labels such as `+ New`, `Save`, `Share`, or `Run`. Keep secondary actions quiet, group related actions, and move genuinely secondary mobile actions into an overflow menu.

Use typography, order, spacing, and contrast to establish hierarchy before increasing button size, saturation, border radius, or shadow. Default to subtle rounded rectangles rather than oversized pills. Use cards only when they improve grouping; a plain row is often clearer.

### 3. Preserve compact usability

Keep visible controls compact, but provide adequate keyboard and touch interaction areas. Every icon-only action needs an accessible name, tooltip, focus indicator, and unmistakable meaning. Avoid icon-only controls for destructive, unfamiliar, or high-consequence actions.

Read `references/responsive-accessibility.md` whenever the UI includes a phone layout, touch input, icon controls, a dense toolbar, a dropdown, or a keyboard flow.

### 4. Review the actual screen

Inspect the implementation at its target desktop and mobile widths. Ask whether the primary action is clear, controls feel oversized, content has breathing room, secondary actions are discoverable, and the UI has become generic AI SaaS decoration.

Read `references/review-checklist.md` before delivery. Fix the most consequential usability and accessibility issues first, then remove visual excess.

## Decision rules

| Situation | Default decision |
|---|---|
| Toolbar action, filter, tab, nav item, status control | Use a compact visual control with clear grouping and space around it. |
| Important creation, save, or submit action | Use a restrained medium-weight primary control, not a full-width slogan CTA. |
| Multiple secondary actions on mobile | Preserve the primary action and move the rest into a labelled or well-signposted overflow. |
| Obvious standard action | Use a familiar icon with tooltip and accessible label. |
| Unfamiliar, destructive, or consequential action | Use text or text-plus-icon; make consequence and recovery clear. |
| Dense information list | Prefer aligned rows, concise metadata, and progressive disclosure over oversized cards. |
| Empty space | Keep it when it improves scanning; do not fill it with controls or decoration. |

## Non-negotiables

Never automatically generate giant gradient buttons, repeated uppercase calls to action, oversized pills, card-within-card layouts, rainbow gradients, glow-heavy glassmorphism, dramatic hover scaling, fake futuristic controls, or giant floating actions. A primary action may be stronger than its neighbors, but it should still feel calm and precise.

Use motion only to clarify state. Keep transitions short and subtle, respect reduced-motion preferences, and never rely on hover for essential information or controls.

## Completion standard

The surface passes when a real person can quickly identify where they are, what matters most, what each visible control does, and how to recover from an error. It should feel **sharp, calm, premium, fast, and intentional**—not cramped, shouty, or generic.
