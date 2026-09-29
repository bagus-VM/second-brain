---
title: "Color Gamut"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [cie-chromaticity-diagram, color-models-overview]
---

## One-line Summary
A colour gamut is the **subset of colours that a device (monitor, printer, camera) can accurately reproduce**, represented as a region within the [[cie-chromaticity-diagram]].

## Core Intuition
No real device can reproduce all colours visible to humans. Each device has a bounded range — its gamut. Understanding gamuts is essential for multimedia databases because colours may need to be mapped between devices (e.g., capturing with a camera, displaying on a monitor, printing on paper). Colors outside a device's gamut must be clipped or compressed.

## Formal Definition / Statement
- Gamut = the set of reproducible colours in a colour space
- For additive systems (RGB): gamut is a triangle in CIE xy, with vertices at the three primary chromaticities
- For subtractive systems (CMYK): gamut is an irregular polygon, typically smaller than RGB
- Gamut mapping: the process of converting colours from one gamut to another (perceptual intent: relative colorimetric, absolute colorimetric, perceptual, saturation)

## Key Properties / Complexity
- Human vision gamut > CRT/LED monitor gamut > inkjet printer gamut
- Highly saturated colours (corners of the CIE horseshoe) are hardest to reproduce
- Different standards define different gamuts: **sRGB (narrow, web standard)**, **Adobe RGB (wider, photography)**, **DCI-P3 (cinema)**, **Rec. 2020 (ultra-wide, UHD TV)**
- Gamut mismatch causes clipping — saturated colours appear less vivid on a narrower-gamut device

## Worked Example
A saturated lime-green on an Adobe RGB monitor (large triangle) may fall outside the sRGB triangle. When displayed on a standard sRGB monitor, it gets clipped to the nearest in-gamut colour, appearing duller.

## Common Pitfalls
- Confusing colour space with gamut — the colour space is the mathematical framework; the gamut is the achievable subset for a specific device
- Assuming higher gamut always means "better" — it must be matched to the content and use case

## Connections
- Visualized via [[cie-chromaticity-diagram]]
- Practical for [[rgb-color-model]] vs [[cmyk-color-model]] conversions
- Important for multimedia database storage: which colour space/gamut to use as canonical?

## Open Questions
- Should multimedia databases store a gamut tag alongside colour data for accurate reproduction?
