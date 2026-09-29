---
title: "Color Histogram"
tags: [concept, multimedia-databases, semester-1, color-histogram, feature, cbr]
course: "Multimedia Databases"
source_count: 2
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]"]
---

## One-line Summary
A colour histogram is a feature vector that counts how many pixels of an image (or region) fall into each colour bin — a compact, translation-invariant representation of the colour distribution, widely used in [[content-based-retrieval|content-based retrieval]] as the simplest and most common low-level feature.

## Core Intuition
The colour histogram answers a simple question: "what colours are in this image, and how much of each?" For each colour in some discrete palette (e.g., 8 representative colours, or 256 red values × 256 green values × 256 blue values), count the number of pixels with that colour. Normalise by the total pixel count to get a probability distribution.

This loses all spatial information (you can't tell where the colours are) but is robust to translation, rotation, and small deformations. Two images with similar histograms have similar colour distributions — and may be visually similar.

## Formal Definition / Statement

For an image I with pixels p_1, p_2, ..., p_n, and a colour palette of k colours c_1, ..., c_k:

    H_I(j) = |{i : colour(p_i) = c_j}|  (the count of pixels with colour c_j)

Normalised (so it sums to 1):
    h_I(j) = H_I(j) / n

The histogram h_I ∈ ℝ^k is the colour-based feature vector of I.

**Colour space choices**:
- **RGB histogram**: 256 × 256 × 256 bins (16M bins) — too many, usually quantised
- **RGB with 4 bits per channel**: 16 × 16 × 16 = 4096 bins
- **HSV histogram**: 8 hue × 4 saturation × 4 value = 128 bins (more perceptually meaningful)
- **Lab histogram**: a × b bins, with L channel often used separately
- **Quantised to dominant colours**: e.g., 8 representative colours

**Distance functions** (for histogram comparison):
- L1, L2 ([[minkowski-distance]])
- Chi-squared ([[chi-squared-distance]])
- Kolmogorov-Smirnov ([[kolmogorov-smirnov-distance]])
- Earth Mover's Distance (EMD) — accounts for bin adjacency

## Key Properties / Complexity

### Why histograms are useful
- **Translation-invariant**: shifting the image doesn't change the histogram
- **Rotation-invariant**: rotating the image doesn't change the histogram (for many colour spaces)
- **Scale-invariant**: scaling the image doesn't change the normalised histogram
- **Compact**: 8-256 bins is much smaller than the image itself
- **Easy to compute**: O(n) per image
- **Easy to compare**: distance functions are well-studied

### Why histograms are limited
- **No spatial information**: "blue sky on top, green grass on bottom" looks the same as "blue and green mixed randomly"
- **No shape information**: a circle and a square with the same colours look the same
- **No texture information**: smooth and rough surfaces with the same colour look the same
- **Semantic gap**: two semantically different images (sunset vs fire) may have similar histograms
- **Sensitive to lighting changes**: a single RGB histogram is not robust to illumination

### Histogram types
- **Global histogram**: one histogram for the whole image
- **Spatial histogram**: histogram per region, or per block (e.g., 4×4 grid of histograms)
- **Fuzzy histogram**: each pixel contributes to multiple bins (with weights)
- **Cumulative histogram**: the CDF, used with Kolmogorov-Smirnov distance

### Range quantization vs bin quantization
Two separate quantization steps control the histogram size:
- **Range quantization** (colour space quantization): reduces the number of bins. A typical JPG has 256 values per RGB channel = 16.7M colours. Range quantization distributes these into n bins (e.g., 512 bins, each containing 32,768 colours). The histogram is a vector of bin values (pixel counts or percentages).
- **Bin quantization**: defines the bit-coding of values in each bin. For an image with 65,536 pixels, 16 bits are theoretically needed per bin. In practice, 15 bits may be precise enough, saving ~50% space (15 bits * 512 bins = 7,680 bits vs 16 * 512 = 8,192).
- **Adaptive (individual) binning**: adapts bin definitions to each image (e.g., several shades of blue for a sea image). Equalizes the distribution of bin values. Tends to provide more accurate content representation.
- **Regular (uniform) binning**: fixed, uniform bin definitions across all images.

### Query processing with histograms
- QBF on a single descriptor returns a sorted *feature sequence* (images with similarity > 0, ordered by degree of match).
- QBF on several descriptors requires fusion of the individual feature sequences.
- QBE is a QBF that uses the feature sequences extracted from the query image. See [[query-by-example-and-feature]].

### MPEG-7 colour descriptors
MPEG-7 standardises several colour features:
- **Dominant Colour Descriptor (DCD)**: a small set of (colour, percentage) pairs
- **Colour Structure Descriptor (CSD)**: captures both colour distribution and spatial structure
- **Colour Layout Descriptor (CLD)**: a compact representation of spatial colour distribution
- **Scalable Colour Descriptor (SCD)**: a Haar-transform-based histogram in HSV space

## Worked Example

For a 4×4 image with 8 blue pixels and 8 white pixels:
- Colour palette: {blue, white} (just for the example)
- Histogram: H(blue) = 8, H(white) = 8
- Normalised: h = (0.5, 0.5)

For a more complex 4×4 image with a 2×2 block of black in one corner and a 2×2 block of white in the other:
- Histogram: H(black) = 4, H(white) = 12
- Normalised: h = (0.25, 0.75)

The first image and the second image have different histograms (different colour distributions). But if you scramble the pixels of the second image (still 4 black and 12 white, just in different positions), the histogram is the same. The histogram does not capture spatial information.

For a more discriminative feature, you'd also include spatial information (e.g., a 2×2 grid of histograms).

## Common Pitfalls
- **Comparing histograms of different sizes**: normalise first, or use a distance function that handles scale (e.g., chi-squared).
- **Using the wrong colour space**: RGB histograms are sensitive to lighting; HSV or Lab are more robust.
- **Confusing histograms with colour lists**: a colour list is the set of colours present; a histogram is the count of each.
- **Ignoring bin adjacency**: bins that are next to each other in colour space are perceptually similar. EMD accounts for this; L1 and L2 don't.
- **No spatial information**: histograms alone miss where colours are. Combine with spatial features (e.g., spatial pyramid) for better discrimination.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[feature-vector]] — what histograms are
- [[dominant-color]] — a more compact alternative
- [[spatial-coherency]] — the property histograms ignore
- [[minkowski-distance]] — common distance function
- [[chi-squared-distance]] — scale-invariant distance
- [[mpeg-7]] — standardised colour descriptors
- [[query-by-example-and-feature]] — histograms produce the feature sequences that QBF and QBE operate on
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- How do colour histograms compare to modern deep-learning features (CNN embeddings)? (CNNs are more discriminative but less interpretable.)
- What's the best colour space for a given application? (Empirically: depends on the data and the task.)
- Can histograms be made robust to lighting changes? (Yes — use HSV value-invariant features, or apply histogram equalisation.)
- How do you choose the number of bins? (Too few loses information; too many is sparse. 32-256 bins is typical.)
