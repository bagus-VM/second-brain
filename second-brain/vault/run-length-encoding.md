---
title: "Run-Length Encoding (RLE)"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lossless-vs-lossy-compression]
---

## One-line Summary
Run-length encoding compresses data by replacing consecutive identical bytes (runs) with a single byte plus a count, achieving high compression on data with long repetitive sequences.

## Core Intuition
Many data types contain long stretches of identical values — think of a black-and-white fax image with large white areas, or the many zero-valued high-frequency DCT coefficients after JPEG quantization. Instead of storing each repeated byte individually, RLE stores the byte once along with how many times it repeats. The simpler the repetition pattern, the better RLE works.

## Formal Definition / Statement
Given a sequence of bytes, RLE replaces each run of identical bytes (longer than a threshold `x`, the offset) with:
1. The repeated byte value
2. A flag/separator character
3. The run length minus the offset: (count - x)

If a byte appears ≤ x times in sequence, it is stored literally (no compression for short runs).

Example with separator '!' and offset x=4:
```
Input:  ABCCCCCCCCCCDEFGGGGH
Runs:   A(1) B(1) C(10) D(1) E(1) F(1) G(4) H(1)
Output: ABC!6DEFG!0H
```
C has 10 repetitions, exceeds offset 4: stored as C!6 (10-4=6)
G has 4 repetitions, equals offset 4: stored as G!0 (4-4=0)

## Key Properties
- **Lossless**: decode(encode(x)) = x exactly
- **Simple and fast**: O(n) encoding and decoding
- **Best case**: data with very long runs → compression ratio up to ~259:3 (as in the example)
- **Worst case**: data with no runs → output is larger than input (overhead from flags for single bytes)
- **Requires a separator/escape character**: must not appear literally in the data (or use a more complex encoding scheme)
- **Two-pass (static)**: first pass counts frequencies, second pass codes; or one-pass (adaptive)
- RLE is often combined with other methods — e.g., in JPEG, RLE is applied to zero-valued AC coefficients after quantization, then Huffman coding is applied

## Worked Example
Consider encoding "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB" (fax-like data):
- Run of 12 W's: W!8 (12-4=8)
- B (literal)
- Run of 12 W's: W!8
- Run of 3 B's: B (literal, below threshold)
- Run of 24 W's: W!20
- B (literal)

Without RLE: 53 bytes. With RLE: significantly fewer, especially for images with large uniform regions.

In JPEG specifically, after DCT and quantization, many high-frequency AC coefficients become zero. The zig-zag scan groups these zeros together, creating long runs that RLE can compress efficiently. The RLE encoding used in JPEG is specialized: it encodes (run_of_zeros, value) pairs rather than simple byte repetition.

## Common Pitfalls
- Assuming RLE always compresses — for data with no runs (e.g., natural text, random data), RLE increases size
- Forgetting the overhead: each run requires a flag character and count, so short runs (below offset) must be handled
- Confusing JPEG's specialized RLE (which encodes zero-run + coefficient pairs) with generic byte-level RLE
- Not realizing RLE is almost always combined with other methods (Huffman, arithmetic coding) in practice
- Thinking RLE is only for images — it's also used in fax transmission (ITU T.4), BMP files, and PCX format

## Connections
- [[lossless-vs-lossy-compression]] — RLE is a fundamental lossless compression method
- [[entropy-coding-huffman-arithmetic]] — RLE output is often further compressed with Huffman coding
- [[jpeg-compression-pipeline]] — JPEG uses RLE on zero-valued AC coefficients after zig-zag scan
- [[mpeg-video-compression]] — MPEG intra-frame coding uses RLE on DCT coefficients
- [[h264-avc-video-compression]] — H.264 uses similar run-level coding for transform coefficients

## Open Questions
- What is the optimal offset threshold for different data types?
- How does RLE compare to dictionary-based methods ([[lz77-lzw-compression]]) for structured data?
- Can adaptive RLE schemes outperform fixed-threshold RLE?
