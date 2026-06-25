---
title: "HMMD Color Space"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [hsv-color-model, rgb-color-model]
---

## One-line Summary
HMMD (Hue-Max-Min-Diff) is a color space designed to be closer to perceptual uniformity (how close a color space is perceived to the human eye) than HSV, using hue plus four derived intensity/chrominance components.

## Core Intuition
HSV has known perceptual non-uniformities. HMMD improves on it by decomposing intensity into multiple components that better correlate with human perception. Max indicates darkness, Min indicates pallor, Diff indicates chrominance (proximity to a pure color), and Sum represents overall brightness.

## Formal Definition / Statement
Given an RGB color:
- **Hue**: Same as in HSV, derived from the dominant color direction
- **Max** = ==max(R, G, B) — indicates how dark the color is (higher = less dark)==
- **Min** = ==min(R, G, B) — indicates how pale the color is (higher = more pale)==
- **Diff** = ==Max − Min — indicates chrominance; 0 = achromatic (gray), higher = more saturated==
- **Sum** = ==(Max + Min) / 2 — represents overall brightness==

## Key Properties
- Closer to perceptual uniformity than HSV/HSL
- Diff component directly measures saturation intensity
- Used in MPEG-7 color descriptor standard for image/video retrieval
- Decomposition into Max, Min, Diff gives more control over perceptual attributes

## Worked Example
For RGB(200, 100, 50):
- Max = 200, Min = 50, Diff = 150, Sum = 125
- Hue ≈ 20° (orange-red)
- The high Diff value indicates a strongly saturated color; high Max/low Min indicates a moderately bright, warm color

## Common Pitfalls
- Confusing HMMD with HSV — the key difference is the decomposition of intensity into Max/Min/Diff/Sum rather than a single Value
- Noting that MPEG-7 uses a specific variant of HMMD with quantized bins

## Connections
- An improvement over [[hsv-color-model]] for perceptual tasks
- Shares the hue concept with [[hsv-color-model]]
- Relevant for content-based image retrieval in multimedia databases (MPEG-7 descriptors)
- Less perceptually uniform than [[lab-color-space]] but simpler

## Open Questions
- Why did MPEG-7 choose HMMD over L*a*b* for color descriptors?
