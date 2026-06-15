---
title: "Spatial Coherency"
tags: [concept, multimedia-databases, semester-1, spatial-coherency, cbr, compression]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[color-histogram]]"]
---

## One-line Summary
Spatial coherency is the property that neighbouring pixels in a natural image tend to have similar values — exploited in image compression (JPEG's DCT on 8×8 blocks), in segmentation (regions of similar colour), and as a flag in MPEG-7's Dominant Color Descriptor to indicate whether a colour forms a coherent region.

## Core Intuition
Natural images are not random. Pixels next to each other are usually similar — sky is uniformly blue, grass is uniformly green, faces have smooth skin tones. This is **spatial coherency**. It's the reason image compression works (JPEG can compress natural images 10:1 with little visible loss), and the reason segmentation algorithms can find regions.

The opposite of spatial coherency is **noise** (or "salt-and-pepper" patterns, where neighbouring pixels are unrelated). High-entropy images (snow on TV, fine-grained textures) have low spatial coherency.

## Formal Definition / Statement

**Spatial coherency** of a pixel p with respect to its neighbours N(p):
    Coherency(p) = similarity of p's value to N(p)'s values

For a colour image, the "value" is the colour vector, and the similarity is a distance (e.g., L2 in RGB, or perceptual distance in Lab).

**Block-level coherency** (used in JPEG and other block-based coders):
    Coherency(B) = average pixel-wise similarity within block B

**Image-level coherency**:
    Coherency(I) = average of block-level coherency over all blocks

A block is "coherent" if its pixels are similar; "incoherent" if they vary widely. JPEG's 8×8 blocks exploit this: in a coherent block, the DCT coefficients are concentrated in the low-frequency components, which can be encoded efficiently.

**MPEG-7's spatial coherency flag**: for each dominant colour, a flag indicating whether the colour forms a spatially coherent region (1) or is scattered (0). This helps distinguish "blue sky region" (coherent) from "blue dots scattered across the image" (incoherent).

## Key Properties

### Why spatial coherency matters
- **Compression**: natural images are compressible because of spatial coherency. Random images are not.
- **Segmentation**: regions of similar colour/texture can be found by clustering spatially-adjacent pixels
- **Feature extraction**: spatial pyramids (histograms at multiple spatial resolutions) exploit spatial coherency
- **Denoising**: spatial coherency can be used to smooth out noise (e.g., bilateral filter)
- **Perception**: humans perceive spatial coherency — we see "blue sky" not "individual blue pixels"

### Spatial coherency in compression
- **JPEG's DCT**: 8×8 blocks are chosen because they balance: small enough to assume spatial coherency, large enough to allow compression
- **JPEG 2000's wavelet transform**: applies multi-resolution analysis, exploiting spatial coherency at multiple scales
- **Video compression (H.264, H.265)**: also exploits *temporal* coherency (consecutive frames are usually similar)

### Spatial coherency in segmentation
- **Region growing**: start with a seed pixel, add neighbours with similar colour
- **Watershed segmentation**: treat the image as a topographic surface, find "watersheds"
- **Mean shift**: find modes in the colour-space-position joint distribution
- **Graph cuts**: treat pixels as nodes, edges as similarities; cut the graph to find regions

### Spatial coherency vs noise
- High spatial coherency: smooth regions, easy to compress
- Low spatial coherency: noise, textures, complex patterns — harder to compress
- Spatial-coherency-preserving filters: bilateral filter, anisotropic diffusion, non-local means

## Worked Example

A 4×4 block of a smooth sky region:
```
[200, 200, 200, 200]
[200, 200, 200, 200]
[200, 200, 200, 200]
[200, 200, 200, 200]
```
Spatial coherency: very high (all pixels identical). JPEG DCT: only the DC coefficient is non-zero. Highly compressible.

A 4×4 block of grass (rough texture):
```
[80, 120, 95, 110]
[105, 90, 115, 100]
[95, 110, 85, 105]
[100, 95, 110, 90]
```
Spatial coherency: moderate (pixels vary in a small range). JPEG DCT: DC + a few low-frequency AC coefficients. Moderately compressible.

A 4×4 block of random noise:
```
[10, 230, 45, 180]
[200, 15, 220, 50]
[100, 175, 30, 210]
[150, 65, 190, 25]
```
Spatial coherency: very low. JPEG DCT: many high-frequency AC coefficients. Poorly compressible.

## Common Pitfalls
- **Confusing spatial coherency with low entropy**: a region can have low spatial coherency but still be structured (e.g., a checkerboard pattern). Both are compressible, but the compression algorithms differ.
- **Forgetting the colour space**: spatial coherency in RGB is different from spatial coherency in Lab. Perceptual colour spaces give more "intuitive" coherency.
- **Assuming natural images are always coherent**: textured regions (grass, fabric, foliage) have moderate coherency; very high-entropy regions (fine sand, dappled light) have low coherency.
- **Block size trade-off**: too small a block, and spatial coherency is high but the overhead of the block structure is too much. Too large a block, and the assumption of coherency breaks down. JPEG's 8×8 is a good balance.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[color-histogram]] — doesn't capture spatial coherency
- [[dominant-color]] — uses spatial coherency as a flag
- [[minkowski-distance]] — distance functions used in coherency calculation
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- Can spatial coherency be quantified in a way that's useful for CBR? (Yes — entropy, autocorrelation, spectral slope.)
- How does spatial coherency relate to perceptual similarity? (Humans use spatial coherency implicitly when judging image similarity.)
- Can deep learning features replace hand-crafted spatial-coherency-aware features? (In many cases, yes — but interpretability suffers.)
