---
title: "Entropy Coding: Huffman and Arithmetic Coding"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lossless-vs-lossy-compression]
---

## One-line Summary
Entropy coding assigns variable-length codes to symbols based on their probability — frequent symbols get short codes, rare symbols get long codes — achieving compression bounded by the source entropy.

## Core Intuition
Shannon's information theory tells us that the minimum average code length for a symbol is its information content: -log₂(p) bits. Entropy coding tries to approach this limit. The key insight: if a symbol appears 80% of the time, it should get a much shorter code than a symbol appearing 1% of the time. The challenge is ensuring no ambiguity in decoding — the coded bitstream must be uniquely decodable.

## Formal Definition / Statement
**Entropy** of a source with symbols {s₁, s₂, ..., sₙ} with probabilities {p₁, p₂, ..., pₙ}:
```
H = -Σ pᵢ × log₂(pᵢ)    (bits per symbol)
```

Shannon's source coding theorem: no uniquely decodable code can have average length less than H. Entropy coding methods aim to approach this bound.

**Huffman Coding**:
1. Sort symbols by frequency
2. Build a binary tree bottom-up: repeatedly merge the two least-frequent nodes
3. Assign 0/1 to left/right branches
4. Code for each symbol = path from root to leaf

**Arithmetic Coding**:
- Represents the entire message as a single floating-point number in [0, 1)
- Successively narrows the interval based on symbol probabilities
- More efficient than Huffman for short messages and can achieve fractional bit lengths

## Key Properties
- **Huffman coding** is optimal among prefix-free codes (no codeword is a prefix of another)
- **Prefix-free property** ensures unique decodability without explicit separators
- **Static Huffman**: two passes — first to count frequencies, second to encode. Requires storing the code tree with the data (overhead, negligible for large data, or use standard codebook like JPEG)
- **Adaptive Huffman**: one pass, updates tree as symbols are processed
- **Arithmetic coding** can be more efficient than Huffman (fractional bits per symbol) but is computationally more expensive
- Both are **lossless** and remove only statistical redundancy
- No compression for random data (all symbols equally probable → entropy = log₂(n))
- Both are used as final stages in multimedia compression pipelines (JPEG, MPEG, H.264)

## Worked Example
**Huffman coding** for text "AABAACDAAEABACD":

| Symbol | Frequency | Probability | Huffman Code |
|--------|-----------|-------------|--------------|
| A      | 8         | 8/15        | 0            |
| B      | 2         | 2/15        | 100          |
| C      | 2         | 2/15        | 101          |
| D      | 2         | 2/15        | 110          |
| E      | 1         | 1/15        | 111          |

Tree construction (bottom-up):
```
Start: E:1  B:2  C:2  D:2  A:8
Merge E+B → Z:3:          Z:3  C:2  D:2  A:8
Merge C+D → Y:4:          Z:3  Y:4  A:8
Merge Z+Y → X:7:          X:7  A:8
Merge X+A → W:15 (root)
```

Encoded: AABAACDAAEABACD → 0|0|100|0|0|101|0|0|111|0|100|0|101|110 = 29 bits
(Original: 15 chars × 8 bits = 120 bits → compression ratio ~4:1)

## Common Pitfalls
- Confusing Huffman (optimal prefix-free codes) with arithmetic coding (optimal sequential codes) — arithmetic can be better for small alphabets or skewed distributions
- Forgetting that the code tree/codebook must be stored or agreed upon — constant overhead
- Assuming Huffman coding works well on random data — it doesn't (no redundancy to exploit)
- Not recognizing that Huffman requires two passes (static version), making it unsuitable for streaming without adaptation
- Thinking entropy coding alone is sufficient for multimedia compression — it's always combined with source coding (transform, prediction, motion compensation)

## Connections
- [[lossless-vs-lossy-compression]] — entropy coding is the lossless component of multimedia compression pipelines
- [[run-length-encoding]] — often applied before Huffman coding to create longer runs of identical symbols
- [[jpeg-compression-pipeline]] — uses Huffman coding as final entropy coding stage (DC differentials + AC RLE + Huffman)
- [[mpeg-video-compression]] — MPEG uses Huffman coding for DCT coefficients
- [[h264-avc-video-compression]] — H.264 uses context-adaptive binary arithmetic coding (CABAC) instead of Huffman
- [[lz77-lzw-compression]] — dictionary-based compression is an alternative to statistical coding
- [[ascii-unicode-character-encoding]] — character encoding is prerequisite for understanding symbol alphabets

## Open Questions
- When does arithmetic coding definitively outperform Huffman, and by how much?
- How do modern entropy coders (ANS, range coding) compare to Huffman and arithmetic coding?
- What is the practical overhead of storing Huffman codebooks for small data?
