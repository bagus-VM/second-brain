---
title: "Disassembly — Instruction Decoding, Linear Sweep and Recursive Traversal"
tags: [concept, reverse-and-reengineering, semester-2, disassembly, binary-analysis]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[binary-reverse-engineering]]", "[[x86-assembly-and-abi]]", "[[elf-executable-format]]"]
---

## One-line Summary
Disassembly is the reverse of assembly — machine code back into mnemonics — and because x86 instructions have variable length, *where you start decoding decides what you see*, which is the whole reason the field splits into linear sweep and recursive traversal.

## Core Intuition
The assembler goes one way: it translates instruction mnemonics into machine code and builds an executable file format containing code and data. The disassembler goes back: it converts machine code into mnemonics, identifies code and data sections in the executable, includes labels in the code for jump targets, and recovers other relevant data such as string tables and jump tables (slide 2).

The difficulty is not the translation of one instruction — it is *synchronisation*. x86 opcodes are variable-length, so the instruction stream is only well-defined relative to a known instruction start. Get one byte off and every subsequent "instruction" is a fiction that happens to decode successfully (slide 6). The consequence for the rest of this course: anything that attacks the analyst's knowledge of instruction boundaries — jumping *into* an opcode, packing, generating code at runtime — is an attack on disassembly itself, not on reasoning.

A second consequence is worth stating explicitly, because it is what makes the tool choice matter: compilers do not interleave code and data, so linear sweep works on compiler output. Hand-written or obfuscated code does exactly what compilers do not.

## Formal Definition / Statement
**The instruction format (slides 3).** An x86 instruction is a sequence of optional instruction prefixes (1 byte each, in any order, with the REX prefix — if used — immediately before the opcode), primary opcode bytes (up to three), an addressing-form specifier consisting of the **ModR/M** byte and sometimes the **SIB** byte, a displacement (if required) and immediate data (if required). The deck prints Intel's own table:

| Field | Size | Notes |
|---|---|---|
| Instruction prefixes | 1 byte each, optional | REX must be immediately before the opcode |
| Opcode | 1, 2 or 3 bytes | |
| ModR/M | 1 byte if required | `Mod` (7:6), `Reg/Opcode` (5:3), `R/M` (2:0) |
| SIB | 1 byte if required | `Scale`, `Index`, `Base` |
| Displacement | address displacement of 1, 2 or 4 bytes, or none | rare instructions can take 8 bytes |
| Immediate | immediate data of 1, 2 or 4 bytes, or none | rare instructions can take 8 bytes |

The complete rules occupy roughly 200 pages of Intel's *Architecture Software Developer's Manual*, Volume 2 — which is the deck's reason for the next slide: **do not write your own decoder**. Open-source decoders exist for several ISAs; the popular one named here is **Capstone** (slide 4).

**Linear sweep disassembly (slide 5).** Initialise a program counter to the entry point. Loop: decode the opcode at PC, where its length is *k* bytes; increment PC by *k*; repeat. Simple and fast, and used by many debuggers — but it only works if no data is included in the stream of opcodes.

**Recursive traversal (slide 7).** Re-start disassembly at every jump target (and at the fall-through for a conditional jump), analyse jump tables for their targets. This guarantees proper alignment of actual instructions. Its problem is indirect jump targets — computed at runtime — so in general it is **undecidable**. Practical disassemblers compensate with heuristics for function headers (function prologues) and jump tables, allow manual intervention, and are correspondingly slow: "may take very long time based on heuristics and analyses employed". Commercial tools (Ghidra, IDA Pro) work this way.

## Key Properties
- **Variable length is the root cause.** Anything from 1 to ~15 bytes; the only reason a listing can desynchronise at all.
- **Linear sweep's precondition is a code-only stream.** True for clang/gcc output, false for jump tables, embedded strings, hand-written assembly, and everything an obfuscator produces (slide 5).
- **Recursive traversal's precondition is that the control-flow graph can be followed statically.** Indirect jumps end that (slide 7).
- **Both are heuristics in practice.** Linear sweep is exact on compiler output; recursive traversal is exact where it can reach, partial everywhere else, and undecidable in general.
- **Entry points are the scarce resource.** Slide 22's summary says it plainly: disassembly "needs knowledge of function entry points for correct synchronization".
- **Capstone (or equivalent) turns decoding into a library call**; the hard part left is where to call it (slide 4).

## Worked Example
The deck's own failure example (slide 6), verified on this machine rather than repeated from the slide. The byte string is 11 bytes, and the second column is what the source assembles to:

