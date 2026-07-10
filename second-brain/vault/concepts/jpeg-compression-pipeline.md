---
title: "JPEG Compression Pipeline (DCT-based)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [pixel-formats-and-bit-depth, image-file-formats]
---

## One-line Summary
JPEG compression uses a three-stage pipeline — forward DCT transform, quantization, and entropy encoding — to achieve lossy compression of natural images by exploiting human visual perception limitations.

## Core Intuition
The human eye is more sensitive to low-frequency changes (smooth gradients) than high-frequency details (sharp edges, noise). JPEG exploits this ==by transforming 8×8 pixel blocks into frequency space using the Discrete Cosine Transform (DCT), then aggressively quantizing the high-frequency coefficients (which the eye won't miss) while preserving low-frequency ones==. The result is dramatic compression with acceptable quality loss for photographs.
![[Pasted image 20260708123921.png]]
## Formal Definition / Statement
The JPEG compression pipeline consists of three stages:

1. **Forward Transform**:
   - Level-shift pixel values by subtracting 2^(p-1) (where p is bit depth)
   - ==Divide image into 8×8 pixel blocks==
   - Apply forward DCT to each block:
     ```
     [C]_ij = (2/N) × c(i) × c(j) × Σ Σ f(x,y) × cos((2x+1)iπ/2N) × cos((2y+1)jπ/2N)
     ```
     where c(0) = 1/√2, c(k) = 1 for k > 0

2. **Quantization**:
   - Divide each DCT coefficient by the corresponding entry in a quantization table
   - Round to nearest integer: `l_ij = round(θ_ij / Q_ij)`
   - Zigzag scan to group low-frequency coefficients first
   - Higher frequencies are quantized more aggressively (larger Q values)

3. **Entropy Encoding**:
   - DC coefficient (top-left): encode difference from previous block
   - AC coefficients: run-length encoding + Huffman coding

## Key Properties
- **Lossy compression**: irreversible quality loss, but adjustable via quantization table
- **8×8 block structure**: each block is transformed independently
- **DCT basis functions**: represent horizontal/vertical frequencies from DC (constant) to highest frequency
- **Quantization table**: controls quality/size tradeoff — smaller values = higher quality = larger file
- **Blockiness artifact**: at low bit rates, the 8×8 block boundaries become visible
- DC coefficient represents average brightness of block; AC coefficients represent frequency details
- **Tradeoff**: Increase bit rate (decrease quantization table elements) for more accuracy; decrease bit rate for less accuracy

## Worked Example
Original 8×8 block (pixel values):
```
124 125 122 120 122 119 117 118
121 126 124 127 143 150 156 158
121 124 124 127 142 148 159 160
120 123 125 128 143 152 158 159
119 122 125 129 142 152 155 156
119 121 126 130 140 152 158 159
120 121 125 128 139 152 158 158
120 120 124 127 139 150 157 156
```

After DCT (frequency coefficients):
```
 39.88   6.56  ...  (large DC value = average brightness)
-102.43  4.56  ...  (AC coefficients represent frequencies)
 37.77   1.31  ...
  ...              (high-frequency coefficients are small)
```

After quantization with standard table (Q[0,0]=16):
- DC: 39.88/16 ≈ 2 (heavily reduced)
- Most high-frequency coefficients become 0 (lossy compression achieved)

## Common Pitfalls
- Confusing JPEG (lossy, DCT-based) with JPEG2000 (can be lossless, wavelet-based)
- Forgetting that JPEG operates on 8×8 blocks — this causes visible "blockiness" at high compression
- Assuming JPEG quality slider is linear — the relationship between quality setting and quantization table is non-linear
- Not understanding that the quantization table is the key to controlling quality vs. file size
- Overlooking that DC coefficients are encoded differentially (difference from previous block)

## Connections
- [[image-file-formats]] — JPEG is one of the most widely used image formats
- [[jpeg2000-wavelet-compression]] — successor using wavelet transform instead of DCT
- [[pixel-formats-and-bit-depth]] — JPEG typically operates on 24-bit color images
- [[color-quantization]] — JPEG does not use CLUT; quantization is in frequency domain
- [[image-representation-bitmap]] — JPEG compresses raster/bitmap image data

## Open Questions
- How does JPEG2000's wavelet transform compare to DCT in terms of compression efficiency?
- What is the perceptual optimal quantization table for specific image types?
- How do modern learned image codecs (neural compression) compare to JPEG's handcrafted pipeline?
