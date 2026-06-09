---
title: "Multimedia Databases — Lecture 01 Overview"
tags: [topic, multimedia-databases, semester-1]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 01 establishes the foundations: what multimedia is, how media types are classified, what constitutes a multimedia system, how data streams work, and what a multimedia database must do.

## Core Map

This lecture builds a layered understanding, from definition to system requirements:

```
[[multimedia-definition]]           What IS multimedia?
    │
    ├── [[media-types-discrete-continuous]]   Discrete vs continuous media
    │
    ├── [[data-streams]]                      How media is transmitted (timing constraints)
    │
    └── [[multimedia-system]]                 Full system definition (Herrtwich/Steinmetz)
            │
            └── [[multimedia-main-domains]]   Steinmetz's 4-layer model
                    │
                    └── [[multimedia-database-intro]]     The MMDBMS concept
                            │
                            ├── [[structured-vs-unstructured-retrieval]]   DBMS + IR fusion
                            │
                            └── [[multimedia-query-predicates]]            How to query MM data
```

## Key Concepts at a Glance

| Concept                                  | Core Idea                                                                              |
| ---------------------------------------- | -------------------------------------------------------------------------------------- |
| [[multimedia-definition]]                | Multimedia = digitally manipulable media combination; medium classified by MHEG axes   |
| [[media-types-discrete-continuous]]      | Discrete (time-independent: text, images) vs Continuous (time-dependent: audio, video) |
| [[data-streams]]                         | Asynchronous/synchronous/isochronous transmission; FBR vs VBR; periodicity             |
| [[multimedia-system]]                    | Computer-controlled system handling ≥1 discrete + ≥1 continuous medium independently   |
| [[multimedia-main-domains]]              | Steinmetz layers: Basics → System → Services → Usage                                   |
| [[multimedia-database-intro]]            | MMDBMS = DBMS + IR; stores, indexes, retrieves, streams multimedia objects             |
| [[structured-vs-unstructured-retrieval]] | DBMS (exact, deterministic) vs IR (similarity, ranked); MMDBMS combines both           |
| [[multimedia-query-predicates]]          | Attribute, structure, spatial, semantic predicates for expressing MM queries           |


## Lecture Structure

The lecture follows this outline:
1. **Multimedia Definition** — MHEG medium classification, strict vs loose definitions, interactivity, linearity
2. **Multimedia System** — Herrtwich/Steinmetz definition, four characteristics
3. **Multimedia Main Domains** — Steinmetz's layered model (Basics/System/Services/Usage)
4. **Data Streams** — Transmission modes, periodicity, bitrate regularity
5. **Types of Media** — Discrete vs continuous
6. **Multimedia Databases** — MMDBMS requirements, retrieval paradigms, query predicates, query by example

## Key Takeaways for the Exam

1. **The strict multimedia definition** requires both discrete AND continuous media with independence. Know the difference between strict and general definitions.
2. **The Herrtwich/Steinmetz system definition** is a formal definition — memorize the four characteristics (combination, independence, integration, communication).
3. **Data stream modes** (asynchronous → synchronous → isochronous) form a spectrum of increasing timing precision. Know the buffer calculation: `buffer = data_rate × max_delay`.
4. **MMDBMS combines DBMS and IR** — this is the central thesis. Know what each paradigm provides and why both are needed.
5. **Four predicate types** (attribute, structure, spatial, semantic) — be able to classify example queries.
6. **Query by example** is a key user interaction paradigm: submit a sample, system extracts features, returns ranked matches.

## Connections to Future Lectures
- **Lecture 02 (Colors)**: Basics layer — color perception and representation
- **Lecture 03 (Image medium)**: Discrete media — raster/vector graphics, formats
- **Lecture 04 (Video/Text/Audio)**: Continuous + discrete media details
- **Lecture 05 (Compression)**: Basics layer — encoding and compression (MP3, JPEG)
- **Lecture 06 (Modeling)**: Metadata modeling for multimedia (MPEG-7)
- **Lecture 07 (CBIR)**: Content-based retrieval — semantic predicates in practice
- **Lecture 08 (Query languages)**: Formal multimedia query languages
- **Lecture 09 (Index structures)**: High-dimensional indexing for feature vectors

## References
- Steinmetz R & Nahrstedt K, "Multimedia Systems", Springer, 2004
- Steinmetz R & Nahrstedt K, "Multimedia Applications", Springer, 2004
- Herrtwich & Steinmetz, "Towards Integrated Multimedia Systems", 1991
