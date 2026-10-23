---
title: "Binary Reverse Engineering"
tags: [concept, reverse-and-reengineering, semester-2, binary-analysis, reverse-engineering]
course: "Reverse- and Reengineering"
source_count: 2
status: current
last_updated: 2026-10-22
prerequisites: ["[[reverse-engineering]]"]
---

## One-line Summary
Binary reverse engineering is the analysis of a program when the artefact available is machine
code rather than source, spanning the abstraction ladder from object code up to source and using
static and dynamic techniques to recover behaviour.

## Core Intuition

The central picture of lecture 2 is the **abstraction ladder** (slide 10). It arranges software
artifacts by *increasing abstraction*, from physics at the bottom to application software at the
top:

- Worst case: only binary/object code.
- Higher level: bytecode/intermediate representation; assembly language; machine code.
- Best case: source code (which might still be cryptic).

Alongside the ladder sit the layers the artifact rests on: programming language, hardware,
instruction set architecture, micro architecture, gates and registers, devices and transistors,
physics.

The ladder's punchline is the last line of the slide: **"Common goal: IR suitable for further
analysis."** Regardless of where on the ladder the input sits, the analyst wants to end up at
an intermediate representation that other analysis can consume. That is the shared target that
makes disassembly, decompilation, control-flow reconstruction and the rest of the topic
cohere.

The word "worst case" and the parenthetical "might still be cryptic" are both doing work. Source
code is not automatically understandable; cryptic source is a real case, only less bad than
object code.

The second organising idea is that binary analysis is not only about *not having source*. Slide
11 asks: "Even if source code is available: correspondence of source and binary?" Then it lists
the areas of binary analysis proper: understanding of computer organization and low-level code;
executable formats; the interface to OS/HW; assembly.

So the subject is the *relationship* between the artifact you have and the machine it runs on,
and that relationship survives even when the source is in your hands.

## Formal Definition / Statement

Lecture 2 slide 12 defines the two levels of binary reverse engineering:

> **Code level**: low-level, machine code or assembly. Recognize design, data structures,
> algorithms — lists, trees, tables, vectors, matrices, dictionaries, heaps; data structure
> traversals, iterators, applicators, manipulators; searching (linear, binary, hashing); event
> handling; exceptions.
>
> **System level**: higher level, e.g. interface with OS, protocols, etc.

Slide 13 gives **static analysis** — analysis of code without execution:

- Code level: disassembly; control flow reconstruction (non-trivial); decompilation
  (reconstruction of higher level constructs, **undecidable**); detection (vulnerabilities, etc.).
- System level: header information (meta data); imported libraries, functions; resources (fixed
  locations for embedded data, GUI, etc.).

Slide 14 gives **dynamic analysis** — analyzing program executions, at runtime:

- Observe the target program's behaviour; execute the program (requires input/test data);
  potentially dangerous (malware? side effects) → VM; emulator, etc. for legacy software; see the
  program testing lecture.
- Code level: debugging (manual, user mode / kernel level) vs. (semi-)automatic (fuzzing,
  symbolic execution).
- System level (automatic, efficient): monitoring of system and library calls; process creation,
  file system, network.

The word on the slide that carries the most theoretical weight is **"undecidable"** next to
decompilation. Reconstructing higher-level constructs from machine code is not merely hard; the
slide marks it as undecidable, which is why no amount of tooling produces a guaranteed-correct
decompilation.

From lecture 1, slide 37, the **problems of reverse engineering** apply directly to the binary
case:

- Loss of information (e.g. methods and attribute names) during the compilation process ⇒
  interpretation and expert knowledge of the code during the analysis becomes necessary.
- Static analysis cannot always make statements about whether code is actually executed in
  practice.
- The reverse engineering process can only be partially automated due to the analyst's own high
  level of effort.

## Key Properties

- **The target is an IR, not a listing.** Every technique is judged by whether it moves the
  artifact toward an intermediate representation suitable for further analysis.
- **Both static and dynamic techniques are needed, and neither is sufficient.** Static analysis
  cannot establish reachability in practice; dynamic analysis sees only what was exercised.
- **Decompilation is undecidable** — a theoretical limit, not a tooling deficiency.
- **Control flow reconstruction is "non-trivial"** — the slide's own adjective — because the
  machine-level control transfer graph must be rebuilt into higher-level structure.
- **Dynamic analysis has a safety dimension.** Executing untrusted code is potentially
  dangerous; VMs and emulators are the stated mitigations, and emulators are also the answer
  for legacy software that no longer runs on current hardware.
