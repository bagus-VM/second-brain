---
title: "MMDB Exercise 6 — Image Compression"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-15
---

## Exercises

### Task 1: JPEG Baseline Process

1. What are the main goals of the **baseline process**?
2. For each step in the JPEG pipeline, summarize its function and mark whether it is lossy or lossless.

### Task 2: Pre-processing

1. Why convert RGB → YUV (Y′C_bC_r)?
2. What is **chroma subsampling**? Explain the ratios **4:4:4**, **4:2:2**, **4:2:0**.
3. Why must the image size be scaled before encoding? How does scaling interact with **MCUs (Minimum Coded Units)**?

### Task 3: Discrete Cosine Transform

1. What is the task of the **Forward DCT (F-DCT)** in JPEG compression?
2. In a DCT-transformed 8×8 block, which parts are most useful for compression?
3. Explain **DC** vs **AC** coefficients.

### Task 4: Quantization

1. Advantages and disadvantages of quantizing DCT coefficients? What property of DCT coefficients must you keep in mind when choosing the 64 quantization values?
2. How does the quantization matrix / factor influence perceived quality?

### Task 5: Entropy Coding

1. What is the purpose of entropy coding as the last step of JPEG? Lossy or lossless?
2. What is the main contribution of **RLE** to compression? How is a data block processed at this stage?
3. Why are DC and AC coefficients entropy-coded **differently**? Which procedure is recommended for each?

### Task 6: LZW Compression

Encode and decode the string `TATTARRATTAT` using the **Lempel–Ziv–Welch** algorithm.

### Task 7: Huffman Coding

Generate the **Huffman code** (incl. code tree) for the following 8 symbols:

| Symbol | A    | R    | Y    | O    | S    | T    | X    | U    |
|--------|------|------|------|------|------|------|------|------|
| Prob   | 30.1 | 17.5 | 21.5 | 14.9 | 9.3  | 2.2  | 2.3  | 2.2  |

(Probabilities are in %; sum = 100%.)

## Solutions

> [!note]- Solution
> **1.1) Goals of the baseline process:**
> - **Lossy compression** of still images.
> - **Reversibility** — a corresponding inverse decompression must reconstruct a (slightly degraded) image.
> - Low computational cost, suitable for both software and hardware pipelines.
> - Tunable compression ratio via the quantization factor.
>
> **1.2) Pipeline steps:**
>
> | Step | Function | Lossy? |
> |------|----------|--------|
> | Image scale + block formation | Pad to multiple of MCU size; divide into blocks | No (lossless) |
> | Color space conversion RGB → Y′C_bC_r | Separate luma from chroma | No (lossless) |
> | Subsampling (chroma) | Reduce chroma resolution — exploit human insensitivity to color detail | **Yes** |
> | F-DCT (8×8 blocks) | Spatial → frequency domain | No (lossless) |
> | Quantization | Discard perceptually insignificant high-frequency coefficients | **Yes** |
> | Entropy coding (RLE + Huffman) | Lossless compression of the quantized coefficient stream | No (lossless) |

> [!note]- Solution
> **2.1) Why RGB → YUV:**
> Human vision is far more sensitive to **luminance (brightness)** than to **chrominance (color)**. By splitting Y (luma) from C_b, C_r (chroma), we can **subsample** the chroma channels aggressively and lose almost no perceived quality, while cutting ⅓ to ½ of the data.
>
> **2.2) Chroma subsampling ratios X:a:b:**
> - **X** = luma reference sample width (usually 4).
> - **a** = number of C_b/C_r samples on the **first row** of that luma block.
> - **b** = number of C_b/C_r samples on the **second row**.
>
> | Ratio | Luma samples | Chroma samples (per 4 luma) | Visual effect |
> |-------|--------------|------------------------------|---------------|
> | **4:4:4** | 4 | 4 + 4 (full chroma) | No quality loss |
> | **4:2:2** | 4 | 2 + 2 (half horizontal) | Mild softening of color edges |
> | **4:2:0** | 4 | 2 + 0 (half each direction) | Quarter chroma; the default for digital video and DVDs |
>
> **2.3) Image scale and MCUs:**
> The F-DCT operates on **8×8** blocks. So both image width and height must be divisible by 8 (or by 16 when chroma is 4:2:0 subsampled, since one 16×16 luma region then corresponds to one **MCU** of 16×16 luma + 8×8 C_b + 8×8 C_r).
>
> If the image isn't an exact multiple, **pad to the right and bottom** by replicating the rightmost column / bottommost row's pixel values. The padded region is decoded but discarded on display.

> [!note]- Solution
> **3.1) F-DCT task:**
> Convert each 8×8 pixel block from the **spatial domain** (intensity values) into the **frequency domain** (sum of 64 cosine basis functions of increasing frequency). It is **invertible** (lossless) and concentrates image energy into a few low-frequency coefficients — the basis for the heavy quantization that follows.
>
> **3.2) Most useful parts for compression:**
> **Low-frequency coefficients** (top-left of the 8×8 block). Real images are mostly smooth, so most of the energy is in low frequencies; high-frequency coefficients (bottom-right) are typically near zero and can be heavily quantized.
>
> **3.3) DC vs AC:**
> - **DC coefficient** = `DCT(0,0)` — the average brightness of the 8×8 block. One per block.
> - **AC coefficients** = the other 63 values — describe how intensity **changes** across the block (the spatial variations).

