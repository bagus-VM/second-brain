---
title: "Image Interpolation: Nearest Neighbor, Bilinear, Bicubic"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [image-representation-bitmap, image-resolution-dpi-ppi]
---

## One-line Summary
Image interpolation computes new pixel values when scaling images, using methods ranging from simple nearest-neighbor to sophisticated bicubic spline techniques.

## Core Intuition
When you enlarge a bitmap image, you need to "invent" pixels that didn't exist before. Scaling by factor s means computing P'(x, y) from P(x/s, y/s) — but x/s and y/s are generally not integers. Interpolation methods differ in how they estimate these non-integer pixel values: from simply copying the nearest pixel, to blending surrounding pixels linearly, to fitting smooth curves through them.

## Formal Definition / Statement
Given an original image P and a scale factor s, the scaled image P' requires computing:

```
P'(x, y) = f(P(x/s, y/s))
```

where x/s, y/s are typically non-integer coordinates, and f is the interpolation function.

Three main methods:

1. ==**Nearest Neighbor**==: P'(x,y) gets the color of the original pixel whose center is closest to (x/s, y/s). Simplest, fastest, produces blocky results.

2. ==**Bilinear Interpolation**==: Uses color values of the four "covered" pixels, weighted by the area of intersection. Produces smoother results but can blur edges.

3. ==**Bicubic Interpolation**==: Uses cubic splines (similar to Bézier curves) instead of linear interpolation across a 4×4 neighborhood of pixels. Best quality, most computationally expensive.

## Key Properties
- Nearest neighbor: O(1) per pixel, preserves hard edges, produces blockiness
- Bilinear: O(4) per pixel (2×2 kernel), smooth gradients, may blur sharp features
- Bicubic: O(16) per pixel (4×4 kernel), best quality, sharpest results
- All methods introduce artifacts — the tradeoff is between sharpness and smoothness
- Downscaling (reducing resolution) also requires interpolation or averaging

## Worked Example
Enlarging a 100×100 image by factor 2× (to 200×200):
- Pixel (50, 50) in the new image maps to (25, 25) in the original → integer, no interpolation needed
- Pixel (51, 50) maps to (25.5, 25) → non-integer
  - **Nearest neighbor**: copies pixel (25, 25) or (26, 25)
  - **Bilinear**: blends pixels (25,25), (26,25), (25,26), (26,26) with weights based on distance
  - **Bicubic**: uses a 4×4 neighborhood of 16 pixels with cubic polynomial weights

Height comparison (each method produces different characteristics at 50px height).

## Common Pitfalls
- Using nearest neighbor for photographs — produces unacceptable blockiness
- Using bicubic for pixel art — destroys the intentional sharpness
- Forgetting that interpolation cannot create information that wasn't in the original — it can only estimate
- Confusing upscaling interpolation with downscaling (which requires different strategies)

## Connections
- [[image-resolution-dpi-ppi]] — interpolation is needed when resolution mismatches between image and device
- [[image-representation-bitmap]] — interpolation operates on the bitmap pixel grid
- [[image-file-formats]] — some formats store resolution metadata that triggers automatic interpolation

## Open Questions
- How do modern AI-based super-resolution methods (e.g., ESRGAN) compare to classical interpolation?
- Is there a theoretical limit to interpolation quality given a fixed source resolution?
