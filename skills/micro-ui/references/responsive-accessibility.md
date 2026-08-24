# Responsive Accessibility

## Small visual controls, usable interaction targets

Keep compact controls visually restrained while ensuring their interactive area is comfortable for touch and keyboard use. On touch layouts, target an interaction area of approximately 44 × 44 CSS pixels where practical; use transparent padding, a wrapper, or an expanded hit area rather than making every visible icon huge.

| Concern | Required handling |
|---|---|
| Icon-only control | Provide a descriptive accessible name, tooltip, visible keyboard focus, distinct pressed/disabled state, and a familiar icon. |
| Keyboard use | Preserve logical tab order, activate standard controls with expected keys, and avoid focus traps outside deliberate dialogs/menus. |
| Focus visibility | Ensure focus is visible against every relevant surface and is not hidden by sticky headers, drawers, or overflow. |
| Hover | Use hover only as enhancement. Essential labels, status, and actions must remain available to touch and keyboard users. |
| Contrast | Maintain readable label/icon contrast in resting, hover, active, disabled, and focus states. |
| Mobile toolbar | Keep the main action visible; collapse secondary actions into an overflow; avoid horizontal scrolling or clipped action labels. |
| Content density | Preserve readable type, line height, and row separation. Do not shrink body copy solely to fit more content. |

## Responsive decision sequence

1. Preserve the user’s current task and the primary action.
2. Remove duplicate decoration and low-value secondary controls.
3. Move truly secondary actions into overflow with a clear route back.
4. Reflow information into readable rows or sections; do not simply shrink everything.
5. Verify touch, keyboard, focus, error, loading, and empty states at the target viewport.

## Interaction feedback

Use restrained background, opacity, border, or icon changes to acknowledge hover, focus, press, success, and error. Avoid huge scaling, glows, or long animations. Feedback must communicate state without distracting from the work.
