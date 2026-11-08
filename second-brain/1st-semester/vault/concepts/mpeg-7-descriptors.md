---
title: "MPEG-7 Visual Descriptors"
tags: [concept, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
MPEG-7 defines standardized low-level visual descriptors for colour (7), texture (3), shape (3), motion (4), localization (2), and face recognition (1) — totaling 20 descriptor types.

## Core Intuition
To search and compare multimedia content, you need to reduce complex visual information to compact, comparable numerical representations. MPEG-7 descriptors are exactly that: standardized mathematical representations of visual properties that enable content-based comparison without requiring semantic understanding.

## Formal Definition / Statement
MPEG-7 Visual Descriptors (ISO/IEC 15938-3) cover:

**Colour (7 descriptors):**
- Colour Space & Colour Quantization
- Scalable Colour (HSV colour space + Haar transformation)
- Dominant Colour
- Colour Layout
- Colour Structure
- Group-of-Frames/Group-of-Pictures (GoF/GoP) Colour

**Texture (3 descriptors):**
- Homogeneous Texture (directionality, coarseness, regularity of patterns)
- Texture Browsing
- Edge Histogram (non-homogeneous)

**Shape (3 descriptors):**
- Contour-based: Curvature Scale-Space (CSS)
- Region-based: Angular Radial Transformation (ART)
- 3D Shape

**Motion (4 descriptors):**
- Motion Activity (intensity, direction, spatial distribution)
- Camera Motion
- Motion Trajectory
- Parametric Motion

**Localization (2 descriptors):**
- Region Locator
- Spatial-Temporal Locator

**Face Recognition (1 descriptor):**
- Face Recognition

## Key Properties / Complexity
- Descriptors are compact numerical representations (not raw pixels)
- Scalable Colour uses Haar transform for multi-resolution representation
- Dominant Colour reduces an image to its few most prominent colours
- Edge Histogram captures spatial distribution of edges (5 types: vertical, horizontal, 45°, 130°, non-directional)
- GoF/GoP Colour extends single-frame colour descriptors to video sequences
- All descriptors are part of the [[mpeg-7]] standard

## Worked Example
Scalable Colour Descriptor for an image:
```xml
<VisualDescriptor xsi:type="ScalableColorType" numOfCoeff="16"
  numOfBitplanesDiscarded="0">
  <Coeff>1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6</Coeff>
</VisualDescriptor>
```
This encodes the colour distribution of an image using 16 Haar coefficients in HSV colour space. The descriptor is "scalable" — you can discard bitplanes to reduce precision/bandwidth.

## Common Pitfalls
- Confusing descriptors with features — descriptors are standardized representations, features are the underlying properties
- Assuming descriptors capture semantics — they are purely low-level/syntactic
- Forgetting that descriptor extraction is not part of the standard — MPEG-7 defines the format, not the algorithm to compute it
- Overlooking that descriptors need distance/similarity measures for comparison

## Connections
- [[mpeg-7]] — these descriptors are defined within the MPEG-7 standard
- [[mpeg-7-indexing-pyramid]] — descriptors map to pyramid levels 1–4 (syntactic)
- [[feature-extraction]] — the process of computing these descriptors from raw data
- [[similarity-measures]] — needed to compare descriptor values
- [[content-based-retrieval]] — descriptors are the foundation for content-based search

## Open Questions
- How do MPEG-7 descriptors compare to CNN feature vectors in retrieval performance?
- Are MPEG-7 descriptors still used in modern multimedia systems, or have they been superseded by learned representations?
