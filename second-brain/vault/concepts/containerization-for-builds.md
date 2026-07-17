---
title: "Containerization for Builds"
tags: [concept, reproducibility-engineering, semester-1, containers, builds]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [build-environment-isolation]
---

## One-line Summary

Containers (Docker, Podman) provide a mechanism to encapsulate the entire build environment -- OS, tools, libraries, and configuration -- into a reproducible, portable image.

## Core Intuition

The lecture exercises show how build output depends on the host environment: compiler version, installed libraries, filesystem layout, and even the order files appear on disk. Containers solve this by packaging the entire build environment into a single, versionable artifact. The Dockerfile becomes the "recipe" for the build environment, and the image digest becomes the "fingerprint" that guarantees environment identity.

## Formal Definition / Statement

A **containerized build** is a build executed inside a container where:

1. The base image is pinned by digest (not just tag)
2. All installed tools and libraries are version-pinned
3. The build instructions are fully specified in a Dockerfile
4. The container image itself is reproducible (same Dockerfile → same image)

The Dockerfile serves as both the build recipe and the environment specification, making it a single source of truth for both what is built and how.

## Key Properties

- **Image pinning**: Use `FROM ubuntu:22.04@sha256:abc...` for exact reproducibility.
- **Layered builds**: Each Dockerfile instruction creates a layer that can be cached and verified.
- **Isolation from host**: The container's filesystem, network, and process space are isolated.
- **Reproducible image builds**: Given the same Dockerfile and base image, `docker build` produces the same image.
- **Portability**: The same container runs identically on any host with the same container runtime.
- **Version control**: Dockerfiles can be version-controlled alongside source code.

## Worked Example

### Reproducible C Build Container

```dockerfile
# Pin exact base image
FROM ubuntu:22.04@sha256:aabbccdd...

# Install exact compiler version
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc=4:11.3.0-1ubuntu1 \
    make=4.3-4.1build1 && \
    rm -rf /var/lib/apt/lists/*

# Set reproducible environment
ENV SOURCE_DATE_EPOCH=1748784000
ENV TZ=UTC
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Copy source
COPY . /build/
WORKDIR /build

# Build
RUN make clean && make
```

### Building in the Container

```bash
# Build the image
docker build -t my-build-env .

# Run the build
docker run --rm -v $(pwd)/output:/output my-build-env \
    cp /build/tool /output/

# Verify reproducibility
docker run --rm my-build-env sha256sum /build/tool
# Run again -- should produce same hash
docker run --rm my-build-env sha256sum /build/tool
```

## Common Pitfalls

1. **Not pinning base image digest**: `FROM ubuntu:22.04` pulls the latest 22.04, which changes. Use `@sha256:...`.
2. **Not pinning package versions**: `apt-get install gcc` installs whatever is current. Pin versions.
3. **Not cleaning apt cache**: `rm -rf /var/lib/apt/lists/*` prevents cache from affecting the build.
4. **Using `ADD` instead of `COPY`**: `ADD` can fetch URLs and extract archives, introducing network dependencies.
5. **Not setting timezone/locale**: Default values vary by base image.
6. **Caching too aggressively**: Build cache can mask non-determinism.

## Connections

- [[build-environment-isolation]] -- Containers are the primary isolation mechanism
- [[reproducible-builds]] -- Containerized builds enable reproducibility
- [[ci-cd-for-reproducibility]] -- CI systems use containers for isolated builds
- [[deterministic-builds]] -- Container isolation eliminates environment-based non-determinism
- [[source-date-epoch]] -- Set in the container environment
- [[package-manager-reproducibility]] -- Lock files complement container pinning
- [[reproducibility-engineering-lecture-5]] -- Lecture context
- [[multi-stage-docker-build]] -- an optimization technique that separates build and runtime stages

## Open Questions

1. Can Docker images themselves be made fully reproducible (same Dockerfile → bit-for-bit same image)?
2. How do you handle GPU dependencies in reproducible containerized builds?
3. What is the relationship between container image digests and reproducibility guarantees?
