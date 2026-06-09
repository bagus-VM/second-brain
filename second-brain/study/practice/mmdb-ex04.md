---
title: "MMDB Exercise 4 — Image Processing Part 1"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: Image Formats

1. Describe the differences between vectorial and raster (bitmap) image formats.
2. Outline the main properties of the following image formats: GIF, PNG and JPEG with respect to: color model, color depth, compression, file size.

### Task 2: Image Processing and Resolution

Let I be a 12 × 12 RGB image.

1. Consider an RGB image implementation in Java that stores pixels in a 3D array (of integers), where each dimension corresponds to a color channel. How much memory is required to store I?
2. One way to reduce memory consumption is to transform the 3D array representation into a 2D array representation. A pixel is packed into a single integer (32 bit), where each channel is coded in 8 bits. How much memory is saved compared to the 3D array representation?
3. Describe how we can retrieve the individual R, G, B samples from the packed pixel.
4. For an iPhone 17, given a screen size of 6.3 inches, an aspect ratio of 19.5:9, and a resolution of 2622 × 1206 pixels, calculate its pixel density (show the steps).

### Task 3: Quantization and Dithering

1. Write down the uniform and median cut color quantization algorithms (in simple steps, not code/pseudocode).
2. Give a brief explanation of noise dithering.

## Solutions

### Task 1: Image Formats

> [!note]- Solution
> **1a) Vector vs Raster:**
> - **Vector:** Uses sequential commands/mathematical statements to place lines or shapes in 2D/3D. Each control point has (x,y) position and determines a graphic primitive (shapes, curves, splines). Occupies less space, scales well for printing.
> - **Raster:** Pixel-based, uses bitmaps to store information. Consumes more memory, scaling up leads to degradation.
>
> **1b) Format properties:**
> - **GIF:** Color model: RGB. Color depth: 8 bpp (256 colors from 24-bit space). Compression: LZW (lossless). Small file size. Supports animations/logos but not suitable for photos due to color limitation.
> - **PNG:** Color model: RGB/RGBA. Color depth: variable — grayscale (1-16 bpp), indexed (1-8 bpp, 24-bit palette), truecolor (24/48 bpp). Compression: LZSS + Huffman (lossless). No animation support.
> - **JPEG:** Color model: RGB. Color depth: 24 bpp (most common). Compression: DCT-based (lossy). No animation or transparency support.

### Task 2: Image Processing and Resolution

> [!note]- Solution
> **2a) 3D array memory:** Java stores each int as 4 bytes. The 3D array int[3][12][12] also has overhead: references (H+WH = 4 bytes each), object headers (1+H+WH = 4 bytes each). Total: 4(H+WH) + 4(WH+H+1) + 4(3WH) = **2980 bytes** for W=H=12.
>
> **2b) 2D packed array:** int[12][12] → 12×12×4 = 576 bytes (plus minor overhead). Savings ≈ 2980 - 576 ≈ **2404 bytes**.
>
> **2c) Retrieving R, G, B from packed pixel:**
> - R = (pixel >> 16) & 0xFF
> - G = (pixel >> 8) & 0xFF
> - B = pixel & 0xFF
>
> **2d) Pixel density:**
> - Aspect ratio 19.5:9 → H = (19.5/9) × W
> - Pythagorean theorem: W² + ((19.5/9)×W)² = 6.3²
> - Solving: W ≈ 2.64575 inches
> - 2.64575 inches = 1206 pixels → 1 inch ≈ **456 PPI**

### Task 3: Quantization and Dithering

> [!note]- Solution
> **3a) Uniform Quantization:**
> 1. Each axis of the color space is divided into equal-sized segments (e.g. 8 for red, 8 for green, 4 for blue for 8-bit storage)
> 2. Each original color is mapped to the region it falls in (256 regions for 8 bits)
> 3. Representative color for each region = average of all colors mapped to that region
>
> **Median Cut Quantization:**
> 1. Find the smallest box containing all colors in the image
> 2. Sort enclosed colors along the longest axis of the box
> 3. Split the box into 2 regions at the median of the sorted list
> 4. Repeat until the color space is divided into 256 regions
> 5. Representative colors = average of colors in each box
>
> **3b) Noise Dithering:** Reduce effects of quantization (such as color banding) by adding uniformly distributed white noise (dither signal) to the input image prior to quantization. Formula: P(x,y) = Q(I(x,y) + noise(x,y))

## Related Lectures

- [[multimedia-databases-lecture-05]]
- [[multimedia-databases-lecture-06]]
