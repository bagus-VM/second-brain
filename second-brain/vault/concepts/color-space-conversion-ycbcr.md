---
title: "Color Space Conversion and Chroma Subsampling (YCbCr)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [pixel-formats-and-bit-depth]
---

## One-line Summary
Colour space conversion from RGB to YCbCr separates luminance (brightness) from chrominance (colour), enabling chroma subsampling — discarding colour detail the human eye barely perceives — for an easy 50% data reduction before any compression algorithm runs.

## Core Intuition
The human visual system is much more sensitive to brightness changes than to colour changes. By converting from the hardware-oriented RGB model to the perception-oriented YCbCr model, we can keep all luminance (Y) information while reducing chrominance (Cb, Cr) resolution with minimal perceptual impact. This is a "free" compression step that happens before DCT, quantization, or any other processing.

## Formal Definition / Statement
**RGB to YCbCr conversion**:
```
Y  =  0.30R + 0.59G + 0.11B    (luminance)
Cb =  B - Y                      (blue chrominance)
Cr =  R - Y                      (red chrominance)
```
Y captures brightness using weighted RGB values reflecting human sensitivity. Cb and Cr capture colour difference information.

**Chroma subsampling notation**: J:a:b where:
- J = width of the reference region (usually 4)
- a = number of chrominance samples in the first row
- b = number of chrominance samples in the second row

Common formats:
| Format | Description | Data reduction |
|--------|-------------|----------------|
| 4:4:4  | Full chroma (no subsampling) | 0% |
| 4:2:2  | Half horizontal chroma | ~33% |
| 4:2:0  | Quarter chroma (both directions) | ~50% |

With 4:2:0, for every 4 luminance samples, only 1 Cb and 1 Cr sample are stored (shared across a 2×2 block).

## Key Properties / Complexity
- **Perception-based**: exploits the human eye's lower sensitivity to colour vs. brightness
- **Reversible transform**: RGB ↔ YCbCr conversion is mathematically lossless
- **Subsampling is lossy**: discarding chroma samples loses colour information permanently
- **4:2:0 is most common**: used in JPEG, MPEG, H.264, H.265 — 50% reduction with minimal quality loss
- **Hardware-oriented (RGB) vs. perception-oriented (YCbCr)**: monitors use RGB; compression uses YCbCr
- Applied BEFORE any compression algorithm (DCT, wavelet, etc.)
- Colour subsampling combined with 8-bit quantization gives SQNR ≈ 6.02×8 + 1.76 ≈ 50 dB

## Worked Example
For an HD 1080p image (1920×1080):
- **RGB (4:4:4)**: 1920 × 1080 × 3 bytes = 6.22 MB
- **YCbCr 4:4:4**: same size (just different colour space, no data reduction)
- **YCbCr 4:2:2**: Y = 1920×1080 = 2.07 MB, Cb = 960×1080 = 1.04 MB, Cr = 960×1080 = 1.04 MB → total = 4.15 MB (33% reduction)
- **YCbCr 4:2:0**: Y = 1920×1080 = 2.07 MB, Cb = 960×540 = 0.52 MB, Cr = 960×540 = 0.52 MB → total = 3.11 MB (50% reduction)

For video at 60 fps: raw RGB = 373 MB/s; with 4:2:0 = ~187 MB/s — a massive savings before any lossy compression.

## Common Pitfalls
- Confusing YCbCr (digital, used in JPEG/MPEG) with YPbPr (analog) and YUV (PAL analog) — they're related but different
- Thinking 4:2:0 means "half the data" — it's ~50% less than 4:4:4, but the actual savings depend on bit depth
- Forgetting that subsampling is lossy and irreversible — once chroma is subsampled, it cannot be perfectly reconstructed
- Assuming 4:4:4 is always better — for most natural images, 4:2:0 is perceptually indistinguishable
- Not understanding that the weighted Y formula (0.30R + 0.59G + 0.11B) reflects human sensitivity, not equal RGB contribution

## Connections
- [[lossless-vs-lossy-compression]] — chroma subsampling is a form of lossy compression (perceptual irrelevancy removal)
- [[jpeg-compression-pipeline]] — JPEG pipeline starts with RGB→YCbCr conversion and chroma subsampling
- [[mpeg-video-compression]] — MPEG uses YCbCr 4:2:0 for all standard profiles
- [[h264-avc-video-compression]] — H.264 supports 4:2:0, 4:2:2, and 4:4:4 profiles
- [[transform-coding]] — DCT/DWT operate on Y, Cb, Cr components separately after subsampling
- [[pixel-formats-and-bit-depth]] — colour depth determines quantization precision per channel
- [[color-quantization]] — colour quantization (CLUT) is different from chroma subsampling

## Open Questions
- How does 4:2:0 vs. 4:2:2 vs. 4:4:4 affect compression efficiency for different content types?
- What is the perceptual threshold for chroma subsampling in HDR content?
- How do modern codecs handle chroma subsampling in combination with adaptive quantization?
