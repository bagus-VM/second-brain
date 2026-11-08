---
title: "Reverse- and Reengineering — Lecture 3: Binaries — ELF, Symbols, Dynamic Linking"
tags: [topic, reverse-and-reengineering, semester-2, lecture, binary-analysis]
course: "Reverse- and Reengineering"
source_count: 2
status: current
last_updated: 2026-11-05
prerequisites: ["[[reverse-and-reengineering-lecture-2]]"]
---

## One-line Summary
From *what a binary is* to *what it leaks*: the executable file format as a first-class analysis
target, the symbol tables as the analyst's best friend, and the load sequence + GOT/PLT machinery as
the reason dynamic linking cannot be stripped away.

## Core Map

```
Reverse- and Reengineering — Lecture 3 (03-binaries.key)
│
├── Slides 00-19: the SAME material as lecture 2, re-presented
│   ├── purposes of reverse engineering, information exploration
│   ├── RE levels, binary analysis, binary reverse engineering
│   ├── static vs dynamic analysis, their tools
│   ├── x86 registers (16/32/64), ISA, ia64 ABI, subregisters, instruction types
│   └── the legal disclaimer
│       → [[reverse-and-reengineering-lecture-2]]
│
├── Slide 20: references (ELF 101, Learning Linux Binary Analysis, Kinder, MS docs)
│
├── Slide 21: the call stack — prologue and epilogue in ia64 form
│   └── mov [RSP+8],RCX / push R15,R14,R13 / sub RSP,0x40 / lea RBP,64[RSP] …
│       → [[x86-assembly-and-abi]]
│
├── THE NEW MATERIAL: the executable file
│   ├── Binary executable formats → ELF / PE / Mach-O / legacy
│   ├── Binary in executables → object files, (static) linking, relocation
│   ├── Loading an executable → the kernel's six-step sequence
│   ├── ELF format → header, Program Header Table, Section Header Table
│   ├── Common sections → .text .data .rodata .bss .plt .got .got.plt .symtab …
│   ├── Segment types → PT_NULL PT_LOAD PT_INTERP PT_TLS PT_DYNAMIC
│   └── ELF symbols + symbol tables → st_name, st_info, st_shndx; .symtab vs .dynsym
│       → [[elf-executable-format]]
│       → [[elf-symbols-and-tables]]
│
├── Dynamic linking in detail
│   ├── the interpreter loads first, sets up recursively from .dynamic
│   │   └── DT_NEEDED / DT_SYMTAB / DT_FLAGS (BIND_NOW)
│   ├── relocations, library initialisers, transfer to the entry point
│   ├── GOT: addresses of globals and external functions
│   ├── PLT: trampolines that jump via GOT
│   └── eager vs lazy linking — when the GOT entry is resolved
│       → [[got-plt-lazy-linking]]
│
├── Slide 33: the summary that is the whole thesis
│   └── "the more metadata can be found, the easier semantics can be inferred"
│
└── Slides 36-38: data acquisition, knowledge organization, RE origin
    └── also repeated from lecture 2
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[elf-executable-format]] | The ELF container in two tables — segments for the loader, sections for the linker — and the six-step sequence the kernel and dynamic loader run before your `main` executes. |
| [[elf-symbols-and-tables]] | What the compiler emits beyond code, and why `.symtab` can be stripped while `.dynsym` cannot. |
| [[got-plt-lazy-linking]] | The two tables that make a call into a shared library possible, and the difference between resolving at load time and resolving at first use. |
| [[x86-assembly-and-abi]] | The register set and ABI material this deck repeats, plus the call-stack slide's exact prologue/epilogue. |
| [[binary-reverse-engineering]] | The static/dynamic analysis ladder, from lecture 2 — repeated verbatim here. |

## What the Deck Actually Is

This is a **Keynote file** (`.key`), not a PDF, and it is the first lecture source in this vault that
had to be opened as a zip archive to be read: a `.key` is a package containing
`Index/Slide-*.iwa` files, one per slide, each a Snappy-compressed IWA blob. The text was recovered
by decompressing each `Slide-*.iwa` and extracting its strings, in slide order. That is why the
page cites "slide 26" style references rather than page numbers: the deck has **39 slides**, in
order, and 13 of them produce no usable text (title slides, images, animation artefacts).

**The PDF export, added 2026-11-05.** `raw/` now also holds `03-binaries.pdf` — the same deck exported
from Keynote (15 pages, produced 2026-10-28, 1024×768, footer numbers 2–15). It contains the new
material of this lecture and none of the lecture-2 recap that the `.key` package carries, so the two
sources are not the same slide set. Its fourteen slides run in the same order as the `.key`'s
new-content block — the PDF's slide 2, "Binary Executable Formats", is the `.key`'s slide 22 — and
the text agrees page for page from there to the summary; the one ordering difference is that the PDF
puts the references at the end (slide 15) where the `.key` has them before the call-stack slide. The
page below therefore keeps the `.key`'s slide numbers and cites the PDF only as corroboration: the
PDF is the cleaner source, the `.key` the complete one.

The deck's own structure is worth stating because it affects how to study it:

- **Slides 00–19** are lecture 2's material, re-shown. Roughly half the deck is revision.
- **Slide 20** is a reading list, and it is the most useful slide in the deck for anyone who wants to
  go deeper: Ignacio Sanmillan and Paul Litvak's *Executable and Linkable Format 101* (two posts on
  intezer.com — one on sections and segments, one on dynamic linking), Ryan O'Neill's *Learning
  Linux Binary Analysis* (Packt, 2016), J. Kinder's *Reverse Engineering* lecture from UBW 2020, and
  the Microsoft Visual Studio 2022 documentation.
- **Slide 21** is the call stack, in the ia64 form, and is the bridge from the ABI material to the
  binary material: the prologue and epilogue shown are what the ELF loader's entry point will be
  executing.
- **Slides 22–34** are the new content: the executable format, its two tables, its sections and
  segments, its symbols, and dynamic linking.
- **Slide 33** is the summary, and it is the deck's thesis: *"Executable files store significant
  metadata alongside binary. Metadata for dynamic linking cannot be stripped. The more metadata can
  be found the easier semantics can be inferred."*
- **Slides 36–38** return to lecture 2's data-acquisition and knowledge-organisation material.

## The Argument That Connects the Three New Pages

Lecture 2 established that decompilation is **undecidable** — reconstructing higher-level constructs
from machine code has no guaranteed-correct procedure — and that the analyst's effort is the
bottleneck that prevents full automation. Lecture 3 is the practical answer to that: *you do not
have to reconstruct everything from the instructions, because the file format carries structured
metadata that says a great deal for free.*

The chain, in the deck's own order:

1. **The container tells you what kind of thing you have.** The ELF header declares 64-bit vs
   32-bit, endianness, OS ABI and instruction set at fixed offsets from a four-byte magic number
   (`0x7f 'E' 'L' 'F'`). Before a single instruction is decoded, the architecture is known.
2. **The section header table tells you where to look.** `.text` is code, `.rodata` is constants,
   `.data` is initialised data, `.bss` is uninitialised, `.plt` and `.got` are the calling
   machinery. A string found in `.rodata` is a constant; the same bytes in `.text` might be
   anything.
3. **The symbol table, if present, tells you what things are called.** `.symtab` holds names for
   functions and objects; `.dynsym` holds the ones dynamic linking needs. The slide's summary line
   for a stripped binary is a *degradation gradient*: metadata can be removed, and what cannot be
   removed (`.dynsym`) is therefore where an analyst looks first.
4. **The dynamic-linking metadata tells you what the program depends on.** `.dynamic` holds
   `DT_NEEDED` entries naming the libraries, which names the subsystems the program uses without
   reading a single call site.
5. **Only then do the instructions need to be read**, and even then the `PLT`/`GOT` pair says which
   calls go outside the binary.

This is why [[binary-reverse-engineering]]'s claim that "system-level metadata is a first-class
information source" is not a sidebar: it is the reason the whole task is tractable in practice.

## Exam-Relevant Points

1. **Both tables, and why there are two.** The Program Header Table describes *segments* and is what
   the loader uses; the Section Header Table describes *sections* and is what the linker uses. All
   segments other than `PT_LOAD` are mapped into a `PT_LOAD`. Segments and virtual addresses must be
   aligned to the page size.
2. **The load sequence, in order.** New OS process; program image loaded into its memory; runtime
   dependencies resolved recursively; relocation (absolute and relative virtual addresses patched,
   imported-function addresses resolved); shared-library initialisation functions invoked; jump to
   the entry point.
3. **`.symtab` is removable, `.dynsym` is not.** Unless nothing is dynamically linked — which is why
   a fully static binary is a harder target, and why stripping is a first, cheap anti-analysis move
   that the format itself limits.
4. **Two symbol tables maximum per ELF object**, each with its own string table (`.strtab` for
   `.symtab`, `.dynstr` for `.dynsym`).
5. **GOT holds addresses, PLT holds trampolines.** The PLT entry jumps *via* the corresponding GOT
   entry; in lazy linking that entry initially points at the dynamic linker, and is rewritten on
   first use.
6. **`DT_NEEDED`, `DT_SYMTAB`, `DT_FLAGS`** are the three `.dynamic` entries the slide names, with
   `BIND_NOW` as the `DT_FLAGS` example — the eager-binding flag.
7. **Platform variants:** ELF (Unix System V Release 4 origin; Linux, Unix variants, consoles, mobile
   phones), PE (Windows, and also UEFI as BIOS's successor), Mach-O (Mac), and the legacy `com`,
   DOS `MZ`, `a.out` and `COFF`.
8. **Tools:** `readelf -h` (header), `readelf -l` (segments), `readelf -d` (dynamic entries),
   `elfutils`, `objdump`, `file`.

## Connections

- [[reverse-and-reengineering-lecture-2]] — the prerequisite lecture: the abstraction ladder, static
  and dynamic analysis, x86 and the ABI. Half of this deck is that lecture again.
- [[reverse-and-reengineering-exercise-3]] — Homework 3, which exercises the x86 material the deck
  opens with.
- [[reverse-and-reengineering]] — the course page.
- [[dynamic-linking]] — the Virtual Machines course's treatment of the same mechanism from the
  library-user's side: `dlopen`, `-fPIC`, `mmap`, `LD_LIBRARY_PATH`. The two pages are complementary;
  that one is about *using* dynamic linking, these are about *reading* it.
- [[process-memory-layout]] — where the loaded segments end up.
- [[runtime-system]] — the C runtime system, whose initialisation is the last step of the load
  sequence.
- [[x86-assembly-and-abi]] — the prologue/epilogue on slide 21.
- [[static-vs-dynamic-analysis]] — the two analysis modes the ELF metadata feeds.
- [[reengineering]] — where binary recovery leads: the restructuring and forward-engineering half of
  the course.

## Open Questions

- **The deck never states which compiler or platform produced its ELF examples.** The section list
  and segment types are generic ELF, but the tool examples mix Unix tools (`readelf`, `objdump`) with
  Windows tools (`PEiD`, `PeStudio`), so the course is teaching both formats without naming a target
  platform. Which one the exam will ask about is not indicated.
- **Slide 28 ("Binary Loading with Segments and Sections") is an image and produced no text.** Its
  annotations survive — *"Segments and virtual addresses must be aligned to page size!"* and a
  `decimal` label — but the diagram itself does not. The page describes the relationship from the
  surrounding slides; the specific figure is not recoverable.
- **Slide 31 ("Symbols Example") also produced no usable text**, only fragments. So the deck lists
  the `st_*` fields and the two tables but shows no worked symbol-table dump. The worked example on
  [[elf-symbols-and-tables]] is built from the field definitions rather than from the slide's own
  figure.
- **No slide describes how obfuscation or packing interacts with this metadata.** Lecture 2's content
  list mentions "effects of obfuscation techniques", and the ELF/PLT structure here is exactly what a
  packer rewrites — but the deck does not draw the connection.
- **The `.key` format means the deck's animation stages are lost.** Where a slide animates (the
  Symbol Table slide carries several `$GUID` artefacts), the intermediate frames may have carried
  content that a single-pass string extraction cannot order. The extracted text is complete for the
  final state of each slide, which is what the page uses.
- **`PT_TLS` is listed as "common in statically linked binaries"**, which is the slide's own note and
  is the kind of claim that is worth checking against `readelf` on a real binary; the deck gives no
  example.
