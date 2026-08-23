# Professional UI patterns for developer tools

## Evidence boundary

This reference decomposes publicly observable Replit and Vercel patterns; it does not copy their private implementation, claim their exact tokens, or prescribe one universal aesthetic. Pixel ranges below are **design starting points and hypotheses**, not vendor facts. Validate them against the product task, content density, input method, accessibility, and live behavior.

## Shell and navigation model

| Element | Starting range | Decision rule | Required states |
|---|---:|---|---|
| Desktop expanded sidebar | 240–288 px | Use the smallest width that keeps labels, active context, and essential actions legible without truncation. | Expanded, collapsed, keyboard focus, selected, nested open, tooltip, overflow |
| Desktop collapsed rail | 56–72 px | Preserve orientation with recognizable icons and accessible labels; never hide the only route to a task. | Expanded-on-hover is optional, not required for access |
| Top bar | 48–56 px | Reserve for global identity, project context, search, status, and one primary action; do not duplicate sidebar navigation. | Loading, account/workspace switch, overflow, responsive collapse |
| Main content gutter | 24–40 px desktop | Increase separation for dense content only when it improves grouping; align primary content to a stable grid. | Narrow, wide, zoom/reflow |
| Mobile navigation | Drawer or bottom bar | Use a drawer for many destinations; use a bottom bar for a small set of frequent, one-handed destinations. | Open/close, focus trap, back behavior, safe area, selected |
| Docked assistant/panel | 320–400 px starting range | Keep the task visible; allow minimize or close; do not let the assistant permanently consume the primary workspace. | Open, minimized, maximized, loading, error, close, restore |

## Button hierarchy and sizing

| Role | Starting size | Use | Avoid |
|---|---:|---|---|
| Compact | 32 px high | Dense toolbars and table rows when pointer/keyboard use is primary | Tiny touch-only controls or long labels |
| Default | 36–40 px high | Most desktop actions and forms | Making every action primary |
| Comfortable | 44–48 px high | Touch, prominent mobile actions, or high-consequence confirmation | Inflating low-priority controls |
| Icon-only | Square, at least 44×44 px touch target | Repeated or space-constrained actions | Unlabeled icons, ambiguous glyphs, hover-only meaning |

Use one primary action per local region. Use secondary actions for support, error/destructive variants for consequences, and links for navigation. Labels should name the result and target, such as **Deploy project**, **Copy preview URL**, or **Delete workspace**, rather than generic **Submit**, **OK**, or **Confirm**.

Loading should preserve the control’s position and label context, expose a busy state, prevent duplicate submission, and remain understandable to assistive technology. Disabled controls should be disabled only when the action is impossible and should explain the reason nearby. Use `:focus-visible` or an equivalent visible focus treatment; never remove focus indicators for visual cleanliness.

## Spacing and density

Use a base 4 px token scale with 8 px as the dominant grouping rhythm. Treat these as starting tokens:

| Token | Starting value | Typical use |
|---|---:|---|
| `space-1` | 4 px | icon-to-label micro-gap |
| `space-2` | 8 px | control internals and related items |
| `space-3` | 12 px | compact field or list spacing |
| `space-4` | 16 px | standard component gap |
| `space-6` | 24 px | section separation |
| `space-8` | 32 px | major region separation |
| `space-12` | 48 px | page-level breathing room |

Density is a product variable. A code editor, deployment console, and marketing page should not share the same spacing merely for consistency. Preserve alignment and hierarchy across contexts while allowing the content and task to set density.

## State-complete component rule

Every reusable navigation item, button, input, panel, and table must specify its default, hover, focus, active/selected, disabled, loading, success, error, empty, and recovery behavior where applicable. A polished screenshot is incomplete if it does not show what happens after the click, on a slow connection, after an error, or when the viewport changes.

## High-information examples

| Kind | Example |
|---|---|
| GOOD EXAMPLE | A developer dashboard uses a 256 px expanded sidebar, a 64 px collapsed rail with labeled icon buttons, a 52 px top bar, one **Deploy project** primary action, and a docked assistant that can minimize without hiding the task. |
| BAD EXAMPLE | Every sidebar item is a brightly colored rounded button, the sidebar is 360 px wide, the top bar repeats the same links, and the only visible labels disappear at 125% zoom. |
| BORDERLINE EXAMPLE | A 64 px icon rail looks clean, but new users cannot identify icons and there is no tooltip, accessible name, or persistent route label. |
| EXCEPTION | A data-heavy operations console may use a denser 32 px control height and narrower row gaps when keyboard users and large monitors dominate; touch targets still need an accessible activation area. |
| TRANSFORMATION | Replace a 12-card decorative dashboard with a stable shell, one primary task, grouped navigation, meaningful empty state, clear loading/error/recovery states, and only the metrics needed for the next decision. |

## Review checklist

Evaluate shell geometry, navigation orientation, local action hierarchy, button labels, target sizes, focus visibility, state completeness, content density, responsive behavior, zoom/reflow, contrast, reduced motion, and recovery. Mark exact vendor measurements as **UNKNOWN** unless publicly documented. Mark screenshot-only interaction claims as **not assessable from screenshot**.

## Public pattern references

1. [Replit Design components](https://docs.replit.com/design/core-components)
2. [Replit — Setting up a Design System](https://docs.replit.com/teams/custom-design-system)
3. [Vercel Geist Button](https://vercel.com/geist/button)
4. [Vercel — New dashboard navigation available](https://vercel.com/changelog/new-dashboard-navigation-available)
5. [W3C WCAG 2.2 — Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
