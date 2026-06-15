---
title: "Dominant Colour"
tags: [concept, multimedia-databases, semester-1, dominant-color, mpeg-7, feature]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]", "[[color-histogram]]"]
---

## One-line Summary
Dominant colour is a compact representation of the most prominent colours in an image or region — a small set of (colour, percentage) pairs — that captures the dominant colour distribution with far less storage than a full histogram.

## Core Intuition
A full colour histogram has hundreds or thousands of bins. But most of those bins have negligible mass. A typical photograph has only 5-10 visually distinct "main" colours. **Dominant colour** captures only the most prominent colours: a small list of (colour, percentage) pairs.

This is more compact than a histogram and more interpretable (you can see the dominant colours at a glance). The trade-off: it loses fine-grained colour information. A photograph of a sunset and a photograph of a fire might have the same dominant colours (orange, red) but different distributions.

## Formal Definition / Statement

For an image (or region) I, the **dominant colour descriptor** is a set of tuples:
    DC(I) = { (c_1, p_1), (c_2, p_2), ..., (c_k, p_k) }
where:
- c_i is a colour (in some colour space, usually with a small quantisation)
- p_i is the percentage of pixels with colour "close to" c_i
- Σ p_i = 1 (the percentages sum to 100%)
- k is small (typically 1-8)

MPEG-7's Dominant Color Descriptor (DCD) standardises this with up to 8 dominant colours per descriptor.

**Computation** (one common method):
1. Quantise the image's colours to a small palette (e.g., 32 or 64 colours)
2. Count pixels per palette colour
3. Sort by count, descending
4. Take the top k
5. Optionally, merge similar colours (e.g., two shades of red)

## Key Properties

### Why dominant colour is useful
- **Compact**: 8 colours × (3 colour components + 1 percentage) = 32 numbers per descriptor
- **Interpretable**: humans can look at the descriptor and see the dominant colours
- **Fast to compute**: quantise + sort is O(n log k) per image
- **Robust to small changes**: small colour variations don't change the dominant colours

### Why dominant colour is limited
- **No spatial information**: where the colours are is lost
- **No fine-grained information**: two images with the same dominant colours but different distributions are indistinguishable
- **Bin selection is heuristic**: the choice of k (number of colours) and the quantisation affects the result
- **Semantic gap**: dominant colour doesn't capture what the image is "about"

### Dominant colour vs colour histogram
| | Dominant Colour | Colour Histogram |
|---|---|---|
| Size | Tiny (8 tuples) | Larger (256+ bins) |
| Information | Most prominent colours | Full distribution |
| Spatial | No | No (unless spatial histogram) |
| Comparison | Custom distance (DCD) | L1, L2, chi-squared, EMD |
| Use | Compact retrieval, summarisation | Detailed retrieval |

### MPEG-7's Dominant Color Descriptor
- **Up to 8 dominant colours** per descriptor
- Each colour in a quantised colour space (e.g., 5-bit per channel for RGB)
- Spatial coherency flag (whether the colour forms a coherent region)
- Variance (how much variation around the dominant colour)

## Worked Example

For a sunset image with mostly orange, red, and a small amount of dark blue:
- Dominant colours: (orange, 60%), (red, 30%), (dark blue, 8%), (other, 2%)
- DC = {(255, 128, 0, 0.6), (200, 30, 0, 0.3), (0, 0, 80, 0.08), (128, 128, 128, 0.02)}

For a fire image with similar colours but different distribution:
- DC = {(255, 100, 0, 0.5), (200, 50, 0, 0.4), (0, 0, 0, 0.1)}

The two descriptors are similar (both orange-red heavy) but distinguishable by the specific colours and percentages. A CBR system using dominant colour would likely return both images for a sunset query — but the user can refine with relevance feedback.

## Common Pitfalls
- **Choosing k too small**: misses important colours
- **Choosing k too large**: defeats the purpose of compactness
- **Ignoring spatial information**: two images with the same dominant colours but very different layouts are indistinguishable
- **Not normalising percentages**: when comparing, the percentages should sum to 1
- **Confusing with "average colour"**: dominant colour is a *set* of prominent colours, not the average. The average of a sunset and a forest is brown — useless.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[color-histogram]] — the more detailed alternative
- [[feature-vector]] — what DC is
- [[mpeg-7]] — the standardising body
- [[spatial-coherency]] — a flag in MPEG-7's DCD
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- How do you choose the optimal k for dominant colour extraction? (Empirically: 4-8 is typical; depends on the application.)
- Can dominant colour be combined with spatial information? (Yes — "dominant colours per region" or "spatial dominant colour pyramid".)
- How does dominant colour compare to modern deep-learning features? (CNNs are more discriminative; DC is more interpretable.)
- For video, can you use dominant colour as a keyframe summary? (Yes — common technique for video summarisation.)
