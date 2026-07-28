---
title: "Image Resolution: DPI, PPI, and Pixel Density"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [image-representation-bitmap]
---

## One-line Summary
Image resolution measures how accurately a device or system approximates an image, expressed as dots per inch (DPI) for printers/scanners or pixel dimensions for monitors/cameras.

## Core Intuition
Resolution answers: "**How much detail can we capture or display?**" For printers and scanners, it's a density measure — how many dots fit in one inch. For monitors and cameras, it's an absolute pixel count. The key insight is that the same pixel count looks different on devices of different physical sizes: a 1024×768 image on a 17" monitor has different PPI than on a 19" monitor.

## Formal Definition / Statement
Resolution takes two forms:

**Relative (density-based)** — for printers, scanners:
- Measured in **dots per inch (DPI)**
- Desktop Printer: ~600 DPI; Typesetter: ~1270 DPI; Scanner: 300–3600 DPI

**Absolute (pixel count)** — for monitors, digital cameras:
- Measured in pixel dimensions (e.g., PAL TV: 768×576 px)
- The resulting DPI depends on both resolution and physical size

**Pixels Per Inch (PPI)** formula:

```
PPI = Pixel Dimension / Physical Dimension (in inches)
```

Where physical dimension = pixel dimension × (device physical size / device pixel dimension)

## Key Properties / Complexity
- DPI is device-relative; PPI is a computed property of pixel count and physical size
- Higher resolution → more detail → more memory required
- When Image Resolution < Device Resolution: [[image-interpolation|interpolation]] required (quality loss)
- When Image Resolution > Device Resolution: downsampling required ("Oversampling" technique)
- Oversampling is useful when good downsampling algorithms are used — subjective quality can exceed device resolution

## Worked Example
A 19" monitor (1280×1024 pixels, 376mm × 301mm):
- Width: 1280 px / 376 mm = 3.4 px/mm → 3.4 × 25.4 ≈ 86.5 PPI
- Height: 1024 px / 301 mm = 3.4 px/mm → 3.4 × 25.4 ≈ 86.4 PPI

Comparison of device resolutions:

| Device          | Typical Resolution |
| --------------- | ------------------ |
| Desktop Printer | 600 DPI            |
| Typesetter      | 1270 DPI           |
| Scanner         | 300–3600 DPI       |
| PAL TV          | 768 × 576 px       |
| 17" LCD         | 1024 × 768 px      |

## Common Pitfalls
- Confusing DPI (printer/scanner density) with PPI (computed pixel density) — they are related but distinct
- Assuming a higher pixel count always means better quality — the physical display size matters
- Ignoring that oversampling (resolution > device) can actually improve perceived quality via better downsampling algorithms

## Connections
- [[image-representation-bitmap]] — resolution defines the grid size of a bitmap
- [[image-interpolation]] — required when scaling between different resolutions
- [[pixel-formats-and-bit-depth]] — each pixel at any resolution needs a bit depth
- [[image-file-formats]] — resolution metadata is stored in file headers (e.g., TIFF tags 100/101)

## Open Questions
- How does perceptual resolution (what the eye can distinguish) relate to device DPI?
- At what point does increasing resolution yield diminishing returns for human perception?
