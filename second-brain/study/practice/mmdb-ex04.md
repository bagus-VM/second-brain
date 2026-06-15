---
title: "MMDB Exercise 4 — Image Processing Part 1"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-15
---

## Exercises

### Task 1: Image Formats

1. Describe the differences between vectorial and raster (bitmap) image formats.
2. Outline the main properties of the following image formats: **GIF, PNG, JPEG** with respect to:
   - color model
   - color depth
   - compression
   - file size

### Task 2: Image Processing and Resolution

Let `I` be a 12 × 12 RGB image.

1. An RGB image is stored in Java as a 3D integer array (one dimension per channel). How much memory does this require for `I`?
2. Refactor: pack each pixel into a single 32-bit integer (8 bits per channel). How much memory is saved?
3. How do we retrieve the individual R, G, B samples from a packed pixel?
4. For an iPhone 17: screen 6.3 inches, aspect ratio 19.5:9, resolution 2622 × 1206 pixels. Calculate the pixel density (show the steps).

### Task 3: Quantization and Dithering

1. Write down the **uniform quantization** and **median cut** color quantization algorithms (high-level steps, not code).
2. Give a brief explanation of **noise dithering**.

## Solutions

> [!note]- Solution
> **1a) Vector vs. Raster:**
>
> | Property | Vector | Raster (Bitmap) |
> |----------|--------|-----------------|
> | Representation | Mathematical primitives (lines, curves, splines, Béziers) defined by control points with (x, y) coordinates | Pixel grid (bitmap) of fixed resolution |
> | Resolution | Resolution-independent — scales without quality loss | Resolution-dependent — scaling up causes degradation (pixelation) |
> | File size | Small for simple shapes; grows with primitive count | Large; grows with width × height × bit depth |
> | Use cases | Logos, fonts, technical drawings, print graphics | Photos, scanned images, anything with continuous tone |
> | Rendering | Re-rasterized at output resolution | Displayed as-is; resampling needed for scaling |
>
> **1b) Image formats:**
>
> | Format | Color model | Color depth | Compression | Typical file size |
> |--------|-------------|-------------|-------------|-------------------|
> | **GIF** | RGB (8-bit indexed palette, 256 colors) | 8 bpp | LZW (lossless) | Small |
> | **PNG** | RGB / RGBA (true color + alpha) | 1–16 bpp grayscale; 1–8 bpp indexed; 24/48 bpp true color | LZ77 (LZSS) + Huffman (lossless) | Medium |
> | **JPEG** | RGB (Y′CbCr internally) | 24 bpp (most common) | DCT-based (lossy) | Small (tunable via quality factor) |
>
> **Caveats the prof likes to test:**
> - GIF can hold animations; PNG and JPEG cannot.
> - JPEG does **not** support transparency (no alpha channel).
> - PNG is the go-to "lossless photo" format; GIF is for graphics with few colors.
> - All three handle RGB; CMYK support is a different question (JPEG *can* store CMYK, PNG typically not).

> [!note]- Solution
> **2a) 3D array memory (12×12 RGB, Java):**
>
> Naive 3D array `int[H][W][C]`, 1 sample = 4 bytes (Java `int`).
> - Pure pixel data: `H × W × C × 4 bytes = 12 × 12 × 3 × 4 = 1728 bytes`
> - **But** in Java, multi-dimensional arrays are arrays-of-arrays. The runtime allocates:
>   - 1 outer array (H references, each 4 bytes + object header)
>   - H inner arrays (W references each, 4 bytes + header)
>   - H·W innermost arrays (C references = 3·H·W·4 bytes + headers)
> - Per the official solution:
>   - References: `4(H + W·H) = 4(12 + 144) = 624 bytes`
>   - Object headers: `4(W·H + H + 1) = 4(144 + 12 + 1) = 628 bytes`
>   - Image data: `3·W·H·4 = 3·144·4 = 1728 bytes`
>   - **Total: 624 + 628 + 1728 = 2980 bytes**
>
> **2b) Packed-integer savings:**
> - Packed representation: 1 pixel = 1 integer = 4 bytes → `W·H·4 = 12·12·4 = 576 bytes`
> - But: still need the outer array + object header. The reference overhead drops because there's only **one** pixel array (not three nested ones).
> - **Memory saved ≈ 2980 − ~600 = ~2380 bytes** (the exact number depends on which overhead charges you keep; the salient point is "orders of magnitude less overhead").

