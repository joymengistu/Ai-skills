# Bounded Planning-Quality Behavior Tests

These manual contract tests show that the companion changes planning behavior. They do not constitute production builds, independent evaluation, or proof of universal quality improvement.

| Case | Feature-first plan | Integrated planning behavior | Evidence limit |
|---|---|---|---|
| Study workspace | “Build pages for tasks, notes, calendar, timer, and dashboard.” | Establishes the experience promise (“know the next commitment in three seconds”), sets a first observable task flow, reserves one hierarchy review, and blocks extra pages until the flow is observed. | No running app was built. |
| Voxel exploration game | “Terrain, mining, inventory, enemies, crafting, and music.” | Creates a landmark-led exploration slice, makes movement/feedback and visible composition prerequisites, and defers feature count until a playable loop is observed. | No game runtime or player study was conducted. |
| Poster generator | “Prompt input, image output, template picker, export.” | Adds a composition constraint, output-comparison evidence, controlled variation, and a replan trigger if results are repetitive. | No images were generated. |

## Result

Across all three cases, the companion transforms a flat feature list into an experience promise, observable first slice, quality dependencies, evidence need, iteration budget, and stop rule. That is a demonstrable process change. Future work should compare matched baseline and companion-enabled builds with runtime evidence and human review.
