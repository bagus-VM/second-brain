---
title: "Undefined Behavior in C"
tags: [concept, c, semester-2, virtual-machines]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-11-12
prerequisites: ["[[abstract-machine-semantics]]"]
---

## One-line Summary
Undefined behavior means the C standard imposes no requirements for a program execution, so a compiler may optimize under the assumption that the undefined case does not occur.

## Core Intuition
The CPU may appear to do something predictable when an error occurs, but the C language contract does not promise it. Once code invokes undefined behavior, reasoning from one observed build is unsafe because the optimizer may transform surrounding code using the assumption that the case is impossible.

## Formal Definition / Statement
In C, behavior is undefined when the standard specifies no requirements for that case. The lecture identifies unsequenced modification/access (example `i = i++` in C99), signed integer overflow, and dereferencing a null pointer as examples. Unsigned integer arithmetic, by contrast, is defined modulo the type's range.

## Key Properties
- A compiler need not diagnose every undefined operation.
- Optimizers may exploit the assumption that undefined behavior never occurs.
- A signed overflow check such as `if (s + 1 < s)` can be removed because without overflow the condition is always false.
- Dead-code elimination and undefined-behavior reasoning can interact in unintuitive ways.
- Observed machine-level wraparound does not make signed overflow defined by C.

## Worked Example
Suppose `int s` is incremented and then checked with `if (s + 1 < s) abort();`. If signed overflow is excluded by the language contract, `s + 1 < s` is always false. The compiler may therefore remove the branch, even if the programmer expected wraparound to detect overflow.

## Common Pitfalls
- Assuming signed integers wrap because the target CPU instruction wraps.
- Treating a sanitizer warning or a particular compiler's output as the definition of C.
- Assuming a null check after dereferencing a pointer makes the earlier dereference safe.
- Using `i = i++` while assuming a single evaluation order.

## Connections
- [[abstract-machine-semantics]] — specifies which program behaviors C guarantees.
- [[virtual-machines-and-runtime-systems-lecture-3]] — the source deck's C99 examples and optimizer reasoning.
- [[decompilation]] — machine code may embody transformations that are surprising from source-level intuition.

## Open Questions
- The source cites C99; exact rules differ across standard versions and should be checked before applying the examples to another version.
- The slide's null-pointer example is presented with a dead assignment and a later check; its optimizer explanation is specific to that exact code.
