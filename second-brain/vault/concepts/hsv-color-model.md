---
title: "HSV Color Model"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-models-overview, rgb-color-model]
---

## One-line Summary
HSV (Hue, Saturation, Value) represents colours in a way that aligns with human perception: hue as the colour wheel angle, saturation as colour purity, and value as brightness.

## Core Intuition
RGB is mathematically convenient but unintuitive for humans. HSV decouples "what colour" (hue), "how vivid" (saturation), and "how bright" (value) — making it natural for colour pickers and image editing. The model is a cylindrical or conical solid where hue wraps around 0°–360°.

## Formal Definition / Statement
- **H (Hue)**: 0°–360°. Red = 0°, Green = 120°, Blue = 240°. Circular.
- **S (Saturation)**: 0%–100%. 0% = gray (no colour), 100% = fully saturated.
- **V (Value/Brightness)**: 0%–100%. 0% = black, 100% = full brightness.

### RGB → HSV Conversion (Gonzalez & Woods)
1. W = min(R, G, B)  — the "white" component
2. R' = R − W, G' = G − W, B' = B − W  — only two values are non-zero
3. If B' = 0: H = G' × 120 / (R' + G')  [hue between R and G]
   If R' = 0: H = B' × 120 / (G' + B') + 120  [hue between G and B]
   If G' = 0: H = R' × 120 / (R' + B') + 240  [hue between B and R]
4. S = (max(R,G,B) − W) / max(R,G,B)
5. V = max(R, G, B)

## Key Properties / Complexity
- Perceptually more intuitive than RGB for selecting/adjusting colours
- Not perceptually uniform — equal steps in HSV don't produce equal perceived changes
- All fully saturated colours (S=100%, V=100%) lie on the outer rim of the hexcone

## Worked Example
Convert RGB(0.6, 0.2, 0.4) to HSV:
- W = min(0.6, 0.2, 0.4) = 0.2
- R' = 0.4, G' = 0.0, B' = 0.2
- G' = 0, so H = 0.4 × 120/(0.4+0.2) + 240 = 80 + 240 = 320°
- S = (0.6 − 0.2)/0.6 = 0.667 (66.7%)
- V = 0.6 (60%)
Result: H=320°, S=66.7%, V=60% — a medium-saturation magenta-pink.

## Common Pitfalls
- Confusing HSV with HSL — in HSL, L=100% is always white; in HSV, V=100% can still be a saturated colour
- Assuming HSV is perceptually uniform — it's not; [[lab-color-space]] is closer

## Connections
- Conversion partner: [[rgb-color-model]]
- Less perceptually uniform than [[lab-color-space]] but simpler to compute
- Useful for colour-based image retrieval in multimedia databases (query by hue)
- Related: [[hmmd-color-space]] attempts better perceptual uniformity

## Open Questions
- When is HSV preferable to L*a*b* in multimedia database queries?
