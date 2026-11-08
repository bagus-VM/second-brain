---
title: "MMDB Exercise 4 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What is the difference between vector and raster image formats?
> [!answer]- **Vector:** Uses mathematical statements/commands to place lines/shapes. Each control point has (x,y) position. Occupies less space, scales well. **Raster:** Pixel-based, uses bitmaps. Consumes more memory, scaling up degrades quality.

> [!question]- What are the main properties of GIF, PNG, and JPEG?
> [!answer]- **GIF:** RGB, 8bpp (256 colors), LZW lossless, small files, supports animation, not for photos. **PNG:** RGB/RGBA, variable depth, LZSS+Huffman lossless, no animation. **JPEG:** RGB, 24bpp, DCT-based lossy, no animation/transparency.

> [!question]- How do you extract R, G, B channels from a packed 32-bit pixel integer?
> [!answer]- R = (pixel >> 16) & 0xFF, G = (pixel >> 8) & 0xFF, B = pixel & 0xFF. Each channel uses 8 bits of the 32-bit integer.

> [!question]- What is the difference between uniform and median cut quantization?
> [!answer]- **Uniform:** Divide each color axis into equal segments, map colors to regions, average per region. **Median Cut:** Find smallest bounding box, sort along longest axis, split at median, repeat until 256 regions, average per box. Median cut adapts to actual color distribution.

> [!question]- What is noise dithering?
> [!answer]- Adding uniformly distributed white noise to the input image before quantization to reduce visible effects like color banding. Formula: P(x,y) = Q(I(x,y) + noise(x,y)).


---

## Related Resources

### 📖 Topic: Multimedia Databases — Lecture 03 (Image and Dithering)
- Lecture topic: [[multimedia-databases-lecture-03]]

**Key concepts covered:**
- [[image-representation-bitmap]]
- [[image-resolution-dpi-ppi]]
- [[image-interpolation]]
- [[pixel-formats-and-bit-depth]]
- [[color-quantization]]
- [[color-lookup-table]]
- [[dithering]]
- [[floyd-steinberg-dithering]]
- [[image-file-formats]]
- [[jpeg-compression-pipeline]]
- [[jpeg2000-wavelet-compression]]
- [[vector-graphics-svg]]
- [[bezier-curves]]
- [[image-point-operations]]
- [[linear-convolution-filters]]
