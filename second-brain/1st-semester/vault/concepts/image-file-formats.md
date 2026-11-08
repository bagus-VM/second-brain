---
title: "Image File Formats: TIFF, GIF, PNG, JPEG"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [pixel-formats-and-bit-depth, color-lookup-table]
---

## One-line Summary
Image file formats **define how pixel data, metadata, and compression are organized on disk**, with major formats (TIFF, GIF, PNG, JPEG, JPEG2000) differing in compression method, colour depth support, and use cases.

## Core Intuition
An image file is not just raw pixels — it needs a header (dimensions, bit depth, colour model), optional metadata, and usually compression to reduce file size. Different formats make different tradeoffs: JPEG sacrifices some quality for tiny files (photos on the web), PNG preserves exact quality (illustrations, transparency), GIF is limited to 256 colours but supports animation, and TIFF is the Swiss Army knife of image formats (flexible but bulky).

## Formal Definition / Statement
Key image formats and their properties:

| Format | Compression | Max Colors | Transparency | Animation | Typical Use |
|--------|------------|------------|--------------|-----------|-------------|
| JPEG | Lossy (DCT) | 16.7M | No | No | Photos, web |
| TIFF | Lossless (LZW, etc.) | 16.7M+ | Yes | No | Professional, print |
| GIF | Lossless (LZW) | 256 (8-bit) | Yes (1-bit) | Yes | Web graphics, animation |
| PNG | Lossless (Deflate) | 48-bit | Yes (alpha) | No | Web, illustrations |

Other formats: BMP (Windows raw), RLE (compressed BMP), TGA (Targa), PBM/PGM/PPM (portable maps), RAW (camera-specific), PSD (Photoshop), JP2/JPX/JPM (JPEG2000).

## Key Properties / Complexity

### TIFF (Tagged Image File Format, ~1985)
- Developer: Aldus Corporation, 1986
- Structure: File Header (8 bytes: endianness, version, IFD pointer) → Image File Directories (IFDs) → Tags
- Each tag: 2 bytes ID + 2 bytes type + 4 bytes length + 4 bytes value/offset
- Key tags: ImageWidth (100), ImageHeight (101), BitsPerPixel (102), Compression (103), ColorCoding (104)
- Compression options: none, CCITT (B/W), LZW, JPEG, Huffman
- Colour options: WhiteIsZero, BlackIsZero, RGB, CMYK, colour table
- Very flexible but large file sizes

### GIF (Graphics Interchange Format, 1987)
- Developer: CompuServe Inc., 1987
- Structure: Header → Application → [Control → Image] → Comment → Plain Text → Trailer
- Uses [[color-lookup-table|CLUT]] (8-bit indexed colour, max 256 colours)
- Compression: LZW (Lempel-Ziv-Welch) — identifies repeating bit patterns
- Supports animation (multiple images per file) and 1-bit transparency
- Limitations: max 16,000 × 16,000 pixels, max 256 colours, cannot handle TrueColor
- Developed for fast transmission at low bandwidth

### PNG (Portable Network Graphics, 1996)
- Proposed as free, less complex replacement for GIF (patent issues, resolved 2004)
- Lossless compression with pre-filters to improve compressibility:
  - None: original pixels
  - Sub: differences to left neighbour
  - Up: differences to top neighbour
  - Average: differences to average of top and left
  - Paeth: uses Paeth predictor (top, left, top-left)
- After pre-filtering: Deflate algorithm (same as ZIP/gzip)
- Pre-filters enable smaller file sizes than GIF

**PNG Variants:**

| Variant | Colour Depth / Features | Typical Use |
|---------|------------------------|-------------|
| PNG-8 | 8-bit indexed (up to 256 colours) | Icons, logos, simple graphics |
| PNG-24 | 24-bit true colour (~16.7M colours) | Photos, detailed graphics |
| PNG-32 | 24-bit + 8-bit alpha transparency | Transparent graphics, UI elements |
| APNG | Animation support | Animated web graphics |
| Interlaced PNG | Progressive loading (Adam7) | Web delivery over slow connections |
| Grayscale PNG | Grayscale image storage | Monochrome images, scans |

**PNG Standards:** RFC 2083 (1997), W3C Recommendation (1996), ISO/IEC 15948 (2003)

### Comparison

| Criterion | JPEG | TIFF | GIF | PNG |
|-----------|------|------|-----|-----|
| Storage | Low-avg | High | Average | Avg-low |
| Use cases | Photos, web | Print, data exchange | Web, animation | Web, illustrations |
| Compression | Lossy | Lossless possible | Lossless (LZW) | Lossless (Deflate) |
| Colour depth | 24-bit | Up to 48-bit | 8-bit indexed | Up to 48-bit |

### JPEG vs JPEG2000

| Criterion | JPEG | JPEG2000 |
|-----------|------|----------|
| Transform | Discrete Cosine Transform (DCT) | Discrete Wavelet Transform (DWT) |
| Block structure | Fixed 8×8 blocks | Flexible blocks, no blockiness |
| Lossless mode | No | Yes |
| Progressive transmission | No | Yes (layered file structure) |
| Compression efficiency | Baseline | Typically 20-30% better |
| Image type | Natural imagery | Natural + computer-generated |
| Computational cost | Lower | Higher |
| File formats | .jpg, .jpeg | .jp2, .jpx, .jpm |

See [[jpeg-compression-pipeline]] and [[jpeg2000-wavelet-compression]] for detailed compression pipelines.

## Worked Example
Saving a 1024×768 photograph:
- As JPEG (quality 85): ~200 KB, slight quality loss, no transparency
- As PNG: ~1.5 MB, perfect quality, full alpha transparency
- As GIF: ~400 KB, reduced to 256 colours (posterization), 1-bit transparency
- As TIFF (LZW): ~1.2 MB, perfect quality, maximum flexibility

## Common Pitfalls
- Using GIF for photographs — limited to 256 colours, causes severe posterization
- Using JPEG for graphics with text/sharp edges — lossy compression creates visible artifacts
- Confusing TIFF's flexibility with universal support — not all viewers handle all TIFF variants
- Forgetting that PNG's pre-filters are lossless — they transform data for better compression, not for visual effect
- Overlooking that GIF's 256-colour limit makes [[dithering]] essential for photographs

## Connections
- [[pixel-formats-and-bit-depth]] — formats differ in supported bit depths
- [[color-lookup-table]] — GIF relies on CLUT; PNG supports it optionally
- [[color-quantization]] — required before saving to GIF format
- [[dithering]] — commonly applied before GIF export
- [[image-representation-bitmap]] — all these formats store raster (bitmap) data
- [[jpeg-compression-pipeline]] — detailed JPEG DCT compression process
- [[jpeg2000-wavelet-compression]] — JPEG2000's wavelet-based approach

## Open Questions
- How does JPEG2000 (JP2) compare to JPEG in terms of compression efficiency?
- What role will AVIF and WebP play as successors to these legacy formats?
