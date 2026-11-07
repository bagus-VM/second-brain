---
title: "Reverse- and Reengineering — Lecture 4: Disassembly and Obfuscation"
tags: [topic, reverse-and-reengineering, semester-2, lecture, disassembly, obfuscation]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[reverse-and-reengineering-lecture-3]]"]
---

## One-line Summary
Machine code back to mnemonics — and then the arms race: everything the first three lectures assumed (a readable binary, stable instruction boundaries, a control-flow graph) is what the second half of this deck teaches you to attack and to recover.

## Core Map

```
Reverse- and Reengineering — Lecture 4 (04-disasssembly.pdf, 23 slides)
│
├── Slides 2-4: the translation itself
│   ├── assembler: mnemonics -> machine code, plus the executable format
│   ├── disassembler: machine code -> mnemonics, code/data sections, labels for
│   │   jump targets, string and jump tables
│   └── instruction decoding: prefixes | opcode (1-3B) | ModR/M | SIB |
│       displacement | immediate  ->  Intel SDM Vol. 2, ~200 pages
│       └── do not write your own: Capstone
│           → [[disassembly]]
│
├── Slides 5-6: linear sweep, and exactly how it fails
│   ├── PC = entry; decode k bytes; PC += k; repeat
│   ├── works because clang/gcc do not mix code and data
│   └── the failure table, verified against GNU objdump
│       → [[disassembly]]
│
├── Slide 7: recursive traversal
│   ├── restart at jump targets and conditional fall-throughs; jump tables
│   ├── guarantees alignment; indirect jumps make it undecidable
│   └── heuristics for function prologues; Ghidra, IDA Pro
│       → [[disassembly]]
│
├── Slides 8-9: the framing
│   ├── anti-disassembly obfuscation: jump *into* an opcode (15-byte window)
│   └── obfuscation = semantics-preserving transformation; no perfect scheme
│       → [[code-obfuscation]]
│
├── Slides 10-14: dynamic code rewriting and packing
│   ├── modify/pack/encrypt, reverse at runtime; code exists only at runtime
│   ├── dynamic code loading, self-modifying code (unset W^X), packing
│   ├── packed layout, unpacking stub, manual import resolution, tail jump
│   ├── reversing packed code: stub reversal | memory dump | (research) auto
│   └── simple obfuscations: metamorphic syntax changes, jump insertion
│       → [[dynamic-code-rewriting]] [[binary-packing]] [[code-obfuscation]]
│
├── Slides 15-20: control-flow obfuscation
│   ├── in-/outlining, OS-based indirection (exception handlers, longjmp)
│   ├── opaque predicates: (x*x>=0), (x << 1 % 2 == 0); brute force, SMT
│   ├── function joining: one entry, a selector argument, a shared body
│   ├── control-flow flattening: number the blocks, add a dispatcher
│   └── virtualization: code array + virtual program counter + operand array
│       └── unvirtualization: symbolic execution -> clone blocks -> optimize
│           → [[control-flow-obfuscation]]
│
└── Slide 21: data-based obfuscation
    ├── constant unfolding, data encoding, dead code insertion
    ├── arithmetic substitution: -x = ~x + 1
    ├── MBA expressions: (x1&&x2)+(x1&&!x2)+(!x1)+(x3||x4)  -> 1 + (x3||x4)
    └── pattern-based obfuscation
        → [[code-obfuscation]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[disassembly]] | Variable-length opcodes make the instruction stream relative to its start point, which is why linear sweep and recursive traversal exist and where each breaks. |
| [[code-obfuscation]] | Semantics-preserving transformation against analysis: the taxonomy, the impossibility claim, and the superlinear cost of combining techniques. |
| [[control-flow-obfuscation]] | Hide which block runs next — flattening, opaque predicates, function joining, virtualization — and how each is undone. |
| [[binary-packing]] | Encrypt the program after linking, decrypt it in memory at load time; the stub is the only readable code and imports are resolved by hand. |
| [[dynamic-code-rewriting]] | Keep the code out of the file entirely: runtime generation, self-modifying code, and the W^X dance that makes it possible. |
| [[reverse-and-reengineering-lecture-3]] | The prerequisite deck: ELF, symbols, dynamic linking — the metadata the packer has to rewrite and the analyst reads first. |

## Lecture Structure

The deck is a Keynote export (`04-disasssembly.pdf`, 23 pages, produced 2026-11-04, title page ×1 plus slides numbered 2–23), so slide numbers below are the deck's own footers. There are three movements:

1. **Disassembly as a translation problem (slides 2–7).** What the disassembler adds beyond mnemonics; the instruction encoding in six fields; why hand-writing a decoder is a mistake (Capstone); linear sweep and its failure; recursive traversal and its undecidability. This is the technical core, and it is the only part with worked data.
2. **Obfuscation as an answer to it (slides 8–20).** The framing slide (semantics-preserving, no perfect scheme), then four families in escalating strength: simple syntax changes; dynamic code rewriting and packing; control-flow obfuscation; virtualization. Each family gets one slide of mechanism and most get a counter-measure bullet.
3. **Data-based obfuscation and the summary (slides 21–23).** Arithmetic and data transformations, then slide 22's summary — which is worth reading as the deck's thesis: decoding is tedious but straightforward; disassembly needs entry points; there are no formal guarantees; combining techniques costs analysis superlinearly; and obfuscation slows the program, so it is applied to sensitive parts only.

Slide 23 lists the reading: B. Dang et al., *Practical Reverse Engineering* (Wiley 2014); J. Kinder, *Reverse Engineering* (UBW, 2020) — also cited in lecture 3; Andrew Griffiths, *Protecting binaries* (2005) and *Binary protection schemes*.

## Exam-Relevant Points

1. **The instruction format, in order and with sizes.** Prefixes (1 byte each, optional, REX immediately before the opcode), opcode (1–3 bytes), ModR/M (1 byte if required, split `Mod` / `Reg-Opcode` / `R/M`), SIB (if required, `Scale` / `Index` / `Base`), displacement (1/2/4 bytes, rarely 8) and immediate (1/2/4 bytes, rarely 8). Slide 3 prints Intel's table; the ~200 pages of Volume 2 are the reason for slide 4.
2. **Linear sweep: the loop and the precondition.** PC ← entry; decode *k* bytes at PC; PC += *k*. Simple, fast, used by debuggers, and valid only while the stream contains no data.
3. **The failure, with numbers.** `b8 34 02 00 00` / `eb 01` / `e0` / `31 c0` / `c3`: five bytes, then a two-byte jump to offset 8, so a linear sweep resynchronises at offset 7, decodes `e0 31` as a two-byte `loopne 0x3a`, and is left with `c0` at offset 9 — a real instruction's first byte, reported as data. Verified against `objdump` on this machine; see [[disassembly]].
4. **Recursive traversal.** Restart at jump targets and conditional fall-throughs, analyse jump tables, guarantee alignment; the blocker is indirect jump targets computed at runtime, hence undecidable in general; heuristics (function prologues, jump tables) plus manual intervention; used by Ghidra and IDA Pro.
5. **The definition of obfuscation, and its limit.** Semantics-preserving transformation; prevents or blows up static analysis, precludes manual debugging; perfect obfuscation is theoretically impossible; practical schemes exist for restricted classes or with reduced strength.
6. **The four families and their members.** Simple (metamorphic syntax changes, jump insertion); dynamic (code loading, self-modifying code, packing/encryption); control flow (in-/outlining, OS-based indirection, opaque predicates, function joining, flattening, virtualization); data-based (constant unfolding, data encoding, dead code, arithmetic substitution, MBA, pattern-based).
7. **Control-flow flattening in three steps.** Number the basic blocks, add a dispatcher (`switch` on the block number), replace every control-flow instruction with a jump to the dispatcher carrying the successor's number — optionally with spurious blocks and dead paths.
8. **Opaque predicates: definition and four countermeasures.** A runtime-constant expression that is hard to prove constant by analysis; defeats pattern matching, brute force over 2^32/2^64, SMT, and dynamic analysis that ignores unused code.
9. **Packing's load sequence.** Decrypt into sections, resolve imports manually (duplicating the OS loader), jump to the original entry point (tail jump, possibly obfuscated through `call`/`ret` variants).
10. **The summary's four claims.** Decoding is tedious but straightforward; disassembly needs function entry points for synchronisation; no formal guarantees for obfuscation; combination increases analysis cost superlinearly; and obfuscation slows execution, so it is used selectively.

## Connections

- [[reverse-and-reengineering-lecture-3]] — the prerequisite: ELF, the two tables, symbols, GOT/PLT. The packer's job is defined against exactly that metadata.
- [[reverse-and-reengineering-lecture-2]] — the abstraction ladder and static/dynamic analysis, which this deck now attacks and extends.
- [[reverse-and-reengineering-exercise-4]] — Homework 4: recover C from a frame-based x86-64 listing, then flatten a loop and draw the flattened CFG. Both are exercises in this deck's own material.
- [[reverse-and-reengineering-exercise-3]] — the previous homework's assembly recovery; the same prologue-spill shape appears again in Homework 4 problem 1.
- [[disassembly]] — the page for slides 2–8.
- [[code-obfuscation]], [[control-flow-obfuscation]], [[binary-packing]], [[dynamic-code-rewriting]] — the four concept pages this lecture produced.
- [[x86-assembly-and-abi]] — the register set, the frame layout, and the CISC decoding the deck's instruction-format slide presupposes.
- [[elf-executable-format]] — `.text` as read-execute, `.data` as read-write; the packer restores both, and the analyst's first `readelf -l` shows what it must reproduce.
- [[static-vs-dynamic-analysis]] — the distinction every obfuscation technique is priced against.
- [[symbolic-execution]], [[constant-propagation]], [[dead-code-elimination]] — the three tools the deck names on the unvirtualization slide.
- [[control-flow-graph]] and [[basic-block]] — what flattening destroys and what the exercise asks you to draw.
- [[reverse-and-reengineering]] — the course page.

## Open Questions

- **The deck never exercises a real obfuscated binary.** Every mechanism is a slide; there is no lab, no sample and no tool walkthrough, and no sheet in `raw/` covers packing, flattening or virtualization.
- **`03-binaries.pdf` and this PDF are both Keynote exports of lecture halves.** The `03` export has 15 pages and omits the lecture-2 recap that the `.key` package contains, so the two sources for lecture 3 do not cover exactly the same slides — recorded on [[reverse-and-reengineering-lecture-3]] rather than silently reconciled.
- **Anti-debugging and anti-VM are named twice** (packing slide, dynamic-unpacking slide) and described nowhere in the deck.
- **"No formal guarantees" and "theoretically impossible" are asserted, not derived.** The deck's references are all practitioner literature; the impossibility result behind the claim is not cited.
- **The opaque-predicate example `(x << 1 % 2 == 0)` is not a tautology as printed** — C precedence makes it `(x << 1) == 0`. Whether that is a typo or a deliberate precedence trap is unrecorded.
- **Multi-slide coverage of the same technique is uneven.** Flattening gets one slide and one diagram, virtualization two; simple obfuscations get one slide and are then dismissed as useless against compiler techniques, which leaves the ordering of strengths implied rather than stated.
- **No slide states which of these techniques the exam treats as implementable** (write the flattening transform) versus recognisable (name the family from a listing). Homework 4 problem 2 is the only evidence, and it asks for the transform.
