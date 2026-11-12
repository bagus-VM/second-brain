---
title: "Decompilation"
tags: [concept, reverse-engineering, semester-2, reverse-and-reengineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[binary-reverse-engineering]]"]
---

## One-line Summary
Decompilation translates machine code into a higher-level representation that explains likely program behavior, but compiler transformations make exact source recovery impossible in general.

## Core Intuition
Compilation throws information away and changes structure. A decompiler works backward from the surviving behavior, inferring types, control flow and expressions; different source programs may compile to the same or similar machine code.

## Formal Definition / Statement
Decompilation is the analysis and transformation of a compiled binary into a higher-level representation or source-like output. The lecture's pipeline includes instruction-to-IR translation, control-flow recovery, optimization/simplification, and reconstruction of structured constructs.

## Key Properties
- Machine instructions are untyped; a bit pattern might represent an integer, pointer, address, or another value.
- Comments and original file structure are absent from the binary.
- Inlining, loop unrolling, dead-code elimination and constant propagation can alter source-level structure.
- Decompiler output is a behavioral hypothesis and must be checked against the binary, not accepted as the original source.
- Control-flow reconstruction is difficult for indirect jumps and unstructured control flow.

## Worked Example
A loop multiplying an accumulator by a counter may compile to a conditional jump, multiply, decrement and backward jump. A decompiler may reconstruct a `for` loop, but the original could have been a `while`, a `goto` loop, or a different source form optimized to the same instruction sequence.

## Common Pitfalls
- Treating reconstructed variable names or types as ground truth.
- Assuming the source-level loop shape is recoverable after optimization.
- Confusing disassembly (instructions to mnemonics) with decompilation (instructions to a higher-level structure).
- Ignoring semantics: a structurally attractive reconstruction can be wrong if it changes branch behavior.

## Connections
- [[binary-reverse-engineering]] — the broader abstraction ladder from bytes to program behavior.
- [[disassembly]] — produces mnemonics but does not recover source-level structure.
- [[control-flow-graph]] — the graph used as a basis for structured reconstruction.
- [[structural-analysis-decompilation]] — recognizes and collapses CFG regions.

## Open Questions
- The lecture does not give a formal statement of which source properties are undecidable to recover.
- Its sample decompiler output is partly corrupted in the extracted PDF text.
