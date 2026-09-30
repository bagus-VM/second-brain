---
title: "Lossless vs. Lossy Compression"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lossless compression preserves all original data exactly (reversible), while lossy compression discards perceptually insignificant information to achieve higher compression ratios (irreversible).

## Core Intuition
Raw multimedia data contains massive redundancy — repeated patterns, predictable structures, and information humans cannot perceive. Compression exploits this. The fundamental question is: do we need perfect reconstruction (lossless), or is "close enough" acceptable (lossy)? Lossless methods only remove statistical redundancy; lossy methods additionally remove perceptual irrelevancy, achieving much higher compression at the cost of some quality degradation.

## Formal Definition / Statement
- **Lossless compression**: `decode(encode(x)) = x` for all inputs x. The original data is perfectly reconstructed. Achievable compression ratio is bounded by the entropy of the source (Shannon's source coding theorem).
- **Lossy compression**: `decode(encode(x)) ≈ x`. Some information is permanently discarded. Compression ratio is limited by a rate-distortion tradeoff — more distortion allows higher compression.

Classification of compression methods:
- **Entropy coding** (lossless): **ignores data properties, reduces statistical redundancy.** Examples: [[entropy-coding-huffman-arithmetic]], [[run-length-encoding]]. Low compression factors (~2×).
- **Source coding** (lossless or lossy): **exploits knowledge of the data source and human perception**. Examples: [[transform-coding]], [[mpeg-video-compression]]. Much higher compression (up to 240× for video with H.265/HEVC).

## Key Properties / Complexity
- **Entropy coding** = lossless by definition; properties of data ignored, only statistical redundancy removed
- **Source coding** = can be lossless or lossy; exploits perceptual models (e.g., human visual system, masking thresholds)
- **Static methods** = two-pass (first pass determines frequencies, second pass codes) — e.g., static Huffman
- **Adaptive methods** = one-pass (code in single scan) — e.g., [[lz77-lzw-compression]]
- **Hybrid methods** = combine both approaches
- Compression ratios vary enormously by media type:
  - Text: Huffman ~1:2, gzip ~1:3
  - Image: JPEG ~1:15 (near lossless) to ~1:35 (lossy good quality)
  - Video: MPEG-2 ~1:60, H.264 ~1:120, HEVC ~1:240
- Every compression method must provide a **CODEC** (coder + decoder pair)

## Worked Example
Consider an HD 1080p image (1920×1080, True Colour = 3 bytes/pixel):
- Raw size: 1920 × 1080 × 3 = 6.22 MB
- JPEG lossless-like (quality 100): ~415 KB → ratio ~1:15
- JPEG lossy (good quality): ~178 KB → ratio ~1:35
- JPEG2000 lossless: ~2.5 MB (perfect reconstruction)

For video at 60 fps: raw data rate = 6.22 × 60 × 8 ≈ 3 Gbit/s. Without compression, 1 second of video = 373 MB.

## Common Pitfalls
- Confusing "lossless" with "lossy" modes of the same standard (JPEG has a lossless mode, but it's rarely used and poorly supported)
- Assuming lossless compression can achieve arbitrarily high ratios — it's bounded by the source entropy
- Thinking entropy coding alone is sufficient for multimedia — the compression factors are too low for images/video
- Forgetting that **lossy compression requires a perceptual model to decide what to discard**
- Not distinguishing between symmetric (equal encode/decode time, e.g., video conferencing) and asymmetric compression (expensive encode, cheap decode, e.g., multimedia distribution)

## Connections
- [[entropy-coding-huffman-arithmetic]] — Huffman and arithmetic coding are lossless entropy coding methods
- [[run-length-encoding]] — simple lossless method for data with repeated sequences
- [[lz77-lzw-compression]] — adaptive lossless dictionary-based methods
- [[transform-coding]] — DCT/wavelet transforms enable lossy compression
- [[jpeg-compression-pipeline]] — JPEG uses lossy source coding (DCT + quantization + entropy coding)
- [[mpeg-video-compression]] — MPEG uses both intra-frame (lossy) and inter-frame (lossy) coding
- [[h264-avc-video-compression]] — H.264 achieves ~2× better compression than MPEG-2
- [[color-quantization]] — another form of lossy compression for images

## Open Questions
- What is the theoretical limit of lossless compression for typical multimedia data?
- How do learned/neural compression codecs compare to traditional lossy methods?
- Can perceptual quality metrics (SSIM, VMAF) replace PSNR for evaluating lossy compression?
