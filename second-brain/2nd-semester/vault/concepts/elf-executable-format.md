---
title: "The ELF Executable Format"
tags: [concept, reverse-and-reengineering, semester-2, elf, executable-formats]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-29
prerequisites: ["[[binary-reverse-engineering]]", "[[x86-assembly-and-abi]]"]
---

## One-line Summary
ELF is the Unix executable container: a header carrying the magic bytes `7f 45 4c 46` plus the machine, word size, endianness and ABI description, a program header table of loadable segments the operating system maps into memory when a program starts, and a section header table of named sections that linkers and reverse-engineering tools read without running the binary.

## Core Intuition
With only a binary in hand, the format is the first thing readable without executing anything. Slide 22 calls the executable format the "natural candidate for static analysis of target binary": you must identify the machine code to run and the other artifacts, plus the metadata — libraries and functions referenced at runtime, and potentially exported functionalities. The format is platform dependent: ELF (Unix System V Release 4; Linux, Unix variants, game consoles, mobile phones), PE (Windows, also UEFI), Mach-O (Mac) and the legacy com, dos MZ, a.out and COFF.

One file carries two overlapping tables for two readers. The program header table answers "how does this get into memory" — it lists segments, the units the loader maps. The section header table answers "how is this organised for linking and reading" — it lists named sections. Both address the same bytes at different granularity, and reading the header first tells you which machine, word size and endianness the rest of the bytes assume.

## Formal Definition / Statement
Slide 25 ("ELF Format") presents ELF as cross-platform. The header begins with `0x7f ELF` and defines 32- and 64-bit class, endianness, OS ABI, ISA, pointer sizes, and the size and number of program header table entries.

- **Program Header Table** — the segments of the executable: loadable segment, dynamic linking info, interpreter info, thread-local storage.
- **Section Header Table** — the sections important for linking and execution; it provides a mapping to virtual memory, covering program, symbols, strings, dynamic linking info, constructors and destructors, with examples `.text` (read-execute), `.data` (read-write) and no-load sections.

Slide 27 lists the segment types: `PT_NULL` (unassigned, usually the first entry), `PT_LOAD` (loadable; **all others are mapped into one of these**), `PT_INTERP` (holds `.interp`), `PT_TLS` (thread-local storage, common in statically linked binaries) and `PT_DYNAMIC` (holds `.dynamic`). Segments usually differ in access attributes; `readelf -l <exec>` shows them.

Slide 26 lists the common sections: `.text` (code), `.data` (initialised data), `.rodata` (initialised read-only data), `.bss` (uninitialised data), `.plt` (Procedure Linkage Table, the IAT equivalent), `.got` (GOT entries for dynamically linked global variables), `.got.plt` (GOT entries for dynamically linked functions), `.symtab` (global symbol table), `.dynamic` (all information needed for dynamic linking), `.dynsym` (symbol table for dynamically linked symbols), `.strtab` (string table of `.symtab`), `.dynstr` (string table of `.dynsym`), `.interp` (the RTLD embedded string), `.rel.dyn` (global variable relocation table) and `.rel.plt` (function relocation table).

Slide 28 states the alignment rule: **segments and virtual addresses must be aligned to page size.** Slide 23 gives the build chain: source compiles to object files (`.o`/`.obj`); (static) linking integrates them into the executable with the stated goal — **relocation of code and data in virtual memory** — and the dynamic linker must load external libraries into a shared memory space. Slide 24 gives the load sequence: creation of a new OS process; loading of the program image into its memory; (recursive) resolving of runtime dependencies; relocation — patching absolute and relative virtual addresses and resolving imported function addresses; invoking shared library initialization functions; jump to the entry point. On Windows, `Start`/`MainCRTStartup` calls `main`/`WinMain`.

