---
title: "Exercise Sheet 11: Reproducible Experiment Workflows"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-17
---

# Exercise Sheet 11: Reproducible Experiment Workflows

## 2 Multi-Stage Builds

### 2.1 The Single-Stage Image

> [!note]- Solution
> Build and check size:
>
> ```bash
> cd LabSession11/multistage
> docker build -f Dockerfile.singlestage -t mentos-singlestage .
> docker images mentos-singlestage
> ```
>
> The image is based on `gcc:14`, which carries the entire GCC toolchain (compiler, linker, libc headers, make, etc.). The resulting image is roughly 1.2 GB.

### 2.2 The Multi-Stage Image

> [!note]- Solution
> Write a multi-stage `Dockerfile`:
>
> ```dockerfile
> FROM gcc:14 AS builder
> WORKDIR /src
> COPY mentos.c .
> RUN gcc -O2 -static -o mentos mentos.c -lm
>
> FROM scratch
> COPY --from=builder /src/mentos /mentos
> ENTRYPOINT ["/mentos"]
> ```
>
> Build and compare:
>
> ```bash
> docker build -t mentos-multistage .
> docker images | grep mentos
> ```
>
> Test:
>
> ```bash
> docker run --rm mentos-multistage > measurements.csv
> ```
>
> **Size comparison:** The single-stage image is ~1.2 GB (full GCC toolchain). The multi-stage image is ~100 KB (just the statically linked binary on `scratch`). The image shrinks by roughly 99.9%.
>
> **Why:** The multi-stage build has two stages. The `builder` stage (based on `gcc:14`) compiles the binary, then discards the entire toolchain. The runtime stage (`scratch`, the empty image) copies only the compiled binary. The toolchain never ships in the final image.
>
> **Key properties of this approach:**
> - The binary is **statically linked** (`-static`), so it has zero runtime dependencies. It can run on `scratch` (an image with no OS, no libc, nothing).
> - The binary is **bitwise identical** in both images -- same source, same compiler, same flags.
> - In the single-stage image you can call `gcc` to recompile; in the multi-stage image you cannot (no compiler in the runtime stage).
> - The single-stage image contains `mentos.c` (it was copied in); the multi-stage image does not (the source was only in the build stage, and `scratch` has no filesystem beyond what you copy in).

## 3 Working with Remote Containers

### 3.1 Setting up the "Remote" Server

> [!note]- Solution
> ```bash
> cd LabSession11/remote
> docker build -f Dockerfile.remote -t lab11-remote .
> docker run --rm -d -p 2222:22 --name lab11-remote lab11-remote
> ```
>
> The container runs an SSH server (`sshd`) on port 22, published to the host on port 2222. We don't connect to it directly from the host -- instead, the build container (next task) connects to it over the network.

### 3.2 Building and Shipping the Experiment Execution Package

> [!note]- Solution
> Build the builder container and start it with host networking:
>
> ```bash
> docker build -f Dockerfile.builder -t lab11-experiment-builder .
> docker run --rm -it --network host lab11-experiment-builder
> ```
>
> Inside the builder container, the experiment is already compiled (the Dockerfile compiles `mentos.c` to a static binary and strips it). Bundle and ship:
>
> ```bash
> repro@builder$ tar -czf experiment.tar.gz package
> repro@builder$ scp -P 2222 experiment.tar.gz repro@localhost:~/
> ```
>
> Password: `repro`
>
> This is the **experiment execution package** pattern from [[reproducibility-engineering-lecture-10|Lecture 10]]: build in a controlled environment, ship a self-contained binary to the target machine, run it there.

### 3.3 Running an Experiment that Survives Disconnects

> [!note]- Solution
> Connect to the remote server, unpack, and run inside `tmux`:
>
> ```bash
> repro@builder$ ssh -p 2222 repro@localhost
> repro@remote$ tar -xzf experiment.tar.gz
> repro@remote$ cd package
> repro@remote$ chmod +x mentos dispatch.sh
> repro@remote$ tmux new -s mentos
> repro@remote$ ./dispatch.sh
> ```
>
> Detach: `Ctrl-b`, then `d`. Log out: `exit`.
>
> Reconnect and reattach:
>
> ```bash
> repro@builder$ ssh -p 2222 repro@localhost
> repro@remote$ tmux a
> ```
>
> The experiment is still running (or finished). `tmux` keeps the session alive independently of the SSH connection. This is critical for long-running experiments: if you ran the experiment directly in an SSH session, closing the connection would send SIGHUP and kill the process.
>
> After the experiment finishes, detach again (`Ctrl-b`, `d`).

