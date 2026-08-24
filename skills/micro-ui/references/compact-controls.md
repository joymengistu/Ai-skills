# Compact Controls

## Core principle

Treat controls as instruments, not advertisements. Favor the smallest visual treatment that preserves clarity, hierarchy, and confidence. Let whitespace create calm; do not enlarge controls merely to occupy space.

| Component | Preferred behavior | Avoid |
|---|---|---|
| Primary action | Use a concise label and restrained visual weight. Example: `+ New`, `Save`, `Share`. | Long marketing labels, full-width CTAs inside tool surfaces, or multiple competing primaries. |
| Secondary action | Use compact text, an outline/subtle treatment, or a familiar icon where the meaning is clear. | Making every action bright, filled, or equally large. |
| Icon button | Pair a familiar icon with tooltip, accessible name, focus state, and hover/pressed feedback. | Obscure glyphs, unlabeled destructive icons, or icon-only actions that require guessing. |
| Toolbar | Group related controls; use sparse separators; keep a clear reading order. | A wall of large buttons or a separate card for every action. |
| Tabs | Use text with a subtle active indicator and stable layout. | Giant tab buttons, drifting indicators, or many equally prominent tabs. |
| Dropdown | Keep labels scannable, show current selection, and use a deliberate menu width. | Huge menus, overly nested menus, or menus that obscure the trigger with no escape route. |
| Sidebar | Use narrow, consistent rows with recognisable active state and logical groups. | Giant navigation cards or treating every destination as a dashboard tile. |
| Card | Use only when it creates a meaningful bounded group or action cluster. | Decorative card stacking, deep shadows, and rounded containers around ordinary lists. |

## Label and shape rules

Write the shortest unambiguous label. Prefer sentence case, a medium weight, and ordinary verbs. Use a text-plus-icon pairing when it improves recognition. Do not use uppercase for emphasis alone.

Default to a modest corner radius that matches the existing system. Strongly pill-shaped components should communicate an actual semantic reason—such as a status token or a single-choice chip—not a default design habit.

## Density without clutter

Information-rich screens need alignment, predictable rhythm, and progressive disclosure. Use rows for repeated objects and reserve cards for truly distinct groups. Keep controls close enough to their content to establish association, while retaining enough surrounding space for scanning and confident selection.

> Compact does not mean crowded. When a control feels cramped, increase local spacing or simplify choices before increasing every control’s height and width.
