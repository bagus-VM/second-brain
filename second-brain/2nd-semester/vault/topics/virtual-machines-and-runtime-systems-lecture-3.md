---
title: "Virtual Machines and Runtime Systems — Lecture 3 Overview (Abstract C Machine and Warren Abstract Machine)"
tags: [topic, virtual-machines, semester-2, lecture, abstract-machines]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[virtual-machines-and-runtime-systems-lecture-2]]"]
---

## One-line Summary
The lecture uses abstract machines both to specify C semantics—including undefined behavior—and to explain how Prolog's logic, unification and backtracking are implemented efficiently by the Warren Abstract Machine.

## Core Map

```
Abstract machines
├── specification model: abstract C machine
│   ├── observable semantics; optimization may remove unneeded work
│   ├── undefined behavior and signed-overflow rules
│   └── compiler optimizations may exploit undefined cases
└── implementation model: Prolog / Warren Abstract Machine
    ├── relations, facts, rules, goals; query resolution by unification
    ├── alternatives require continuations and restoring variable bindings
    └── WAM: heap + local stack + trail + registers + instructions
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[abstract-machine-semantics]] | An abstract machine defines language behavior independently of a particular processor implementation. |
| [[undefined-behavior-in-c]] | C leaves some operations without defined behavior, allowing optimizers to assume those cases do not occur. |
| [[warren-abstract-machine]] | The WAM executes Prolog with explicit term storage, argument registers, choice points, and a trail for undoing bindings. |
| [[unification-and-backtracking]] | Prolog resolves goals by unifying terms and restores bindings when exploring alternative clauses. |

| [[virtual-machines-and-runtime-systems-lecture-2]] | Prior lecture on runtime systems, process state, signals and implementation mechanisms. |

## Lecture Structure

The 34-slide deck has three parts. The introduction distinguishes theoretical models from language-semantics and implementation machines, then notes that C99 describes behavior through an abstract machine. The C portion explains undefined behavior using unsequenced modification, signed integer overflow and a null-dereference example; the compiler may optimize based on the standard's guarantees, not typical hardware behavior. The Prolog portion defines relations, facts, rules, terms and queries, then traces query resolution and multiple answers. The implementation portion introduces continuations, alternatives, variable-binding restoration via a trail, and the WAM's heap, local stack, registers, term tags and instruction families. The final slides show compiling a recursive relation to WAM code and note that the lecture is only a sketch, with 17 of the WAM's 39 instructions covered.

## Exam-Relevant Points

1. A language's abstract machine specifies semantic behavior; it is not necessarily a physical interpreter that runs the program.
2. Undefined behavior is a promise gap in the source language. Hardware behavior observed in one build does not make the C operation defined.
3. Signed integer overflow is undefined in the cited C standard, whereas unsigned arithmetic is defined modulo its range; compiler optimizations may exploit the signed rule.
4. Prolog rules define relations, and query execution repeatedly selects matching clause heads, unifies terms, and replaces goals with clause bodies.
5. Multiple answers require alternatives and restoration of bindings. The trail records which bindings to undo when backtracking.
6. WAM memory roles: heap for terms, local stack for locals/choice points and saved registers, trail for restoring variable bindings; X/A registers pass terms and S traverses structure.
7. `get_structure` selects read or write mode; WAM instructions such as `try_me_else`, `retry_me_else`, and `trust_me` manage alternatives.

## Connections

- [[virtual-machines-and-runtime-systems-lecture-2]] — C runtime and low-level process behavior; this lecture explains the language-semantics contract above machine behavior.
- [[abstract-machine-semantics]], [[undefined-behavior-in-c]], [[warren-abstract-machine]] and [[unification-and-backtracking]] — this lecture's new concept pages.
- [[virtualization-vs-abstraction]] — distinguishes abstraction from virtualization; abstract machines here serve as semantic and operational models.
- [[reverse-and-reengineering-lecture-5]] — intermediate representations also make program execution semantics explicit, but target reverse-engineering rather than language specification.

## Open Questions

- The deck is a sketch and explicitly omits detailed memory allocation and unification rules; it covers only 17 of 39 WAM instructions.
- The cited C standard is C99 (ISO/IEC 9899:1999); later standards and concurrency semantics are not fully treated.
- The slides contain duplicated numbering and a malformed explanatory expression in one IR example; those transcription defects are not silently repaired here.
- No lecture date is printed in the extracted text.
