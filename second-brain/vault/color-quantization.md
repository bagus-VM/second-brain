---
title: "Color Quantization"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [pixel-formats-and-bit-depth, color-lookup-table]
---

## One-line Summary
Color quantization reduces the number of distinct colors in an image, trading off quantization error against storage costs when mapping from a large color space to a limited palette.

## Core Intuition
A 24-bit image can have 16.7 million colors, but an 8-bit display can only show 256. Color quantization is the problem of choosing the "best" 256 colors and assigning each original pixel to the closest match. It's a clustering problem in 3D color space — you want to find 256 representative colors that minimize the total error across all pixels. The result often shows banding/posterization, which [[dithering]] can help hide.

## Formal Definition / Statement
Given an image with N pixels in a color space C (e.g., RGB with 2^24 possible colors), color quantization finds a reduced palette P = {c₁, c₂, ..., cₖ} where k ≪ |C|, and a mapping function:

```
Q(p) = argmin_{c ∈ P} distance(p, c)    for each pixel p
```

The goal is to minimize the total quantization error:

```
E = Σ distance(p, Q(p))²   over all pixels p
```

Two main approaches:
1. **Direct assignment**: ==Store full color value== (e.g., 32-bit in some color space) — no quantization needed
2. **Color Lookup Table ([[color-lookup-table|CLUT]])**: Store index into a palette of k colors + [[dithering]] to reduce visible artifacts

## Key Properties
- Trade-off: quantization error vs. storage costs
- Dependent on the representation capabilities of the target device
- Common algorithms: median cut, octree, k-means clustering in color space
- Web-safe palette: standardized 216 colors for cross-platform compatibility
- Per-image adaptive palettes produce better quality than fixed/global palettes
- Quantization is lossy — information is permanently discarded

## Worked Example
Reducing a photograph from TrueColor to 256 colors:
1. Analyze all pixels in RGB color space
2. Cluster pixels into 256 groups (e.g., using median cut)
3. Choose the centroid of each cluster as a palette entry
4. Replace each pixel with its nearest palette color
5. Result: visible banding in smooth gradients (posterization)
6. Apply [[dithering]] to reduce perceived banding

## Common Pitfalls
- Confusing quantization (choosing colors) with [[dithering]] (arranging pixels to simulate missing colors)
- Assuming quantization is always needed — only relevant when reducing color depth
- Forgetting that quantization error accumulates in multi-step processing pipelines
- Overlooking that different images may need different optimal palettes

## Connections
- [[color-lookup-table]] — the data structure that stores the quantized palette
- [[dithering]] — technique to reduce visible effects of quantization
- [[pixel-formats-and-bit-depth]] — quantization reduces bit depth
- [[image-file-formats]] — GIF requires 8-bit quantization; PNG supports it optionally

## Open Questions
- What are the perceptual limits of color quantization (just-noticeable difference)?
- How do modern perceptual color spaces (e.g., CIELAB) improve quantization over RGB?