> [!note]- Solution
> **4.1) Quantization of DCT coefficients:**
>
> Divide each transformed coefficient `F(u,v)` by the corresponding entry in the quantization matrix `Q(u,v)`, then round to integer.
>
> **Advantages:**
> - Massive bit savings — restrict each value's range from many bits to a few.
> - Aggressively throw away high-frequency detail the eye can't see.
>
> **Disadvantages:**
> - **Lossy** — quantization error is irreversible.
> - Edge artifacts, ringing, banding at low quality factors.
>
> **What to keep in mind:** the human eye is most sensitive to **low frequencies**. So `Q` should be **small (fine quantization) for low-frequency entries** and **large (coarse) for high-frequency entries**. That is why the standard luminance quantization matrix has small numbers in the top-left and large ones in the bottom-right.
>
> **4.2) Effect on perceived quality:**
> Larger quantization values → smaller file → more visible artifacts. The quality factor in JPEG encoders (e.g. libjpeg's `q` parameter 1–100) is just a global multiplier on `Q`. Quality 75–85 is the typical "visually lossless" sweet spot; below 50, block artifacts become obvious.

> [!note]- Solution
> **5.1) Entropy coding purpose:**
> Compress the stream of quantized DCT coefficients (which still have statistical redundancy) into a compact bitstream. **Lossless** — every bit of the quantized representation is preserved.
>
> **5.2) RLE on quantized blocks:**
> After quantization, the 8×8 block is read in **zig-zag order** (so the long runs of zeros that come from discarded high-frequency coefficients cluster at the end of the sequence). RLE then encodes each non-zero value as `(skip, value)` — the number of preceding zeros plus the value. This shrinks long zero runs dramatically.
>
> **5.3) DC vs AC coding:**
> - **AC coefficients:** many of them, most are zero → **RLE + Huffman** of the (run, value) symbols.
> - **DC coefficients:** one per block, neighbouring blocks' DC values are similar → **Differential Pulse Code Modulation (DPCM)**: encode the **difference** between current and previous block's DC, then Huffman-code the differences. The differences are small integers, so Huffman compresses them tightly.

> [!note]- Solution
> **6) LZW on `TATTARRATTAT`:**
>
> Dictionary seeded with single characters: `1:T, 2:A, 3:R`.
>
> | Input char | P (current prefix) | P+z | In dict? | Output | Add to dict | New P |
> |------------|--------------------|-----|----------|--------|-------------|-------|
> | T | "" | T | yes | — | — | T |
> | A | T | TA | no | 1 (T) | 4:TA | A |
> | T | A | AT | no | 2 (A) | 5:AT | T |
> | T | T | TT | no | 1 (T) | 6:TT | T |
> | A | T | TA | yes | — | — | TA |
> | R | TA | TAR | no | 4 (TA) | 7:TAR | R |
> | R | R | RR | no | 3 (R) | 8:RR | R |
> | A | R | RA | no | 3 (R) | 9:RA | A |
> | T | A | AT | yes | — | — | AT |
> | T | AT | ATT | no | 5 (AT) | 10:ATT | T |
> | A | T | TA | yes | — | — | TA |
> | T | TA | TAT | no | 4 (TA) | 11:TAT | T |
> | (end) | T | — | — | 1 (T) | — | — |
>
> **Encoded bitstream:** `1 2 1 4 3 3 5 4 1` (9 codes, vs. 12 raw characters — ~25% compression).
>
> **Decoding** is the inverse; the dictionary is rebuilt identically on the decoder side because the encoder publishes each new entry the moment it emits the code that triggered its creation.

> [!note]- Solution
> **7) Huffman tree and codes:**
>
> Build the tree bottom-up by repeatedly merging the two **lowest-probability** nodes.
>
> Final codes (canonical from the official solution):
> ```
> A → 11
> Y → 01
> R → 00
> O → 100
> S → 1011
> X → 10100
> T → 101010
> U → 101011
> ```
>
> **Verification (prefix-free):** every code is a leaf — no code is a prefix of another. ✓
>
> **Expected length:** `0.301·2 + 0.175·2 + 0.215·2 + 0.149·3 + 0.093·4 + 0.022·6 + 0.023·5 + 0.022·6 ≈ 2.55 bits/symbol`, very close to the entropy `H = -Σ p log₂ p ≈ 2.54 bits/symbol`. The Huffman code is essentially optimal here.

## Common Pitfalls

- Confusing "lossy" with "the whole pipeline." Only **subsampling** and **quantization** lose information. The other steps are perfectly reversible.
- Forgetting that the **DC** coefficient gets **DPCM**, not RLE. The prof loves to ask "why is DC special?"
- Writing a Huffman code where one symbol is a prefix of another — that's not a valid code.
- Reporting the LZW output as the literal characters instead of the **dictionary codes** (you output the code for the prefix `P`, not for `P+z`).

## Related Lectures

- [[multimedia-databases-lecture-05]]
- [[jpeg-compression-pipeline]]
- [[yuv-color-space]]
- [[entropy-coding-huffman-arithmetic]]
- [[run-length-encoding]]
- [[lz77-lzw-compression]]
- [[transform-coding]]
- [[lossless-vs-lossy-compression]]
