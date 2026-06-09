---
title: "Data Provenance"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Data Provenance

## One-line Summary
Data provenance is the documented lineage of data -- where it came from, how it was collected and transformed, and every step that produced the current version.

## Core Intuition
Data does not appear from nowhere. Every dataset has a history: who collected it, what instruments were used, what cleaning and transformations were applied. Without this lineage, you cannot assess data quality, debug errors, or reproduce results that depend on it.

## Formal Definition / Statement
Data provenance (a subset of [[provenance-in-reproducibility]]) records:
- **Origin**: the source of raw data (sensor, survey, API, simulation).
- **Transformation chain**: every processing step applied to the data (cleaning, normalisation, feature engineering, aggregation).
- **Dependencies**: which upstream datasets or processes contributed to the current dataset.
- **Metadata**: timestamps, versions, responsible parties, quality metrics.

This is closely related to the W3C PROV model, which defines entities, activities, and agents as the core vocabulary for provenance.

## Key Properties
- **Forward provenance** (also called "why-provenance"): given an output, trace back to the source data and transformations that produced it.
- **Backward provenance**: given a source, trace forward to all outputs that depend on it.
- **Essential for trust**: without data provenance, published results cannot be verified or audited.
- **Distinguishes from execution provenance**: data provenance focuses on the data lineage, while execution provenance ([[provenance-in-reproducibility]]) also captures runtime details.

## Worked Example
A public health dataset used in an epidemiology study:
1. Raw data: hospital admission records (2020-2025).
2. Cleaning: remove duplicates, standardise ICD codes.
3. Transformation: aggregate by region and week, compute incidence rates.
4. Final dataset: `weekly_incidence.csv` published alongside the paper.

Data provenance records each step, the code that performed it, and the intermediate datasets, so a reader can verify the transformation chain.

## Common Pitfalls
- Publishing a "clean" dataset without documenting the cleaning steps.
- Losing provenance when data passes through multiple tools (Excel → Python → R → database).
- Confusing data provenance with [[workflow-reproducibility]] -- they overlap but are distinct concepts.

## Connections
- [[provenance-in-reproducibility]] -- data provenance is a specific type of provenance focused on data lineage.
- [[levels-of-reproducibility]] -- data provenance directly supports availability and confirmability.
- [[reproducibility-standards-bronze-silver-gold]] -- Bronze requires "data published and downloadable," but data provenance goes further by requiring the transformation chain.
- [[computational-reproducibility-in-ml]] -- ML training data provenance is critical for detecting data leakage and bias.

## Open Questions
- How do we capture provenance for data that passes through non-scripted tools (GUI-based software)?
- What is the right granularity for transformation steps?
