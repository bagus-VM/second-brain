---
title: "Topic: Multimedia Databases — Lecture 03 (Image and Dithering)"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 2
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Multimedia Databases — Lecture 03: Media: Image and Dithering (Parts 1 & 2)

**Lecturers**: Prof. Dr. Michael Granitzer, Prof. Dr. Harald Kosch  
**Date processed**: 2026-06-01  
**Exam**: 21 July 2026

## Lecture Overview

This two-part lecture covers digital image representation (Part 1) and vector graphics, image manipulation, and filtering (Part 2). Part 1 focuses on raster images, resolution, color quantization, dithering, and file formats. Part 2 covers vector graphics/Bézier curves, image point operations, histograms, and linear convolution filters.

## Sections Covered

### 1. Basics of Image Representation
- [[image-representation-bitmap]] — Bitmap/raster images as 2D pixel arrays
- Image editing (software-based modification) vs. image processing (mathematical algorithms)
- Applications: restoration, analysis, segmentation, classification

### 2. Image Resolution
- [[image-resolution-dpi-ppi]] — DPI for printers/scanners, PPI for monitors/cameras
- Resolution mismatch between image and device
- Oversampling and downsampling strategies

### 3. Image Interpolation
- [[image-interpolation]] — Methods for computing pixels at non-integer coordinates
- Nearest neighbor, bilinear, bicubic interpolation
- Quality vs. computational cost tradeoff

### 4. Image Organization
- [[pixel-formats-and-bit-depth]] — Bit depth from 1-bit (bitonal) to 48-bit (deep TrueColor)
- ARGB pixel layout and channel organization
- Memory calculation: width × height × bits_per_pixel / 8

### 5. Color Reduction / Quantization
- [[color-quantization]] — Reducing from 16.7M colors to a manageable palette
- [[color-lookup-table]] — CLUT/palette mechanism for 8-bit indexed color
- [[dithering]] — Noise, pattern, and error diffusion approaches
- [[floyd-steinberg-dithering]] — The classic error diffusion algorithm (1976)
- Posterization as the main artifact of quantization

### 6. Image File Formats
- [[image-file-formats]] — TIFF, GIF, PNG, JPEG, JPEG2000 comparison
- TIFF: flexible, tag-based, multiple compression options
- GIF: 8-bit indexed, LZW compression, animation support
- PNG: lossless with pre-filters + Deflate, up to 48-bit (PNG-8, PNG-24, PNG-32, APNG variants)
- [[jpeg-compression-pipeline]]: lossy DCT, three-stage pipeline (forward transform → quantization → entropy encoding)
- [[jpeg2000-wavelet-compression]]: lossless/lossy DWT, progressive transmission, no blockiness

---

## Part 2: Vector Graphics, Image Manipulation, and Filtering

### 7. Vector Graphics and SVG
- [[vector-graphics-svg]] — Mathematically defined drawing instructions vs. pixel arrays
- Resolution-independent: scales without quality loss
- Requires rendering to become visible
- SVG: W3C XML standard for 2D vector graphics (shapes, images, text)
- Coordinate system: (0,0) top-left, default units = screen pixels
- Other formats: PostScript, PDF, WMF, Corel Draw, VRML (3D)

### 8. Bézier Curves
- [[bezier-curves]] — Parametric curves defined by control points using Bernstein polynomials
- Derived from Hermite splines (endpoints + derivatives) → geometric control points
- First and last control points interpolated; intermediate ones influence shape
- Convex hull property, tangent property, affine invariance
- Used in SVG paths (C, Q commands), PostScript/PDF, font outlines

### 9. Shading and Lighting Models (3D rendering context)
- Shading models: flat, Gouraud, Phong
- Lighting model: calculates final color from components
- Material properties: reflectance per channel
- Light sources: point light (originates from single point), directional (single direction)

### 10. Image Point Operations
- [[image-point-operations]] — Per-pixel transforms: negative, brightness, contrast, gamma correction
- [[image-point-operations|Image histograms]]: frequency distribution of pixel values per channel
- Cumulative histogram → histogram equalization (spread values across full dynamic range)
- Three categories: point operations, neighborhood operations/filters, geometric operations

### 11. Linear Convolution Filters
- [[linear-convolution-filters]] — Kernel-based neighborhood operations
- Convolution: weighted sum of pixel neighborhood using kernel matrix
- Low-pass filters: blur/smooth (e.g., box blur, Gaussian blur)
- High-pass filters: sharpen/edge detection (e.g., Sobel)
- Applications: enhancement, denoising, edge detection, blurring
- Separable kernels (e.g., Gaussian) decompose into two 1D passes for efficiency

## Key Concepts Summary

| Concept | Core Idea |
|---------|-----------|
| Bitmap image | 2D array of color-valued pixels |
| Resolution | Detail density (DPI/PPI) |
| Bit depth | Colors per pixel (2^b) |
| CLUT | Index-to-color mapping table |
| Quantization | Reducing color count |
| Dithering | Spatial pattern to simulate missing colors |
| Floyd-Steinberg | Error diffusion to neighbors (7/16, 3/16, 5/16, 1/16) |
| JPEG | Lossy DCT, 8×8 blocks, quantization table |
| JPEG2000 | Lossless/lossy DWT, progressive, no blockiness |
| TIFF | Flexible professional format with tags |
| GIF | 8-bit indexed, LZW, animation |
| PNG | Lossless, pre-filtered, Deflate |
| Vector graphics | Mathematically defined shapes, resolution-independent |
| SVG | W3C XML format for 2D vector graphics |
| Bézier curve | Parametric curve via control points + Bernstein polynomials |
| Image histogram | Frequency distribution of pixel values |
| Point operation | Per-pixel transform (negative, brightness, contrast) |
| Convolution filter | Kernel-weighted neighborhood sum (blur, sharpen, edge detect) |
| Low-pass filter | Attenuates high frequencies → blurring |
| High-pass filter | Attenuates low frequencies → edge detection |

## Connections to Other Lectures
- Lecture 02 (Audio) — Analogous [[color-quantization|quantization]] concepts apply to audio sampling
- Lecture 03 Part 1 — Foundation: raster images, color, dithering, file formats

## Exam-Relevant Points
- Know the three interpolation methods and their tradeoffs
- Be able to calculate memory requirements given dimensions and bit depth
- Explain Floyd-Steinberg error diffusion with the standard kernel weights
- Compare TIFF, GIF, PNG, JPEG on compression, color depth, and use cases
- Understand why dithering is necessary after color quantization
- Know JPEG's three-stage pipeline: DCT → quantization → entropy encoding
- Compare JPEG (DCT, lossy) vs JPEG2000 (DWT, lossless/lossy, progressive)
- Understand PNG variants (PNG-8, PNG-24, PNG-32) and pre-filter options
- Distinguish vector vs. raster graphics: resolution independence, rendering requirement, use cases
- Bézier curve properties: endpoint interpolation, tangent property, convex hull, Bernstein polynomials
- Explain convolution with a kernel matrix; distinguish low-pass vs. high-pass filtering
- Know common kernels: box blur, Gaussian, Sobel (horizontal/vertical edges)
- Image point operations: negative, brightness, contrast, histogram equalization
- Distinguish three categories: point operations, neighborhood operations (filters), geometric operations
