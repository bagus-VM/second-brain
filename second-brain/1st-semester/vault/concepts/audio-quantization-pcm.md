---
title: "Audio Quantization"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [audio-sampling-nyquist-theorem, pcm-digital-audio]
---

## One-line Summary
Quantization in audio is the process of mapping continuous amplitude values to a finite set of discrete levels, introducing a small error that is inversely proportional to the number of bits used.

## Core Intuition
After sampling captures the signal's amplitude at regular time intervals, each measured value is a continuous real number. But digital systems can only store discrete values — we must round each sample to the nearest representable level. This rounding is quantization. More bits = more levels = smaller rounding error = higher quality. Fewer bits = fewer levels = larger error = audible distortion. The quantization error is the difference between the true amplitude and the stored value — it manifests as noise (quantization noise).

## Formal Definition / Statement
- **Quantization**: Mapping a continuous amplitude value to the nearest of N = 2^b discrete levels, where b = bit depth.
- **Quantization error**: The difference between the true sample value and the quantized value. Bounded by ±(1/2) × (step size), where step size = (max amplitude - min amplitude) / N.
- **Signal-to-Quantization-Noise Ratio (SQNR)**: For linear PCM with b bits:
  - SQNR ≈ 6.02b + 1.76 dB
  - Each additional bit adds ~6 dB of dynamic range.

**Quantization levels by bit depth:**
| Bit Depth | Levels (2^b) | Dynamic Range | Use Case |
|-----------|-------------|---------------|----------|
| 8-bit | 256 | ~48 dB | Low-quality, telephone |
| 16-bit | 65,536 | ~96 dB | CD audio |
| 24-bit | 16,777,216 | ~144 dB | Professional audio |
| 32-bit float | N/A (floating point) | ~1528 dB | Audio processing |

**The three-step digitization process (illustrated):**
1. Start with a continuous sine wave.
2. **Sample**: Measure amplitude at regular intervals → discrete time, continuous amplitude.
3. **Quantize**: Round each measurement to nearest level → discrete time, discrete amplitude (4-bit in the lecture example).

## Key Properties / Complexity
- Quantization is **lossy** — information is permanently lost. You cannot recover the original continuous signal from quantized samples (though the error can be made arbitrarily small with more bits).
- **Uniform quantization** (linear PCM): All levels are equally spaced. Simple but wastes bits on quiet signals where fine precision matters most.
- **Non-uniform quantization** (μ-law, A-law): Levels are closer together near zero (quiet sounds) and farther apart at extremes (loud sounds). Better perceptual quality at the same bit depth.
- **Dithering** (audio context): Adding low-level noise before quantization to decorrelate quantization error from the signal, making it sound like white noise rather than distortion. Analogous to image dithering from [[multimedia-databases-lecture-03|Lecture 3]].
- **Quantization noise** is approximately uniformly distributed and uncorrelated with the signal (for fine quantization).

## Worked Example
Quantizing a sine wave with amplitude range [-1, +1] using 4 bits (16 levels):

Step size = 2 / 16 = 0.125

| True Value | Quantized Value | Error |
|-----------|----------------|-------|
| 0.73 | 0.75 (level 12) | +0.02 |
| 0.31 | 0.3125 (level 10) | +0.0025 |
| -0.18 | -0.1875 (level 7) | -0.0075 |
| -0.91 | -0.9375 (level 1) | -0.0275 |

SQNR ≈ 6.02 × 4 + 1.76 = 25.84 dB (poor quality — audible noise)

With 16 bits: SQNR ≈ 6.02 × 16 + 1.76 = 98.08 dB (CD quality — noise below hearing threshold)

## Common Pitfalls
- Confusing quantization with sampling: sampling determines *when* to measure (temporal resolution); quantization determines *how precisely* to measure (amplitude resolution).
- Thinking more bits always means better quality: beyond 24-bit, the quantization noise is below the thermal noise floor of any analog circuit — additional bits are wasted.
- Ignoring quantization in compression: lossy audio codecs (MP3, AAC) intentionally reduce quantization precision for frequency components that are masked by louder sounds — this is how they achieve compression.
- Confusing quantization error with clipping: clipping occurs when the signal exceeds the representable range; quantization error occurs within the range due to finite precision.

## Connections
- [[audio-sampling-nyquist-theorem]] — sampling determines temporal resolution; quantization determines amplitude resolution. Both are needed for PCM.
- [[pcm-digital-audio]] — quantization is the second step of PCM encoding
- [[multimedia-databases-lecture-03]] — colour quantization in images is directly analogous (reducing colour palette ≈ reducing amplitude levels)
- [[dithering]] — audio dithering and image dithering share the same underlying principle
- [[video-formats-container-vs-codec]] — lossy codecs exploit quantization to achieve compression (both audio and video)

## Open Questions
- How do perceptual audio codecs (MP3, AAC) decide which frequency components to quantize more coarsely?
- What is the relationship between quantization bit depth and dynamic range in practical recording scenarios?
- How does noise shaping in audio dithering compare to error diffusion in image dithering (Floyd-Steinberg)?
