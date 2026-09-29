---
title: "H.264/AVC Video Compression"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [mpeg-video-compression, transform-coding]
---

## One-line Summary
H.264/AVC (MPEG-4 Part 10) achieves roughly double the compression efficiency of MPEG-2 through flexible macroblock partitioning, quarter-pixel motion estimation, intra-prediction, advanced entropy coding (CABAC), and in-loop deblocking filtering.

## Core Intuition
H.264 retains the fundamental MPEG approach (I/P/B frames, motion compensation, DCT-like transform) but improves every stage. Smaller and more flexible block partitions capture motion more precisely. Quarter-pixel motion estimation enables sub-pixel accuracy. Intra-prediction uses neighboring pixels as references (not just DCT). CABAC (context-adaptive arithmetic coding) replaces Huffman for better entropy coding. A deblocking filter smooths block artifacts at decode time. Together, these improvements yield ~2× better compression than MPEG-2 at the same quality.

## Formal Definition / Statement
**H.264/AVC** = MPEG-4 Part 10, Advanced Video Coding (finalized 2003, joint ITU/ISO).

Key technical improvements over MPEG-2:

1. **Flexible macroblock partitioning**: 16×16 macroblock can be split into partitions of 16×16, 16×8, 8×16, 8×8, and further into sub-partitions of 8×4, 4×8, 4×4. Partition is the unit for motion compensation.

2. **Skipped (S) macroblocks**: Only a motion vector is stored (no residual) — for static or slowly moving regions. Motion vector prediction from neighboring blocks reduces overhead.

3. **Intra-prediction** (9 modes): **Instead of coding blocks independently, predicts each block from already-decoded neighboring pixels. Only the prediction residual is coded**. Modes include: vertical, horizontal, DC (average), diagonal directions (45° left/right, 26.6° variations).

4. **Quarter-pixel (QPEL) motion estimation**: Image is upsampled 4× using a 6-tap FIR filter for luma. Motion vectors can point to ¼-pixel positions, enabling smoother motion compensation. Example: object moving 1 pixel over 4 frames = ¼ pixel/frame.

5. **Motion vector prediction**: Neighboring blocks have similar motion vectors. **Predict MV from median of neighboring blocks; only the difference (MVD) is stored**.

6. **Integer transform**: 4×4 integer approximation of DCT (avoids floating-point rounding errors).

7. **CABAC** (Context-Adaptive Binary Arithmetic Coding): better compression than Huffman by **adapting probability models based on context**.

8. **In-loop deblocking filter**: Applied at block boundaries during decoding to reduce blocking artifacts.

## Key Properties / Complexity
- **~2× compression improvement over MPEG-2** at same quality
- **Flexible block sizes**: from 16×16 down to 4×4 — adapts to image content
- **Macroblock types**: I (intra), P (inter forward), B (inter bi-directional), S (skipped)
- **Sub-pixel motion**: QPEL enables ¼-pixel accuracy → smoother motion, better prediction
- **Multiple reference frames**: can reference more than just the immediately preceding frame
- **Used everywhere**: smartphones, Blu-ray, DVB-S2 (HDTV), YouTube HD, video conferencing
- **Successor**: H.265/HEVC (2013) doubles compression again using coding tree units instead of macroblocks

## Worked Example
Encoding a macroblock in H.264:

**Step 1: Partition decision** — The 16×16 macroblock contains a moving object edge. Encoder splits into two 16×8 partitions for better motion capture.

**Step 2: Motion estimation** — For each partition, search for best match in reference frame using QPEL:
- Partition 1: best match at (12.5, 8.75) pixels offset → motion vector (50, 35) in ¼-pixel units
- Partition 2: best match at (12.25, 9.0) → motion vector (49, 36)

**Step 3: Motion vector prediction** — Neighboring blocks have MVs of (48,32), (52,34), (50,36). Median prediction = (50,34). Store MVD for partition 1: (0, 1), for partition 2: (-1, 2).

**Step 4: Transform + quantize** — Compute residual, apply 4×4 integer transform, quantize.

**Step 5: Entropy code** — CABAC encodes the quantized coefficients and metadata.

Comparison (1920×1080, 24 fps, 654 seconds):
| Method    | Size      | Ratio |
|-----------|-----------|-------|
| Raw RGB   | 91 GB     | 1:1   |
| Raw 4:2:0 | 45.5 GB   | 2:1   |
| MJPEG     | 2.9 GB    | 31:1  |
| MPEG-1    | 1.2 GB    | 75:1  |
| MPEG-4    | 1.1 GB    | 82:1  |
| H.264     | ~600 MB   | 151:1 |

## Common Pitfalls
- Confusing H.264 (codec) with MP4 (container format) — they are independent
- Forgetting that H.264's intra-prediction is fundamentally different from JPEG's independent block coding — H.264 predicts from neighbours
- Thinking QPEL is "free" — the 6-tap filter is computationally expensive
- Not understanding that the standard specifies decoding (syntax), not encoding — encoders can use any motion estimation strategy
- Overlooking the deblocking filter's role — it's applied *during* decoding (in-loop), not as a post-processing step
- Confusing H.264/AVC with H.265/HEVC — HEVC uses coding tree units (up to 64×64) instead of fixed 16×16 macroblocks

## Connections
- [[mpeg-video-compression]] — H.264 improves on MPEG-2's I/P/B frame structure and motion compensation
- [[transform-coding]] — H.264 uses 4×4 integer transform (vs. MPEG-2's 8×8 float DCT)
- [[entropy-coding-huffman-arithmetic]] — H.264 uses CABAC (arithmetic coding) instead of Huffman
- [[lossless-vs-lossy-compression]] — H.264 is lossy; deblocking filter helps mask artifacts
- [[video-formats-container-vs-codec]] — H.264 is a codec; used in MP4, MKV, FLV containers
- [[jpeg-compression-pipeline]] — I-frame coding in H.264 shares concepts with JPEG but uses intra-prediction
- [[color-space-conversion-ycbcr]] — H.264 operates on YCbCr with 4:2:0 subsampling

## Open Questions
- How does H.265/HEVC's coding tree unit approach compare to H.264's macroblock partitions in practice?
- What is the impact of reference frame count on compression efficiency vs. memory requirements?
- How do machine-learning-based codecs (e.g., learned video compression) compare to H.264?
- When does rate-distortion optimization (choosing QP per frame/macroblock) significantly improve results?
