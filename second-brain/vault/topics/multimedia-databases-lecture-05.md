---
title: "Topic: Multimedia Databases — Lecture 05 (Coding and Compression)"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Multimedia Databases — Lecture 05: Coding and Compression

**Lecturer**: Prof. (FH) PD Dr. Mario Döller
**Date processed**: 2026-06-01
**Exam**: 21 July 2026

## Lecture Overview

This lecture covers data compression for multimedia — the techniques that make storage and transmission of images, video, and audio practical. It begins with motivation (why compression is essential for multimedia), covers classification criteria (lossless vs. lossy, symmetric vs. asymmetric, entropy vs. source coding), then presents three fundamental compression methods: run-length encoding, statistical coding (Huffman), and transform coding (DCT). The lecture then applies these to JPEG image compression and extends to video compression (MPEG-1/2, MPEG-4, H.264/AVC), covering motion estimation, motion compensation, and the I/P/B frame structure.

## Sections Covered

### 1. Motivation: Why Compression?
- Raw multimedia data is enormous: HD 1080p image = 6.22 MB; 1 second of 60fps video = 373 MB
- Compression ratios by medium: text (1:2–1:3), images (1:15–1:35), video (1:60–1:240)
- Compression makes storage, transmission, and streaming feasible

### 2. Compression Criteria
- [[lossless-vs-lossy-compression]] — fundamental distinction: reversible (lossless) vs. irreversible (lossy)
- Symmetric vs. asymmetric: symmetric for real-time communication (≤150ms delay); asymmetric for one-to-many distribution (encode once, decode many)
- Entropy coding (data-agnostic, lossless, ~2× ratio) vs. source coding (perception-aware, lossless or lossy, much higher ratios)
- Requirements: resolution independence, audio/video sync, interoperability, random access (≤0.5s), fast forward/backward

### 3. Run-Length Encoding
- [[run-length-encoding]] — lossless method replacing repeated byte sequences with (byte, count) pairs
- Best for data with long runs (e.g., black-and-white images, zero-valued DCT coefficients)
- Offset threshold determines minimum run length for compression

### 4. Statistical Coding (Entropy Coding)
- [[entropy-coding-huffman-arithmetic]] — variable-length codes based on symbol probability
- Huffman coding: optimal prefix-free codes, bottom-up tree construction, two-pass (static) or one-pass (adaptive)
- Properties: no compression for random data, code tree must be stored (overhead)
- Used as final stage in JPEG, MPEG, and many other compression pipelines

### 5. Transformation Coding
- [[transform-coding]] — convert data to frequency domain for better compression
- DCT (JPEG, MPEG), DWT (JPEG2000), FFT (general)
- Energy compaction: most information in few low-frequency coefficients
- Quantization of high-frequency coefficients → zeros → RLE + Huffman

### 6. JPEG Compression
- [[jpeg-compression-pipeline]] — (already exists) 8×8 DCT + quantization + entropy coding
- Four modes: baseline (DCT+Huffman), progressive, lossless (DPCM), hierarchical
- Pipeline: RGB→[[color-space-conversion-ycbcr|YCbCr]] → subsampling → DCT → quantization → zig-zag → RLE → Huffman
- DC coefficients: differential coding; AC coefficients: RLE of zero-runs + Huffman

### 7. Video Compression: MPEG-1/2
- [[mpeg-video-compression]] — intra-frame (JPEG-like) + inter-frame (motion-compensated) coding
- I-frames (independent), P-frames (forward prediction), B-frames (bi-directional prediction)
- GOP structure: I-BB-P-BB-P-BB-P-BB-I; GOP = unit of random access
- Motion estimation: block matching with MSE/SAE; motion vectors + residual
- Slices for error resilience; macroblocks (16×16) as coding units

### 8. Motion Compensation
- Motion estimation: find best matching block in reference frame within search window
- Algorithms: exhaustive search, spiral search, three-step search, sub-sampling, Fourier-based
- Rate control: decide per-block whether inter-coding (MV+residual) or intra-coding is more efficient
- Smaller blocks → better motion capture but more overhead (more MVs to store)

### 9. MPEG-4
- Object-based coding: video = multiple independent AV-objects, each with own codec
- Scene description (BIFS/LASeR): interactive scenes, user can manipulate objects
- Focus on new use cases (mobile, video conferencing) rather than compression improvement

