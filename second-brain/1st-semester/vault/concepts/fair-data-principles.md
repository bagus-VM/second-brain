---
title: "FAIR Data Principles"
tags: [concept, reproducibility-engineering, semester-1, data-management, open-science, metadata]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-17
prerequisites: []
---

## One-line Summary
Four principles (Findable, Accessible, Interoperable, Reusable) that make digital research objects machine-actionable.

## Core Intuition
Research data accumulates in every lab, on every project, in every format imaginable. Without a shared set of principles for how to describe, store, and expose that data, it becomes a pile of files that only the original author can navigate. The FAIR principles (Wilkinson et al., Nature, 2016) don't prescribe a specific tool or format -- they define *properties* that digital research objects should have so that both humans and machines can discover, access, and reuse them.

The key design goal: **machine-actionability**. FAIR data isn't just human-readable -- it's structured so that computational agents can autonomously find, interpret, and process it without human hand-holding.

## Formal Definition / Statement
The FAIR Guiding Principles (Findable, Accessible, Interoperable, Reusable) were published by Wilkinson et al. in Nature Scientific Data (2016). They apply to digital research objects: data, algorithms, tools, and workflows.

### F -- Findable
- F1: (Meta)data are assigned a globally unique and persistent identifier
- F2: Data are described with rich metadata
- F3: Metadata clearly and explicitly include the identifier of the data they describe
- F4: (Meta)data are registered or indexed in a searchable resource

### A -- Accessible
- A1: (Meta)data are retrievable by their identifier using a standardized communications protocol
- A1.1: The protocol is open, free, and universally implementable
- A1.2: The protocol allows for authentication and authorization where necessary
- A2: Metadata remain accessible even when the data are no longer available

### I -- Interoperable
- I1: (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation
- I2: (Meta)data use vocabularies that themselves follow the FAIR principles
- I3: (Meta)data include qualified references to other (meta)data

### R -- Reusable
- R1: (Meta)data are richly described with accurate and relevant attributes
- R1.1: (Meta)data are released with a clear and accessible data usage licence
- R1.2: (Meta)data are associated with detailed provenance
- R1.3: (Meta)data meet domain-relevant community standards

## Key Properties / Complexity

### Stakeholders
FAIR identifies five stakeholder groups:
- **Original researchers** -- produce and describe the data
- **Reusers** -- researchers who want to build on existing data
- **Professional data publishers** -- make data discoverable
- **Funding agencies** -- increasingly mandate FAIR compliance
- **Computational agents** -- machines that autonomously process data

The inclusion of computational agents is what separates FAIR from earlier data management guidelines.

### Not a standard, a framework
FAIR doesn't mandate specific formats, tools, or repositories. It defines *desired outcomes* (machine-actionable, discoverable, accessible) and leaves implementation to domain-specific communities. This is deliberate -- a genomics lab and a climate modeler need different tools, but both can follow FAIR.

### Metadata survives data loss
Principle A2 (metadata remain accessible even when data are no longer available) is often overlooked. Data storage costs money; metadata is cheap. Even if the raw data must be deleted, the metadata (what it was, how it was collected, who created it) should persist -- it's the provenance record that makes future research aware of what existed.

### Connection to reproducibility
FAIR directly supports [[computational-reproducibility-in-ml|computational reproducibility]]: if data is findable and accessible, experiments can be rerun. If it's interoperable, different tools can process it. If it's reusable with clear licenses and provenance, others can verify and extend the work.

## Worked Example
A climate research group publishes temperature data:
- **Findable**: each dataset gets a DOI (persistent identifier). Metadata includes spatial/temporal coverage, measurement method, and the DOI itself. The dataset is indexed in a data catalogue.
- **Accessible**: data is retrievable via HTTPS (open protocol). Metadata persists even if the dataset is deprecated.
- **Interoperable**: data uses NetCDF format (standard in climate science) with CF conventions (community vocabulary). References link to related datasets (ocean salinity, atmospheric pressure).
- **Reusable**: CC-BY 4.0 licence. Provenance records show raw sensor data, calibration steps, and quality flags. Follows CMIP6 community standards.

## Common Pitfalls
- **FAIR is not open data.** FAIR data can be behind authentication (A1.2). "Accessible" means retrievable via a standard protocol, not necessarily publicly available.
- **FAIR is not a checklist.** The principles are goals, not binary pass/fail criteria. A dataset can be partially FAIR (findable and accessible but not interoperable).
- **Metadata is not optional.** F2 (rich metadata) and R1 (richly described) are what make data reusable. Without metadata, data is just numbers.
- **Persistent identifiers must actually persist.** A DOI that redirects to a 404 page violates F1. The identifier must resolve for as long as the data is referenced.
- **FAIR doesn't address data quality.** Data can be FAIR and wrong. The principles govern *management and stewardship*, not *accuracy*.

## Connections
- [[reproducibility-engineering-lecture-8]] -- data formats (HDF5, JSON, XML) support interoperability (I1)
- [[hdf5]] -- HDF5's self-describing nature (groups, datasets, attributes) directly supports FAIR's metadata requirements
- [[reproducibility-engineering-sheet-11]] -- Exercise Sheet 11 (IC_11) tests FAIR knowledge
- [[legal-frameworks-research-data]] -- licensing (R1.1) connects to copyright, GDPR, and database rights
- [[data-provenance]] -- provenance (R1.2) is a core FAIR requirement
- [[tidy-data]] -- tidy data conventions support interoperability

## Open Questions
- How do you measure FAIR compliance quantitatively? (Several metrics exist -- FAIRmetrics, F-UJI -- but none are universally accepted.)
- How does FAIR apply to AI/ML models, not just data? (Model cards and datasheets are emerging as the FAIR equivalent for ML.)
- What happens when FAIR principles conflict with privacy (GDPR)? (A1 says accessible, but GDPR says minimise. The resolution is authentication-gated access.)
