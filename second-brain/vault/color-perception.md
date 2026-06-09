---
title: "Color Perception"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Human color perception arises from three types of retinal cones sensitive to short (blue), medium (green), and long (red) wavelengths of visible light (400–700 nm).

## Core Intuition
Light is electromagnetic radiation. Only the 400–700 nm band is visible to humans. The retina contains ~120 million rods (luminance only) and ~5 million cones (color). Three cone types — S (~430 nm), M (~530 nm), L (~560 nm) — form the biological basis of trichromatic vision. This is why three primary colors suffice to model human-visible color.

## Formal Definition / Statement
- Visible spectrum: wavelengths ==400 nm to 700 nm== (frequencies ~==385–789 THz==)
- Light properties: direction (propagation), frequency (perceived as color), amplitude (perceived as brightness)
- Cone types:
  - S-cones: short wavelength (~430 nm), ==blue domain==
  - M-cones: medium wavelength (~530 nm), ==green domain==; genetically close to L-cones
  - L-cones: long wavelength (~560 nm), ==red domain==
- Opponent processing: Red–Green channel, Blue–Yellow channel, plus achromatic luminance channel

## Key Properties
- Rods are far more numerous (~120M vs ~5M) and handle low-light/scotopic vision
- Cones handle photopic (daylight) color vision
- Color perception is subjective — colorblindness affects ~8% of males
- The opponent-process model (red–green, blue–yellow, luminance) explains why we don't perceive "reddish-green"

## Worked Example
White light hitting the retina stimulates all three cone types roughly equally. A pure 530 nm light strongly stimulates M-cones, weakly stimulates L-cones, and barely stimulates S-cones — the brain interprets this as "green."

## Common Pitfalls
- Confusing wavelength (physical) with color (perceptual) — the same color can be produced by different spectra (metamerism)
- Assuming rods contribute to color perception — they only detect luminance

## Connections
- Explains why [[rgb-color-model]] uses three primaries
- Foundation for [[cie-chromaticity-diagram]] and [[lab-color-space]]
- Opponent processing inspires [[yuv-color-space]] (luminance/chrominance separation)

## Open Questions
- How does metamerism affect color accuracy in multimedia databases?
- What are the implications of tetrachromatic vision (4 cone types) for future displays?
