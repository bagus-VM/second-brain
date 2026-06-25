---
title: "Query By Example and Query By Features"
tags: [concept, multimedia-databases, semester-1, query-process, qbe-qbf]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-25
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]", "[[color-histogram]]"]
---

## One-line Summary
Two ways to drive a CBIR search: hand the system a sample picture and ask for similar ones (Query By Example), or type in feature values and ask for matches (Query By Features).

## Core Intuition
A user looking at a butterfly identification system rarely has a perfect photo and rarely speaks the language of feature vectors. The lecture's butterfly use case captures the tension well: non specialists cannot describe a butterfly in expert terms, they may not remember its exact appearance, and they will not page through hundreds of results.

The system answers this with a two mode, user controlled loop. In **Query By Features (QBF)** the user supplies values for descriptors such as dominant color, texture pattern, or shape. This is a loose, exploratory way to start. In **Query By Example (QBE)** the user hands over a concrete image and asks for similar ones. This is the precise, narrowing step.

The two modes feed each other. Every result page reports both the matching images and the features those images produced. A user can grab a result image and run another QBE, or grab a reported feature value and run another QBF. This keeps the search interactive and lets a user who starts fuzzy gradually tighten the query.

## Formal Definition / Statement

**Query By Features (QBF)**: the user submits values for a set of content descriptors. The system returns all database items whose descriptors match those values, ranked by degree of similarity.

**Query By Example (QBE)**: the user submits a sample image. The system extracts that image's feature sequences and runs a QBF against them. QBE is therefore QBF executed on the feature sequences of the query image.

**Characteristics** (from the lecture):
- QBF tends to be inaccurate. It applies to the initial query and whenever the user wants to *expand* the search space.
- QBE is accurate and supports detailed search. It applies to the final query and whenever the user wants to *restrict* the search space.

**Result page composition**: each result page has two parts.
1. **Result images**: database images that satisfy the query conditions. Users may compose further QBEs from these images.
2. **Similar features**: the features of the retrieved images. Users may compose further QBFs from these features.

**Query processing** (descriptor level):
- QBF on a **single descriptor**: returns the images with a degree of similarity greater than 0, sorted by similarity. This ordered list is a *feature sequence*.
- QBF on **several descriptors**: requires fusion of the individual feature sequences.
- QBE: a QBF that uses the feature sequences extracted from the query image.

## Key Properties / Complexity

### When to use which mode
- QBF for the **opening** move and for broadening the result set. Cheap to start, no sample image needed, but imprecise because users guess feature values.
- QBE for the **closing** move and for narrowing the result set. Precise because it compares real extracted features, but it requires a sample image to exist.

### The feedback loop
- Result images seed the next QBE. This is how a user tightens the search without knowing feature values.
- Similar features seed the next QBF. This is how a user learns which feature values correspond to what they want.
- The loop turns an inaccurate first query into an increasingly precise one without forcing the user to understand the underlying descriptors.

### Fusion cost
- Single descriptor: one sorted feature sequence, O(N log N) to rank N items, or O(N) with an index for top k.
- Several descriptors: each descriptor produces its own sequence. Fusion must combine them, which adds a weighting or merging step on top of the per descriptor search. The choice of fusion rule (weighted sum, rank fusion, voting) directly affects ranking quality.

## Worked Example

Butterfly identification, after the lecture's scenario.

1. **Opening QBF (expand)**: the user remembers an orange-yellow butterfly with many spots. They submit feature values: color = orange_yellow, texture = many_spots. The system returns every butterfly matching those features, ranked by similarity. The result is loose. Orange butterflies of several species appear.
2. **Read the result page**: the page lists matching butterfly images and, alongside them, the extracted features (color shares, texture match degrees, shape values).
3. **QBE to restrict**: the user spots the right species in the result images and clicks it as the example. The system extracts that image's feature sequences and runs a QBF on them. Now the ranking is tight and detailed because the comparison uses real, fully populated descriptors rather than the user's rough guesses.
4. **Iterate**: if the QBE still returns a few wrong species, the user picks a better result image and runs another QBE. Each pass restricts the search space further.

The key idea: QBF opens the search wide, QBE closes it down. The result page is built so either mode can pick up where the other left off.

## Common Pitfalls
- **Treating QBF as a precision tool**: QBF is intentionally loose. Expecting exact matches from guessed feature values leads to disappointment. Use QBF to explore, QBE to pin down.
- **Stopping after one QBE**: the first example image is rarely optimal. The result page exists to give you a better example for the next round.
- **Ignoring the "similar features" half of the result page**: those values are the bridge back to QBF. Skipping them breaks the feedback loop.
- **Forgetting that QBE is QBF underneath**: QBE is not a separate algorithm. It extracts feature sequences from the example and runs the same QBF machinery. This is why a single descriptor yields one sorted sequence and several descriptors require fusion.
- **Fusing descriptors with equal weights by default**: when several descriptors are in play, naive equal weighting can let a weak descriptor drown out a strong one. Fusion weights should reflect which descriptor matters for the current query.

## Connections
[[content-based-retrieval]]: QBE and QBF are the two query modes that drive the interactive CBR loop.
[[feature-vector]]: both modes ultimately compare feature vectors; QBF takes values, QBE takes an image whose vector is extracted.
[[color-histogram]]: a typical single descriptor whose sorted comparison produces a feature sequence for QBF.
[[mpqf]]: standardizes QBE and QBF as query by example and query by feature input formats.
[[sql-mm]]: offers SI_Score based similarity comparison that backs QBE style queries in a SQL setting.
[[multimedia-query-languages]]: places QBE and QBF among the similarity query types a MMQL must support.

## Open Questions
- How should fusion weights be chosen when several descriptors disagree? Manual tuning, relevance feedback, or learned weights?
- Can the system suggest the next QBE image automatically, instead of waiting for the user to pick one from the result page?
- For very large databases, can the feature sequence be produced approximately to keep the interactive loop fast?