```
offset  bytes              source                    what linear sweep decodes
0       b8 34 02 00 00     mov eax, 0x234            mov    $0x234,%eax
5       eb 01              jmp label                 jmp    0x8
7       e0                 db E0                     loopne 0x3a
8       31 c0              label: xor eax, eax       (never reached linearly)
a       c3                 ret                       ret
```

Run through GNU objdump — itself a linear-sweep disassembler — the recovery is exactly the slide's third column:

```
$ objdump -D -b binary -m i386:x86-64 --adjust-vma=0 linear.bin
   0:  b8 34 02 00 00   mov    $0x234,%eax
   5:  eb 01            jmp    0x8
   7:  e0 31            loopne 0x3a
   9:  c0               .byte 0xc0
   a:  c3               ret
```

Two details make the arithmetic checkable rather than plausible: `jmp 0x8` is `5 + 2 + 0x01`, the offset of `xor`; and `loopne 0x3a` is `7 + 2 + 0x31`, so the two-byte `loopne` **swallows the first byte of the real `xor`** (`e0 31`), leaving offset 9 pointing at `c0` — an opcode that needs a ModR/M byte and an immediate that are not there. Restarting the disassembly at the jump target recovers the truth:

```
$ objdump -D -b binary -m i386:x86-64 --adjust-vma=0 --start-address=8 linear.bin
   8:  31 c0            xor    %eax,%eax
   a:  c3               ret
```

That is recursive traversal in one command: the same bytes, the same tool, a different starting point.

## Common Pitfalls
- **Reading a linear-sweep listing as ground truth.** It is correct up to the first data byte or jump table and silently wrong after it — no warning, just plausible instructions.
- **Assuming `db 0xc0` means the byte is unreachable.** In the example above `c0` is the first byte of a real instruction sequence reached by the jump; the disassembler labelled it as data because *its* stream desynchronised, not because the CPU considers it data.
- **Confusing "the disassembler printed an instruction" with "this instruction executes".** Decoding succeeds on arbitrary bytes; that is the illustrated failure, not a tool bug.
- **Forgetting that the obfuscator attacks the entry point.** Control-flow obfuscation that jumps *into* the middle of an instruction is defeatable by restarting from every offset and discarding offsets that fail to decode — the deck's own countermeasure (slide 8) — which is why obfuscation escalates to packing and code generation.
- **Ignoring the prefix rules.** REX must immediately precede the opcode; a prefix, a 3-byte opcode and a SIB byte make the same mnemonic occupy different byte counts, so length is not a property of the mnemonic.

## Connections
- [[reverse-and-reengineering-lecture-4]] — the lecture this page comes from; the obfuscation half is the reason the topic matters.
- [[reverse-and-reengineering-exercise-4]] — Homework 4 problem 2 flattens a `while` loop and asks for the flattened CFG, which is the source-level form of the same block-dispatcher problem.
- [[binary-reverse-engineering]] — the abstraction ladder; disassembly is its first rung, the one that turns bytes into a readable listing.
- [[x86-assembly-and-abi]] — the encoding the listing exposes: registers, subregisters, CISC addressing and the frame prologue every recovered listing begins with.
- [[elf-executable-format]] — the file that tells the disassembler *where* the code section is and which architecture the bytes assume.
- [[static-vs-dynamic-analysis]] — linear sweep and recursive traversal are static; the runtime code generation of [[dynamic-code-rewriting]] is the reason dynamic analysis exists.
- [[basic-block]] and [[control-flow-graph]] — recovering a CFG is worthless if the block boundaries came from a desynchronised listing.
- [[symbolic-execution]] — the engine behind unvirtualization, the deck's answer to the strongest obfuscation (slide 20).
- [[code-obfuscation]] — the adversary: the deck's second half.

## Open Questions
- **Whether the exam asks for the ModR/M or SIB bit layouts.** The deck prints the field table and the bit split but never works an example byte; whether it is examinable is not stated.
- **No slide shows decoding as code.** Capstone is named and its use is assumed; how a hand-written decoder would be structured — and where it must give up — is left to the 200 pages of the Intel manual the slide points at.
- **Automatic decoding is presented as a solved problem, but no slide explains a decoder's failure modes** (unsupported instruction sets, 8-byte immediates, VEX encodings), which is where "just use Capstone" stops being sufficient.
- **The countermeasure to instruction-splitting is given one line** — "start disassembly from any offset; invalid instruction found: disregard that offset" (slide 8). That is exponential in the worst case and the deck does not say how a real tool bounds it.
- **The maximum instruction length (15 bytes) appears only in passing** in the obfuscation slide, not in the encoding slide where it belongs; whether it is examinable material is unclear.
