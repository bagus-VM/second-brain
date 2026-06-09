---
title: "MMDB Exercise 1 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What are the two main steps of Pulse Code Modulation (PCM)?
> [!answer]- **Sampling:** A fixed grid of measuring points of equal distance Δt is defined on the analog signal. The values at these points are samples. The sampling rate determines reconstruction accuracy. **Quantization:** Conversion of measured values to a discrete, countable value range (usually binary). Resolution = bits per sample. Accuracy depends on bit depth.

> [!question]- What is the maximum quantization error for a signal with amplitude A=10V and 5-bit uniform quantization?
> [!answer]- Range Δx = 10 - (-10) = 20V. Error Q = Δx / (2^N · 2) = 20 / 64 = **0.3125 V**

> [!question]- State the Nyquist-Shannon Sampling Theorem.
> [!answer]- If a function with highest frequency f_g is sampled at rate f_s > 2·f_g, it can be reconstructed from the sampled values without losing the underlying information.

> [!question]- What is aliasing?
> [!answer]- Aliasing arises when a signal is sampled at a rate insufficient to capture its changes (below the Nyquist rate). It produces artifacts not present in the original signal.

> [!question]- What is the difference between structured, unstructured, and semi-structured data?
> [!answer]- **Structured:** Predefined schema, fits in fixed fields/columns (e.g. names, addresses), SQL querying. **Unstructured:** No predefined model (text, video, audio), needs metadata or IR methods. **Semi-structured:** Contains tags/markers (XML, JSON) but no rigid schema, queried via XPath or keywords.
