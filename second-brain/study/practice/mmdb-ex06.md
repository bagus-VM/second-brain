---
title: "MMDB Exercise 6 — Image Compression"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: JPEG Baseline Process

The workflow shows the lossy sequential DCT-based JPEG compression algorithm (Baseline Process).

1. What are the main goals of the baseline process?
2. Shortly summarize the function of each step, and outline which ones are lossy.

### Task 2: Pre-processing

1. What are the advantages of converting the color space from RGB to YUV (or YCbCr)?
2. What does subsampling of chrominance elements mean? (Consider the ratios 4:4:4, 4:2:2 and 4:2:0).
3. Why should the size of the image be scaled first before encoding? And how does scaling work with respect to image blocks and minimum coded units (MCUs)?

### Task 3: Discrete Cosine Transformation

1. What is the task of the Forward Discrete Cosine Transform (F-DCT) during JPEG compression?
2. In a DCT-transformed block, which parts are most useful for compression?
3. Explain the notions DC coefficient and AC coefficient.

### Task 4: Quantization

1. What are the general advantages and disadvantages of quantizing DCT coefficients? Which characteristics of DCT coefficients have to be kept in mind when selecting the 64 quantization values?
2. How can the values of the quantization matrix (and quantization factor) influence the perceived quality?

### Task 5: Entropy Coding

1. Describe the purpose of entropy coding as a last step of JPEG compression. Is it lossy or lossless?
2. What is the main contribution of Run Length Encoding (RLE) to data compression? How is a data block processed at this stage?
3. Why are DC and AC coefficients entropy coded differently? Which procedure is generally recommended for encoding DC coefficients, and which one for AC coefficients?

### Task 6: LZW Compression

Use the Lempel-Ziv-Welch Algorithm to encode and decode the following string: TATTARRATTAT

### Task 7: Huffman Coding

Generate the Huffman code (including code tree) for the following symbols:

| Symbol | A | R | Y | O | S | T | X | U |
|--------|------|------|------|------|-----|-----|-----|-----|
| Prob. | 30.1% | 17.5% | 21.5% | 14.9% | 9.3% | 2.2% | 2.3% | 2.2% |

## Related Lectures

- [[multimedia-databases-lecture-07]]
- [[multimedia-databases-lecture-08]]
