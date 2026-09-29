---
title: "Reproducibility Engineering - Sheet 1 Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 1

## Flashcards

> [!question]- What is the difference between a Docker image and a container?
> [!answer]- An **image** is a read-only template (blueprint) defining the contents of a container. A **container** is a running instance of an image, isolated from other containers and the host system.

> [!question]- How do you build a Docker image from a Dockerfile?
> [!answer]- Use `docker build -t <tag> .` in the directory containing the Dockerfile. The `-t` flag assigns a name/tag to the image.

> [!question]- What does `docker cp` do and how does it differ from bind mounts?
> [!answer]- `docker cp` copies files between host and container filesystems one-off. Bind mounts (`-v`) map a host directory into the container persistently, created at container startup, so changes are reflected in both directions.

> [!question]- Why do two visually identical images produce different SHA-256 checksums?
> [!answer]- Because SHA-256 operates on the raw byte content. A secret message embedded in the image alters bytes without visibly changing the image (e.g., steganography). Even a single-bit change produces a completely different hash.

> [!question]- Why do Alice and Bob get the same output when running the same Docker container on different host machines?
> [!answer]- Because the container provides a consistent, isolated environment. The script is deterministic, and the container bundles all dependencies (OS packages, libraries). The host hardware/OS differences don't affect the containerized execution.


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
