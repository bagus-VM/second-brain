---
title: "CIE L*a*b* Color Space"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [cie-chromaticity-diagram, color-perception]
---

## One-line Summary
CIE L*a*b* is a 3D, perceptually uniform, device-independent colour space where L* = lightness, a* = red–green axis, and b* = yellow–blue axis.

## Core Intuition
The CIE xy chromaticity diagram is not perceptually uniform — equal distances don't map to equal perceived colour differences. L*a*b* fixes this by applying non-linear transformations to the XYZ values, producing a space where Euclidean distance approximates human-perceived colour difference. This makes it ideal for colour comparison, matching, and quality metrics.

## Formal Definition / Statement
- **L***: Lightness, 0 (black) to 100 (white)
- **a***: Red–Green axis, −128 (green) to +127 (red)
- **b***: Yellow–Blue axis, −128 (blue) to +127 (yellow)
- Derived from CIE XYZ via non-linear cube-root transformation
- Reference white point required (e.g., D65)
- Device-independent: contains all possible device-dependent colour spectra
- Enables lossless conversion between colour systems

## Key Properties / Complexity
- Perceptually uniform: ΔE (CIE76) = Euclidean distance in L*a*b* approximates perceived colour difference
- Device-independent — no gamut limitation inherent to the space
- Widely used for colour difference evaluation (ΔE < 1: imperceptible, ΔE > 5: clearly visible)
- Standardized and equidistant

## Worked Example
Two colours with L*a*b* values (50, 30, 20) and (50, 35, 25) have ΔE = √(0² + 5² + 5²) ≈ 7.07, which is a noticeable colour difference. This quantitative measure is impossible in RGB or HSV.

## Common Pitfalls
- Confusing L*a*b* with L*u*v* — both are perceptually uniform, but L*a*b* is more commonly used
- Forgetting that device independence doesn't mean all L*a*b* values are displayable — they still must fall within a device's gamut

## Connections
- Built on top of [[cie-chromaticity-diagram]] (XYZ values)
- Superior to [[hsv-color-model]] for perceptual uniformity
- Used in colour-based image retrieval for meaningful distance metrics
- Conceptually related to [[yuv-color-space]] (both separate luminance from chrominance)

## Open Questions
- How does ΔE* (CIEDE2000) improve on ΔE76 for multimedia database similarity queries?
