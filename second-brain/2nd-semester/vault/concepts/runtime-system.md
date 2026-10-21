---
title: "Runtime System"
tags: [concept, virtual-machines, semester-2, runtime-systems]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-19
prerequisites: ["[[virtualization-vs-abstraction]]"]
---

## One-line Summary
A runtime system is everything a program needs at run time but did not get from the compiler — memory, I/O, threads, error handling — delivered as an API, and therefore source-compatible, not binary-compatible.

## Core Intuition
Two programs in different languages both "open a file". Neither talks to the disk. Something in between does the work and hides the platform: the runtime system, whose real product is an *interface*, not a machine.

This is what separates it from a virtual machine. A runtime system defines an API — a set of functions you can call. Code written against it runs elsewhere only after **re-compilation**. A virtual machine also defines the instructions a program may execute, so the same binary runs elsewhere. That is the whole difference: API versus API + instruction set.

The C runtime is the interesting case because it is nearly universal. C is the most common language for low-level system programming, so the C runtime is often an indirect part of other runtime systems, e.g. for high-level languages.

## Formal Definition / Statement

**Runtime system (s01):** supports the execution of a program by providing various services at run time. These are used *explicitly* (calling an API function, e.g. for memory allocation) or *implicitly* (without direct action, e.g. thread scheduling).

Usually the runtime system provides an abstraction from the operating system — the C runtime abstracts from Linux/BSD/Solaris/Windows. The abstraction is often **incomplete**: OS-specific differences remain (`man 2 signal`). A runtime system commonly virtualizes resources such as CPU time, memory, network. The dividing line between operating system and runtime system is not always clearly defined.

**Virtual machine (s01):** a VM does not only define an API but also the instructions a program can execute. Depending on type, that instruction set is an **ABI** (application binary interface) or an **ISA** (instruction set architecture).

**Main tasks of the C runtime (s02):** memory management (`malloc`, `free`), process and signal management, I/O, error handling, string manipulation, threads and locks (newer standards). C is low-level, so its runtime offers no advanced services; the main task is the (rather low) abstraction from kernel services.

## Key Properties

- **Placement depends on the OS.** On Unix-like systems the C runtime is mostly a "wrapper" around kernel functions. On Windows the C runtime *implements* its services using the operating system's functions.
- **API ⇒ source compatibility**, at the price of recompiling per platform. **Instruction set ⇒ binary compatibility.** Java: API = class library, instruction set = byte code (an abstraction from any real ISA). QEMU/VMware/VirtualBox: instruction set = x86/x86_64 instructions, API ≙ emulated hardware interfaces.
- **Layering is real.** SATA controller → AHCI → block device interface in the kernel → file I/O in the kernel → file I/O in the C runtime → `java.io.FileOutputStream` → `java.io.OutputStream`.
- **Services are not virtualized.** Memory allocation, signals and exceptions are the lecture's summary of what leaks between "guests". The design fix is explicit virtualization with a context parameter (MPI's communicator).

## Worked Example

Ask the same program two questions.

| | API | Instruction set | Compatibility |
|---|---|---|---|
| C runtime | libc functions | — (native ISA used directly) | source, recompile |
| Java VM | Java class library | Java byte code | binary |
| QEMU / VMware / VirtualBox | emulated hardware interfaces | x86/x86_64 | binary |

"What can I call?" gives you the runtime system. "What can I execute?" gives you the virtual machine. A JVM answers both; libc answers only the first.

## Common Pitfalls

- **Equating the runtime system with a library.** `libc` is one implementation; the runtime is the service layer plus the interface contract.
- **Believing the OS abstraction is complete.** It is not — `man 2 signal` exists because signal semantics differ per system.
- **Thinking only managed languages have runtime systems.** C has one; it is just thin.
- **Assuming a crisp OS/runtime boundary.** The lecture says it is not clearly defined, which makes "is X part of the OS?" a discussion question, not a fact.

## Connections

- [[virtualization-vs-abstraction]] — the API/ISA distinction is that definition applied here.
- [[process-memory-layout]] — what the runtime's memory management operates on.
- [[dynamic-linking]] — how library code reaches a process at run time.
- [[errno-error-handling]], [[unix-signals]] — the C runtime's error surface, and its weakest point.
- [[exception-handling-implementation]] — where a runtime must supply what C lacks.

## Open Questions

- If the OS/runtime boundary is undefined, what is the exam-safe criterion — privilege level, address space, or interface ownership?
- The lecture calls C's non-virtualized services the "underlying weakness". Does a runtime that avoids libc entirely escape the interaction problems, or only move them?
