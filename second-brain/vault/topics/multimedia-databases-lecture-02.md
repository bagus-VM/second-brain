---
title: "Lecture 02: Color Models"
tags: [topic-overview, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 2 covers how humans perceive color and the mathematical models (RGB, CMYK, HSV, CIE, L*a*b*, YUV) used to represent and convert between color spaces in multimedia systems.

## Overview
This lecture progresses from the physics of light and biology of human color perception to the practical color models used in multimedia databases. Understanding color representation is fundamental because multimedia data (images, video) must be stored, queried, and rendered consistently across devices.

## Key Concepts

### Perception
- [[color-perception]] — How light, the visible spectrum, and retinal cones create the experience of color

### Color Model Fundamentals
- [[color-models-overview]] — Additive vs. subtractive systems, primary and complementary colors
- [[color-gamut]] — The range of colors a device can reproduce

### Device-Dependent Models
- [[rgb-color-model]] — Additive model for screens; the RGB color cube
- [[cmyk-color-model]] — Subtractive model for printing; four-color process
- [[hsv-color-model]] — Perceptual model with Hue, Saturation, Value

### Perceptually-Oriented Models
- [[cie-chromaticity-diagram]] — The CIE horseshoe and device-independent color specification
- [[lab-color-space]] — CIE L*a*b*: perceptually uniform, device-independent
- [[yuv-color-space]] — Luminance/chrominance separation for video compression

### Specialized
- [[hmmd-color-space]] — Hue-Max-Min-Diff, closer to perceptual uniformity

## Connections
- Builds on basic signal processing concepts (frequency, amplitude)
- Directly enables understanding of [[multimedia-databases-lecture-03]] (image/video compression relies on YUV)
- Color models underpin content-based image retrieval in multimedia databases

## Exam Relevance
- Know the difference between additive and subtractive color mixing
- Be able to explain RGB ↔ HSV conversion steps
- Understand why CIE L*a*b* and YUV exist (perceptual uniformity, compression)
- Color gamut diagrams: what device covers what range
