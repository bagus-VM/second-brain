---
title: "Dithering: Noise, Pattern, and Error Diffusion"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [color-quantization, color-lookup-table]
---

## One-line Summary
Dithering creates the apparent increase of perceivable colours through spatial displacement of pixel patterns, compensating for the limited palette after [[color-quantization|color quantization]].

## Core Intuition
When you reduce a 16.7-million-colour image to 256 colours, smooth gradients become ugly bands of flat colour (posterization). Dithering tricks the eye by mixing pixels of available colours in patterns that *optically* blend into the missing colours — just like newspaper halftone photos use dots of different sizes to simulate shades of grey. Stand back and the dots blur together into smooth tones.

## Formal Definition / Statement
Given a pixel with original colour P and the two nearest available palette colours C_low and C_high:
- Quantization without dithering: assign P to whichever of C_low or C_high is closer
- Dithering: distribute pixels of C_low and C_high in a spatial pattern proportional to P's distance from each

Three types of dithering:

1. **Noise Dithering**: Random threshold — each pixel independently compared against a random value
2. **Pattern Dithering**: Fixed threshold matrix applied tile-by-tile across the image
3. **Error Diffusion**: Quantization error is distributed to neighboring pixels (see [[floyd-steinberg-dithering]])

## Key Properties / Complexity
- Does not actually increase the number of colours — **creates optical illusion through spatial arrangement**
- Noise dithering: simplest, introduces visible random noise
- Pattern dithering: uses ordered threshold matrices (e.g., Bayer matrix), can create visible repeating patterns
- Error diffusion (Floyd-Steinberg): best quality, propagates error to neighboring pixels, produces visually pleasing results
- Dithering increases file entropy (less compressibility) because it introduces high-frequency patterns
- The eye's limited resolution at normal viewing distance is what makes dithering work

## Worked Example
A smooth gradient from black (0) to white (255), quantized to 4 levels (0, 85, 170, 255):
- Without dithering: harsh bands of 4 flat greys
- With 2×2 ordered dithering: alternating patterns like:
  ```
  [0 85] [85 170] [170 255]
  ```
  create the illusion of intermediate shades
- With Floyd-Steinberg: error from each quantization decision spreads right and down, creating natural-looking gradation

## Common Pitfalls
- Confusing dithering with [[color-quantization]] — quantization chooses colours, dithering arranges them
- Forgetting that dithering makes lossless compression less effective (increases entropy)
- Assuming dithering always improves quality — at very low palette sizes (2–4 colours), artifacts become obvious
- Applying dithering to images that will be further scaled — the patterns break down

## Connections
- [[color-quantization]] — dithering compensates for quantization artifacts
- [[color-lookup-table]] — dithering operates within the constraints of a CLUT
- [[floyd-steinberg-dithering]] — the most important error diffusion algorithm
- [[pixel-formats-and-bit-depth]] — dithering is needed when reducing bit depth
- [[image-file-formats]] — GIF (8-bit only) commonly uses dithering; PNG supports it but doesn't require it

## Open Questions
- How does dithering interact with lossy compression (e.g., JPEG)?
- Are there perceptually optimal dithering patterns for specific display technologies?
