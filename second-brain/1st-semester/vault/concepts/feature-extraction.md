---
title: "Feature Extraction"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Feature extraction is the process of computing low-level numerical representations (colour, texture, shape, motion) from raw multimedia data to enable content-based comparison and retrieval.

## Core Intuition
Raw multimedia data (pixels, audio samples) is too high-dimensional and noisy for direct comparison. Feature extraction distills this raw data into compact, meaningful numerical vectors that capture essential properties. A colour histogram reduces millions of pixels to a few hundred bins; a texture descriptor reduces a patch to a handful of coefficients. This is the bridge between raw data and the lower levels of the [[mpeg-7-indexing-pyramid]].

## Formal Definition / Statement
Feature extraction transforms raw multimedia data into a set of numerical descriptors that characterize its properties. In the MPEG-7 context, this maps to:

**Visual features:**
- Colour: colour histogram, dominant colour, colour layout, colour structure
- Texture: homogeneity, directionality, coarseness, edge histogram
- Shape: contour-based (CSS), region-based (ART), 3D shape
- Motion: motion activity, camera motion, motion trajectory

**Audio features:**
- Spectral, temporal, and cepstral features

Feature extraction operates at pyramid levels 1–4 (syntactic) and feeds into higher-level analysis.

## Key Properties / Complexity
- Feature extraction is NOT standardized by MPEG-7 — the standard defines descriptor formats, not extraction algorithms
- Different extraction algorithms may produce different features for the same data
- Features are typically compact numerical vectors suitable for indexing
- Quality of features directly impacts retrieval performance
- Features can be global (whole image) or local (specific regions)

## Worked Example
Extracting a colour histogram from an image:
1. Convert image to HSV colour space
2. Quantize into N bins per channel
3. Count pixel occurrences per bin
4. Normalise to form a probability distribution
5. Result: a vector of N³ values representing the colour distribution

This can then be represented as an MPEG-7 ScalableColor descriptor.

## Common Pitfalls
- Confusing feature extraction with feature representation (descriptors) — extraction is the algorithm, representation is the format
- Assuming features capture semantics — they are purely syntactic
- Ignoring that feature quality depends on the domain (colour features work poorly for B&W images)
- Forgetting that MPEG-7 only standardizes the output format, not the extraction process

## Connections
- [[mpeg-7-descriptors]] — the standardized output formats for extracted features
- [[mpeg-7-indexing-pyramid]] — features populate levels 1–4
- [[semantic-gap]] — features are on the low-level side of the gap
- [[content-based-retrieval]] — features are the basis for content-based search
- [[multimedia-annotation]] — automatic annotation relies on feature extraction
- [[sensory-gap]] — feature extraction operates within the constraints of the sensory gap

## Open Questions
- How do hand-crafted features (MPEG-7) compare to learned features (CNNs)?
- Can feature extraction be made domain-agnostic?
- What is the optimal feature dimensionality for multimedia retrieval?
