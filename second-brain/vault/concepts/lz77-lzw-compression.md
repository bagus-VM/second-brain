---
title: "LZ77 and LZW Compression"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lossless-vs-lossy-compression]
---

## One-line Summary
LZ77 and LZW are adaptive, dictionary-based lossless compression methods that replace repeated subsequences with references to earlier occurrences, forming the basis of gzip, PNG, and many other widely-used formats.

## Core Intuition
Instead of encoding individual symbols (like Huffman), dictionary-based methods encode repeated *patterns*. LZ77 uses a sliding window of previously seen data as the "dictionary" — when a sequence matches something in the window, it's replaced by a (distance, length) back-reference. LZW builds an explicit dictionary on the fly — both encoder and decoder construct the same dictionary without transmitting it, enabling single-pass compression.

## Formal Definition / Statement
**LZ77** (Ziv & Lempel, 1977):
- Maintains a sliding window of the last N bytes (e.g., 32 KB)
- For each position, finds the longest match in the window
- Outputs triplets: (offset, length, next_char)
  - offset: how far back in the window the match starts
  - length: how many bytes match
  - next_char: the first unmatched byte
- If no match found: outputs literal byte (offset=0, length=0, char)
- Adaptive (one-pass), no need to transmit dictionary

**LZW** (Welch, 1984, improvement of LZ78):
- Starts with a dictionary containing all single symbols
- Reads input character by character, extending the current match
- When the match is no longer in the dictionary: output the code for the current match, add the extended string to the dictionary, start new match with the current character
- Both encoder and decoder build the same dictionary independently
- No need to transmit the dictionary

## Key Properties
- **Lossless and adaptive**: single pass through data, no prior knowledge needed
- **LZ77**: dictionary is implicit (sliding window), no dictionary storage needed
- **LZW**: dictionary is explicit and grows dynamically; fixed-width codes (e.g., 12-bit) simplify implementation
- **Combines well with other methods**: gzip = LZ77 + Huffman (Deflate algorithm); PNG uses Deflate
- **Good for text and structured data**: captures repeated words, phrases, patterns
- **Not specialized for multimedia**: doesn't exploit perceptual models; used for generic compression
- **LZ77/LZ78**: foundational; LZW was patented (patent expired 2004), which initially limited adoption

## Worked Example
**LZ77** encoding of "ABABABABABAB":
- Position 0: A → literal (0, 0, A)
- Position 1: B → literal (0, 0, B)
- Position 2: AB matches at offset 2, length 2 → (2, 2, ?)
  - Next char at position 4 is A, so (2, 2, A)
- Position 5: ABAB matches at offset 5, length 4 → (5, 4, ?)
  - Next char at position 9 is A, so (5, 4, A)
- Position 10: B → literal (0, 0, B)

Original: 12 characters = 96 bits (8-bit ASCII)
LZ77: 5 tokens with small values → significantly fewer bits

**LZW** encoding of "ABABABAB":
- Initial dictionary: {A:0, B:1}
- Read A → in dict. Read B → AB not in dict → output 0 (A), add AB:2
- Read A → in dict. Read B → AB in dict (2). Read A → ABA not in dict → output 2 (AB), add ABA:3
- Read B → in dict. Read A → BA not in dict → output 1 (B), add BA:4
- Read B → in dict. End → output 1 (B)
- Output: 0, 2, 1, 1 (4 codes, each ~2 bits = 8 bits vs. 64 bits original)

## Common Pitfalls
- Confusing LZ77 (sliding window, implicit dictionary) with LZW (explicit growing dictionary) — they're different algorithms with different tradeoffs
- Forgetting that LZW builds the same dictionary on both encoder and decoder side — no dictionary transmission needed
- Thinking dictionary-based methods are good for multimedia raw data — they're better for text/structured data; multimedia uses transform + entropy coding instead
- Not recognizing that gzip/Deflate = LZ77 + Huffman, not just LZ77 alone
- Overlooking that LZ77's sliding window size limits how far back matches can be found

## Connections
- [[lossless-vs-lossy-compression]] — LZ77/LZW are lossless, adaptive compression methods
- [[entropy-coding-huffman-arithmetic]] — Deflate (gzip) combines LZ77 with Huffman coding
- [[run-length-encoding]] — RLE is simpler but less general than dictionary-based methods
- [[ascii-unicode-character-encoding]] — dictionary-based methods operate on byte/character sequences
- [[multimedia-databases-lecture-05]] — Source lecture: Coding and Compression (RLE → entropy → transform → JPEG → video)

## Open Questions
- How do modern LZ variants (LZ4, Zstandard, Brotli) compare in speed vs. compression ratio?
- When should dictionary-based methods be preferred over entropy coding for multimedia metadata?
- What is the relationship between dictionary size and compression ratio for different data types?
