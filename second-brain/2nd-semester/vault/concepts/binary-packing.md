---
title: "Binary Packing — Encrypt the Code After Linking, Unpack It at Load Time"
tags: [concept, reverse-and-reengineering, semester-2, packing, anti-analysis]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[code-obfuscation]]", "[[elf-executable-format]]", "[[disassembly]]"]
---

## One-line Summary
A packer compresses or encrypts the program after linking and prepends a stub that reverses the transformation in memory, so the file on disk contains almost nothing an analyst can read — but the stub itself is code, and it has to be visible.

## Core Intuition
The previous lecture established that a binary leaks metadata whether its author likes it or not. Packing is the counter-move at the level of the *file*: the code packed and encrypted after linking, "so the actual code is not available in binary for disassembly, only at runtime" (slides 10 and 12). What remains readable is the unpacking routine.

That residual is the whole game. Packing does not remove the need to execute; it moves the analyst's work from the file to the process a moment *after* the process has decrypted itself. Every attack in the deck's third slide follows from that: reverse the stub, or let the stub do its job and then look at memory. The defence is anti-debugging and anti-VM — i.e. attacking the analyst's ability to observe step two rather than step one.

The motivation is stated three ways on slide 10: to protect intellectual property (a secret algorithm, copy protection), to hide application secrets ("magic keys" for special APIs, decryption keys for media decoding), and to hide malicious behaviour. Slide 11 adds the practical note that packing is popular with malware precisely because it defeats simple pattern detection.

## Formal Definition / Statement
**What the packed file contains (slide 12).** The slide's figure is a three-stage diagram — the file before packing, the packed file on disk, and the state in memory after the stub has run — and the extracted text fragments are ordered here by component rather than by column, because the figure itself is an image:

- **Before packing:** header, `.text` section, `.data` section.
- **Packed file:** header, *Packed code*, *Pack Run*, the remaining `.text` section, and **Unpacking code**.
- **In memory after unpacking:** the sections restored into place, with the unpacking code still present.

The load-time behaviour, in the slide's own steps:

1. Decrypt code and data into the sections.
2. **"Manually" resolve imports** — duplicating the OS loader's functionality, because the operating system's loader can no longer do it: the import table it would read has been encrypted along with everything else.
3. **Jump to the original entry point** (the **tail jump**) — and this transfer may be obfuscated with `call`, `ret` or "intricate transfer variants", so that it is not detectable as an ordinary jump.

Step 2 is the one that connects this page to the ELF material of [[reverse-and-reengineering-lecture-3]]: the packer has to rebuild by hand what `PT_LOAD`, `.dynamic`, `DT_NEEDED`, `.rel.dyn` and `.rel.plt` do ([[elf-executable-format]], [[got-plt-lazy-linking]]), which is why a packed binary's dynamic-linking metadata is a poor guide to what it actually calls.

**Reversing packed code (slide 13).** Two families, and the slide states the status of each:

- **Static.** Reverse the unpacking stub and fold its functionality into the disassembly routine; automatic static unpackers exist for certain tools (i.e. they are tool-specific).
- **Dynamic.** Run the program until the unpacker has finished and dump memory, then disassemble the dump. Automated dynamic unpacking is "ongoing research": it detects the tail call, dumps and disassembles, and **rediscovers the imports**.
- **The complication:** dynamic analysis is "potentially thwarted by anti-debugging, anti-VM", and unpacking may happen at finer granularity — "by function, no single memory dump" — which invalidates the one-dump-then-analyse recipe entirely.

## Key Properties
- **The transformation is applied after linking**, so it sees the finished program: relocations resolved, imports listed, sections laid out. Everything the loader needed is inside the encrypted blob.
- **There is always a visible stub.** It must run before anything else, so a first disassembly pass *does* produce code — just not the program's code.
- **The original entry point still exists**, reached by the tail jump; finding it is the static attack's goal.
- **One dump is not always enough.** Per-function unpacking is the stated countermeasure to the dump-and-disassemble approach.
- **Anti-debugging and anti-VM attack the analyst, not the code.** They add nothing to the program's semantics; they remove the analyst's ability to observe it.
- **Packing is cheap and therefore ubiquitous in malware**, which is exactly why it "defeats simple pattern detection".

## Worked Example
**What a packer has to overwrite: the segment table the loader itself consumes.** Not from the deck — `readelf -l` on this host's own `/bin/ls` (Ubuntu 22.04 in WSL, binutils 2.38), included because it makes slide 12's "duplicate OS loader's functionality" concrete:

