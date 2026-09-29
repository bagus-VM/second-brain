---
title: "Levels of Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---


## One-line Summary
Reproducibility can be assessed along three independent dimensions: *availability* (how much of the experiment is accessible), *repeatability* (whether it can be re-executed), and *confirmability* (how much of the result can be independently verified).

## Core Intuition
Not all reproducibility is equal. A paper that shares data but not code is "more reproducible" than one that shares nothing, but less than one that shares data, code, and environment. The three-level framework lets you classify *where* an experiment falls on the reproducibility spectrum rather than treating it as a binary property.

## Formal Definition / Statement
From VisTrails (Freire et al.), reproducibility is characterized by three orthogonal dimensions:

1. **Availability** -- how much of the experiment is available (data, code, workflow, environment).
2. **Repeatability / Reproducibility / Replicability** -- whether the experiment can be re-run to yield the same (repeatable), similar (reproducible), or equivalent-but-independent (replicable) results.
3. **Confirmability** -- how much of the experiment can be independently confirmed (e.g., by a third party with different tools).

These dimensions are not a strict hierarchy; an experiment can score high on availability but low on confirmability if the method is not documented clearly enough for independent verification.

## Key Properties / Complexity
- **Orthogonal dimensions**: increasing availability does not guarantee confirmability.
- **Practical example**: an experiment requiring special hardware can achieve *computational reproducibility* by providing the hardware-produced data plus the analysis workflow, even if the hardware itself is not shareable.
- **Spectrum, not binary**: real experiments occupy a point in a 3D space, not a simple "reproducible / not reproducible" label.

## Worked Example
Consider a neuroscience experiment using an MRI scanner:
- *Availability*: raw MRI scans are published, but the scanner firmware is proprietary.
- *Repeatability*: the analysis pipeline (Python scripts) re-runs identically on the published data.
- *Confirmability*: a second lab can independently analyse the published scans with their own tools and confirm the findings.

The experiment is computationally reproducible (analysis re-runs) even though the full physical experiment is not repeatable without the same scanner.

## Common Pitfalls
- Treating reproducibility as a binary yes/no property.
- Confusing availability of data with confirmability of results.
- Assuming that sharing code automatically makes an experiment reproducible (the environment may differ).

## Connections
- [[provenance-in-reproducibility]] -- provenance records are the mechanism for tracking all three levels.
- [[reproducibility-standards-bronze-silver-gold]] -- the Bronze/Silver/Gold standards operationalize these levels into actionable tiers.
- [[workflow-reproducibility]] -- workflow systems like [[vistrails]] manage availability and repeatability.
- [[computational-reproducibility-in-ml]] -- ML experiments face specific challenges across all three dimensions.

## Open Questions
- How do we measure confirmability quantitatively?
- Should the three levels be weighted equally when assessing reproducibility?
