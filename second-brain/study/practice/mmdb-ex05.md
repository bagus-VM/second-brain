---
title: "MMDB Exercise 5 — Image Processing Part 2"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: Point Operations

The HK point operation is defined as: P_output = α·P_input + β (8-bit grayscale image).

1. How do the parameters α and β influence the result of the operation?
2. Explain which HK operation could be applied to implement the image inversion function.
3. Which problems could appear if HK is used with unadapted α and β parameters? Propose a method to deal with these effects.
4. Let G be a grayscale image with minimum pixel value a and maximum pixel value b. Which HK operation could be applied to G in order to maximize its contrast ratio?

### Task 2: Linear Filters

1. Which problems can occur to edge pixels when using convolution filters? Propose possible approaches to deal with these problems.
2. Calculate a 5×5 kernel for the 'moving average' variant of the smoothing filter.
3. Calculate 5×5 kernels for weighted smoothing using the pyramid-area function f(x,y) = -α·max(|x|,|y|) + k and the conical area function f(x,y) = -α·√(x²+y²) + k, with α=2.
4. Why are Laplacian filters used? Give an example.

## Solutions

### Task 1: Point Operations

> [!note]- Solution
> **1.1) Parameters α and β:**
> - α (gain): contrast factor — controls how much contrast is adjusted
> - β (bias): brightness factor — shifts pixel values up or down
>
> **1.2) Image inversion:**
> P_out = -P_in + MaxValue (i.e. α=-1, β=255 for 8-bit images)
>
> **1.3) Problems with unadapted parameters:**
> - No limits on output pixel values — can exceed valid range [0, 255]
> - **Solution: Clamping** — given sample value x defined on n bits (x ∈ [min, max=2^n-1]), clamp values to [0, 255]
>
> **1.4) Maximum contrast:**
> - Maximum contrast achieved when HK(a)=0 and HK(b)=255
> - α·a + β = 0 → β = -a·α
> - α·b + β = 255 → α = 255/(b-a)
> - **α = 255/(b-a), β = -a·255/(b-a)**

### Task 2: Linear Filters

> [!note]- Solution
> **2.1) Edge pixel problems:**
> - The kernel extends beyond source image boundaries near edges
> - **Solutions:** (1) Redefine convolution at edge boundary (output 0 or I(x,y) when kernel falls off), (2) Padding — zero padding or symmetric padding
>
> **2.2) Moving average 5×5 kernel:**
> ```
> [1  1  1  1  1]     [1/25  1/25  1/25  1/25  1/25]
> [1  1  1  1  1]     [1/25  1/25  1/25  1/25  1/25]
> [1  1  1  1  1] × 1/25  =  [1/25  1/25  1/25  1/25  1/25]
> [1  1  1  1  1]     [1/25  1/25  1/25  1/25  1/25]
> [1  1  1  1  1]     [1/25  1/25  1/25  1/25  1/25]
> ```
>
> **2.3) Weighted smoothing kernels (α=2):**
>
> *Pyramid-area* f(x,y) = -2·max(|x|,|y|) + k, with k=4:
> ```
> [0  0  0  0  0]
> [0  2  2  2  0]
> [0  2  4  2  0]
> [0  2  2  2  0]
> [0  0  0  0  0]
> ```
>
> *Conical area* f(x,y) = -2·√(x²+y²) + k, with k=2√8 (rounded):
> ```
> [0  1  2  1  0]
> [1  3  4  3  1]
> [2  4  6  4  2]
> [1  3  4  3  1]
> [0  1  2  1  0]
> ```
>
> **2.4) Laplacian filters:** Derivative filters used to find areas of rapid change (edges) in images. The Laplacian L(x,y) approximates the second derivative. Example kernel:
> ```
> [0   1  0]
> [1  -4  1]
> [0   1  0]
> ```

## Related Lectures

- [[multimedia-databases-lecture-05]]
- [[multimedia-databases-lecture-06]]
