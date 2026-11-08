---
title: "Reproducibility Engineering - Sheet 3 Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 3

## Flashcards

> [!question]- What is the difference between a source container and a binary container?
> [!answer]- A **source container** is built from a Dockerfile (rebuildable but may pull different dependencies over time). A **binary container** is created from an exported Docker image (`docker save`/`docker load`) where all dependencies are fixed in time — fully reproducible but not rebuildable.

> [!question]- How do you share a Docker image as a binary container?
> [!answer]- Use `docker save -o <name>.tar <image>` to export the image to a tar file. The recipient uses `docker load -i <name>.tar` to import it, then runs it with `docker run --rm <image>`.

> [!question]- If an external API used by a script goes offline, will a binary container still fail? Why?
> [!answer]- Yes. Binary containers freeze the software environment but not runtime network dependencies. If the script makes HTTP calls to an external service at runtime, that service being offline causes failure regardless of container type.

> [!question]- What is a usage block in a shell script and why is it important?
> [!answer]- A usage block is an if-condition that checks whether the script was called with the correct number of arguments. If the check fails, it prints the correct syntax. This prevents silent failures from malformed invocations and improves usability.

> [!question]- What is the purpose of encoding experiment parameters in the result directory name?
> [!answer]- It makes results self-documenting: the directory name (e.g., `recipe_runs_10_seed_42_exp1`) encodes all parameters, so you can identify the experiment configuration without opening any files. This aids organization and traceability.


---

## Related Resources

### 📖 Reproducibility Engineering – Lecture 3: Hypotheses
- Lecture topic: [[reproducibility-engineering-lecture-3]]

**Key concepts covered:**
- [[hypothesis-formulation]]
- [[presenting-experiments]]
- [[levels-of-equivalence]]
- [[reproducibility-crisis]]
- [[repeat-reproduce-replicate]]
- [[computational-reproducibility-in-ml]]
- [[research-artifacts]]
