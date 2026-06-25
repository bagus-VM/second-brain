---
title: "Image Representation: Bitmap / Raster Images"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A bitmap (raster) image is a 2D array of pixels where each pixel stores a color value, forming the fundamental representation for digital images.

## Core Intuition
Think of a bitmap image as a grid of tiny colored squares — like a mosaic. Each square (pixel) has a specific color value. When viewed from far enough away, the grid blends into a continuous image. The more squares you have and the more colors each can represent, the more detailed and realistic the image looks. Sources include scanners, digital cameras, and drawing programs (which simulate analog tools like brushes and spray cans).

## Formal Definition / Statement
A bitmap image is defined as a 2D matrix of dimensions N × M, where each element P(x, y) at row x and column y stores a color value. The color value's representation depends on the [[pixel-formats-and-bit-depth|bit depth]] and color model used.

Image operations fall into two categories:
- **Editing**: Modification of digital images using specialized software (e.g., Photoshop) — improvement, alteration, manipulation.
- **Processing**: Mathematical algorithms for professionally modifying/analyzing digital images.

Further applications include:
- Image improvement: restoration, retouching
- Image analysis: segmentation, texture analysis, contour extraction
- Image classification, recognition, sorting

## Key Properties
- Each pixel stores a discrete color value (determined by [[pixel-formats-and-bit-depth|bit depth]])
- Requires significant memory: memory = ==width × height × bits_per_pixel==
- Quality degrades when scaled up (requires [[image-interpolation|interpolation]])
- Can represent any photographic or scanned content
- Disadvantages: high memory usage, quality loss on scaling
- Contrast with vector graphics which store geometric descriptions instead of pixel grids

## Worked Example
A 19" monitor displaying 1280 × 1024 pixels:
- Physical width: 376 mm → 1280/376 ≈ 3.4 px/mm ≈ 86.5 ppi (px/i)
- Physical height: 301 mm → 1024/301 ≈ 3.4 px/mm ≈ 86.4 ppi (px/i)

A 24-bit TrueColor image at 1280 × 1024 requires:
1280 × 1024 × 24 bits = 3,932,160 bits ≈ 3.75 MB (uncompressed)

## Common Pitfalls
- Confusing DPI (device-dependent, physical) with PPI (pixels per inch, image property)
- Assuming bitmap images scale losslessly — upscaling always requires [[image-interpolation|interpolation]]
- Forgetting that memory requirements grow quadratically with resolution

## Connections
- [[image-resolution-dpi-ppi]] — determines the pixel density of a bitmap
- [[pixel-formats-and-bit-depth]] — determines how color is stored per pixel
- [[image-interpolation]] — required when scaling bitmaps
- [[color-lookup-table]] — alternative to storing full color per pixel
- [[image-file-formats]] — how bitmaps are stored on disk (TIFF, PNG, GIF, JPEG)

## Open Questions
- What are the theoretical limits of bitmap resolution before diminishing returns?
- How do modern neural upscaling methods compare to classical interpolation?
