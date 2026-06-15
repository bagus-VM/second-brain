---
title: "MMDB Exercise 5 — Image Processing Part 2"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-15
---

## Exercises

### Task 1: Point Operations

HK point operation: `P_out = α · P_in + β`, with 8-bit grayscale (`P ∈ [0, 255]`).

1. How do `α` and `β` influence the result?
2. Which HK operation implements **image inversion**?
3. What problems occur with poorly chosen `α, β`? How do you deal with them?
4. Let `G` have minimum pixel value `a` and maximum `b`. Which HK operation maximizes the contrast ratio of `G`?

### Task 2: Linear Filter

1. What problem occurs at edge pixels during convolution? How do you fix it?
2. Compute the 5×5 kernel for a **moving-average smoothing filter** (each pixel = mean of itself and 8-neighbours = mean of 5×5 window).
3. Weighted smoothing using two 2D weight functions:
   - **Pyramid area:** `f(x, y) = -α · max(|x|, |y|) + k`
   - **Conical area:** `f(x, y) = -α · √(x² + y²) + k`
   - With `α = 2`, compute the 5×5 kernel for both, choosing `k` so the smallest coefficient = 0, then round to integers.
4. Why are **Laplacian filters** used? Give an example.

## Solutions

> [!note]- Solution
> **1a) Parameters α and β:**
> - `α` = **gain** / **contrast factor** — scales the spread between pixel values. `α > 1` increases contrast, `0 < α < 1` decreases it, `α < 0` inverts the intensity order.
> - `β` = **bias** / **brightness offset** — shifts the whole image up (brighter) or down (darker).
>
> **1b) Image inversion:**
> `P_out = -1 · P_in + 255`, i.e. `α = -1, β = 255`. Black becomes white, white becomes black, mid-gray stays mid-gray.
>
> **1c) Overflow / underflow with bad parameters:**
> If `α · P_in + β` falls outside `[0, 255]`, the raw result is undefined for an 8-bit image. Fix: **clamping** — saturate any value below 0 to 0, and any value above 255 to 255.
> ```
> clamp(x) = max(0, min(2^n - 1, x))
> ```
>
> **1d) Maximum contrast:**
> Map `a ↦ 0` and `b ↦ 255`:
> ```
> α·a + β = 0
> α·b + β = 255
> ```
> Subtract: `α(b − a) = 255` → **`α = 255 / (b − a)`**, **`β = −α·a = −255·a / (b − a)`**.
> This is the **min-max normalization / contrast stretch** used in every image viewer.

> [!note]- Solution
> **2.1) Edge problem and fixes:**
>
> **Problem:** the kernel extends beyond the image boundary at the edges, so the convolution has no defined neighbour values.
>
> **Fixes:**
> 1. **Redefine convolution at the boundary:**
>    - Set output to 0 if the kernel falls off the edge (zero-fill on output).
>    - Or: keep the original `I(x, y)` unchanged at the boundary (no-op at edges).
> 2. **Padding** the image first:
>    - **Zero padding** — fill missing cells with 0.
>    - **Symmetric (mirror) padding** — reflect values across the edge. Preserves mean intensity, generally preferred for natural images.

> [!note]- Solution
> **2.2) 5×5 moving-average kernel:**
> Every cell of the 5×5 window gets the same weight. Sum of weights must be 1 to preserve mean intensity, so each weight = `1/25`.
> ```
> (1/25) × [ [1 1 1 1 1]
>            [1 1 1 1 1]
>            [1 1 1 1 1]
>            [1 1 1 1 1]
>            [1 1 1 1 1] ]
> ```
> Often written equivalently as a kernel of all 1s, applied and the result divided by 25.

> [!note]- Solution
> **2.3) Weighted-smoothing kernels (`α = 2`):**
>
> **Pyramid:** `f(x, y) = -2 · max(|x|, |y|) + 4`
> (`k = 4` chosen so the corner value (−4) becomes 0; centre is 4.)
>
> Distance `max(|x|, |y|)` for offsets `(0,0) … (±2, ±2)`:
>
> | offset | max(|x|,|y|) | f |
> |--------|--------------|---|
> | (0,0)  | 0            | 4 |
> | (±1,0), (0,±1), (±1,±1) | 1 | 2 |
> | others with max=2 | 2 | 0 |
>
> Kernel:
> ```
> [0 0 0 0 0]
> [0 2 2 2 0]
> [0 2 4 2 0]
> [0 2 2 2 0]
> [0 0 0 0 0]
> ```
>
> **Conical:** `f(x, y) = -2·√(x² + y²) + 2√8`
> (`k = 2√8 ≈ 5.657` so the corner value `(-2·2√2 + 2√8) = 0`; centre is `2√8 ≈ 5.657`.)
>
> | offset | √(x²+y²) | f (exact) | rounded |
> |--------|----------|-----------|---------|
> | (0,0)  | 0        | 2√8 ≈ 5.657 | 6 |
> | (±1,0), (0,±1) | 1   | 2√8−2 ≈ 3.657 | 4 |
> | (±1,±1) | √2 ≈ 1.414 | 2√8−2√2 ≈ 2.343 | 2 |
> | (±2,0), (0,±2) | 2   | 2√8−4 ≈ 1.657 | 1 |
> | (±2,±1), (±1,±2) | √5 ≈ 2.236 | 2√8−2√5 ≈ 0.343 | 0/1 |
> | (±2,±2) | 2√2 ≈ 2.828 | 0 | 0 |
>
> Approximate kernel (rounding; per the official solution):
> ```
> [0 1 2 1 0]
> [1 3 4 3 1]
> [2 4 6 4 2]
> [1 3 4 3 1]
> [0 1 2 1 0]
> ```
> (Sum = 32.) Note this looks like a discretized Gaussian — that's not a coincidence: the conical function is a 2D isotropic smoothing kernel.

> [!note]- Solution
> **2.4) Laplacian filter — why:**
> A Laplacian is a **second-derivative filter** (∇² image). It highlights regions of rapid intensity change — i.e. **edges**. Unlike a gradient (1st derivative), which gives you an *edge direction*, the Laplacian gives you an *edge magnitude* in a single isotropic kernel. Used as a building block in edge detection (e.g. Laplacian of Gaussian = LoG / Marr–Hildreth), and in image sharpening: `sharpened = original + c · laplacian`.
>
> Discrete 4-neighbour kernel:
> ```
> [ 0  1  0]
> [ 1 -4  1]
> [ 0  1  0]
> ```
> Or 8-neighbour variant:
> ```
> [ 1  1  1]
> [ 1 -8  1]
> [ 1  1  1]
> ```

## Common Pitfalls

- Forgetting the **normalization** in Task 1.4 — `α = 255/(b-a)` is the answer, not just "stretch the histogram."
- Reporting 5×5 kernels without specifying that weights are normalized — the prof will ask "do they sum to 1?" and the answer needs to be yes.
- Calling the Laplacian "for blurring." It's for **edge detection / sharpening**, not smoothing.

## Related Lectures

- [[multimedia-databases-lecture-03]]
- [[multimedia-databases-lecture-04]]
- [[image-representation-bitmap]]
- [[linear-convolution-filters]]
- [[pixel-formats-and-bit-depth]]
