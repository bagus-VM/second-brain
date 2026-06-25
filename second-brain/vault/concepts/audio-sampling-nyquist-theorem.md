---
title: "Audio Sampling and Nyquist Theorem"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The Nyquist-Shannon theorem states that ==to perfectly reconstruct an analog signal, it must be sampled at a rate of at least twice its maximum frequency component==.

## Core Intuition
Sound is a continuous analog pressure wave. To store it digitally, we must sample it — measure the amplitude at regular intervals. But how often must we sample? If we sample too infrequently, we miss important features of the wave and get distortion (aliasing). The Nyquist-Shannon theorem gives us the theoretical minimum: sample at least twice as fast as the highest frequency you want to capture. Since human hearing ranges from 20 Hz to 20 kHz, CDs sample at 44.1 kHz — just above the Nyquist rate for 20 kHz.

## Formal Definition / Statement
- **Audio waves**: One-dimensional acoustic (pressure) waves. Cause vibration of the eardrum (human perception) or a microphone.
- **Human hearing range**: 20 Hz – 20,000 Hz (20 kHz).
- **Perception model**: Quasi-logarithmic. The ratio of amplitudes A and B is expressed in decibels: **dB = 20 × log₁₀(A/B)**.

**Nyquist-Shannon Sampling Theorem:**
If a continuous signal contains no frequencies higher than f_max, it is completely determined by sampling at a uniform rate of at least **2 × f_max**.

- Sampling rate ≥ 2 × f_max → perfect reconstruction (theoretically)
- Sampling rate < 2 × f_max → **aliasing** (irrecoverable distortion)

**Standard sampling rates:**
| Application | Sampling Rate | Max Captured Frequency |
|-------------|--------------|----------------------|
| Telephone | 8 kHz | 4 kHz |
| CD Audio | 44.1 kHz | 22.05 kHz |
| DVD Audio | 48 kHz / 96 kHz | 24 kHz / 48 kHz |
| Professional | 96 kHz / 192 kHz | 48 kHz / 96 kHz |

**Sound pressure levels (dB SPL):**
| Source | Level |
|--------|-------|
| Very low pressure (threshold of hearing) | 0 dB |
| Conversation | 50–60 dB |
| Heavy traffic | 80 dB |
| Rock band | 120 dB |
| Pain threshold | 130 dB |

## Key Properties
- The theorem applies to *bandlimited* signals — real-world signals must be low-pass filtered before sampling to remove frequencies above f_max.
- **Aliasing**: When sampling below the Nyquist rate, high frequencies "fold" into lower frequencies, creating artifacts that cannot be removed after the fact.
- The 44.1 kHz CD rate was chosen because: (1) it's above 2×20 kHz = 40 kHz, providing a safety margin; (2) it was compatible with video equipment used for early digital audio mastering.
- Decibel scale is logarithmic because human perception of loudness is approximately logarithmic.

## Worked Example
Recording a pure 1000 Hz sine wave:
- Minimum sampling rate (Nyquist): 2 × 1000 = 2000 samples/second
- At 2000 samples/sec: exactly 2 samples per cycle — just enough to reconstruct
- At 8000 samples/sec (telephone): 8 samples per cycle — good reconstruction
- At 44100 samples/sec (CD): ~44 samples per cycle — excellent reconstruction

If we sample a 1000 Hz wave at only 1500 samples/sec (< Nyquist rate):
- The 1000 Hz component aliases to |1500 - 1000| = 500 Hz
- We hear a 500 Hz tone that doesn't exist in the original — aliasing artifact

## Common Pitfalls
- Confusing sampling rate with bit depth: sampling rate determines *temporal* resolution (which frequencies are captured); bit depth determines *amplitude* resolution (quantization precision). Both are needed for digital audio.
- Thinking the Nyquist rate is a practical target: in practice, you need a safety margin above 2×f_max and anti-aliasing filters with a transition band.
- Forgetting anti-aliasing filters: without them, frequencies above f_max still reach the sampler and cause aliasing.
- Confusing Hz (frequency) with kHz (sampling rate): 44.1 kHz sampling rate captures frequencies up to ~22 kHz, not 44.1 kHz.

## Connections
- [[pcm-digital-audio]] — PCM is the standard method of encoding sampled audio; Nyquist determines the sampling rate
- [[audio-quantization-pcm]] — quantization determines amplitude precision; sampling determines temporal precision
- [[video-frame-rate-resolution]] — video frame rate is an analogous temporal sampling concept for visual data
- [[video-formats-container-vs-codec]] — audio codecs (AAC, MP3, Vorbis) compress the sampled audio data
- [[multimedia-database-intro]] — audio is a continuous media type requiring real-time handling in MMDBMS
- [[multimedia-databases-lecture-03]] — color quantization in images is analogous to amplitude quantization in audio

## Open Questions
- Why was 44.1 kHz chosen for CDs instead of exactly 40 kHz (2×20 kHz)?
- How do perceptual audio codecs (MP3, AAC) exploit the limitations of human hearing beyond the Nyquist theorem?
- What are the implications of high-resolution audio (96 kHz, 192 kHz) — is there a perceptible difference?
