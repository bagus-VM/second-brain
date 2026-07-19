---
title: "MMDB Exercise 1 — Multimedia and Multimedia Databases: Initial Concepts"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: Signal Processing

1. In the context of the Pulse Code Modulation process, explain the sampling and quantization steps.
2. The basic formulation of a sine wave is given by f(x) = A · sin(2πfx + φ). Given A = 10V, what is the maximum quantization error if a uniform quantization to 5 bits is applied to this wave?
3. State the Nyquist–Shannon sampling theorem. Based on this theorem, for the composite signal given in equation (1), calculate the minimum sampling rate so that the underlying information is not lost.
   - f(x) = sin(0.8πx) + sin(1.5πx) + sin(3πx)
4. What is meant by the term aliasing?

### Task 2: Structured and Unstructured Data

1. What are the characteristics of structured, unstructured and semi-structured data? Give examples for each.
2. What are the effects of such data on databases and their query properties?

### Task 3: Application History — Compact Discs

1. Research the functional definitions and additions of each of the Rainbow Books.
2. Apply the multimedia definitions and concepts from the lecture to your findings.

## Solutions

### Task 1: Signal Processing

> [!note]- Solution
> **1a) Sampling and Quantization in PCM:**
> - **Sampling:** A fixed grid of measuring points of equal distance Δt is defined on the axis over which the analog signal changes. The current value(s) of the signal at these grid points is called a sample. The density of measured values is called the sampling rate. The fixed grid can be points in time (e.g. audio) or spatial dimensions (e.g. pixels). The sampling rate specifies how accurately the original signal can be reconstructed.
> - **Quantization:** The conversion of measured values obtained during discretization to a discrete, countable value range (usually binary). Resolution = bits per sample. Accuracy depends on the number of bits per measured value.
>
> **1b) Maximum Quantization Error:**
> - Range Δx = 10 - (-10) = 20V
> - Q = Δx / (2^N · 2) = 20 / (32 · 2) = 20 / 64 = **0.3125 V**
>
> **1c) Nyquist-Shannon Sampling Theorem:**
> If a signal with highest frequency f_g is sampled at rate f_s > 2·f_g, it can be reconstructed without losing information.
> - f1 = 0.4 Hz, f2 = 0.75 Hz, f3 = 1.5 Hz
> - f_s > 2 · 1.5 = **f_s > 3 Hz**
>
> **1d) Aliasing:**
> Aliasing arises when a signal is discretely sampled at a rate insufficient to capture the changes in the signal (i.e. below the Nyquist rate). It produces artifacts that were not present in the original signal.

### Task 2: Structured and Unstructured Data

> [!note]- Solution
> **2a) Characteristics:**
> - **Structured:** Predefined schema, quantitative data, fits in fixed fields/columns (e.g. names, addresses). Can be stored in relational DBs with standard SQL querying and exact matching.
> - **Unstructured:** No predefined model, e.g. text, video, audio. Requires metadata for retrieval — if metadata is structured → exact matching; if not → information retrieval methods (fuzzy/similarity-based).
> - **Semi-structured:** Does not obey formal relational structure but contains tags/markers to separate semantic elements (e.g. XML, JSON). Typically queried via XPath or keyword queries.
>
> **2b) Effects on databases:**
> - Structured data: relational DB, standard SQL, exact matching
> - Unstructured data: needs metadata, content-based retrieval, similarity comparison
> - Semi-structured data: structured queries (XPath) or keyword queries

### Task 3: Compact Discs (Rainbow Books)

> [!note]- Solution
> | Book | Media | Additions |
> |------|-------|-----------|
> | CD-DA | Continuous Audio | 24-bit, 79 min audio |
> | CD-ROM | File Storage + Error Correction | Non-continuous files |
> | CD-i | Interactive Elements | Embedding of different types |
> | CD-M/R/RW | Dynamic File Storage | Multi-session |
> | Video-CD | Mix of continuous + interactive | High-fidelity video formats |
> | E-CD | Continuous Audio + File Storage | Compatibility with multi-session |
> | SuperAudioCD | Continuous Audio + copy protection | Policy enforcements |
> | DDCD | File Storage | New storage structure |


---

## Related Resources

### 📖 Multimedia Databases — Lecture 01 Overview
- Lecture topic: [[multimedia-databases-lecture-01]]

**Key concepts covered:**
- [[multimedia-definition]]
- [[media-types-discrete-continuous]]
- [[data-streams]]
- [[multimedia-system]]
- [[multimedia-main-domains]]
- [[multimedia-database-intro]]
- [[structured-vs-unstructured-retrieval]]
- [[multimedia-query-predicates]]
