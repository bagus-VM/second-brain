---
title: "YUV Color Space"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [rgb-color-model, color-perception]
---

## One-line Summary
YUV separates a colour signal into **luminance/brightness** (Y) and two **chrominance/colour** components (U, V), enabling efficient compression by exploiting the human eye's greater sensitivity to brightness than colour detail.

## Core Intuition
Human vision resolves luminance detail far better than chrominance detail (due to the ~24:1 ratio of rods to cones). YUV exploits this by encoding full-resolution brightness and subsampled colour. A monochrome image needs only Y — backward compatible with black-and-white displays. This is the foundation of all modern video compression (JPEG, MPEG, H.264/HEVC).

## Formal Definition / Statement
- **Y** = Luminance, computed from RGB based on physiological sensitivity:
  ==Y = 0.299R + 0.587G + 0.114B==
- **U (Cb)** = Chrominance: **difference between luminance and blue**
- **V (Cr)** = Chrominance: **difference between luminance and red**
- Related variants: YCbCr (digital), YPbPr (analog), YIQ (NTSC)
- Linear transformation from RGB

## Key Properties / Complexity
- Separates intensity (perceptually important) from colour (perceptually less important)
- Enables chroma subsampling: 4:2:2 (half horizontal chroma), 4:2:0 (quarter chroma) — massive bandwidth savings
- Monochrome reproduction needs only Y — backward compatible
- Very close to human visual perception model

## Worked Example
In JPEG compression, an RGB image is converted to YCbCr. The Cb and Cr channels are subsampled by 2× in each dimension (4:2:0). Since the eye is less sensitive to colour resolution, this is visually near-lossless but reduces data by ~50%.

## Common Pitfalls
- Confusing YUV (analog PAL) with YCbCr (digital) — they use slightly different scaling but the principle is identical
- Assuming Y = perceived brightness — it's a weighted sum approximating luminance, not a perceptual lightness like L*

## Connections
- Derived from [[rgb-color-model]]
- Conceptually similar to [[lab-color-space]] (luminance/chrominance separation)
- The weighted sum of RGB reflects the cone sensitivities from [[color-perception]]
- Foundation of image/video compression — links to multimedia database storage

## Open Questions
- How does chroma subsampling affect content-based image retrieval accuracy?
