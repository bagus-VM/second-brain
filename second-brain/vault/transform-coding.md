---
title: "Transform Coding (DCT, DWT, FFT)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lossless-vs-lossy-compression]
---

## One-line Summary
Transform coding converts data from its original domain (e.g., spatial pixels) into a mathematical representation (e.g., frequency coefficients) where redundancy becomes easier to exploit and perceptually insignificant information can be discarded.

## Core Intuition
Raw pixel data is highly correlated — neighboring pixels have similar values. In the frequency domain, most of the important information is concentrated in a few coefficients (typically low frequencies = smooth structures), while high frequencies (fine details, noise) carry less perceptual weight. By transforming to frequency space, quantizing high-frequency coefficients aggressively, then applying entropy coding, we achieve dramatic compression with controlled quality loss.

## Formal Definition / Statement
Transform coding pipeline:
1. **Forward transform**: Convert data from original domain to transform domain
2. **Quantization**: Reduce precision of transform coefficients (lossy step)
3. **Entropy coding**: Losslessly compress the quantized coefficients

Common transforms:
- **DCT** (Discrete Cosine Transform): used in JPEG and MPEG. Operates on 8×8 blocks. Transforms spatial pixel values to frequency coefficients. The DC coefficient (S₀₀) = average pixel value; AC coefficients represent increasing frequencies.
- **DWT** (Discrete Wavelet Transform): used in JPEG2000. Multi-resolution analysis capturing both frequency and spatial location. No block artifacts.
- **FFT** (Fast Fourier Transform): general frequency analysis, less common in compression due to complex-valued output.

The DCT formula for an 8×8 block:
```
S(u,v) = (2/N) × c(u) × c(v) × Σₓ Σᵧ f(x,y) × cos((2x+1)uπ/16) × cos((2y+1)vπ/16)
```
where c(0) = 1/√2, c(k) = 1 for k > 0, N = 8.

## Key Properties
- **Reversible in theory**: the transform itself is lossless (inverse DCT reconstructs original), but quantization introduces irreversible loss
- **Energy compaction**: DCT concentrates energy in few coefficients (top-left of 8×8 block), enabling aggressive quantization of the rest
- **Block-based (DCT)**: 8×8 blocks are independent — causes blockiness artifacts at high compression
- **Multi-resolution (DWT)**: analyzes at multiple scales, no block artifacts, supports progressive transmission
- **Separable**: 2D DCT can be computed as two 1D DCTs (row then column), reducing complexity
- **Quantization is the key to lossy compression**: the quantization table controls quality vs. size tradeoff
- After quantization, many high-frequency coefficients become zero → ideal for [[run-length-encoding]] + [[entropy-coding-huffman-arithmetic]]

## Worked Example
JPEG DCT on an 8×8 pixel block:

**Original pixel values** (after level-shift by subtracting 128):
```
 -4  -3  -6  -8  -6  -9 -11 -10
 -7  -2  -4  -1  15  22  28  30
 -7  -4  -4  -1  14  20  31  32
 -8  -5  -3   0  15  24  30  31
 -9  -6  -3   1  14  24  27  28
 -9  -7  -2   2  12  24  30  31
 -8  -7  -3   0  11  24  30  30
 -8  -8  -4  -1  11  22  29  28
```

**After DCT** (frequency coefficients):
```
 39.88   6.56  ...  (large DC = average brightness)
-102.43  4.56  ...  (AC coefficients)
 37.77   1.31  ...
  ...               (high-frequency coefficients are small)
```

**After quantization** (divide by quantization table, round):
- DC: 39.88/16 ≈ 2
- Most high-frequency coefficients → 0 (lossy compression achieved)
- Zero-valued coefficients form long runs after zig-zag scan → compressed by RLE + Huffman

## Common Pitfalls
- Confusing the transform (mathematically lossless) with quantization (the lossy part) — DCT itself doesn't lose information
- Thinking DCT and DWT are interchangeable — DCT is block-based (causes blockiness), DWT is multi-resolution (no block artifacts)
- Forgetting that DCT operates on 8×8 blocks independently — this is why JPEG shows blockiness at high compression
- Not understanding that the quantization table is the single most important parameter for quality/size control
- Overlooking that after quantization, the combination of zig-zag scan + RLE + Huffman is what achieves the actual bit savings

## Connections
- [[lossless-vs-lossy-compression]] — transform coding enables lossy compression through quantization
- [[jpeg-compression-pipeline]] — JPEG uses 8×8 DCT + quantization + Huffman coding
- [[jpeg2000-wavelet-compression]] — JPEG2000 uses DWT instead of DCT
- [[run-length-encoding]] — RLE compresses the many zero coefficients after quantization
- [[entropy-coding-huffman-arithmetic]] — final entropy coding stage of transform coding pipelines
- [[mpeg-video-compression]] — MPEG uses DCT for intra-frame coding
- [[h264-avc-video-compression]] — H.264 uses integer approximations of DCT (4×4 blocks)
- [[color-space-conversion-ycbcr]] — color space conversion is applied before DCT in JPEG/MPEG

## Open Questions
- How do learned transforms (via neural networks) compare to hand-crafted DCT/DWT?
- What is the optimal block size for DCT-based compression of different image types?
- Why hasn't DWT (JPEG2000) replaced DCT (JPEG) in practice despite theoretical advantages?
