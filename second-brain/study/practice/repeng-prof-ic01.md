---
title: "RepEng In-Class Exercise 1 — Reproducibility Basics"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| Exercise 1 — Survey Interpretation | [[reproducibility-crisis]] |
| Exercise 2 — Repeatability / Reproduction / Replication | [[repeat-reproduce-replicate]] · [[types-of-reproducibility]] |
| Exercise 3 — Artifact Availability | [[artifact-availability]] · [[research-artifacts]] |
| Exercise 4 — Bachelor Thesis Reflection | [[repeat-reproduce-replicate]] · [[artifact-availability]] |

# In-Class Exercise Sheet 1 — Reproducibility Crisis & Terminology

Based on the Nature article on "Reproducibility Crisis" and ACM "Artifact Review and Badging".

---

## Exercise 1 — Survey Interpretation

1,576 researchers were asked if there is a reproducibility crisis. The pie chart shows:

- **52%** — Significant crisis
- **38%** — Slight crisis
- **7%** — No crisis
- **3%** — Don't know

**Takeaway:** 90% of researchers acknowledge at least some level of reproducibility crisis. This is overwhelming consensus — reproducibility is a real, recognized problem in science.

---

## Exercise 2 — Repeatability / Reproduction / Replication

**Definitions (ACM):**
- **Repeatability:** Same team, same experimental setup, same location
- **Reproducibility:** Different team, same (or very similar) experimental setup
- **Replication:** Different team, different experimental setup, trying to achieve same result

**(a)** Why do scientists perform experiments of other scientists?
→ **"This helps confirm and verify the results."** ✓

**(b)** Alice reads about experiments in a physics journal, plans to reconstruct the setup herself.
→ **Reproduction** — different person, same procedure/setup described in the article.

**(c)** Bob collects water samples weekly for 4 weeks (same person, same method).
→ **Repetition** — same person repeating the same measurement.

**(d)** Environmental group obtains Nina's artifacts (software, data, equipment) to check her simulation results.
→ **Reproduction** — different team using the original artifacts.

**(e)** Charlie asks Alice to visit his lab, use his ingredients and procedure.
→ **Repetition** — same lab, same equipment, same procedure (different person, but same setup).

**(f)** Dave asks Eve to follow same directions in her own kitchen.
→ **Reproduction** — same procedure but different environment (her kitchen vs his).

**(g)** Fay runs her hamster through a maze 20 times with different treats.
→ **Repetition** — same experimenter, same setup, multiple runs.

**(h)** George drops golf balls 10 times each, measuring bounce height.
→ **Repetition** — same experimenter, same setup, repeated measurements.

**(i)** Harry asks Joy to use his equipment and redo the density experiment.
→ **Repetition** — different person, but same equipment and same procedure in same location.

> **Note:** Some of these are borderline. The key distinguishing factor: if the setup/equipment changes, it moves from repetition → reproduction → replication.

---

## Exercise 3 — Artifact Availability

**ACM definition:** Author-created artifacts placed on a publicly accessible archival repository with a DOI or link.

**How to ensure for a Master's thesis:**
1. **Code:** Publish on a public repository (GitHub/GitLab) and archive with a DOI via Zenodo or Software Heritage.
2. **Data:** Upload datasets to a public archive (e.g., Zenodo, Figshare, institutional repository). For sensitive data, provide a synthetic version or access instructions.
3. **Environment:** Provide Dockerfiles or conda environments specifying exact dependencies and versions.
4. **Documentation:** Include a README with build/run instructions, and a CITATION.cff file.
5. **Versioning:** Tag releases corresponding to thesis milestones (submission, revision, final).

---

## Exercise 4 — Bachelor Thesis Reflection

**(a) Research question as hypothesis:**
*Personal — write your own. Example:* "Our classification model achieves ≥90% accuracy on the test dataset for detecting spam emails."

**(b) How did you confirm/reject?**
*Personal — describe whether you wrote code, ran experiments, collected data.*

**(c) Research artifacts produced:**
*Personal — list code, datasets, scripts, figures, reports, etc.*

**(d) Could you repeat in 24 hours?**
Likely challenges: dependency rot (libraries updated/broken), missing environment specifications, unclear data preprocessing steps, hardcoded paths, lost intermediate data.

**(e) Ensuring repeatability from day one:**
- Use version control (git) from day one
- Containerize the environment (Docker/conda)
- Pin all dependency versions
- Automate the full pipeline (Makefile/Snakemake)
- Archive everything with a DOI at submission time
- Write clear documentation *during* development, not after


---

## Related Resources

### 📖 Reproducibility Engineering — Lecture 1 Overview
- Lecture topic: [[reproducibility-engineering-lecture-1]]

**Key concepts covered:**
- [[reproducibility-crisis]]
- [[repeat-reproduce-replicate]]
- [[research-artifacts]]
- [[artifact-availability]]
- [[types-of-reproducibility]]
