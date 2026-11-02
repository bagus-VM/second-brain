---
title: "GOT, PLT and Lazy Linking"
tags: [concept, reverse-and-reengineering, semester-2, elf, dynamic-linking]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-29
prerequisites: ["[[elf-executable-format]]", "[[dynamic-linking]]"]
---

## One-line Summary
A call to an external function goes through a Procedure Linkage Table stub that jumps via a Global Offset Table slot, and the dynamic linker fills that slot either at load time (eager linking) or on first use, when the slot initially points back at the dynamic linker itself (lazy linking).

## Core Intuition
A dynamically linked function call is not a direct call. The compiler does not know where `printf` lives, so it emits an indirect jump through a two-level table: the PLT entry is a short trampoline that jumps through the corresponding GOT slot, and the GOT slot is writable so the loader can put the real address there (slide 34). That indirection is the price of position-independent, run-time-resolved code — and it is also what makes the mechanism deferrable.

The deferral is the point. Under lazy linking the GOT slot does not start at the target function's address; it points back into the dynamic linker, and the first call through it triggers the resolution, after which the slot is overwritten with the real address and every later call is a plain indirect jump (slide 34). Under eager linking all GOT entries are relocated at load time, so no first call is special (slide 34). The switch is `DT_FLAGS` with the `BIND_NOW` flag, read from `.dynamic` when the interpreter sets up the process (slide 32).

None of this is hidden from the analyst. Slide 33 states the consequences: executables store significant metadata alongside the binary, metadata for dynamic linking cannot be stripped, and the more metadata can be found the easier the semantics can be inferred. That is why a reverse engineer reads the ELF header and the dynamic section first: the loader's own bookkeeping names the libraries, names the imported functions, and shows where each call is patched.

## Formal Definition / Statement
Slide 32 ("Dynamic Linking") describes the dynamic linker, called the **interpreter**: it is loaded first; it sets up its environment recursively using entries from the `.dynamic` section — `DT_NEEDED` (name of a required dependency to load), `DT_SYMTAB` (address of the dynamic symbol table), `DT_FLAGS` (e.g. the `BIND_NOW` flag); it performs relocations; it loads the main executable and its (eager) dependencies and invokes library initialization(s); finally it transfers control to the executable's entry point.

Slide 34 ("Lazy Linking") defines the two tables and the two policies:

- **Resolve function references only when needed** — the definition of lazy linking.
- **Global Offset Table (GOT)** — addresses of global variables and external functions.
- **Procedure Linkage Table (PLT)** — short entries of instructions (trampolines, thunks) that jump to the corresponding GOT entry.
- **Eager linking** — GOT entries relocated at load time.
- **Lazy linking** — the GOT entry is determined, through loading of the library, and relocated at first use; initially the GOT entry points to the dynamic linker.

Slide 26 places these in the section map: `.plt` is the Procedure Linkage Table (the IAT equivalent), `.got` holds GOT entries for dynamically linked global variables, `.got.plt` holds GOT entries for dynamically linked functions, `.dynamic` holds all needed information for dynamic linking, `.rel.dyn` is the global variable relocation table, `.rel.plt` the function relocation table, and `.interp` embeds the RTLD string. Slide 27 adds that `PT_INTERP` holds `.interp` and `PT_DYNAMIC` holds `.dynamic`, so the interpreter path and the dynamic metadata are themselves segments of the same file.

## Key Properties
- **Two indirections in series.** A PLT entry jumps through a GOT slot, so the call target is data the loader can rewrite (slide 34).
- **The GOT holds addresses**, for global variables (`.got`) and external functions (`.got.plt`) (slides 26, 34).
- **The PLT holds code** — short entries the slide calls trampolines, or thunks (slide 34).
- **Eager versus lazy is one policy switch.** Eager relocates all GOT entries at load time; lazy relocates each on first use, with the slot initially pointing at the dynamic linker (slide 34).
- **`BIND_NOW` is the eager toggle**, carried in `DT_FLAGS` and read from `.dynamic` (slide 32).
- **Resolution is recursive.** `DT_NEEDED` names the dependencies to load (slide 32).
- **Control is transferred last.** The interpreter loads, relocates, calls library initialisers, then jumps to the entry point (slide 32).
- **The metadata is permanent.** Dynamic-linking metadata cannot be stripped, so imports, dependency names and relocation tables survive any stripping pass (slide 33).

