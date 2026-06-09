---
title: "MMDB Exercise 3 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What are metamers in color perception?
> [!answer]- Color stimuli with different spectral power distributions that are perceived as identical by a given observer — different spectral profiles that produce exactly the same relative stimulation to L, M, and S cones.

> [!question]- What is chromatic adaptation and why does a white paper look white under different lighting?
> [!answer]- Our eye constantly recalibrates what it sees as "white light" (like camera auto white balance). All other colors are judged relative to that white point. Despite changing illumination spectra, we perceive "the light changed" rather than "objects changed color."

> [!question]- What are the main properties of the HSV color model?
> [!answer]- **H**ue = color (0-360°), **S**aturation = degree to which hue differs from neutral gray (0=gray, 1=full), **V**alue/Brightness = illumination level (0=black, 1=white). Designed to approximate human color perception. HS and B are treated separately.

> [!question]- How do you convert RGB (0.2, 0.6, 0.3) to HSV?
> [!answer]- W = min(0.2,0.6,0.3) = 0.2. R'=0, G'=0.4, B'=0.1. Since R'=0: H = (0.1×120/0.5)+120 = **144°**. S = (0.6-0.2)/0.6 = **66.7%**. V = 0.6 = **60%**.

> [!question]- How does CIE L*a*b* differ from CIE XYZ?
> [!answer]- **CIE XYZ:** Additive, linear, good for color mixtures but NOT perceptually uniform — distance doesn't predict perceived similarity. **CIE L*a*b*:** Oriented to human perception, distance accurately predicts perceived similarity, chromatically adapted to D50 (5000K) for consistent comparison.