### 3.4 Inspecting the Recorded Environment

> [!note]- Solution
> ```bash
> repro@remote$ cd package/out/config
> repro@remote$ ls
> repro@remote$ cat hostname os-release
> ```
>
> The dispatcher (`dispatch.sh`) records:
> - `hostname` -- the machine's name (identifies which server ran the experiment)
> - `os-release` -- the OS distribution and version (e.g., Ubuntu 24.04)
> - Kernel config (`kconfig.gz`), boot command line (`cmdline`), CPU info (`cpuinfo`), loaded modules (`modules`), cgroup info (`cgroups`)
>
> For a real experiment, `os-release` is the most important record -- it tells you the exact OS and version, which affects library versions, kernel behavior, and compiler defaults. The hostname identifies the machine but doesn't describe its software environment. CPU info matters for performance-sensitive experiments (floating-point behavior varies across architectures).

### 3.5 Collecting the Results and Analyzing Them Locally

> [!note]- Solution
> Bundle results on the remote machine:
>
> ```bash
> repro@remote$ tar -czf results.tar.gz out
> repro@remote$ exit
> ```
>
> Copy back to the builder:
>
> ```bash
> repro@builder$ scp -P 2222 repro@localhost:~/package/results.tar.gz .
> ```
>
> Note: `ssh` uses lowercase `-p` for port; `scp` uses uppercase `-P`.
>
> Analyze in the builder container:
>
> ```bash
> repro@builder$ tar -xzf results.tar.gz
> repro@builder$ python3 plot.py
> ```
>
> This writes `out/measurements.png`. The analysis runs in the same containerized environment as the build, so the analysis step is also reproducible.
>
> The `README.md` should describe:
> - What the experiment measures (Mentos-and-cola eruption heights)
> - The machine environment (from `out/config/`)
> - The results (the chart and CSV data)
>
> Stop the server when done:
>
> ```bash
> docker stop lab11-remote
> ```

## 4 Storing and Inspecting Experimental Data in HDF5

### 4.1 Preparation

> [!note]- Solution
> ```bash
> cd LabSession11/hdf5
> docker build -t lab11-hdf5 .
> docker run -it lab11-hdf5
> ```
>
> The container includes `h5ls`, `h5dump`, and `python3` with `h5py`.

### 4.2 Writing an HDF5 File

> [!note]- Solution
> Write `store.py`:
>
> ```python
> import csv
> import h5py
>
> # Read CSV
> data = {}
> with open("measurements.csv", newline="") as fh:
>     for row in csv.DictReader(fh):
>         key = (row["flavor"], row["cola"])
>         data.setdefault(key, []).append(
>             [int(row["mentos"]), float(row["height_cm"])]
>         )
>
> # Write HDF5
> with h5py.File("measurements.h5", "w") as f:
>     for (flavor, cola), rows in data.items():
>         grp = f.create_group(f"meas/{flavor}")
>         ds = grp.create_dataset(cola, data=rows)
>         ds.attrs["columns"] = ["mentos", "height_cm"]
> ```
>
> The structure mirrors the experiment:
> ```
> meas/
>   fruit/
>     cola   -> Dataset {8, 2}
>     diet   -> Dataset {8, 2}
>     zero   -> Dataset {8, 2}
>   mint/
>     cola   -> Dataset {8, 2}
>     diet   -> Dataset {8, 2}
>     zero   -> Dataset {8, 2}
> ```
>
> Each dataset is a 2D array with 8 rows (one per Mentos count) and 2 columns (mentos count, eruption height).

### 4.3 Inspecting the File You Created

> [!note]- Solution
> **(a)** List the object tree:
>
> ```bash
> h5ls -r measurements.h5
> ```
>
> Output shows the full hierarchy: `/meas` (Group), `/meas/fruit` (Group), `/meas/fruit/cola` (Dataset {8, 2}), etc. The hierarchy matches the requested structure -- one group per flavor, one dataset per cola type, nested under `meas`.
>
> **(b)** Dump one dataset:
>
> ```bash
> h5dump -d /meas/fruit/cola measurements.h5
> ```
>
> - The `columns` attribute contains `["mentos", "height_cm"]` (stored as a variable-length UTF-8 string array).
> - The dataset shape is `{8, 2}` -- 8 rows, 2 columns.
> - The datatype is native double (`float64`), since h5py infers float64 from Python floats.
>
> **(c)** Header-only dump:
>
> ```bash
> h5dump -H measurements.h5
> ```
>
> `h5dump -H` shows the structure and metadata (group names, dataset shapes, datatypes, attributes) **without** printing the actual data values. `h5ls -r` shows the tree structure and dataset shapes but does **not** show attributes. So `h5dump -H` reveals attribute values (like `columns = ["mentos", "height_cm"]`) that `h5ls -r` hides.

