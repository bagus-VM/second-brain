---
title: "Pixel Formats and Bit Depth"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [image-representation-bitmap]
---

## One-line Summary
Bit depth determines how many distinct colors each pixel can represent, with common formats ranging from 1-bit (black/white) to 48-bit (deep TrueColor), directly controlling the tradeoff between color fidelity and memory usage.

## Core Intuition
Each pixel in a [[image-representation-bitmap|bitmap image]] needs bits to describe its color. More bits = more possible colors = more faithful reproduction of reality, but also more memory. The bit depth defines the "color vocabulary" of the image: 1 bit gives you only black or white, 8 bits give 256 colors, 24 bits give millions of colors (enough for the human eye), and beyond that is mainly useful for editing headroom.

## Formal Definition / Statement
For an image with bit depth b per pixel:
- Number of possible colors: 2^b
- Memory per pixel: b bits
- Total memory: width × height × b bits

**Standard bit depths:**

| Bits | Colors        | Name                     | Description                                 |                         |
| ---- | ------------- | ------------------------ | ------------------------------------------- | ----------------------- |
| 1    | 2             | Bitonal                  | Black + white                               |                         |
| 8    | 256           | Grey level / Palette     | Black to white (greyscale) or indexed color |                         |
| 8    | 256           | Palette (color)          | [[color-lookup-table                        | CLUT]] with 256 entries |
| 16   | 65,536        | 16-bit grey / High Color | Fine greyscale or 16-bit color              |                         |
| 24   | 16.7M         | TrueColor                | 8 bits per channel (R, G, B)                |                         |
| 32   | 16.7M + alpha | TrueColor + Alpha        | 24-bit color + 8-bit transparency           |                         |
| 48   | 281 billion   | Deep TrueColor           | 16 bits per channel                         |                         |

## Key Properties
- Bit depth is per-pixel; total color depth = sum of all channels
- Memory formula: ==`memory_bytes = (width × height × bits_per_pixel) / 8`==
- Alpha channel (transparency) adds 8 bits to the depth (e.g., 24→32 bit)
- ARGB layout: Alpha (bits 31-24), Red (23-16), Green (15-8), Blue (7-0) in a 32-bit word
- Channels can be stored as separate planes or interleaved per pixel

## Worked Example
A 1280×1024 image at different bit depths:

| Bit Depth | Memory |
|-----------|--------|
| 1-bit | 1280 × 1024 × 1 / 8 = 163,840 B ≈ 160 KB |
| 8-bit | 1280 × 1024 × 8 / 8 = 1,310,720 B ≈ 1.25 MB |
| 24-bit | 1280 × 1024 × 24 / 8 = 3,932,160 B ≈ 3.75 MB |
| 32-bit | 1280 × 1024 × 32 / 8 = 5,242,880 B ≈ 5.00 MB |

## Common Pitfalls
- Confusing bit depth (per pixel) with color depth (total distinct colors displayable)
- Forgetting that 8-bit color images use a [[color-lookup-table|CLUT]] — the 256 colors are not fixed but chosen per image
- Assuming 32-bit means "more colors" than 24-bit — the extra 8 bits are for alpha (transparency), not color range
- Overlooking that higher bit depth during editing (e.g., 48-bit) preserves quality through multiple edits even if the final output is 24-bit

## Connections
- [[image-representation-bitmap]] — bit depth is the per-pixel data width of a bitmap
- [[color-lookup-table]] — 8-bit color uses a CLUT to map indices to 24-bit colors
- [[color-quantization]] — reducing bit depth requires choosing which colors to keep
- [[dithering]] — technique to simulate missing colors when bit depth is reduced
- [[image-file-formats]] — formats differ in supported bit depths (GIF: 8-bit max, PNG: up to 48-bit)

## Open Questions
- What is the perceptual threshold where increasing bit depth stops being visible to humans?
- How does HDR (High Dynamic Range) imaging relate to higher bit depths?
