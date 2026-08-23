# Professional UI taste research notes

## Evidence and limitations

These notes separate public guidance, empirical research, and design judgment. Design-system recommendations are not universal laws; they are context-sensitive starting points. A screenshot-only reviewer cannot fully establish interaction quality, accessibility, or professional usefulness without live inspection.

## Primary findings

### Apple Human Interface Guidelines
Apple's public design principles frame quality around purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, and delight. The guidance says there is no single right application of the principles; they are tools for weighing competing priorities. It explicitly distinguishes simplicity from minimalism, asks designers to make every element earn its place, emphasizes hierarchy and clear feedback, and says delight should not become decoration that interferes with core purpose.[1]

### Material Design 3 typography
Material Design 3 organizes type into display, headline, title, body, and label roles with size variants to establish hierarchy across devices. It recommends expressive typefaces for short high-emphasis text, readable typefaces for body text, line-height and padding/bounding-box discipline, and approximately 1.2 line-height for larger text and 1.5 for body text. It also documents contrast targets of 3:1 for large text and 4.5:1 for small text.[2]

### WCAG contrast
WCAG 2.2's understanding document states that normal text should meet a 4.5:1 contrast ratio and large text 3:1, with exceptions for incidental text, inactive controls, decoration, and logotypes. The document explains that contrast is a threshold for legibility and that hue alone is not a reliable substitute for luminance contrast.[3]

### Aesthetic-usability evidence
The search surfaced the well-known aesthetic-usability effect and empirical studies, but the results are mixed across contexts and sessions. The defensible conclusion is not that beauty equals usability; rather, attractive visuals can influence perceived usability and may mask problems, so professional-taste evaluation must score aesthetics, usability, accessibility, and task success separately.[4] [5]

## Operational implications

Professional taste should be evaluated as contextual intentionality: hierarchy that guides the current task, proportion that matches content and input method, consistency that reduces learning cost, density that supports the job, typography that preserves reading flow, and restraint that removes competition without removing necessary functionality. Anti-patterns such as cards, rounding, gradients, large type, whitespace, and animation are signals to inspect, not automatic violations.

## Sources

[1]: https://developer.apple.com/design/human-interface-guidelines/design-principles "Apple Human Interface Guidelines — Design principles"
[2]: https://m3.material.io/styles/typography/applying-type "Material Design 3 — Applying type"
[3]: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html "W3C WCAG 2.2 — Contrast minimum"
[4]: https://www.nngroup.com/articles/aesthetic-usability-effect/ "Nielsen Norman Group — The Aesthetic-Usability Effect"
[5]: https://www.sciencedirect.com/science/article/pii/S1071581922000647 "Visual aesthetics and user experience: A multiple-session experiment"
