---
title: "Floyd-Steinberg Dithering (Error Diffusion)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [dithering, color-quantization]
---

## One-line Summary
Floyd-Steinberg dithering (1976) distributes quantization error from each pixel to its neighboring pixels using a fixed diffusion kernel, producing visually superior results compared to noise or pattern [[dithering]].

## Core Intuition
Instead of making an irreversible color choice for each pixel and moving on, Floyd-Steinberg asks: "What was the error?" and pushes that error into the surrounding pixels that haven't been processed yet. The right and bottom neighbors absorb the leftover, so their color values get adjusted *before* they are quantized. This means errors don't accumulate in one place but spread out naturally, creating a visual texture that the eye perceives as smooth gradation.

## Formal Definition / Statement
For each pixel at position (x, y):

1. Find the nearest available palette color: `new_pixel = nearest_color(old_pixel)`
2. Compute quantization error: `error = old_pixel - new_pixel`
3. Distribute error to unprocessed neighbors using the kernel:

```
            x    x+1
row x:         [α]  [β]  [γ]
row x+1:  [δ]
```

Where the standard Floyd-Steinberg weights are:
- α = 7/16 (right neighbor)
- β = 3/16 (bottom-right neighbor)
- γ = 5/16 (bottom neighbor)
- δ = 1/16 (bottom-left neighbor)

Constraint: **α + β + γ + δ = 1.0** (all error is conserved)

Processing order: left-to-right, top-to-bottom (scanning raster order).

## Key Properties
- Published in 1976 by Robert W. Floyd and Louis Steinberg
- Widely used in practice — de facto standard for error diffusion dithering
- Error is usually dispersed to the right and bottom (forward diffusion)
- Produces visually pleasing, natural-looking results
- Increases file entropy (harder to compress) due to introduced high-frequency patterns
- Single-pass algorithm — processes each pixel exactly once
- The kernel weights (7/16, 3/16, 5/16, 1/16) are heuristically chosen, not theoretically optimal

## Worked Example
Pixel at (3, 5) has value 180, palette has {0, 128, 255}:
1. Nearest color: 128
2. Error: 180 - 128 = +52
3. Distribute error:
   - (4, 5): add 52 × 7/16 ≈ +22.75
   - (4, 6): add 52 × 3/16 ≈ +9.75
   - (3, 6): add 52 × 5/16 ≈ +16.25
   - (2, 6): add 52 × 1/16 ≈ +3.25

The neighbors are now "warmer" by these amounts, so when they're quantized, they'll tend toward lighter colors — compensating for this pixel's darkening.

## Common Pitfalls
- Forgetting that error diffusion is applied in raster order — processing order matters
- Not clamping pixel values after error addition (values can go below 0 or above 255)
- Confusing Floyd-Steinberg (error diffusion) with ordered dithering (pattern-based) — they are fundamentally different approaches
- Assuming the kernel weights are the only option — many variants exist (Jarvis-Judice-Ninke, Stucki, Burkes)

## Connections
- [[dithering]] — Floyd-Steinberg is a specific type of error diffusion dithering
- [[color-quantization]] — the quantization step that generates the error
- [[color-lookup-table]] — the palette that defines the available colors
- [[image-file-formats]] — commonly used when saving images in GIF or 8-bit PNG format

## Open Questions
- How do newer error diffusion kernels (e.g., Jarvis-Judice-Ninke, Stucki) compare in quality vs. speed?
- Can Floyd-Steinberg be parallelized, or is the sequential dependency fundamental?
