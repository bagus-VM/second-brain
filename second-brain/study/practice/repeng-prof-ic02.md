---
title: "RepEng In-Class Exercise 2 — Levels & Provenance"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 2 — Levels of Reproducibility & Provenance

Based on the VisTrails article and Heil et al. "Reproducibility standards for machine learning in the life sciences".

---

## Exercise 1 — VisTrails: Levels and Provenance

### (a) Levels of reproducibility:

- **Sharing** — how much of an experiment is available (data, code, workflow)
- **Reproducibility** — whether the experiment is repeatable, reproducible, or even replicable
- **Trustworthiness** — how much of the experiment can be confirmed

For the example with special hardware: **Computational reproducibility** can be obtained by providing the data produced by the hardware, and the analysis processes to derive the plots from the paper.

### (b) Types of provenance:

- **Prospective** provenance — describes the experiment specification: workflow structure, modules, connections, and inputs (the "recipe")
- **Retrospective** provenance — captures what actually happened during execution (the "baking log")
- **Evolution** provenance — tracks the history of the workflow, all different versions over time

### (c) Is VisTrails still maintained?

→ **No.** The VisTrails project is no longer actively maintained. The website and source code are still accessible, but development has ceased. This itself is a lesson in reproducibility — even tools designed for reproducibility can become unmaintained.

---

## Exercise 2 — Heil et al.: ML Reproducibility Standards

### (a) Main motivation:

"For machine-learning models in the life sciences to become **clinically useful**, scientists must prioritize computational reproducibility."

### (b) Reproducibility standards table:

| Criterion | Bronze | Silver | Gold |
|-----------|--------|--------|------|
| Data published and downloadable | ✓ | ✓ | ✓ |
| Models published and downloadable | | ✓ | ✓ |
| Source code published and downloadable | | ✓ | ✓ |
| Dependencies set up in a single command | | | ✓ |
| Key analysis details recorded | | | ✓ |
| Analysis components set to deterministic | | | ✓ |
| Entire analysis reproducible with a single command | | | ✓ |

### (c) Problem with merely reporting experiments and model:

If authors only *report* on their experiments (describing methods and results in text) without providing actual artifacts, other scientists cannot verify the claims. The reported numbers cannot be independently checked, and subtle implementation details that affect results are lost.

### (d) Platforms for sharing:

1. **Zenodo** — for datasets of up to 50GB (general-purpose, provides DOIs)
2. **Figshare** — for datasets larger than 50GB (also general-purpose, provides DOIs)

### (e) Why GitHub + Zenodo (double effort)?

GitHub is great for version control and collaboration, but GitHub repositories can be deleted, renamed, or made private at any time. Zenodo creates an immutable, citable snapshot with a DOI — a permanent archival record. The combination gives you development workflow (GitHub) + long-term preservation (Zenodo).

### (f) Hardware-related problem in ML:

ML experiments often depend on specific hardware (GPUs, TPUs) whose exact behavior may vary across architectures and driver versions. Floating-point arithmetic is not perfectly deterministic across different hardware, making exact reproduction difficult.

### (g) What is "badging"?

Badging is a system where journals/conferences assign badges (e.g., "Artifacts Available", "Artifacts Evaluated", "Results Reproduced") to papers that meet reproducibility criteria. It serves as an incentive because: (1) it's a visible mark of quality, (2) it can be listed on CVs, (3) it encourages authors to invest effort in packaging reproducible research.

### (h) Recommendation for compute-intensive analyses:

Store and share the intermediate results (e.g., trained models, processed data) so that reviewers and other researchers can verify the analysis without needing access to the same expensive compute infrastructure.

---

## Exercises 3 & 4 — Academic English (Vocabulary)

### Exercise 3: Describing methods and results

**(a)** "The samples were prepared **following** Jude [2012]."
**(b)** "The third mixture was prepared **using** the same procedure as for the first."
**(c)** "The criteria for **selecting** the subjects to participate in the survey were: ..."
**(d)** "By **reducing** the amount of liquid to the minimum, the mixture becomes more solid."
**(e)** "**Generally speaking**, our results show that bankers have no social conscience."
**(f)** "The **following** solution to this problem can be expressed as . . ."
**(g)** "**Taking** advantage of the properties of gold, we can now . . ."
**(h)** "**Subtracting** the first result from the second, we obtain . . ."
**(i)** "**Having** these features meant that we could . . ."

### Exercise 4: Highlighting drawbacks of previous research

**(a)** "The **shortcomings** of their method have been clearly recognized."
**(b)** "A serious **weakness** with this argument, however, is that . . ."
**(c)** "Their approach is not **appropriate** for those kinds of patients."
**(d)** "Their experiments were **flawed** by the fact that they were almost impossible to replicate."
**(e)** "This then is the major **drawback** to their experiments."
**(f)** "Such a **misleading** assumption can lead to serious consequences with regard to . . ."
**(g)** "Their claims seem to be somewhat **speculative**."
**(h)** "In our view, their findings are only **conjectures** based on unsubstantiated assumptions."
**(i)** "Their attempts to solve this simple problem are unnecessarily **complicated**."
**(j)** "An even greater source of **concern** is the fact that . . ."

---

## Related Lectures
- [[reproducibility-engineering-lecture-2]]