## Worked Example
```sh
$ readelf -d /bin/ls
Dynamic section at offset 0x2ddc8 contains 29 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libselinux.so.1]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x0000000000000006 (SYMTAB)             0x...      <- DT_SYMTAB
 0x000000000000001e (FLAGS)              BIND_NOW
```

The lazy path is visible in the disassembly of a PLT stub:

```asm
0000000000001030 <puts@plt>:
    1030: ff 25 e2 2f 00 00   jmp QWORD PTR [rip+0x2fe2]   # 0x4018 -> .got.plt[3]
    1036: 68 00 00 00 00      push 0x0                     # relocation index
    103b: e9 e0 ff ff ff      jmp 1020 <_init+0x20>        # PLT0, the resolver
```

`ff 25 disp32` is the five-byte indirect jump through RIP-relative memory; `0x4018` is the `puts` slot in `.got.plt`. Under lazy linking that slot is initialised to `0x1036`, the second instruction of the stub itself: the first call lands on `push 0x0`, which pushes the relocation index and jumps to `PLT0`, the resolver that calls the dynamic linker. The linker looks the symbol up in `.dynsym` at the `DT_SYMTAB` address, finds `puts` in the library named by `DT_NEEDED`, and writes the real address into `.got.plt[3]`. Every later call takes the `jmp` straight to the resolved function and never touches `0x1036` again. Under eager linking the slot already holds the real address on entry, because `BIND_NOW` told the interpreter to relocate everything at load time (slides 32, 34). `readelf -r` prints the patch list; on x86-64 the relocations slide 26 calls `.rel.dyn` and `.rel.plt` appear as the RELA sections `.rela.dyn` and `.rela.plt`.

## Common Pitfalls
- **Reading the PLT jump and stopping there.** The first `jmp [rip+...]` in a lazy stub goes to the *next* instruction until the slot is patched; the second call does not.
- **Assuming the GOT is read-only.** It must be writable for relocation, which is why `.got.plt` needs write access while `.text` needs read-execute (slide 25).
- **Conflating `.got` and `.got.plt`.** Slide 26 splits them: `.got` serves global variables, `.got.plt` serves functions.
- **Expecting `.rel.dyn` / `.rel.plt` to match the file.** On x86-64 `readelf` prints the RELA variants `.rela.dyn` / `.rela.plt`.
- **Forgetting the interpreter is not the kernel.** The interpreter is loaded first, does the recursive dependency setup and relocation, then transfers control (slide 32).
- **Treating lazy and eager as behaviourally identical.** Lazy defers work to first call and leaves each slot pointing at the resolver until then (slide 34).
- **Assuming imports can be hidden.** Dynamic-linking metadata cannot be stripped, so `DT_NEEDED`, `.dynsym` and the relocation tables are readable (slide 33).

## Connections
- [[elf-executable-format]] — the `.plt`, `.got`, `.got.plt`, `.dynamic` and `.interp` sections and the `PT_DYNAMIC`/`PT_INTERP` segments this page uses.
- [[elf-symbols-and-tables]] — `.dynsym`/`.dynstr` are what the resolver searches for the `UND` symbol.
- [[dynamic-linking]] — the course-neutral treatment of shared objects, `ld.so`, `-fPIC` and `mmap`.
- [[process-memory-layout]] — where the shared libraries and the writable GOT land in the address space.
- [[runtime-system]] — the library initialisers invoked before the entry point.
- [[binary-reverse-engineering]] — the system-level metadata reading this mechanism rewards.
- [[static-vs-dynamic-analysis]] — the relocation tables are static metadata about run-time behaviour.
- [[reverse-and-reengineering-lecture-2]] — the lecture that supplies slides 00–19 and 36–38 of this deck.

## Open Questions
- **The slide never shows the resolver.** Slide 34 says the initial GOT entry points to the dynamic linker, but neither slide 32 nor 34 names the code that performs the first-use resolution.
- **`.dynamic` is sampled, not enumerated.** `DT_NEEDED`, `DT_SYMTAB` and `DT_FLAGS` are the only entries listed (slide 32).
- **No cost model is given for eager versus lazy.** The slides do not say which is faster overall or when each is chosen.
- **The `.interp` description is garbled in the extraction.** Slide 26 annotates it as "RTLD embedded string", a truncated note the deck does not explain.
- **The relocation names are not reconciled with tool output.** The slides say `.rel.dyn` and `.rel.plt`, while x86-64 binaries carry RELA relocations.
