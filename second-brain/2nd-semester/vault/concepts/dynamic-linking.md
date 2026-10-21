---
title: "Dynamic Linking"
tags: [concept, virtual-machines, semester-2, linking]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-19
prerequisites: ["[[process-memory-layout]]"]
---

## One-line Summary
Static libraries are copied into the binary at link time; dynamic libraries are separate objects mapped into the process's `mmap` area at run time — by `ld.so` at startup, or by `dlopen` whenever you like.

## Core Intuition
The question is *when* the code becomes part of your program. Static: at link time, one copy per binary. Dynamic: at run time, one copy in physical memory shared by every process that maps it, with the address chosen by the loader — which is why `-fPIC` and relocation tables exist.

## Formal Definition / Statement

**Libraries (s02):** almost every program uses at least the C library. Two varieties:
- **static libraries** are integrated at compile time — more precisely, at **linking time** — into the program binary;
- **dynamic libraries** ("shared objects") are combined with the program code only at **run time** (when the program is started, or even later).

**Compilation pipeline:**

```
1 compilation:  file.c  → file.s      gcc -S -o file.s file.c
2 assembly:     file.s  → file.o      gcc -c -o file.o file.s
3 link:         file.o  → file        gcc -o file file.o
                file.o  → libMYLIB.a  ar r libMYLIB.a file.o          (static)
                file.o  → libMYLIB.so gcc -shared -fPIC -o libMYLIB.so file.o
```

The `gcc` frontend calls `cpp`, `cc1`, `as` and `ld` as needed.

**Linker flags:** `-Lpath` looks for libraries in `path`; `-lbib` uses `libbib.a` or `libbib.so`. For dynamic libraries additionally `-rpath path` — where to look at run time. `LD_LIBRARY_PATH` is the environment variable searched for shared objects at start-up.

**Dynamic loading (`libdl`):**

```c
void *dlopen(const char *libname, int flags);
int   dlclose(void *handle);
void *dlsym(void *handle, const char *symname);
char *dlerror(void);
```

`dlopen` returns a handle identifying the library when non-NULL. Flags: `RTLD_LAZY` (resolve symbols only when needed), `RTLD_NOW` (resolve at once), `RTLD_GLOBAL` (symbols available to libraries loaded later), `RTLD_LOCAL` (symbols not visible outside). **`dlsym` may legitimately return NULL** — a symbol's address can be NULL — so NULL is *not* a reliable error indicator; call `dlerror()` instead, clearing it before the lookup.

**`ld.so`:** loading is not done by the kernel but by the dynamic loader, whose path is hard-coded in the ELF section `interp` (e.g. `/lib64/ld-linux-x86-64.so.2` on x86_64 Linux). It reads the program's dynamic-library information and assigns each library an address. Because that address is not fixed, libraries should be **position independent code** (`-fPIC`), using only relative addressing; non-PIC code must be patched by the loader via the binary's **relocation tables**.

**`mmap`:**

```c
void *mmap(void *addr, size_t length, int prot,
           int flags, int fd, off_t offset);
```

Maps `length` bytes from `offset` of file `fd`. `addr` is only a wish (often NULL); the real address is returned. `prot` gives access rights (`PROT_READ`, `PROT_WRITE`). `flags` includes `MAP_SHARED` (several processes can access the area) and `MAP_PRIVATE` (no sharing — a write copies the page, "copy on write"). `offset` must be a multiple of the page size.

## Key Properties

- **Three ways to find a library at run time:** `LD_LIBRARY_PATH` (environment), `-rpath` (baked into the binary), `dlopen` (explicit, any time after start).
- **Sharing is the point.** One physical copy serves many address spaces, unlike static libraries, which are copied into every binary.
- **Placement.** Libraries land in the `mmap` area between heap and stack, together with explicitly created mappings.

## Worked Example

```c
/* product.c */
int product(int a, int b) { return a*b; }

/* main.c */
int product(int a, int b);
int main(void) { printf("4*5 = %d\n", product(4,5)); return 0; }
```

```sh
# (a) dynamic, found via LD_LIBRARY_PATH
gcc -fPIC -shared -o libproduct.so product.c
gcc -o main main.c -L. -lproduct
export LD_LIBRARY_PATH=.
./main

# (b) dynamic, path baked in with rpath
gcc -o main main.c -L. -lproduct -Wl,-rpath,.
./main

# (c) not linked at all — loaded at run time
void *hdl = dlopen("libproduct.so", RTLD_LAZY);
double (*f)(double) = dlsym(hdl, "sin");   /* libm example from the slide */
```

Exercise 1 runs the same three modes on `addrs.c`; `-Wl,-rpath,.` is needed even for `dlopen` to find the library. Exercise 2 turns (c) into a **primitive JIT**: write the expression into a C file as `double f(void) { return <input>; }`, compile it with `gcc -fPIC -shared` via `system()`, `dlopen` and call `f` — compilation as a run-time service.

## Common Pitfalls

- **Checking `dlsym`'s result for NULL.** Use `dlerror()`; NULL can be a valid address.
- **Forgetting `-fPIC`.** The library may still load, but only after relocation patching — or not at all.
- **Expecting static and dynamic builds to behave identically.** Different addresses, different symbol resolution — what the exercise asks you to observe.

## Connections

- [[process-memory-layout]] — the `mmap` area and why the heap/stack gap is useful.
- [[runtime-system]] — the C library is the default shared object every process loads.
- [[virtualization-vs-abstraction]] — mapping one physical library into many address spaces is virtualization of memory in action.
- [[virtual-machines-and-runtime-systems]] — course index.

## Open Questions

- `RTLD_LAZY` resolves symbols "only when needed" — is that ever slower overall than `RTLD_NOW`? The lecture gives no numbers.
- The saving from shared libraries depends on page-level sharing, which the slide asserts without quantifying.
