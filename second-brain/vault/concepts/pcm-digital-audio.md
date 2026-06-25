---
title: "PCM and Digital Audio"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [audio-sampling-nyquist-theorem]
---

## One-line Summary
Pulse Code Modulation (PCM) is the standard method for digitizing analog audio by sampling the signal at regular intervals and encoding each sample as a binary number.

## Core Intuition
PCM is the bridge between the analog world (continuous sound waves) and the digital world (discrete numbers stored in computers). It has two steps: (1) **sampling** — measure the amplitude at regular time intervals (determined by the sampling rate), and (2) **quantization** — round each measurement to the nearest level in a finite set (determined by bit depth). The result is a stream of binary numbers that can be stored, transmitted, and reconstructed back into sound.

## Formal Definition / Statement
**PCM encoding process:**
1. **Sample** the analog signal every ΔT seconds (sampling rate = 1/ΔT).
2. **Quantize** each sample to the nearest of 2^b levels, where b = bit depth.
3. **Encode** each quantized value as a b-bit binary number.

**Standard PCM formats:**
| Format | Sampling Rate | Bit Depth | Channels | Data Rate |
|--------|--------------|-----------|----------|-----------|
| CD Audio | 44.1 kHz | 16-bit | 2 (stereo) | 1,411.2 kbps |
| DVD Audio | 48/96 kHz | 16/24-bit | 2–6 | up to 9.2 Mbps |
| Telephone | 8 kHz | 8-bit (μ-law) | 1 (mono) | 64 kbps |

**Data rate calculation:**
Data rate = Sampling rate × Bit depth × Number of channels

Example (CD): 44,100 × 16 × 2 = 1,411,200 bits/s = 176.4 KB/s ≈ 10.6 MB/min

## Key Properties
- PCM is **uncompressed** — it stores every sample at full precision.
- It is the basis for almost all digital audio formats — even compressed formats (MP3, AAC) decode to PCM for playback.
- **Linear PCM (LPCM)**: Each quantization level is equally spaced. This is the standard for CD audio.
- **Companded PCM** (μ-law, A-law): Non-uniform quantization that provides better quality at lower bit depths by using finer levels for quiet sounds and coarser levels for loud sounds. Used in telephone systems.
- PCM audio is stored as raw samples — no compression, no headers (in its purest form). File formats like WAV add headers and metadata.

## Worked Example
Digitizing a 1-second audio clip at CD quality:
1. Sampling rate: 44,100 samples/second
2. Bit depth: 16 bits per sample
3. Channels: 2 (stereo)

Samples collected: 44,100 × 2 = 88,200 samples
Bits per sample: 16
Total bits: 88,200 × 16 = 1,411,200 bits = 176,400 bytes ≈ 172 KB

For a 3-minute song: 172 KB/s × 180s ≈ 30.2 MB (uncompressed)

This illustrates why audio compression (MP3, AAC) is important — MP3 at 128 kbps reduces this to ~2.8 MB, a ~10× reduction.

## Common Pitfalls
- Confusing PCM with a file format: PCM is an encoding method, not a file format. WAV, AIFF, and FLAC all use PCM internally but differ in file structure and compression.
- Thinking bit depth affects frequency: bit depth affects amplitude resolution (dynamic range), not which frequencies are captured. Sampling rate determines frequency range.
- Ignoring that 16-bit PCM provides 2^16 = 65,536 quantization levels — this seems like a lot, but the quantization error is still audible in some contexts (hence 24-bit for professional audio).
- Assuming higher sampling rates always sound better: above ~48 kHz, the benefit is marginal for human perception (see [[audio-sampling-nyquist-theorem|Nyquist theorem]]).

## Connections
- [[audio-sampling-nyquist-theorem]] — Nyquist theorem determines the minimum sampling rate for PCM
- [[audio-quantization-pcm]] — quantization is the second step of PCM, determining amplitude precision
- [[video-formats-container-vs-codec]] — PCM audio streams are stored in container formats (WAV, AVI, MKV)
- [[multimedia-database-intro]] — PCM is the uncompressed representation that MMDBMS must handle for audio storage and streaming
- [[ascii-unicode-character-encoding]] — analogous digitization: characters → code points (text) vs. amplitudes → binary numbers (audio)

## Open Questions
- Why is 44.1 kHz the standard for CD audio instead of 48 kHz (which would be a rounder number)?
- How does companding (μ-law/A-law) work mathematically, and why is it used for telephone audio?
- What is the relationship between PCM and delta modulation / delta-sigma modulation?
