---
title: "MMDB Exercise 2 — Multimedia and Multimedia Databases: Initial Concepts II"
tags:
  - practice
  - multimedia-databases
  - semester-1
course: "Multimedia Databases"
status: current
last_updated: 2026-06-02
---

## Exercises

### Task 1: Semantic Gap

1. Based on the Semantic Gap figure, give examples for "low-level features" and "high-level features". How would you interpret the term "bridging the semantic gap"?
2. Identify analogous "low" and "high level features" for an audio signal from a recording of a phone call.

### Task 2: Components of MMDB

1. Where does the difference between multimedia databases and "classical" databases lie? Consider in particular how the different components of databases (e.g. indexing, data model, query languages) handle the data structures from Exercise 1.
2. Consider a video-hosting platform similar to Youtube. Which components listed in a) are relevant to the functionalities 'account', 'video playlist', 'video recommender' and 'comment section'.

## Solutions

### Task 1: Semantic Gap

> [!note]- Solution
> **1a) Low-level vs High-level features:**
> - **Low-level features:** Color histogram, pixel intensity, pixel gradient, etc. Easy to extract directly from data, but have next to no semantics.
> - **High-level features:** "Winter sports", "Person skiing", "snow", "mountain" — more semantics, more difficult to extract.
> - **Bridging the semantic gap:** The process of mapping low-level features to high-level semantic concepts. This is a central challenge in multimedia databases, as human perception operates at a high semantic level while data is stored at a low feature level.
>
> **1b) Audio equivalents (phone call):**
> - **Low-level:** Audio length, bit/sample rate, frequency spectrum, dynamic range (lowest vs. highest amplitude), signal-to-noise ratio
> - **High-level:** Speech content, gender of the speaker, physical features of the audio source, emotional connotation

### Task 2: Components of MMDB

> [!note]- Solution
> **2a) MMDB vs Classical Databases:**
> - **Data model:** MMDB contains unstructured data, no fixed model. Must manage both unstructured and structured metadata.
> - **Data volume:** MM databases often have huge volumes of data.
> - **Indexing:** Metadata can be multi-dimensional (e.g. color histogram) → classical indexing cannot be adopted. Keywords (metadata) are predominant. Automated indexing uses features like color, shape, texture, spatial information for images; note, tone, duration for music.
> - **Querying/IR:** Retrieval algorithms must support content- and context-based retrieval. Should offer spatial/temporal queries, querying by examples, flexible querying using fuzzy predicates.
>
> **2b) Video platform analysis:**
> - **Account:** Structured data model → SQL, fixed matching and indexing. Embedded links to video history, saved information.
> - **Comment section:** Structured data model embedded within a semi-structured context. Can break if account/video gets deleted, metadata structure changes, or storage limitations change.
> - **Video playlist:** Semi-structured data model → XPath, structured matching and limited indexing. Embedded links to video instances, provides structure and maintains hyperlinks.
> - **Video recommender:** Semi-structured data model → semantic search, fuzzy matching. Result structure changes with underlying content.


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