## Key Properties
- **Magic first.** A file is ELF if its first four bytes are `7f 45 4c 46`; the next bytes give class, endianness and OS ABI (slide 25).
- **Two tables, one file.** Segments serve the loader; sections serve linking and analysis; `.text` is read-execute, `.data` read-write, some sections no-load (slide 25).
- **`PT_LOAD` is the container.** Every other segment type is mapped inside a loadable segment (slide 27).
- **Page-size alignment is mandatory**, which is what lets the kernel map file contents page by page (slide 28).
- **Metadata is free information** — imports, functions and exports are readable without running the binary (slide 22).
- **Slides 00–19 and 36–38 of this deck repeat lecture 2** and are already covered by [[reverse-and-reengineering-lecture-2]], [[binary-reverse-engineering]] and [[x86-assembly-and-abi]].

## Worked Example
```sh
$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, dynamically linked,
         interpreter /lib64/ld-linux-x86-64.so.2
$ readelf -h /bin/ls
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  OS/ABI:                            UNIX - System V
  Type:                              DYN (Position-Independent Executable)
  Machine:                           Advanced Micro Devices X86-64
  Entry point address:               0x5b20
  Start of program headers:          64 (bytes into file)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Number of section headers:         31
```

Those printed fields are the header bytes. In the standard 64-bit ELF layout the offsets are `0x00` `e_ident[16]` (first four bytes `7f 45 4c 46`), `0x04` `EI_CLASS` (`0x02` = ELF64), `0x05` `EI_DATA` (`0x01` little endian), `0x07` `EI_OSABI` (`0x00` System V), `0x10` `e_type` (`0x03` ET_DYN/PIE, `0x02` ET_EXEC), `0x12` `e_machine` (`0x3e` x86-64), `0x18` `e_entry`, `0x20` `e_phoff`, `0x28` `e_shoff`, `0x36` `e_phentsize` (`0x38` = 56), `0x38` `e_phnum`, `0x3c` `e_shnum`. The slide names these fields in prose; the offsets are the ELF specification's, and `e_phoff` tells `readelf` where the program header table starts — here after the 64-byte header, 13 entries of 56 bytes. `readelf -l` prints each segment's `off` and `vaddr`, which are congruent modulo `0x1000` (4096): slide 28's alignment rule as a number.

## Common Pitfalls
- **Confusing segments with sections.** `readelf -l` lists segments, `readelf -S` sections.
- **Reading a section offset as a virtual address.** `sh_offset` is a file offset; `p_vaddr` is where bytes land in the address space.
- **Assuming `PT_LOAD` is one segment.** Binaries typically have several, with different access attributes (slide 27).
- **Forgetting the alignment.** The loader and tooling both rely on page-size alignment (slide 28).
- **Expecting `.text` to be the entry point.** `e_entry` is authoritative, not a section name.
- **Treating the format as Unix-only.** Slide 22 names ELF, PE (also UEFI), Mach-O and the legacy formats.

## Connections
- [[binary-reverse-engineering]] — the format is the system-level artifact static analysis reads first.
- [[x86-assembly-and-abi]] — the ISA named by `e_machine`; its encodings fill `.text`.
- [[elf-symbols-and-tables]] — the `.symtab`, `.dynsym` and string tables from slide 26.
- [[got-plt-lazy-linking]] — `.plt`, `.got`, `.got.plt` and the load sequence past the entry point.
- [[dynamic-linking]] — why a shared object is mapped at run time.
- [[process-memory-layout]] — where `PT_LOAD` segments, heap, stack and mmap area land.
- [[runtime-system]] — the C library and interpreter every dynamically linked binary pulls in.
- [[legacy-systems]] — why com, MZ, a.out and COFF still matter.
- [[reverse-and-reengineering-lecture-2]] — the lecture whose slides 00–19 and 36–38 this deck repeats.

## Open Questions
- **The page size is never given a value.** Slide 28 requires page-size alignment but not the page size; 4096 is the x86-64 default.
- **"no-load" sections are unnamed.** Slide 25 mentions them without saying which they are or what happens at runtime.
- **Slide 25 mixes categories.** Its section description ("program, symbols, strings, dynamic linking info, constructors, destructors") lists contents, not the section names slide 26 gives.
- **The header's fields are prose only.** The offsets in the Worked Example come from the ELF specification, not the deck.
- **Whether the section header table is optional is unstated**, as is what stripping does to it.
