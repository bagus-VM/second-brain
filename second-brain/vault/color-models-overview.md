---
title: "Color Models Overview"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-perception]
---

## One-line Summary
Color models are mathematical frameworks for describing colors as tuples of numbers, divided into ==additive== (light-emitting) and ==subtractive== (light-absorbing) systems.

## Core Intuition
Since spectral colors are theoretically infinite, we need compact models. All practical models use a small set of primary colors and mix them. The key distinction is whether mixing is additive (more light = brighter, used in displays) or subtractive (more pigment = darker, used in printing).

## Formal Definition / Statement
- **Additive color mixing**: combining light sources. ==Primaries: Red + Green + Blue.==
  - R + G = Yellow, R + B = Magenta, G + B = Cyan
  - All three at full intensity = White
- **Subtractive color mixing**: combining pigments/filters. ==Primaries: Cyan + Magenta + Yellow.==
  - C + M = Blue, C + Y = Green, M + Y = Red
  - All three = Black (in theory; K added in practice)
- **Complementary colors**: pairs that combine to produce white (additive) or black (subtractive). E.g., Cyan is complementary to Red.

## Key Properties
- Additive models: [[rgb-color-model]], used for screens, cameras, scanners
- Subtractive models: [[cmyk-color-model]], used for printing, painting
- Perceptual models: [[hsv-color-model]], [[lab-color-space]], oriented toward human vision
- The choice of primary colors determines the achievable [[color-gamut]]

## Worked Example
A monitor displaying RGB(255, 255, 0) emits red and green light, which the viewer perceives as yellow — additive mixing. A printer applying cyan and yellow ink absorbs red and blue light, reflecting green — subtractive mixing.

## Common Pitfalls
- Thinking RGB primaries are universal — they are device-specific; different monitors have different red/green/blue phosphors
- Confusing subtractive primaries (CMY) with additive primaries (RGB) — they are complementary to each other

## Connections
- Specific implementations: [[rgb-color-model]], [[cmyk-color-model]], [[hsv-color-model]]
- [[cie-chromaticity-diagram]] defines the theoretical maximum gamut
- [[color-gamut]] compares what different models/devices can reproduce

## Open Questions
- Why do we need both additive and subtractive models in a multimedia database?