- **System-level metadata is a first-class information source.** Headers, imported libraries and
  functions, and embedded resources can reveal much of a program's structure without executing a
  single instruction.
- **The abstract interface is recovered as well as the code.** Interfaces with the OS, and
  protocols, are system-level targets of the same effort.
- **The environment shapes the analyst's options.** x86 has variable-length encodings from 1 to
  15 bytes and complex addressing modes, so instruction boundaries are not given for free; see
  [[x86-assembly-and-abi]].

## Worked Example

The lecture's example for a *binary* case is not a program but a **disassembly idiom** and an
**addressing-mode encoding**, both from slide 22:

```asm
int *A;          ; ebx = A, ecx = i
... mov eax, 100
A[i+2] += 100    ; add [ebx + ecx*4 + 8], eax
```

*Source material from lecture 2, slide 22.*

Read as a reverse engineer reads it: `ebx` holds the base address of the array `A`, `ecx` holds
the index `i`, `eax` holds the constant 100. The `add` instruction encodes the *effective
address* `ebx + ecx*4 + 8` — base register plus index register scaled by 4 (the size of an
`int`) plus a constant displacement of 8 (two elements' worth). So the compiler has translated
`A[i+2] += 100` into a base+index*scale+displacement memory operand, and the analyst has to
recover the array indexing, the element size, the offset and the constant from the encoded
address alone.

That is the whole problem in one instruction: **the source-level structure is present in the
binary, but encoded in a form that must be decoded rather than read.** Nothing here is
recoverable by pattern-matching names — there are no names — which is why slide 37's "loss of
information" applies directly.

A second source-material example is the shorter-than-`mov` idiom from slide 23: `xor op, op` is
equivalent to but shorter than `mov op, 0`. A reverse engineer sees the zeroing of a register
and must decide whether it is a real computation or the idiom, since the encoding carries no
annotation saying which.

## Common Pitfalls

- **Assuming source availability removes the problem.** Slide 11 asks about the correspondence
  of source and binary even when source exists.
- **Running untrusted code natively.** The slide's warning is blunt: potentially dangerous
  (malware? side effects) → VM.
- **Treating decompilation output as the answer.** The slide marks reconstruction of higher-level
  constructs as undecidable; decompiler output is a hypothesis.
- **Equating disassembly with disassembly quality.** Control flow reconstruction is called
  non-trivial, and the analyst's effort is the stated bottleneck for automation.
- **Using only static or only dynamic analysis.** Static analysis cannot tell whether code is
  actually executed; dynamic analysis only sees the executed paths.
- **Ignoring the system level.** Imported libraries, header metadata and embedded resources are
  often where the architecture of a binary becomes visible.
- **Forgetting that the artifact may not even be a native binary.** The ladder includes bytecode
  and intermediate representations, and dynamic analysis has to handle a VM-based runtime.

## Connections

- [[reverse-engineering]] — the general activity this page specialises.
- [[x86-assembly-and-abi]] — the ISA whose encodings must be decoded; the `add [ebx+ecx*4+8]`
  example lives there.
- [[static-vs-dynamic-analysis]] — the two halves of the analysis strategy.
- [[dynamic-analysis]] — runtime observation, fuzzing and symbolic execution.
- [[symbolic-execution]] — the (semi-)automatic counterpart to manual debugging.
- [[debugging]] — manual dynamic analysis at user and kernel level.
- [[reengineering]] — binary recovery is often the entry point of a reengineering project.
- [[software-analysis]] — the family the IR output is meant to feed.
- [[software-aging]] — the reason the artifact is old enough to need this treatment.
- [[reverse-and-reengineering-lecture-2]] — the source lecture for slides 10–14.

## Open Questions

- **What exactly is undecidable about decompilation?** The slide asserts it without a statement
  of the problem instance or the boundary; the source gives no formal problem definition for
  reconstruction of higher-level constructs.
- **No criterion is given for choosing static over dynamic analysis, and the emulator's role is
  unstated.** The two are presented as parallel lists; the source does not say when each is
  required, or how they are combined into a single workflow. "Emulator, etc. for legacy
  software" is one bullet, without saying whether an emulator serves safety, compatibility, or
  both.
- **The system's own protection against analysis is never mentioned.** Obfuscation appears in
  lecture 1's content list ("Effects of obfuscation techniques on this process") but no slide
  in the source text describes how obfuscation changes the binary-analysis problem.
- **The "detection (vulnerabilities, etc.)" technique is named without procedure.** No
  description of how detection works on binaries, or what its false-positive characteristics
  are, is provided.
