---
title: "CIE Chromaticity Diagram"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-perception]
---

## One-line Summary
The CIE chromaticity diagram is a horseshoe-shaped map of all theoretically possible colors, defined by normalized coordinates (x, y) derived from the CIE XYZ tristimulus values.

## Core Intuition
To compare colors across devices, we need a device-independent reference. The CIE (Commission Internationale de l'Éclairage) created a standard observer model that maps any visible spectrum to a point in a 2D diagram. The boundary is the spectral locus (pure monochromatic wavelengths); the interior contains all mixtures. Any device's gamut appears as a polygon (usually triangle) inside this horseshoe.

## Formal Definition / Statement
- CIE XYZ tristimulus values: X, Y, Z are computed from the spectral power distribution integrated against the standard observer color-matching functions
- Normalization: x = X/(X+Y+Z), y = Y/(X+Y+Z), z = Z/(X+Y+Z) = 1−x−y
- The diagram plots (x, y); the third coordinate z is implicit
- White point W: reference neutral color, depends on illuminant (e.g., D65, D50)
- Any additive color system's gamut is a triangle with vertices at its RGB primary coordinates

## Key Properties
- Device-independent: enables comparison across monitors, printers, cameras
- Not perceptually uniform: equal Euclidean distances in (x,y) do not correspond to equal perceived color differences
- The horseshoe boundary represents spectral colors (380–789 nm); the bottom edge is the line of purples (non-spectral mixtures)
- Adobe RGB has a larger triangle than sRGB, covering more saturated greens and cyans

## Worked Example
sRGB primaries in CIE (x, y): R ≈ (0.64, 0.33), G ≈ (0.30, 0.60), B ≈ (0.15, 0.06). Drawing a triangle through these points defines the sRGB gamut — all colors a standard monitor can reproduce lie inside this triangle.

## Common Pitfalls
- Thinking the diagram shows all colors a human can see at once — it's 2D; luminance (Y) is projected out
- Forgetting that the diagram is not perceptually uniform — use [[lab-color-space]] for perceptual distance

## Connections
- Defines the theoretical framework for [[color-gamut]]
- Used to specify [[rgb-color-model]] primary coordinates
- [[lab-color-space]] was designed to improve perceptual uniformity over CIE xy
- White point selection affects all color conversions

## Open Questions
- How do wide-gamut displays (Rec. 2020) shift the triangle in the CIE diagram?
