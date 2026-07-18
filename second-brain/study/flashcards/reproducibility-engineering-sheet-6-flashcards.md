---
title: "Reproducibility Engineering Sheet 6 — Binary Builds, ReproTest, Make Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-14
---

# Flashcards — Exercise Sheet 6 (Binary Builds, ReproTest, Make)

> [!question]- What is binary build reproducibility?
> [!answer]- The property that compiling the same source code twice — across different days, paths, build directories, or compiler versions — produces *bitwise identical* output binaries. Tested in practice with [[reprotest]].

> [!question]- Of the 4 C "Hello World" snippets in task 6a, how many allow for a bitwise identical build?
> [!answer]- **1** (only the plain `printf("Hello World")`). The other three use `__FILE__` (path-embedding), `__TIME__` (wall-clock), and `__LINE__` (line position) — all of which can change the binary. (`__LINE__` is bitwise identical only if the source is unchanged AND compiled from the same path; in practice, "different day, different machine" breaks it.)

> [!question]- What does `__FILE__` expand to, and why is it a problem for bitwise identical builds?
> [!answer]- `__FILE__` expands to a string literal containing the *path* of the current source file as it was passed to the compiler. Two builds from different working directories (e.g., `gcc hello.c` vs `gcc ./task2/hello.c`) embed different paths → different binaries. Fix: `-ffile-prefix-map=oldprefix=newprefix` to normalise the path.

> [!question]- What does `__TIME__` expand to, and what is the standard fix?
> [!answer]- `__TIME__` expands to a string literal "hh:mm:ss" of the wall-clock time at which preprocessing began. The standard fix: set the `SOURCE_DATE_EPOCH` environment variable to a fixed Unix timestamp. The preprocessor (when conformant) uses this instead of the real time.

> [!question]- What does `__LINE__` expand to?
> [!answer]- `__LINE__` expands to the integer constant of the current line number *in the source file at the point of expansion*. It is deterministic for a given source at a given position, but changes if the source is edited, the file is moved, or the line shifts.

> [!question]- Why does GCC record the source path *as passed on the command line*, not the resolved absolute path?
> [!answer]- GCC's behaviour: it stores the path verbatim from the command line. So `gcc hello.c -o out` and `gcc ./task2/hello.c -o out2` may produce identical binaries (if both paths are recorded identically). But `gcc /tmp/hello.c` from a different cwd records a different path. The "path" is whatever the user typed.

> [!question]- What does ReproTest do, and what are its two key dependencies?
> [!answer]- ReproTest builds a program twice in different simulated environments and checks whether the resulting binaries are identical. The two key dependencies: `disorderfs` (a FUSE filesystem that randomises file metadata) and `faketime` (a library that intercepts time-related system calls). Both run inside a Docker container.

> [!question]- Why does compiling with `-g` (debug info) typically fail ReproTest?
> [!answer]- Debug info (DWARF) embeds the source path (in `.debug_info`) and timestamps (in `.debug_line`). Two builds from different paths or times produce different DWARF data → different binaries. The executable code (`.text`) is identical; only the debug sections differ.

> [!question]- What are the five regions of C program memory, and which one embeds the `__TIME__` string?
> [!answer]- (1) **Stack** — local variables; not in binary. (2) **Heap** — dynamic memory; not in binary. (3) **Globals** — `.data` and `.bss` sections. (4) **Constants** — `.rodata` section. (5) **Code** — `.text` section. The `__TIME__` string literal is a constant, so it lives in `.rodata` — embedded in the binary.

> [!question]- What is an "out-of-source" build, and why is it good practice?
> [!answer]- An out-of-source build keeps build artefacts (.o files, executables, generated code) in a *separate* directory from the source tree. Good practice because: (1) the source tree stays clean and version-control-friendly; (2) `rm -rf build/` cleanly wipes the build; (3) multiple configurations (debug, release) can coexist in parallel build dirs; (4) reproducibility: the build state is well-defined and ephemeral.

> [!question]- In the lecture's Makefile, if you modify `generate_chart.py` and run `make all` again, which targets are recreated?
> [!answer]- `results/chart.pdf` and `experiment.pdf` are recreated. `results/results.csv` is NOT recreated, because none of its prerequisites changed. The Makefile's dependency graph puts the expensive experiment run at the root, and a downstream edit doesn't propagate up.

> [!question]- Why does Make's dependency tracking use mtime, and what can go wrong with mtime-based tracking?
> [!answer]- Make uses mtime (modification time) as a proxy for "is this file newer than that file?" A target is out-of-date iff any prerequisite has a newer mtime. Problems: mtime granularity (FAT32 = 2s), mtime skew after `git checkout` (all files have the checkout time), mtime preservation in `cp -p` (preserves the source's mtime, breaking rebuild expectations), and parallel-build race conditions.

> [!question]- What is the difference between a `client-server` and a `serverless` database architecture?
> [!answer]- **Client-server** (PostgreSQL, MySQL): a separate server process mediates all access; clients connect over a network using a wire protocol. **Serverless / file-based** (SQLite): no server process; the application links the DB library and reads/writes the file directly. Serverless is simpler to reproduce (just copy the file); client-server is more scalable and concurrent.

> [!question]- In the lecture's Docker Compose example, what are the two services and what does each do?
> [!answer]- **db** service: `postgres:16` image, environment `POSTGRES_DB=benchdb`, `POSTGRES_USER=lab`, `POSTGRES_PASSWORD=labpw`, port mapping `5433:5432` (host:container), volume `pgdata:/var/lib/postgresql/data`. **bench** service: same `postgres:16` image (for the `pgbench` binary), depends on `db`, env `PGPASSWORD=labpw`, command runs `pgbench -i` then `pgbench -T 30` to initialise and run a 30-second benchmark.

> [!question]- What is a PostgreSQL foreign table, and when is the file actually read?
> [!answer]- A foreign table is a table-like object whose rows are read on demand from an external source (a file, a remote DB, a web service) through a Foreign Data Wrapper (FDW). The file is *not* read at `CREATE FOREIGN TABLE` time — only when a query is run against the table. This lazy validation is a common source of "the table works, the query fails" surprises.

> [!question]- Why doesn't the `file_fdw` push down `WHERE` predicates?
> [!answer]- `file_fdw` is the basic file-based FDW for CSV/TSV. It reads the *entire* file, then PostgreSQL applies the WHERE clause. There is no index on the file, and the FDW has no way to evaluate predicates during the read. For large CSVs, every query is a full scan. Pushdown requires more sophisticated FDWs (e.g., ` parquet_fdw`, `csv_fdw` with index support).

> [!question]- When is SQLite *not* a good choice for a database?
> [!answer]- (1) High-concurrency server workloads (file-level locking). (2) Very large databases (works up to ~1 TB, but server DBs scale further). (3) Network access (clients need filesystem access; no native network protocol). (4) When you need server-side features like stored procedures, triggers with rich logic, or fine-grained access control. (5) When you need replication or high availability (SQLite has limited replication options compared to PostgreSQL).


---

## Related Resources

### 📖 Reproducibility Engineering - Lecture 5: Reproducible Builds
- Lecture topic: [[reproducibility-engineering-lecture-5]]

**Key concepts covered:**
- [[diffoscope]]
- [[deterministic-builds]]
- [[build-environment-isolation]]
- [[source-date-epoch]]
- [[ci-cd-for-reproducibility]]
- [[containerization-for-builds]]
- [[package-manager-reproducibility]]
- [[make-and-build-systems]]
- [[c-preprocessor]]
