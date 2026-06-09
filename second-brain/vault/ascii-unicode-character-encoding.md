---
title: "ASCII and Unicode Character Encoding"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
ASCII is a 7-bit character encoding for English characters; Unicode extends this to support virtually all writing systems using variable-length encodings like UTF-8, UTF-16, and UTF-32.

## Core Intuition
Computers store numbers, not letters. A character encoding is the mapping between numeric codes and the characters humans read. ASCII (American Standard Code for Information Interchange) was the first widely adopted standard, using 7 bits (128 values) for English letters, digits, and control characters. But 128 values cannot represent the world's writing systems, so ISO character sets (like Latin-1) extended ASCII to 8 bits for accented characters, and Unicode was created to unify all scripts in a single encoding — over 149,000 characters across 159 scripts.

## Formal Definition / Statement
- **ASCII**: 7-bit code (0–127). Covers A–Z, a–z, 0–9, punctuation, and 33 control characters. The 8th bit was left free for extensions or special characters.
- **ISO character sets**: 8-bit extensions of ASCII (e.g., ISO 8859-1 / Latin-1 covers Western European languages using codes 128–255).
- **Unicode**: Universal character set assigning a unique code point (U+0000 to U+10FFFF) to every character. Encoded via:
  - **UTF-8**: Variable-length (1–4 bytes), backward-compatible with ASCII.
  - **UTF-16**: Variable-length (2 or 4 bytes), common in Windows/Java.
  - **UTF-32**: Fixed-length (4 bytes), simple but space-inefficient.

## Key Properties
- ASCII is a subset of UTF-8 — any valid ASCII text is also valid UTF-8.
- UTF-8 is the dominant encoding on the web (~98% of websites).
- Unicode includes not just scripts but also symbols, emoji, and control characters.
- Byte Order Mark (BOM) is used in UTF-16/UTF-32 to indicate endianness.
- "Characters" vs "graphemes": a single user-perceived character may be multiple Unicode code points (e.g., é can be U+00E9 or U+0065 + U+0301).

## Worked Example
Encoding the letter 'A':
- ASCII: 0x41 (65 decimal), 7-bit: `1000001`
- UTF-8: 0x41 (same as ASCII, 1 byte)
- UTF-16: 0x0041 (2 bytes, big-endian)

Encoding '€' (Euro sign):
- ASCII: not representable
- Latin-1 (ISO 8859-1): not representable
- UTF-8: 0xE2 0x82 0xAC (3 bytes)
- Unicode code point: U+20AC

## Common Pitfalls
- Assuming ASCII can store accented characters (é, ü, ñ) — it cannot; these require extensions or Unicode.
- Confusing "character" with "byte" in UTF-8: a single character may occupy 1–4 bytes, so string length ≠ byte count.
- Ignoring encoding when reading files — interpreting UTF-8 bytes as Latin-1 (or vice versa) produces "mojibake" (garbled text).
- Thinking Unicode is a fixed-width encoding — only UTF-32 is fixed-width; UTF-8 and UTF-16 are variable-width.

## Connections
- [[xml-structured-text]] — XML documents specify their character encoding (typically UTF-8) in the prolog
- [[video-formats-container-vs-codec]] — container formats like WebM and MP4 must also handle text encoding for subtitles and metadata
- [[audio-sampling-nyquist-theorem]] — analogous digitization concept: continuous signal → discrete samples (analogous to character → code point)
- [[multimedia-database-intro]] — text is one of the discrete media types managed by MMDBMS
- [[multimedia-databases-lecture-03]] — lecture 3 covered image encoding; this lecture covers text encoding

## Open Questions
- How do modern databases handle Unicode collation (sorting order) across different languages and locales?
- What are the implications of UTF-8's variable-length encoding for text indexing and random access in multimedia databases?
- How does Unicode normalization (NFC vs NFD) affect text search and comparison in a database?
