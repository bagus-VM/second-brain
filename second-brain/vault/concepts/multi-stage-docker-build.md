---
title: "Multi-Stage Docker Build"
tags: [concept, reproducibility-engineering, semester-1, containers, docker, builds, optimization]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-17
prerequisites: ["[[containerization-for-builds]]"]
---

## One-line Summary
A Docker build pattern that compiles in one stage and ships only the artifact in a second, minimal stage.

## Core Intuition
Building software requires compilers, headers, linkers, and build tools. Running the result often requires almost nothing. A single-stage Dockerfile ships the entire toolchain in the final image, wasting hundreds of megabytes on tools that are never used at runtime. Multi-stage builds fix this: one stage builds the artifact, a second stage copies only what's needed to run it. The toolchain stays behind in the discarded build stage.

## Formal Definition / Statement
A **multi-stage Docker build** is a Dockerfile with multiple `FROM` directives. Each `FROM` starts a new, independent build stage. Later stages can copy files from earlier stages using `COPY --from=<stage-name>`. Only the final stage determines the image that gets tagged and shipped.

```dockerfile
FROM gcc:14 AS builder
WORKDIR /src
COPY mentos.c .
RUN gcc -O2 -static -o mentos mentos.c -lm

FROM scratch
COPY --from=builder /src/mentos /mentos
ENTRYPOINT ["/mentos"]
```

The first stage (`builder`) compiles the program. The second stage (`scratch`, the empty image) copies only the binary. The final image contains nothing but the binary.

## Key Properties

- **Size reduction**: the final image carries only the runtime artifact, not the build toolchain. A GCC-based single-stage image is ~1.2 GB; the equivalent multi-stage image on `scratch` can be ~100 KB.
- **Separation of build and runtime dependencies**: the build stage can install any number of tools without bloating the final image.
- **`scratch` base image**: the empty image with no OS, no shell, no libc. Only statically linked binaries can run on `scratch`.
- **Static linking required for `scratch`**: if the binary dynamically links against libc or other libraries, it needs those libraries at runtime. Use `-static` to embed all dependencies in the binary.
- **Named stages**: `AS builder` names the stage so `COPY --from=builder` can reference it. Without a name, stages are numbered (0, 1, 2...).
- **Only the last stage is tagged**: `docker build -t name .` tags the final stage. Intermediate stages are cached but not tagged.
- **Bitwise identical binary**: the compiled binary is the same regardless of whether it was built in a single-stage or multi-stage Dockerfile (same source, same compiler, same flags).

## Worked Example

Comparing single-stage and multi-stage images for the same C program:

**Single-stage** (Dockerfile.singlestage):
```dockerfile
FROM gcc:14
WORKDIR /src
COPY mentos.c .
RUN gcc -O2 -o mentos mentos.c -lm
ENTRYPOINT ["/src/mentos"]
```
Image size: ~1.2 GB (carries the entire GCC toolchain).

**Multi-stage** (Dockerfile):
```dockerfile
FROM gcc:14 AS builder
WORKDIR /src
COPY mentos.c .
RUN gcc -O2 -static -o mentos mentos.c -lm

FROM scratch
COPY --from=builder /src/mentos /mentos
ENTRYPOINT ["/mentos"]
```
Image size: ~100 KB (just the static binary).

The binary produces identical output in both cases. The difference is what else is in the image.

## Common Pitfalls

- **Forgetting `-static`**: without it, the binary dynamically links against libc. Running on `scratch` fails with "not found" errors (the dynamic linker is missing). Always use `-static` when building for `scratch`.
- **Source files leaking into the final image**: if you `COPY` source files in the runtime stage, they end up in the shipped image. Only copy the compiled artifact.
- **Assuming all stages run**: only the last stage's `RUN` commands execute in the final image. Earlier stages are build-time only.
- **Build cache invalidation**: changing a `COPY` or `RUN` in an early stage invalidates the cache for all subsequent commands in that stage. Order commands from least to most frequently changing.

## Connections
- [[containerization-for-builds]] -- multi-stage is an optimization technique within containerized builds
- [[reproducibility-engineering-lecture-10]] -- the remote experiment workflow builds on the same build-then-ship pattern
- [[artifact-packaging]] -- multi-stage builds produce leaner artifacts for shipping
- [[reproducibility-engineering-sheet-11]] -- Exercise Sheet 11 implements multi-stage builds hands-on

## Open Questions
- How do multi-stage builds interact with Docker layer caching? (Each stage has its own cache; invalidating a stage doesn't affect later stages unless they depend on it.)
- When is `scratch` too minimal? (Some binaries need `/etc/ssl/certs` for TLS, or `/tmp` for temp files. Alpine (~5 MB) is a common compromise.)
- How do you handle multi-language builds (e.g., C for the backend, Python for the analysis) in a single multi-stage Dockerfile?
