---
title: "Virtualization vs. Abstraction"
tags: [concept, virtual-machines, semester-2]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
Abstraction throws away detail; virtualization preserves the guest's state transitions inside the host. A VM is not an abstraction of a machine — it is a faithful embedding of one.

## Core Intuition
Both ideas hide the hardware, so they get confused. The difference is what happens to information. An abstraction is allowed to lose detail: the file API does not tell you which disk blocks were used. A virtualization is not allowed to lose detail: two different guest states must map to two different host states, or you can no longer tell them apart. That is why the definition demands an **injective** map.

## Formal Definition / Statement

**Abstraction:** neglects non-essential details, reducing a system to its important aspects. Technical systems form hierarchies of abstraction connected by well-defined interfaces. Example chain: SATA controller → AHCI interface → block device interface in the kernel → file I/O interface → C runtime `FILE*` → `java.io.FileOutputStream`.

**Virtualization:** a system G (guest) is virtualized in a system H (host) when, for every operation (state transformation) σ on G, there exists a corresponding operation σ′ on H.

Formally: let S(G) and S(H) be the state sets of G and H. An **injective** map V : S(G) → S(H) virtualizes G in H when for each σ : S(G) → S(G) there exists σ′ : S(H) → S(H) such that

```
V ∘ σ = σ′ ∘ V
```

Injectivity is required: otherwise two distinct guest states would collapse into one host state, H would be an *abstraction* of G, and the state correspondence would be lost.

**Emulation:** recreates the observable behaviour (semantics) of a system in another system; internals need not be reproduced.

**Simulation:** goes beyond emulation by recreating the internal processes too — e.g. exact clock cycles per instruction, cache behaviour.

## Worked Example — `iadd`

Java bytecode `iadd` pops two values from the operand stack, adds them, pushes the result.

x86 equivalent:

```asm
popl %eax
popl %ebx
addl %eax,%ebx
pushl %eax
```

Three different relationships, same instruction:

- **Abstraction:** Java bytecode has an implicit operand stack; x86 has explicit registers and a stack. The bytecode hides register allocation.
- **Virtualization:** the state transition expressed by `iadd` corresponds exactly to the state transition of the four x86 instructions. The mapping preserves states.
- **Emulation:** the *behaviour* of `iadd` is recreated in x86 assembly. (Note the lecture's phrasing: emulation recreates behaviour; here the implementation happens to be a translation.)

## Key Properties

- Virtualization allows several similar guest systems in one host — the guest is often a *resource plus its interface*, and virtualization makes it look like there are several independent instances.
- Canonical examples: threads/processes (virtualize the CPU), virtual memory (physical RAM), file systems (storage media), windows/display managers (graphics hardware), network sockets (network hardware).
- Simulation ⊃ emulation: simulation reproduces internals, emulation only results.

## Common Pitfalls

- **Dropping injectivity.** Without it you have an abstraction, and "the VM's state" stops being well-defined.
- **Using "emulation" and "simulation" interchangeably.** Timing-accurate CPU models are simulators; a compatibility layer that reproduces results is an emulator.
- **Assuming virtualization must be slower.** The definition says nothing about performance — only about state correspondence.
- **Confusing a runtime system with a VM.** A runtime system defines an API (source-level compatibility, recompilation needed); a VM also defines the instruction set (binary compatibility). See [[runtime-system]].

## Connections

- [[runtime-system]] — the API-level cousin of a VM.
- [[process-memory-layout]] — virtual memory is the most familiar instance of the definition.
- [[dynamic-linking]] — the loader maps libraries into an address space; another application of the same idea.
- [[thread-emulation-longjmp]] — threads as a virtualized CPU, implemented with `setjmp`/`longjmp`.

## Open Questions

- Where exactly is the line between "runtime system" and "operating system"? The lecture says it is "not always clearly defined" — which suggests an exam question with no crisp answer.
- Containers virtualize at the OS level; which part of the formal definition still applies when the guest is a process, not a machine?