```
$ readelf -l /bin/ls
Elf file type is DYN (Position-Independent Executable file)
Entry point 0x6aa0
There are 13 program headers, starting at offset 64

  Type    Offset      VirtAddr    FileSiz     MemSiz      Flags  Align
  PHDR    0x00000040  0x00000040  0x000002d8  0x000002d8  R      0x8
  INTERP  0x00000318  0x00000318  0x0000001c  0x0000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD    0x00000000  0x00000000  0x00003458  0x00003458  R      0x1000
  LOAD    0x00004000  0x00004000  0x00013091  0x00013091  R E    0x1000
  LOAD    0x00018000  0x00018000  0x00007458  0x00007458  R      0x1000
  LOAD    0x0001ffd0  0x00020fd0  0x000012a8  0x00002570  RW     0x1000
  DYNAMIC 0x00020a58  0x00021a58  ...
```

Four `LOAD` segments, each page-aligned at `0x1000` — the lecture-3 alignment rule, visible in real data. The `R E` segment is the code, the `RW` one is where `.data` and `.bss` live (`MemSiz` 0x2570 exceeds `FileSiz` 0x12a8 by exactly the uninitialised tail). A packer's stub has to reproduce the effect of those `LOAD`s and of the `DYNAMIC` entry — map the sections, then resolve what `DYNAMIC` pointed at — from its own encrypted copy. That is the concrete meaning of "duplicate OS loader's functionality" on slide 12, and it is why `readelf -d` on a packed file describes the *packer* rather than the payload.

## Common Pitfalls
- **Analysing the file and concluding the program is small and dull.** The readable code is the stub; the payload is decrypted into memory and never touches the file in cleartext.
- **Trusting the import table of a packed binary.** Imports are resolved manually by the stub, so the loader-visible imports belong to the unpacker.
- **Assuming one memory dump is enough.** The slide explicitly warns about per-function unpacking and about anti-debugging/anti-VM making the dump unreliable.
- **Confusing packing with obfuscation.** Packing hides the code's *bytes*; control-flow obfuscation ([[control-flow-obfuscation]]) hides its *shape* after decryption. Real malware does both, and the answer to the first — get the code into memory — only reveals the second.
- **Expecting a static unpacker to generalise.** "Automatic static unpacking programs exist for certain tools" is the slide's own restriction: they are built for particular packers.
- **Forgetting that the packer is itself a program the analyst may already have.** Unpacking stubs are reused far more often than payloads, which is what makes stub recognition a practical first step.

## Connections
- [[code-obfuscation]] — packing is the dynamic/protecting-the-bytes branch of that taxonomy.
- [[dynamic-code-rewriting]] — the general mechanism packing is an instance of: transform at build time, reverse at run time.
- [[elf-executable-format]] — the segments and sections the stub rebuilds; `PT_LOAD` is what mapping into memory means.
- [[got-plt-lazy-linking]] — the GOT/PLT tables the stub must repair when it "manually resolves imports".
- [[elf-symbols-and-tables]] — stripping is the cheap anti-analysis move; packing is the expensive one that also removes `.symtab`.
- [[dynamic-linking]] — the loader mechanics from the Virtual Machines course that the packer has to duplicate.
- [[process-memory-layout]] — where the decrypted sections have to end up for the tail jump to a valid entry point.
- [[disassembly]] — the stub is a disassembly target; the tail jump is often obfuscated precisely so that linear and recursive traversal both miss it.
- [[static-vs-dynamic-analysis]] — the two families of unpacking, with dynamic analysis named as the more robust and less certain one.
- [[runtime-system]] — the library initialisation the loader would normally perform and the stub must not skip.

## Open Questions
- **The slide's packing figure is an image with fragmented text.** The order of *Packed code*, *Pack Run*, `.text section` and *Unpacking code* within the middle column cannot be recovered from the deck's text; the page describes the components and labels the arrangement as unrecoverable rather than guessing it.
- **"Certain tools" in the automatic-static-unpacking bullet is not named**, so there is no way to tell from the deck which packers are considered solved.
- **How big the unpacking stub typically is**, and therefore how much of the file is readable by default, is not stated.
- **Anti-debugging and anti-VM are named as obstacles and never described.** Whether the course treats them as examinable techniques or as a caveat is unclear — no slide shows a detection trick or a counter to one.
- **Nothing says how a packed program's *tail jump* is found** in the static case; the dynamic research line "detects tail call" leaves the static equivalent unattributed.
- **Whether the course's own exercises pack anything** is unknown: no sheet in `raw/` exercises packing, so this material is lecture-only so far.
