---
title: "Package Manager Reproducibility"
tags: [concept, reproducibility-engineering, semester-1, package-managers, dependencies]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [reproducible-builds, build-environment-isolation]
---

## One-line Summary

Package manager reproducibility ensures that dependency resolution always produces the same set of installed packages, typically through lock files, content-addressable storage, or functional package management.

## Core Intuition

Even with a perfectly deterministic build system, if your dependencies change between builds, the output will differ. The lecture's Makefile exercises show how build ordering matters -- but the same principle applies to dependency versions. A lock file freezes the exact version (and often the hash) of every dependency, ensuring that `npm install` or `pip install` on Tuesday produces the same environment as on Friday.

## Formal Definition / Statement

A package manager achieves **reproducibility** when:

```
resolve(spec, t₁) = resolve(spec, t₂)  for all times t₁, t₂
```

Where `resolve` takes a dependency specification and returns the exact set of packages to install. This is achieved through:

- **Lock files**: Record exact versions and hashes of resolved dependencies
- **Content-addressable storage**: Packages identified by content hash, not version number
- **Functional package management** (Nix/Guix): Packages built from pure functions with explicit inputs

## Key Properties / Complexity

- **Lock files**: `package-lock.json`, `Pipfile.lock`, `Cargo.lock`, `go.sum` freeze dependency versions.
- **Content hashing**: Lock files often include integrity hashes (SHA-256) to detect tampering.
- **Version pinning**: Dependencies specified with exact versions, not ranges.
- **Reproducible resolution**: The same input specification always resolves to the same output.
- **Hermetic builds** (Nix): The build environment is fully described by the Nix expression, including all transitive dependencies.
- **Binary caching**: Nix and Guix cache build outputs by content hash, avoiding redundant rebuilds.

## Worked Example

### npm Without Lock File (Non-Reproducible)

```json
{
  "dependencies": {
    "lodash": "^4.17.0"
  }
}
```

- Monday: `npm install` → lodash 4.17.21
- Wednesday: lodash 4.17.22 is released → `npm install` → lodash 4.17.22

Different dependency versions = different build output.

### npm With Lock File (Reproducible)

```json
// package-lock.json (auto-generated)
{
  "dependencies": {
    "lodash": {
      "version": "4.17.21",
      "resolved": "https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz",
      "integrity": "sha512-v2kDEe57lec..."
    }
  }
}
```

Now `npm ci` (not `npm install`) uses the lock file exactly, ensuring reproducible dependency installation.

### Nix (Functional Package Management)

```nix
# default.nix
{ pkgs ? import (fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/abc123.tar.gz";
    sha256 = "...";
  }) {} }:

pkgs.stdenv.mkDerivation {
  name = "my-tool";
  src = ./.;
  buildInputs = [ pkgs.gcc pkgs.gnumake ];
}
```

Nix builds are fully reproducible because:
- The nixpkgs revision is pinned by hash
- All dependencies are explicitly declared
- Builds run in a sandbox with no network access
- Output paths are content-addressed

## Common Pitfalls

1. **Using `npm install` instead of `npm ci`**: `install` updates the lock file; `ci` uses it exactly.
2. **Not committing lock files**: Lock files must be version-controlled to be useful.
3. **Ignoring transitive dependencies**: A lock file must capture the entire dependency tree.
4. **Mutable registries**: Even with lock files, registries can serve different content for the same version. Integrity hashes mitigate this.
5. **Platform-specific dependencies**: Some packages have different dependencies on different platforms, breaking cross-platform reproducibility.
6. **Not updating lock files**: Lock files must be updated when dependencies change, but only intentionally.

## Connections

- [[reproducible-builds]] -- Reproducible dependencies are a prerequisite for reproducible builds
- [[build-environment-isolation]] -- Containers + lock files together ensure full reproducibility
- [[deterministic-builds]] -- Fixed dependencies enable deterministic compilation
- [[containerization-for-builds]] -- Containers can embed locked dependencies
- [[ci-cd-for-reproducibility]] -- CI should use lock files and verify dependency integrity
- [[reproducibility-engineering-lecture-5]] -- Lecture context

## Open Questions

1. How do Nix and Guix handle security updates for pinned dependencies?
2. Can lock files guarantee reproducibility across different platforms (Linux, macOS, Windows)?
3. What is the maintenance cost of keeping lock files up to date?
