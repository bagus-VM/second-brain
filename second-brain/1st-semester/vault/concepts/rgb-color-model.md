---
title: "RGB Color Model"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-models-overview]
---

## One-line Summary
RGB is an additive colour model where Red, Green, and Blue form the axes of a coordinate system, producing a colour cube with each channel typically quantized to 0–255.

## Core Intuition
Every colour a display can produce is a point in a 3D cube. The origin (0,0,0) is black; the far corner (255,255,255) is white. Moving along one axis adds more of that primary. This maps directly to how screens work: each pixel has three sub-pixels whose intensities are independently controlled.

## Formal Definition / Statement
- Additive colour model with primaries R, G, B as cube axes
- Each component in range [0, 255] (8-bit) or [0.0, 1.0] (normalized)
- Colour = (R, G, B) where 0 = no contribution, max = full contribution
- 8-bit RGB yields 256³ = 16,777,216 distinct colours
- The RGB gamut is a subset of the [[cie-chromaticity-diagram]] (represented as a triangle)

## Key Properties / Complexity
- Device-dependent: the same RGB values look different on different monitors
- The gamut triangle in CIE space depends on the chosen primary chromaticities (e.g., sRGB vs Adobe RGB vs DCI-P3)
- Standard sRGB uses specific CIE coordinates for R, G, B primaries and a D65 white point

## Worked Example
Pure red = (255, 0, 0). Cyan (complement of red) = (0, 255, 255). Mid-gray = (128, 128, 128). Mixing equal R, G, B values produces neutral grays along the cube diagonal from black to white.

## Common Pitfalls
- Assuming RGB is perceptually uniform — doubling R does not double perceived redness
- Forgetting gamma correction — sRGB applies a non-linear transfer function
- Confusing colour depth (bits per channel) with total number of representable colours

## Connections
- Convert to [[hsv-color-model]] for intuitive manipulation
- Convert to [[yuv-color-space]] for video compression
- The RGB gamut is a triangle within the [[cie-chromaticity-diagram]]
- Printing requires conversion to [[cmyk-color-model]]

## Open Questions
- How does the choice of RGB primaries affect colour reproduction fidelity in multimedia databases?
