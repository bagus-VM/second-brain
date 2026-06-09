---
title: "Topic: Multimedia Databases — Lecture 04 (Media: Text, Video, Audio)"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Multimedia Databases — Lecture 04: Media: Text, Video, Audio

**Lecturer**: Prof. (FH) PD Dr. Mario Döller
**Date processed**: 2026-06-01
**Exam**: 21 July 2026

## Lecture Overview

This lecture covers the three major media types — text, video, and audio — with focus on their digital representation, structure, and processing. Text is addressed through character encoding (ASCII, Unicode) and structured markup (XML). Video is examined through its hierarchy (frames → shots → scenes), shot segmentation algorithms, video summarization, and format/container/codec distinctions. Audio is covered through analog-to-digital conversion: sampling (Nyquist theorem), PCM encoding, and quantization.

## Sections Covered

### 1. Characters and Typographic Classification
- [[ascii-unicode-character-encoding]] — 7-bit ASCII, ISO character sets, Unicode (UTF-8/16/32)
- Typographic measurements: font size in points (1 pt = 1/72 inch), relative measures (ex = glyph height, em = glyph width)
- Glyph features: monospaced vs. proportional, serif vs. sans-serif, kerning, ligatures
- Character representation: bitmapped fonts (pixel grids) vs. outlined fonts (vector curves)

### 2. Media Type Text
- [[ascii-unicode-character-encoding]] — Representation: ASCII, ISO character sets, markup text, structured text, hypertext
- Text operations: character/string comparison, concatenation, editing, formatting, pattern recognition (regular expressions), sorting, compression (Huffman coding), encryption (DES, public-key cryptography)
- Hypertext: graph-oriented combination of information units (nodes, edges, links)

### 3. XML (Extensible Markup Language)
- [[xml-structured-text]] — W3C standard since 1996, subset of SGML
- Combines SGML's flexibility with HTML's wide acceptance
- Well-formedness rules: single root, hierarchical tree, valid characters
- Validation via DTD or XML Schema
- Platform-independent, self-describing, ideal for data exchange

### 4. Video Hierarchy
- [[video-hierarchy-shots-scenes]] — Frame (atomic) → Shot (continuous camera take) → Scene (semantically coherent)
- Physical segments (objective, automatable) vs. logical segments (semantic, subjective)
- Shot characteristics: general/medium/close-up; static/dynamic
- Scene = sequence of shots coherent in time and space; scene detection is subjective

### 5. Shot Segmentation
- [[shot-segmentation]] — Automatic detection of shot boundaries
- Shot boundary types: hard cut (sudden), fade (brightness → black), dissolve (mix), wipe (push)
- Detection methods: pixel-based, histogram-based, edge-based (Canny, Sobel), macroblock-based (compressed domain)
- Twin-comparison for gradual transitions: low threshold for cumulative difference, high threshold for hard cuts
- Evaluation: Recall = S_D/(S_D + S_M), Precision = S_D/(S_D + S_F)

### 6. Video Summarization and Key Frames
- [[video-summarization-key-frames]] — Static (storyboard) vs. dynamic (video skim) summaries
- Key frame extraction: optimal (compare all frames), first frame, most complex content
- Requirements: conciseness, content representation, coherence
- Independent (whole-content preview) vs. dependent (query-driven) summarization

### 7. Video Formats
- [[video-formats-container-vs-codec]] — Container (file structure, multiplexing) vs. codec (compression algorithm)
- Containers: MPG, VOB, AVI, ASF, MKV, MP4, WebM, MOV, FLV
- Codecs: H.264/AVC, H.265/HEVC, VP8, VP9, AV1, MPEG-1/2/4
- WebM: open standard by Google (BSD), VP8 + Vorbis, HTML5 `<video>` tag

