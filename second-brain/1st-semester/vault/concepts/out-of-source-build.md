---
title: "Out-of-Source Build"
tags: [concept, reproducibility-engineering, semester-1, out-of-source, build-system, hygiene]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[make-and-build-systems]]", "[[deterministic-builds]]", "[[reproducible-builds]]"]
---

## One-line Summary
An out-of-source (or "out-of-tree") build keeps the build artefacts (.o files, executables, generated code) in a directory *separate* from the source tree — so the source tree stays clean, builds can be wiped with `rm -rf build/`, and multiple parallel builds with different configurations can coexist without interfering.

## Core Intuition
The opposite of an out-of-source build is an **in-source build**, where the build artefacts land in the same directories as the source code. This is the default for many small projects (`gcc hello.c -o hello` puts `hello` next to `hello.c`) and is the source of many reproducibility and hygiene problems:

- `git status` is cluttered with untracked `.o`, `.exe`, `.so` files.
- You can't easily have two builds with different flags (e.g., debug and release) at once.
- Wiping the build requires identifying and deleting all the artefact files (`.o`, `*.gcda`, generated `.c` files, etc.) — error-prone.
- Mixing source and artefacts breaks the implicit assumption that "the source tree is what you version-control".

An out-of-source build solves all of these: the source tree is sacred, the build tree is disposable.

The lecture's exercise 3 uses the standard idiom:
```bash
mkdir build
cd build
../Python-3.12.3/configure --prefix=$HOME/Python-3.12.3-custom
make -j $(nproc)
```

The `../Python-3.12.3/configure` is a relative path from `build/` to the source. All generated files land inside `build/`. The source tree at `../Python-3.12.3/` is untouched.

## Formal Definition / Statement

A build is **out-of-source** if and only if:
- The build artefacts (object files, executables, generated sources, dependency files) are written *only* inside a build directory.
- The build directory is *not* a subdirectory of the source tree (it is a sibling or some other unrelated location).
- The source tree is *not* modified by the build (no generated files written into it, no mtime changes from the build process).

The build directory is typically named `build/`, `out/`, `_build/`, `cmake-build-debug/`, or similar. The build tool is told about it via:
- **CMake**: `-B build -S .` or `cmake -S . -B build`
- **Autoconf/Automake**: separate `build/` directory with `../configure` invoked from inside
- **Meson**: `meson setup build`
- **Cargo** (Rust): always out-of-source, `target/` is separate by convention
- **Go**: always out-of-source, `$GOPATH/pkg/` and binary in `bin/`
- **Python distutils / pip**: not really applicable — Python doesn't compile by default; the equivalent is `python -m build --outdir dist/`

## Key Properties / Complexity

### Why out-of-source is the standard
- **Clean source tree**: `git status` shows only your changes, not the build's litter.
- **Easy wipe**: `rm -rf build/` and start over. No "find . -name '*.o' -delete" rituals.
- **Parallel configurations**: `build-debug/` and `build-release/` can coexist with different flags.
- **CI-friendly**: the build directory is ephemeral; the source is the artifact.
- **Reproducibility aid**: if the source is unchanged but the build directory is wiped, the new build should be bitwise identical to the previous one. With an in-source build, you have to clean the source first.

### Why some projects still do in-source
- **Small, single-file programs**: there's nothing to put in a build directory.
- **Legacy codebases**: the Makefile expects to find `.o` files next to `.c` files.
- **Generated sources mixed with hand-written**: a code generator writes to a directory in the source tree; the build then compiles them in place. (This is a smell — the generator should write to the build tree.)
- **Toolchain limitations**: older toolchains that don't support out-of-source builds (rare in 2026).

### CMake's behaviour
CMake is the canonical out-of-source build system. The default is:
- Configure: `cmake -S . -B build` (source in `.`, build in `build/`)
- Build: `cmake --build build` or `cd build && make`
- The build directory contains all generated Makefiles, object files, executables, CMakeCache.txt, etc.
- The source tree is read-only during the build (modulo permission issues).

If you run `cmake -S . -B .` (in-source), CMake will warn and create a `CMakeFiles/` directory in the source tree. Don't do this.

## Worked Example

The lecture's Python build:
```bash
$ ls                       # inside the source tree
Python-3.12.3/             # source code
$ mkdir build
$ cd build
$ ../Python-3.12.3/configure --prefix=$HOME/Python-3.12.3-custom
# Reads configuration from ../Python-3.12.3/configure (the source)
# Writes Makefile, config.status, etc., into ./ (the build tree)
$ make -j $(nproc)
# Compiles, links, generates pyc files — all into the build tree
# Source tree is untouched
```

After the build:
```
build/
  Makefile
  config.status
  pyconfig.h             # generated header (was: ../Python-3.12.3/pyconfig.h.in)
  Python/                # compiled C extensions
  python                  # final executable
Python-3.12.3/           # source tree, unchanged
```

To rebuild from scratch: `rm -rf build/ && mkdir build && cd build && ../Python-3.12.3/configure ...`

To have a debug build and a release build side by side:
```bash
$ mkdir build-debug build-release
$ cd build-debug && ../Python-3.12.3/configure --prefix=... --with-pydebug
$ cd ../build-release && ../Python-3.12.3/configure --prefix=...
```

Each build tree is independent. The source tree is shared.

## Common Pitfalls
- **Generated headers in the source tree**: `#include "config.h"` requires `config.h` to be findable. If the generator writes to the build tree, you need `-I build/` in the include path. Forgetting this is a common build break.
- **CMake's `in-source` mode**: `cmake .` in the source tree works but is discouraged. Always use `cmake -S . -B build`.
- **Toolchains that assume in-source**: some Makefile templates hard-code `./build/objs/`. Audit before refactoring to out-of-source.
- **IDE confusion**: IDEs like CLion or Visual Studio Code may default to in-source. Check the project's `.vscode/settings.json` or `.idea/` configuration.
- **Build-tree-only files in version control**: `build/` should be in `.gitignore`. If it's committed, you've checked in artefacts.
- **"Out-of-source" vs. "out-of-tree"**: same idea, different words. The lecture uses "out-of-source" / "out-of-tree" interchangeably.

## Connections
- [[make-and-build-systems]] — Make is the classic build tool, often paired with out-of-source
- [[deterministic-builds]] — out-of-source is a prerequisite for bitwise-identical rebuilds
- [[reproducible-builds]] — out-of-source is a step toward reproducibility
- [[binary-build-reproducibility]] — the bitwise-identical property depends on a clean build state
- [[containerization-for-builds]] — Docker is a more aggressive form of build isolation
- [[c-preprocessor]] — `#include` paths are the most common reason source needs to know about the build tree

## Open Questions
- For very large C++ projects (millions of lines), is out-of-source build always faster than in-source? (Yes — because the build cache is preserved across `rm -rf build/ && rebuild`. But ccache/ccache-like tools can replicate this for in-source builds.)
- Can a build system *enforce* out-of-source, or only encourage it? (CMake refuses to do in-source by default. Make has no such mechanism — you have to write the discipline into the Makefile.)
- For monorepos with hundreds of packages, is there a build system that scales to "build this one package, out-of-source, with these flags"? (Bazel, Pants, Please — all support this. Make and CMake do not, by default.)
