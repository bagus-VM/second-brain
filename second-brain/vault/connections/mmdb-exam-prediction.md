---
title: "MMDB Exam Prediction Map — Uebung Pattern Analysis"
tags:
  - connections
  - exam-prep
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-15
prerequisites: []
---

## One-line Summary
A pattern scan of all 7 Uebungsblaetter for SS 2026 MMDB, identifying the recurring exercise archetypes and predicting which are likeliest to reappear in the 2026-07-21 Klausur.

## Source Note (Important)
> **Student intel (2026-06-15):** professor reportedly recycles Uebung material as exam questions. This is a common German-university Klausurarchitektur. Treat every Uebungsblatt as the de-facto syllabus, not optional practice.
> ^[memory note: 2026-06-15 student report]

## Method
1. Extracted text from all 7 exercise sheets (`raw/lectures/multimedia_databases/Uebung/exercise_sheets/Ex01..07.pdf`).
2. Cross-referenced with official solution PDFs (`Ex0X_solutions.pdf`, present for sheets 1–6; sheet 7 has no published solution set yet — solutions derived from lecture material).
3. Classified each Task into one of 11 recurring **archetypes** (see "Exercise Archetypes" below).
4. Counted occurrences and weighted by **topic centrality** (does it touch a concept that has its own lecture slide?).
5. Noted **computed-by-hand** vs. **conceptual** vs. **trace-the-pipeline** styles — these are the three "modes" the prof flips between.

## Exercise Archetypes (11 patterns across 7 sheets)

| # | Archetype | Mechanics | Sheets | Risk in exam |
|---|-----------|-----------|--------|--------------|
| A | **Numeric computation** ("given X, compute Y") | Plug into a formula; show steps. | Ex01, Ex04, Ex05, Ex07 | High — they grade on the arithmetic, easy to slip a unit. |
| B | **Color model conversion** | Convert RGB ↔ CMYK, RGB ↔ HSV. Sometimes RGB → YUV. | Ex03, Ex06 | High — reappears with new RGB triples. |
| C | **Format property table** | Tabulate GIF/PNG/JPEG or PCM/MP3/FLAC on 4–5 axes. | Ex04 | Medium — depends on whether L3 image formats is in scope. |
| D | **Pipeline step explanation** | Name the steps of a pipeline (JPEG, Nyquist sampling, CBR) and label lossless vs. lossy. | Ex01, Ex06 | **Very high** — favourite exam format, easy to grade. |
| E | **Memory-layout calculation** | Compute bytes used by Java int[][][] or packed int[][] for a given image size. | Ex04 | High — gets re-used with new sizes. |
| F | **Algorithm-by-bullets** | "Write the steps of X algorithm (uniform quantization, median cut, Huffman). Not code." | Ex04, Ex06 | High — tests whether you can reconstruct, not just recognize. |
| G | **Algorithm trace** | "Run Huffman / LZW on this specific string." Show the table. | Ex06 | **Very high** — given a new string, you must do the work. |
| H | **Distance-metric computation** | Compute `L₁`, `L₂`, `L∞`, K-S, χ² between two histograms. | Ex07 | High — same shape, new histograms. |
| I | **Concept comparison** | "Compare X and Y along dimensions a, b, c." | Ex02, Ex07 | Medium — open-ended, grading depends on rubric. |
| J | **"Explain the phenomenon"** | "Why does X happen?" Often a perceptual or physics question. | Ex01, Ex03, Ex05 | Medium — tests understanding, not recall. |
| K | **Indexing / data-structure reasoning** | "Why can't you use a B-tree here?" or "What breaks in high-D?" | Ex07 | Medium — open-ended but bounded. |

## Frequency Heatmap

| Archetype | Ex01 | Ex02 | Ex03 | Ex04 | Ex05 | Ex06 | Ex07 | Count |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:-----:|
| A Numeric | ✓ |   |   | ✓ | ✓ |   | ✓ | 4 |
| B Color conv |   |   | ✓ |   |   | ✓ |   | 2 |
| C Format table |   |   |   | ✓ |   |   |   | 1 |
| D Pipeline explain | ✓ |   |   |   |   | ✓ |   | 2 |
| E Memory layout |   |   |   | ✓ |   |   |   | 1 |
| F Algorithm steps |   |   |   | ✓ |   | ✓ |   | 2 |
| G Algorithm trace |   |   |   |   |   | ✓ |   | 1 |
| H Distance compute |   |   |   |   |   |   | ✓ | 1 |
| I Comparison |   | ✓ |   |   |   |   | ✓ | 2 |
| J Phenomenon | ✓ |   | ✓ |   | ✓ |   |   | 3 |
| K Indexing reason |   |   |   |   |   |   | ✓ | 1 |