### 4.4 Reading the Data back in Python

> [!note]- Solution
> Write `read.py`:
>
> ```python
> import h5py
>
> with h5py.File("measurements.h5", "r") as f:
>     ds = f["meas/mint/diet"]
>     print("columns:", ds.attrs["columns"])
>     print(ds[:])
> ```
>
> Output:
> ```
> columns: ['mentos' 'height_cm']
> [[  1.   35. ]
>  [  2.   53.1]
>  [  3.   67.7]
>  [  4.   80.4]
>  [  5.   91.9]
>  [  6.  102.6]
>  [  7.  112.5]
>  [  8.  121.9]]
> ```
>
> `ds[:]` reads the entire dataset into a NumPy array. The `columns` attribute documents what each column means.

## 5 Reproducible Workflows (Multiple Choice)

> [!note]- Solution
> **(a)** How many statements about the single-stage and multi-stage images are true?
>
> | Statement | Verdict |
> |-----------|---------|
> | (i) The multi-stage image is smaller | **TRUE** -- scratch has nothing; single-stage carries gcc |
> | (ii) You can call gcc in the single-stage image, not in multi-stage | **TRUE** -- gcc is in the single-stage image; scratch has no tools |
> | (iii) `./mentos` only runs in the single-stage image | **FALSE** -- the binary runs in both (it's statically linked) |
> | (iv) The binary is bitwise identical in both images | **TRUE** -- same source, same compiler, same flags, same output |
> | (v) Both images contain `mentos.c` | **FALSE** -- the multi-stage image copies only the binary to scratch; the source stays in the discarded build stage |
>
> **Answer: 3** (statements i, ii, iv are true)
>
> ---
>
> **(b)** How many statements about `results.h5` are true?
>
> | Statement | Verdict |
> |-----------|---------|
> | (i) Contains three datasets | **TRUE** -- run1, run2, run3 are all datasets |
> | (ii) Each run stores 120 × 2 = 240 values | **TRUE** -- shape `{120, 2}` means 120 rows × 2 columns = 240 values |
> | (iii) `/experiment` is a group, runs are nested inside | **TRUE** -- h5ls shows `/experiment` as Group with three Dataset children |
> | (iv) Each run stores 120 values, 2 missing (NaN) | **FALSE** -- shape `{120, 2}` means 120 rows and 2 columns, not 122 values with 2 missing |
> | (v) Runs hold floating-point numbers with 2 decimal places | **FALSE** -- the `2` in `{120, 2}` is the number of columns, not decimal places. HDF5 shape says nothing about precision |
>
> **Answer: 3** (statements i, ii, iii are true)
>
> ---
>
> **(c)** How many statements about HDF5 vs JSON for 50 GB of numerical data are true?
>
> | Statement | Verdict |
> |-----------|---------|
> | (i) JSON has an index for jumping to specific runs | **FALSE** -- JSON is plain text with no index; you must parse from the start |
> | (ii) HDF5 lets you read a single run without loading the whole file | **TRUE** -- HDF5 supports chunked storage and direct slice access |
> | (iii) JSON is typically larger than HDF5 for numerical data | **TRUE** -- JSON stores numbers as text (e.g., `3.14159` = 7 bytes); HDF5 stores them as binary (8 bytes for float64, but much less for int8/int16, and compression reduces further) |
> | (iv) HDF5 can store images | **TRUE** -- HDF5 datasets can hold arbitrary n-dimensional arrays, including image pixel data |
> | (v) JSON can store images | **TRUE** -- as base64-encoded strings or as arrays of pixel values. Not efficient, but possible |
>
> **Answer: 4** (statements ii, iii, iv, v are true)

## Related Lectures
- [[reproducibility-engineering-lecture-10]] -- remote experiment workflows and artifact packaging
- [[reproducibility-engineering-lecture-8]] -- HDF5, JSON, XML hierarchical data formats
- [[multi-stage-docker-build]] -- concept page for multi-stage builds
- [[hdf5]] -- concept page for HDF5
- [[containerization-for-builds]] -- Docker for build isolation