### 10. H.264/AVC
- [[h264-avc-video-compression]] — ~2× compression improvement over MPEG-2
- Flexible macroblock partitioning (16×16 down to 4×4)
- Skipped (S) macroblocks with motion vector prediction
- Intra-prediction (9 modes) from neighboring pixels
- Quarter-pixel motion estimation (6-tap FIR filter)
- CABAC (context-adaptive arithmetic coding)
- In-loop deblocking filter

### 11. Rate-Distortion Theory
- [[rate-distortion-theory]] — fundamental tradeoff: rate (bits) vs. distortion (quality loss)
- Quantization parameter (QP) controls the tradeoff per frame/macroblock
- Rate control: constrained optimization to meet bitrate targets
- ML approaches (MuZero) for adaptive rate control

### 12. Further Codecs and Tools
- H.265/HEVC: coding tree units, ~2× better than H.264
- Container formats: MPG, VOB, AVI, MKV, MP4, WebM
- Tools: ffmpeg, mplayer/mencoder, gstreamer, x264
- [[video-formats-container-vs-codec]] — container (file structure) vs. codec (compression algorithm)

## Key Concepts Summary

| Concept | Core Idea |
|---------|-----------|
| Lossless compression | decode(encode(x)) = x; bounded by entropy |
| Lossy compression | decode(encode(x)) ≈ x; rate-distortion tradeoff |
| Entropy coding | Variable-length codes based on probability; Huffman, arithmetic |
| Run-length encoding | Replace repeated sequences with (byte, count) |
| Transform coding | DCT/DWT converts to frequency domain; quantize high frequencies |
| YCbCr + subsampling | Separate luma/chroma; 4:2:0 = 50% reduction with minimal quality loss |
| JPEG | 8×8 DCT + quantization + zig-zag + RLE + Huffman |
| I-frame | Independently coded (like JPEG); random access point |
| P-frame | Predicted from previous I/P frame; motion vector + residual |
| B-frame | Bi-directional prediction from past and future I/P frames |
| GOP | Sequence between I-frames; unit of random access |
| Motion estimation | Find best matching block in reference frame |
| Motion compensation | Encode motion vector + prediction residual |
| Macroblock | 16×16 coding unit in MPEG; flexible partitions in H.264 |
| H.264 improvements | QPEL, intra-prediction, CABAC, deblocking filter, flexible partitions |
| Rate-distortion | Tradeoff between bits spent and quality achieved |
| QP | Quantization parameter; lower = better quality, more bits |

## Connections to Other Lectures
- [[multimedia-databases-lecture-04]] — Lecture 04 covered text, video, audio media types; this lecture covers how to compress them
- [[multimedia-databases-lecture-03]] — Lecture 03 covered image representation and file formats; JPEG is the compression counterpart
- [[jpeg-compression-pipeline]] — detailed JPEG pipeline from Lecture 03
- [[jpeg2000-wavelet-compression]] — JPEG2000 uses DWT instead of DCT (mentioned briefly)
- [[video-formats-container-vs-codec]] — container vs. codec distinction from Lecture 04
- [[audio-quantization-pcm]] — audio quantization (Lecture 04) is analogous to image/video quantization
- [[color-quantization]] — color quantization (Lecture 03) vs. frequency-domain quantization (this lecture)

## Exam-Relevant Points
- Explain the difference between lossless and lossy compression; give examples of each
- Describe the Huffman coding algorithm: frequency counting, bottom-up tree construction, code assignment
- Calculate Huffman codes for a given symbol set; compute compression ratio
- Explain run-length encoding with offset threshold
- Describe the JPEG compression pipeline: color space conversion, subsampling, DCT, quantization, zig-zag, RLE, Huffman
- Explain why DCT concentrates energy in low-frequency coefficients
- Distinguish I-frames, P-frames, and B-frames; explain their roles in GOP structure
- Describe motion estimation and motion compensation: what is a motion vector, how is block matching done?
- Explain the difference between intra-coding and inter-coding
- Know the key improvements of H.264 over MPEG-2: flexible partitions, QPEL, intra-prediction, CABAC, deblocking
- Understand rate-distortion tradeoff and the role of QP
- Distinguish symmetric from asymmetric compression
- Explain entropy coding vs. source coding
