---
title: "Color Lookup Table (CLUT / Palette)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [pixel-formats-and-bit-depth]
---

## One-line Summary
A Colour Lookup Table (CLUT) maps small pixel indices to full-colour values, enabling 8-bit images to display up to 256 chosen colours from a 16.7 million colour space.

## Core Intuition
Instead of storing a full 24-bit RGB colour for every pixel (expensive!), store just a 1-byte index per pixel that points into a shared table of 256 colours. The table itself holds the actual 24-bit colour values. It's like a paint-by-numbers kit: the canvas stores numbers, and the palette maps numbers to actual paints. The key challenge is choosing the best 256 colours to represent a given image — this is the [[color-quantization|color quantization]] problem.

## Formal Definition / Statement
Given an image with 8-bit pixel depth:
- Each pixel P(x,y) stores an index i ∈ {0, 1, ..., 255}
- A Colour Lookup Table (CLUT) maps each index to a 24-bit RGB value: CLUT[i] = (R, G, B)
- The actual colour of pixel P(x,y) is CLUT[P(x,y)]

The CLUT is often directly implemented in hardware (graphics card). The ideal CLUT contains the 256 most important colours of the image.

## Key Properties / Complexity
- Reduces per-pixel storage from 24 bits to 8 bits **(3× compression)**
- CLUT itself requires only 256 × 24 bits = 768 bytes of overhead
- When reducing from 16.7M colours to 256, not all original colours can be represented
- Replacing missing colours with nearest CLUT entries causes **posterization** (banding) effects
- [[dithering]] mitigates posterization by creating optical illusions of missing colours
- Web-safe colours: a standardized set of 216 colours reproducible across all browsers and platforms

## Worked Example
Original: 640×480 pixel image, 24-bit colour
- Without CLUT: 640 × 480 × 24 / 8 = 921,600 bytes ≈ 900 KB
- With CLUT (8-bit indexed): 640 × 480 × 8 / 8 = 307,200 bytes + 768 bytes (CLUT) ≈ 300 KB
- Savings: ~67% reduction in file size

## Common Pitfalls
- Assuming CLUT colours are fixed — they are chosen per image during [[color-quantization|quantization]]
- Forgetting that posterization is inevitable when reducing to 256 colours without [[dithering|dithering]]
- Confusing CLUT (a palette mechanism) with [[color-quantization|color quantization]] (the algorithm for choosing palette colours)
- GIF format is limited to 8-bit CLUT — cannot represent TrueColor images

## Connections
- [[pixel-formats-and-bit-depth]] — CLUT is the mechanism for 8-bit colour depth
- [[color-quantization]] — the algorithm for selecting the optimal 256 colours
- [[dithering]] — technique to compensate for CLUT limitations
- [[image-file-formats]] — GIF uses CLUT; PNG supports it optionally; JPEG does not

## Open Questions
- How do adaptive palette algorithms (per-image vs. fixed palette) affect quality?
- What is the optimal CLUT size for perceptually lossless indexed colour?
