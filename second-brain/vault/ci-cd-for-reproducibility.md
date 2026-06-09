---
title: "CI/CD for Reproducibility"
tags: [concept, reproducibility-engineering, semester-1, ci-cd, verification]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reproducible-builds, build-environment-isolation]
---

## One-line Summary

CI/CD pipelines can be configured to automatically verify that builds are reproducible by building the same source multiple times in isolated environments and comparing the output.

## Core Intuition

Reproducibility is not a property you claim -- it is a property you verify. CI/CD systems provide the ideal infrastructure for this verification: they can build the same code in multiple independent containers, compare the resulting artifacts, and flag any differences. By making reproducibility checks a mandatory part of the build pipeline, you catch non-determinism regressions before they reach users.

## Formal Definition / Statement

A **reproducibility CI check** is a pipeline stage that:

1. Builds the same source code N times (typically N=2 or N=3)
2. In isolated, independent environments (separate containers/VMs)
3. Compares all output artifacts byte-by-byte (or via [[diffoscope]])
4. Fails the pipeline if any artifacts differ

This transforms reproducibility from a manual verification step into an automated quality gate.

## Key Properties

- **Automated verification**: No manual intervention needed; runs on every commit/PR.
- **Independent builds**: Each build runs in a fresh, isolated container to catch environment leaks.
- **Artifact comparison**: SHA-256 checksums or diffoscope for deep comparison.
- **Failure on non-reproducibility**: Pipeline fails if builds differ, preventing non-reproducible code from merging.
- **Historical tracking**: Build artifacts can be archived for future verification.
- **Integration with [[diffoscope]]**: Deep comparison when checksums differ.

## Worked Example

### Simple Reproducibility Check (GitHub Actions)

```yaml
name: Reproducibility Check
on: [push, pull_request]

jobs:
  build-1:
    runs-on: ubuntu-latest
    container: ubuntu:22.04
    steps:
      - uses: actions/checkout@v4
      - run: apt-get update && apt-get install -y gcc make
      - run: make
      - uses: actions/upload-artifact@v4
        with:
          name: build-1
          path: build/tool

  build-2:
    runs-on: ubuntu-latest
    container: ubuntu:22.04
    steps:
      - uses: actions/checkout@v4
      - run: apt-get update && apt-get install -y gcc make
      - run: make
      - uses: actions/upload-artifact@v4
        with:
          name: build-2
          path: build/tool

  verify:
    needs: [build-1, build-2]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
      - run: |
          diffoscope build-1/tool build-2/tool || exit 1
          echo "Builds are reproducible!"
```

### Debian's Approach

Debian runs reproducibility tests on every package:
- Build each package twice in different environments
- Compare with `diffoscope`
- Results published at https://tests.reproducible-builds.org/

## Common Pitfalls

1. **Not isolating builds sufficiently**: Using the same container for both builds defeats the purpose.
2. **Ignoring timestamp differences**: Without [[source-date-epoch]], timestamps will always differ.
3. **Not pinning container images**: `ubuntu:latest` changes over time; pin with digests.
4. **Caching artifacts between builds**: Build caches can leak state between independent builds.
5. **Only checking checksums, not diffs**: When checksums differ, you need diffoscope to understand why.

## Connections

- [[reproducible-builds]] -- CI/CD automates the verification of reproducibility
- [[build-environment-isolation]] -- CI containers provide the isolation needed
- [[diffoscope]] -- Deep comparison tool used in CI verification
- [[source-date-epoch]] -- Must be set in CI to eliminate timestamp differences
- [[containerization-for-builds]] -- Containers are the isolation mechanism in CI
- [[reproducibility-engineering-lecture-5]] -- Lecture context

## Open Questions

1. How do you handle reproducibility checks for cross-compiled binaries in CI?
2. What is the cost (time, compute) of running multiple builds per commit?
3. How do you verify reproducibility of artifacts that include debug information?
