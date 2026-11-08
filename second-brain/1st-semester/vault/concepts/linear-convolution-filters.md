---
title: "Linear Convolution Filters"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [image-point-operations, image-representation-bitmap]
---

## One-line Summary
Linear convolution filters replace each pixel with a weighted sum of its neighbourhood values using a kernel matrix; they perform spatial frequency filtering — smoothing (low-pass) or sharpening/edge detection (high-pass).

## Core Intuition
Imagine sliding a small grid (the kernel) across every pixel of an image. At each position, multiply the kernel values with the underlying pixel values, sum them up, and that's the new pixel value. A kernel with all positive values that sum to 1 averages nearby pixels → blurring. A kernel that subtracts neighbours from the centre → edge detection. It's the spatial-domain equivalent of frequency filtering: removing high frequencies smooths, removing low frequencies reveals edges.

## Formal Definition / Statement
**Convolution** of image B with kernel K at position (x,y):

```
B'(x,y) = Σᵢ Σⱼ K(i,j) · B(x-i, y-j)
```

The kernel K is a small matrix (3×3, 5×5, etc.) defining the weights.

**Example 3×3 kernels**:

| Operation                  | Kernel K                         |
| -------------------------- | -------------------------------- |
| Box blur                   | 1/9 × [[1,1,1],[1,1,1],[1,1,1]]  |
| Gaussian blur              | 1/16 × [[1,2,1],[2,4,2],[1,2,1]] |
| Sharpen                    | [[0,-1,0],[-1,5,-1],[0,-1,0]]    |
| Sobel X (vertical edges)   | [[-1,0,1],[-2,0,2],[-1,0,1]]     |
| Sobel Y (horizontal edges) | [[-1,-2,-1],[0,0,0],[1,2,1]]     |

**Frequency domain interpretation**:
- **Low-pass filter**: attenuates frequencies above the cut-off frequency; passes low frequencies → blurring/smoothing
- **High-pass filter**: attenuates frequencies below the cut-off frequency; passes high frequencies → edge detection/sharpening

**Two levels of image operations** (beyond point ops):
1. **Point operations** (K=1×1): scale amplitude values (see [[image-point-operations]])
2. **Neighbourhood operations / convolution filters**: scale spectral (frequency) ratios

## Key Properties / Complexity
- **Linearity**: convolving with kernel A then B = convolving with A*B (associativity)
- **Commutativity**: A*B = B*A
- **Separability**: some kernels (e.g., Gaussian) can be decomposed into two 1D passes — much faster (O(n·k) vs O(n·k²))
- **Border handling**: pixels outside the image must be handled (zero-padding, mirror, wrap)
- **Kernel size vs. quality**: larger kernels = larger neighbourhood = stronger effect but slower
- **Low-pass** (blurring) removes noise and detail; **high-pass** (sharpening) enhances edges and noise
- Common applications: enhancement, blurring, denoising, edge detection

## Worked Example
Applying a 3×3 box blur to a pixel with neighbourhood:
```
10  20  30
40 [50] 60
70  80  90
```

New value = (10+20+30+40+50+60+70+80+90) / 9 = 450/9 = **50** (same in this case)

For a pixel surrounded by very different values:
```
0   0   0
0 [255] 0
0   0   0
```
New value = 255/9 ≈ **28** — the bright pixel is dramatically reduced, smoothing out the noise.

## Common Pitfalls
- Confusing convolution with correlation (convolution flips the kernel; for symmetric kernels they're identical)
- Forgetting to normalise the kernel (dividing by sum of weights for blurs) — without it, the image gets brighter or darker
- Applying a high-pass filter to a noisy image — it amplifies noise
- Not handling image borders properly — creates artifacts at edges
- Thinking convolution can do everything — it's linear and spatially invariant; nonlinear operations (median filter) need different approaches

## Connections
- [[image-point-operations]] — point operations modify amplitude; convolution modifies frequency content
- [[dithering]] — dithering introduces high-frequency patterns that convolution could smooth out
- [[jpeg-compression-pipeline]] — JPEG operates in frequency domain (DCT); convolution is the spatial-domain equivalent
- [[image-representation-bitmap]] — convolution operates on raster/bitmap pixel arrays
- [[vector-graphics-svg]] — vector graphics don't use convolution; rasterization converts them first

## Open Questions
- How does the median filter (nonlinear) compare to Gaussian blur (linear) for noise removal?
- What is the relationship between kernel size and the effective cut-off frequency?
- How do modern deep learning architectures learn convolution kernels automatically?
