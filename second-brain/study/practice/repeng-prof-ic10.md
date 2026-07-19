---
title: "RepEng In-Class Exercise 10 — Remote Experiments"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 10 — Remote Experiments & Workflow

Based on "Nullius in Verba" by Mauerer & Scherzinger, ICDE 2021.

---

## Exercise 1 — Workflow Labeling

The overall workflow for running experiments on a remote target platform:

```
Docker container                          Target platform
┌──────────────────┐                     ┌──────────────────┐
│ Build environment │ ──Copy──→          │ Run experiments   │
│ (analysis + build)│                     │ on target hardware│
└──────────────────┘                     └────────┬─────────┘
                                                  │
                                          measured data (.csv)
                                                  │
                                          ──Copy──↓
┌──────────────────┐
│ Generate graphs   │ ←── measured data
│ and paper         │
└──────────────────┘
```

**Labels:**
1. **Experiment execution package** — the Docker container with build tools and analysis code
2. **Build artefacts** — compiled binaries copied to the target platform
3. **Run experiments** — executing on the target platform (which may not support Docker)
4. **Measured data** — CSV files with raw results, copied back to the analysis environment
5. **Generate graphs and paper** — final analysis and visualization in the Docker container

**Key insight:** The analysis pipeline (build + graph generation) runs inside a Docker container for reproducibility. The experiments run on the actual target hardware (which may be a shared cluster, cloud VM, or specialized hardware that doesn't support Docker).

---

## Exercise 2 — Dependency and Temporal Flow

The diagram shows dependencies between artefacts with temporal flow:

```
[Code/Build] ──1──→ [Binary] ──3──→ [Results]
     │                                    │
     └──2──→ [Analysis Script] ──4──→ [Plots/Paper]
                                    5
```

**Labels for the numbered steps:**

1. **Build / Compile** — source code is compiled into an executable binary (A → B, B integrates A)
2. **Prepare analysis scripts** — write the data analysis/visualization code
3. **Execute experiments** — run the binary on the target platform, collect measured data (A ⇒ B, B is produced by A)
4. **Analyze results** — run analysis scripts on measured data to generate plots
5. **Write paper** — integrate plots and findings into the paper

**Temporal flow:** Steps 1-2 can happen in parallel. Step 3 depends on 1. Step 4 depends on 2+3. Step 5 depends on 4.

---

## Exercise 3 — SQPolite Project

This exercise involves walking through the reproduction package at https://github.com/lfd/icde2021_tutorial.

**Key concepts from the SQPolite project:**

1. **Experiment execution package** — contains everything needed to build the experiment binary, but NOT to run it (that depends on the target platform)

2. **Measured data handling** — raw results are collected on the target platform and copied back to the analysis environment

3. **Reproducibility chain:**
   - Docker container ensures the build environment is reproducible
   - Binary is built deterministically inside the container
   - Binary is copied to target platform (which has its own constraints)
   - Results are copied back and analyzed in the same container
   - Paper figures are generated from the same container

4. **Separation of concerns:**
   - **Reproducible builds** (Docker + pinned dependencies)
   - **Reproducible analysis** (scripts + data in container)
   - **Experimental execution** (may not be fully reproducible — depends on hardware)

**Takeaway:** Even when the experiment itself can't be containerized (e.g., running on specialized hardware), you can still ensure reproducibility of the build process and the data analysis.


---

## Related Resources

### 📖 Lecture 10: Remote Experiments and Artifact Packaging
- Lecture topic: [[reproducibility-engineering-lecture-10]]

**Key concepts covered:**
- [[reproducible-builds]]
- [[containerization-for-builds]]
- [[artifact-packaging]]
- [[git-for-reproducibility]]
- [[git-patches-and-diffs]]
