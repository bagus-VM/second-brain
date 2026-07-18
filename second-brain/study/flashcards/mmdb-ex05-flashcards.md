---
title: "MMDB Exercise 5 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What do α (gain) and β (bias) do in the HK point operation P_out = α·P_in + β?
> [!answer]- **α (gain):** Controls contrast — multiplies pixel values. **β (bias):** Controls brightness — shifts pixel values up or down. Together they perform linear transformations on pixel intensities.

> [!question]- How do you implement image inversion using the HK operation?
> [!answer]- P_out = -P_in + MaxValue. For 8-bit images: α = -1, β = 255. This maps 0→255 and 255→0.

> [!question]- What problem occurs with unadapted HK parameters and how do you fix it?
> [!answer]- Output pixel values can exceed the valid range [0, 255]. **Fix:** Clamping — restrict values to [0, 2^n - 1] where n is the bit depth.

> [!question]- How do you maximize contrast using HK for an image with pixel range [a, b]?
> [!answer]- Set HK(a)=0 and HK(b)=255. Solving: **α = 255/(b-a)**, **β = -a·255/(b-a)**. This linearly stretches the pixel range to the full [0, 255] interval.

> [!question]- What are the two approaches to handle edge pixels in convolution filtering?
> [!answer]- (1) **Redefine convolution at edges:** Output 0 or I(x,y) when kernel falls off boundary. (2) **Padding:** Zero padding (fill with 0s) or symmetric padding (mirror image at boundary).


---

## Related Resources

### 📖 Topic: Multimedia Databases — Lecture 04 (Media: Text, Video, Audio)
- Lecture topic: [[multimedia-databases-lecture-04]]

**Key concepts covered:**
- [[ascii-unicode-character-encoding]]
- [[xml-structured-text]]
- [[video-hierarchy-shots-scenes]]
- [[shot-segmentation]]
- [[video-summarization-key-frames]]
- [[video-formats-container-vs-codec]]
- [[video-frame-rate-resolution]]
- [[audio-sampling-nyquist-theorem]]
- [[pcm-digital-audio]]
- [[audio-quantization-pcm]]
- [[multimedia-database-intro]]
- [[multimedia-definition]]
- [[image-point-operations]]
- [[dithering]]
- [[jpeg-compression-pipeline]]