> [!note]- Solution
> **2c) Unpacking the pixel:**
> Bit-layout convention (most common, ARGB-style but with 8 unused bits):
> ```
> bits 31..24 : 0 0 0 0 0 0 0 0   (alpha/padding, unused)
> bits 23..16 : R R R R R R R R
> bits 15..8  : G G G G G G G G
> bits  7..0  : B B B B B B B B
> ```
> Java extraction with bit-ops:
> ```java
> int r = (pixel >> 16) & 0xFF;
> int g = (pixel >> 8)  & 0xFF;
> int b =  pixel        & 0xFF;
> ```
> Shift right by 16 (or 8) to drop lower bytes, then mask with `0xFF` (= 255 = `11111111`₂) to keep only the lowest 8 bits of the result.

> [!note]- Solution
> **2d) Pixel density (iPhone 17):**
>
> Given: diagonal `D = 6.3"`, aspect ratio `H:W = 19.5:9`, resolution `2622 × 1206` px.
>
> 1. Express `H` in terms of `W`: `H = (19.5/9) · W`
> 2. Apply Pythagoras: `W² + H² = D²` → `W² + (19.5/9)² · W² = 6.3²`
> 3. Solve: `W² · (1 + 4.6944…) = 39.69` → `W² = 39.69 / 5.6944 ≈ 6.97` → `W ≈ 2.64 inches`
> 4. Pixel density: `PPI = 1206 px / 2.64 in ≈ 456 ppi`
>
> **What the prof is testing:** unit-consistency (inches vs. cm) and whether you remember that "resolution" alone does not give PPI — you need the physical diagonal first.

> [!note]- Solution
> **3a) Quantization algorithms:**
>
> **Uniform quantization** (per-channel axis-split):
> 1. Decide on `k` representative colors (e.g., 256 for 8-bit display).
> 2. For each color axis (R, G, B), divide the axis range `[0, 255]` into `k_axis` equal segments. Example: 8 segments for R, 8 for G, 4 for B → 256 total cells.
> 3. Every input color is mapped to the cell it falls in.
> 4. The representative color of each cell is the **average of all colors mapped into that cell**.
>
> **Median cut** (data-aware):
> 1. Find the smallest axis-aligned bounding box that contains **all** the colors present in the image.
> 2. Sort the enclosed colors along the **longest axis** of that box.
> 3. Split the box into two sub-boxes at the **median** of the sorted list. The two halves are roughly equal in pixel count.
> 4. Repeat steps 2–3 on whichever sub-box has the longest axis, until you have `k` boxes.
> 5. The representative color of each box is the **average of all colors in that box**.
>
> **Trade-off:** uniform is fast and trivial but wastes cells on colors that aren't there. Median cut adapts to the actual color distribution — better quality for the same `k`.
>
> **3b) Noise dithering:**
> Add uniformly distributed white noise to the input image **before** quantization:
> ```
> P(x,y) = Q( I(x,y) + noise(x,y) )
> ```
> This breaks up the **color banding** artifacts that hard quantization would otherwise produce, by spreading the quantization error across neighbouring pixels. The human eye averages out the noise and perceives a smoother gradient. (Dithering is the conceptual cousin of half-toning in print.)

## Common Pitfalls

- Forgetting that a Java `int` is 4 bytes — the 3D array question wants you to account for the **array-of-arrays overhead**, not just the raw data.
- Mixing up "color depth" (bits per pixel) with "bit depth per channel". A 24-bpp RGB image has 8 bits per channel.
- Reporting PPI without showing the geometric step — the prof will dock points for "I just divided them."

## Related Lectures

- [[multimedia-databases-lecture-03]]
- [[multimedia-databases-lecture-04]]
- [[image-representation-bitmap]]
- [[image-file-formats]]
- [[color-quantization]]
- [[dithering]]
- [[pixel-formats-and-bit-depth]]
