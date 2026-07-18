---
title: "MMDB Exercise 6 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What are the main steps of the JPEG Baseline Process and which are lossy?
> [!answer]- Steps: (1) Color space conversion RGB→YCbCr (lossless), (2) Chroma subsampling (lossy), (3) Block splitting into 8×8 blocks, (4) Forward DCT (lossless transform), (5) Quantization (lossy), (6) Entropy coding (lossless). **Lossy steps:** chroma subsampling and quantization.

> [!question]- Why convert RGB to YCbCr for JPEG compression?
> [!answer]- Y (luminance) and Cb/Cr (chrominance) are separated, allowing chrominance to be subsampled since the human eye is less sensitive to color detail than brightness. This enables significant compression with minimal perceptual quality loss.

> [!question]- What is chroma subsampling and what do ratios 4:4:4, 4:2:2, 4:2:0 mean?
> [!answer]- Subsampling reduces chrominance resolution relative to luminance. **4:4:4:** No subsampling (full chroma). **4:2:2:** Half horizontal chroma resolution. **4:2:0:** Quarter chroma resolution (half in both directions). Lower ratios = more compression, less color detail.

> [!question]- What is the role of the DCT in JPEG compression?
> [!answer]- The Forward DCT transforms each 8×8 pixel block from spatial to frequency domain. Low-frequency components (top-left, including DC coefficient) capture most visual information. High-frequency components (bottom-right) can be more aggressively quantized. The DC coefficient is the average value; AC coefficients represent frequency variations.

> [!question]- Why are DC and AC coefficients entropy coded differently in JPEG?
> [!answer]- DC coefficients change slowly between adjacent blocks → **DPCM** (differential coding) encodes the difference from the previous DC value. AC coefficients vary more → **RLE + Huffman** encoding is used to efficiently represent runs of zero values followed by non-zero coefficients.


---

## Related Resources

### 📖 Topic: Multimedia Databases — Lecture 05 (Coding and Compression)
- Lecture topic: [[multimedia-databases-lecture-05]]

**Key concepts covered:**
- [[lossless-vs-lossy-compression]]
- [[run-length-encoding]]
- [[lz77-lzw-compression]]
- [[entropy-coding-huffman-arithmetic]]
- [[transform-coding]]
- [[jpeg-compression-pipeline]]
- [[color-space-conversion-ycbcr]]
- [[mpeg-video-compression]]
- [[h264-avc-video-compression]]
- [[rate-distortion-theory]]
- [[video-formats-container-vs-codec]]
- [[jpeg2000-wavelet-compression]]
- [[audio-quantization-pcm]]
- [[color-quantization]]