### 8. Video Frame Rate and Resolution
- [[video-frame-rate-resolution]] — Progressive (p) vs. interlaced (i) scanning
- Interlaced = two fields per frame (odd + even lines), doubles perceived temporal resolution
- Standard resolutions: 576i (PAL), 720p (HDTV), 1080p/i (Full HD), 2K/4K (cinema), 8K (UHDTV)
- Common frame rates: 24 fps (cinema), 25 fps (PAL), 29.97/30 fps (NTSC), 50/60 fps (HFR)

### 9. Audio: Sampling, Nyquist Theorem, and PCM
- [[audio-sampling-nyquist-theorem]] — Nyquist-Shannon theorem: sampling rate ≥ 2 × f_max
- Human hearing: 20 Hz – 20 kHz; CD sampling at 44.1 kHz
- [[pcm-digital-audio]] — Pulse Code Modulation: sample → quantize → encode
- CD quality: 44.1 kHz × 16-bit × 2 channels = 1,411.2 kbps
- [[audio-quantization-pcm]] — Quantization error, SQNR ≈ 6.02b + 1.76 dB
- Sound pressure levels: 0 dB (threshold) to 130 dB (pain), quasi-logarithmic perception

## Key Concepts Summary

| Concept | Core Idea |
|---------|-----------|
| ASCII | 7-bit character encoding, 128 values |
| Unicode | Universal character set, UTF-8/16/32 encodings |
| XML | Self-describing markup, well-formedness + validation |
| Video hierarchy | Frame → Shot → Scene (increasing semantic level) |
| Hard cut | Sudden full-frame change between consecutive frames |
| Dissolve | Gradual mix of two shots over several frames |
| Color histogram comparison | Robust shot detection via color distribution difference |
| Macroblock analysis | Compressed-domain shot detection using I/P/B block ratios |
| Key frame | Representative frame from a shot/scene |
| Container | File structure holding multiplexed streams (MP4, MKV, AVI) |
| Codec | Compression algorithm (H.264, VP9, AV1) |
| Progressive scan | Full frame captured in single pass |
| Interlaced scan | Two fields (odd + even lines) per frame |
| Nyquist theorem | Sample rate ≥ 2× max frequency for perfect reconstruction |
| PCM | Sample → quantize → encode (standard digital audio) |
| Quantization | Mapping continuous amplitude to discrete levels |
| SQNR | ~6 dB per bit of quantization precision |

## Connections to Other Lectures
- [[multimedia-databases-lecture-03]] — Lecture 3 covered images (bitmap, color quantization, dithering, file formats, filters); this lecture extends to video (temporal sequence of images) and audio
- [[multimedia-database-intro]] — All three media types (text, video, audio) are managed by MMDBMS
- [[multimedia-definition]] — Text is discrete; video and audio are continuous media types
- [[image-point-operations]] — Color quantization in images is analogous to amplitude quantization in audio
- [[dithering]] — Audio dithering shares the same principle as image dithering
- [[jpeg-compression-pipeline]] — JPEG compression (lecture 3) uses Huffman coding; text compression also uses Huffman

## Exam-Relevant Points
- Know ASCII (7-bit, 128 values) vs. Unicode (UTF-8 variable 1–4 bytes, backward-compatible with ASCII)
- Distinguish XML well-formedness (syntactic rules) from validity (conformance to DTD/Schema)
- Explain the video hierarchy: frame, shot, shot boundary, scene — and which levels are objective vs. subjective
- Classify shot boundary types (cut, fade, dissolve, wipe) by spatial and temporal properties
- Describe at least two shot segmentation methods (histogram-based, edge-based, macroblock-based)
- Understand the twin-comparison method for gradual transitions
- Explain key frame extraction methods and their tradeoffs
- Distinguish container (file structure) from codec (compression) — give examples of each
- Know standard video resolutions and frame rates (720p, 1080i/p, PAL vs NTSC)
- Explain the Nyquist-Shannon theorem and why CDs use 44.1 kHz sampling
- Describe PCM: sampling + quantization + encoding
- Calculate SQNR from bit depth (6.02b + 1.76 dB)
- Calculate uncompressed audio data rate (sampling rate × bit depth × channels)
- Understand quantization error and its relationship to bit depth
