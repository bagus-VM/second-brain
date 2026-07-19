---
title: "MMDB Exercise 2 — Flashcards"
tags:
  - flashcards
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Flashcards

> [!question]- What is the semantic gap in multimedia databases?
> [!answer]- The semantic gap is the disconnect between low-level features (easily extracted from data, e.g. color histograms, pixel intensity) and high-level features (semantic concepts, e.g. "person skiing", "winter sports"). Bridging the semantic gap means mapping low-level features to meaningful high-level descriptions.

> [!question]- Give examples of low-level and high-level audio features.
> [!answer]- **Low-level:** Audio length, bit/sample rate, frequency spectrum, dynamic range, signal-to-noise ratio. **High-level:** Speech content, speaker gender, physical features of audio source, emotional connotation.

> [!question]- How do multimedia databases differ from classical databases in terms of indexing?
> [!answer]- MMDB metadata can be multi-dimensional (e.g. color histograms), so classical indexing cannot be adopted. Keywords/metadata are the predominant indexing method. Automated indexing uses features like color, shape, texture, spatial information for images; note, tone, duration for music.

> [!question]- What querying capabilities must MMDB retrieval algorithms support?
> [!answer]- Content- and context-based retrieval, spatial and temporal queries, querying by examples, and flexible querying using fuzzy predicates.

> [!question]- In a video platform, what database component is relevant for a video recommender?
> [!answer]- Semi-structured data model with semantic search (fuzzy matching), embedded links to video instances, linking unstructured data models. The result structure changes with underlying content.


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
