---
title: "Reproducibility Engineering - Lecture 2: Levels and Provenance"
tags: [topic, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Reproducibility Engineering - Lecture 2: Levels and Provenance

## Overview
In-Class Exercise Sheet 2 covers two foundational frameworks for understanding reproducibility:
1. The **three-dimensional model of reproducibility** (from the VisTrails paper by Freire et al.) -- availability, repeatability/reproducibility/replicability, and confirmability.
2. The **Bronze/Silver/Gold reproducibility standards** (from Heil et al., 2021) -- a practical tiered framework for ML reproducibility in the life sciences.

These two frameworks are complementary: the first defines *what reproducibility means* (conceptual), the second defines *how to achieve it* (practical).

## Key Concepts

### Framework 1: Levels of Reproducibility (VisTrails)
- [[levels-of-reproducibility]] -- the three dimensions: availability, repeatability, confirmability.
- [[provenance-in-reproducibility]] -- the three provenance types: prospective, execution, version.
- [[vistrails]] -- the workflow management system that implements these ideas.
- [[workflow-reproducibility]] -- the general principle of making computational workflows reproducible.

### Framework 2: Reproducibility Standards (Heil et al.)
- [[reproducibility-standards-bronze-silver-gold]] -- the tiered framework: Bronze (share), Silver (document), Gold (automate).
- [[computational-reproducibility-in-ml]] -- the specific challenges of ML reproducibility.
- [[data-provenance]] -- the lineage of data through transformation chains.

## How the Concepts Connect

```
[[levels-of-reproducibility]]
    ├── defines dimensions (availability, repeatability, confirmability)
    │
    ├── implemented via [[provenance-in-reproducibility]]
    │   ├── prospective (workflow spec)
    │   ├── execution (run logs)
    │   └── version (history)
    │
    └── operationalised by [[reproducibility-standards-bronze-silver-gold]]
        ├── Bronze: data + code + models shared
        ├── Silver: dependencies documented, key details recorded
        └── Gold: deterministic, single-command reproducibility

[[workflow-reproducibility]]
    └── enabled by tools like [[vistrails]]

[[computational-reproducibility-in-ml]]
    └── addressed by the Bronze/Silver/Gold framework

[[data-provenance]]
    └── subset of [[provenance-in-reproducibility]] focused on data lineage
```

## Source Materials
- Freire et al., "Reproducibility with VisTrails" (the three levels and three provenance types).
- Heil et al. (2021), "Reproducibility standards for machine learning in the life sciences" (Bronze/Silver/Gold).
- Adrian Wallwork, "English for Academic Research: Vocabulary Exercises" (academic writing exercises, not exam-relevant).

## Exam-Relevant Takeaways
1. Be able to name and distinguish the three levels of reproducibility (availability, repeatability, confirmability).
2. Be able to name and distinguish the three types of provenance (prospective, execution, version).
3. Be able to fill in the Bronze/Silver/Gold table from memory.
4. Understand why "merely reporting" on ML experiments is insufficient (narrative vs computational reproducibility).
5. Know the difference between general-purpose sharing platforms (Zenodo for ≤50GB, others for larger) and why GitHub + Zenodo is recommended (archiving vs hosting).