## Most-Likely Exam Questions (Top 10, ranked)

Ordered by (frequency in Uebung) × (concept centrality) × (ease of parameterization for the prof).

1. **JPEG / compression pipeline walk-through with lossless-vs-lossy labels** (Archetype D). Re-uses the Ex06 frame. Expect ~3 sub-questions: "what is the goal?", "which step is the bottleneck?", "where does the loss happen?" The prof can swap in any other pipeline (Nyquist sampling, MPEG encoding).
2. **Hand-trace LZW or Huffman on a new string / symbol set** (Archetype G). The LZW string in Ex06 was `TATTARRATTAT` — extremely memorable. A fresh string in the exam is the single highest-probability "do-the-work" question.
3. **Compute a distance metric (`L₁`, `L₂`, `L∞`, K-S, χ²) on two new histograms** (Archetype H). Ex07 is the only sheet with this archetype — concentration of novelty, perfect exam-question shape.
4. **RGB → CMYK and/or RGB → HSV conversion with new values** (Archetype B). Trivial to parameterize.
5. **Memory-layout calculation in Java** (Archetype E). Prof changes the image size from 12×12 to something else.
6. **Tabulate image format properties** (Archetype C). "Compare GIF, PNG, JPEG on these 4 dimensions" is a 5-minute question for the student and a 30-second question to grade.
7. **"Why does phenomenon X happen?"** (Archetype J). Aliasing (Ex01), chromatic adaptation (Ex03), edge artifacts in convolution (Ex05) — pick whichever the prof wants to test perception-vs-physics intuition.
8. **Algorithm-by-bullets** (Archetype F). "Write the steps of median cut quantization" or "describe Huffman in 5 lines."
9. **Quantization error / Nyquist rate / sampling theorem calculation** (Archetype A, L01–L04 material). PCM error formula or minimum sampling rate for a sum of sines.
10. **Concept comparison** (Archetype I). "Compare QbE vs. QbS" or "Compare structured vs. unstructured retrieval" — open-ended, tests depth.

## "Don't Get Faked Out" — Style Signals

- **"Show the steps"** is the prof's way of saying "I will grade intermediate work, not just the answer." Skip the algebra and you lose half the points.
- **"In your own words"** (Ex07 Task 2 wording) is the Socratic tell — they're testing whether you actually *understand* the term, not whether you can parrot the slide.
- **"Briefly"** or **"shortly"** is a token budget: 2–4 sentences. Not "one word," not "an essay."
- **Tabular "outline the main properties of X, Y, Z"** questions want a *table*, not a paragraph. Format matters.
- When the prof says **"which is lossy"** in a pipeline question, every step needs a yes/no label. Forgetting one loses the point.

## Open Questions

- The Ex07 official solution PDF is missing from `raw/.../solutions/`. The vault's Ex07 practice file is built from the lecture slides + standard textbook treatments. Verify against a tutor's notes or a classmate's submission before relying on the Ex07 numerical answers.
- Ex07's 4×4 image figures weren't in the extracted text — Task 4's histogram and Task 5's distance results assume the left image is a checkerboard of 8 blue + 8 white and the right is two solid blocks (one black, one white). If the actual figures differ, the histograms and the resulting `L₁/L₂/L∞` answers change.

## Connections

- [[mmdb-ex01]] — Ex01: signal processing, data categories, Rainbow Books.
- [[mmdb-ex02]] — Ex02: semantic gap, MMDB components.
- [[mmdb-ex03]] — Ex03: color perception, models, CIE spaces.
- [[mmdb-ex04]] — Ex04: image formats, Java memory layout, quantization.
- [[mmdb-ex05]] — Ex05: point operations, convolution filters.
- [[mmdb-ex06]] — Ex06: JPEG pipeline, LZW, Huffman.
- [[mmdb-ex07]] — Ex07: CBIR concepts, histograms, distance metrics.
- [[jpeg-compression-pipeline]] — Top-1 predicted exam target.
- [[entropy-coding-huffman-arithmetic]] — Top-2 predicted exam target.
- [[minkowski-distance]] — Top-3 predicted exam target.
- [[multimedia-databases-lecture-01]] — L01 scope.
- [[multimedia-databases-lecture-02]] — L02 scope.
- [[multimedia-databases-lecture-03]] — L03 scope.
- [[multimedia-databases-lecture-04]] — L04 scope.
- [[multimedia-databases-lecture-05]] — L05 scope.
- [[multimedia-databases-lecture-06]] — L06 scope.
