---
title: "Signal Safety and Async Reentrancy"
tags: [concept, virtual-machines, semester-2, signals, threads]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-30
prerequisites: ["[[unix-signals]]", "[[errno-error-handling]]", "[[thread-emulation-longjmp]]"]
---

## One-line Summary
Thread-safe and reentrant are two different guarantees — one about concurrent threads, one about nested activations of the same function — and a signal handler is the environment where the difference decides whether your program corrupts itself.

## Core Intuition

A function has one body of code but can have several *activations* alive at once. Threads create
them in parallel; signals create them nested — the main flow stops mid-instruction and the
handler runs on top of it. A function is safe in the first world (thread-safe) if its shared
state is protected by locks; it is safe in the second (reentrant) if a second activation cannot
corrupt the first. Locks do **not** make a function reentrant — a handler that calls a locked
function can deadlock on a lock the interrupted code already holds. And a function whose
"thread-safety" comes from writing results into static buffers (`readdir`, `strtok`,
`localtime`) is thread-safe-ish but not reentrant at all: the nested activation overwrites the
very buffer the interrupted call is about to read.

The C standard solves the "what may a signal handler call" question with a whitelist: the
**async-signal-safe** functions (`man 7 signal-safety`). The rule of thumb behind the list: a
function is async-signal-safe only if it touches no global or static state that another
activation could be using — which is why `write` is on the list and `printf` is not (`printf`
owns stdio buffers), why `malloc` is not (it manipulates global heap metadata), and why anything
that can set `errno` must be wrapped in a save-and-restore.

## Formal Statement

- **Reentrant**: a function can be interrupted mid-execution and called again from the
  interrupting context, and both activations complete correctly. The requirement: no static or
  globally shared, mutable state; all state lives on the stack or is passed in.
- **Thread-safe**: a function works correctly when invoked concurrently from several threads.
  Achieved by locks, atomics, or thread-local storage — none of which implies reentrancy.
- **Async-signal-safe**: a function may be called from a signal handler. The set is small and
  enumerated; everything else is a corruption risk.

The shared-variable rule pairs with this: the only type the C standard guarantees can be read
and written atomically with respect to a signal is `volatile sig_atomic_t`. A plain `int`
counter shared between a loop and a handler is a race by definition.

`errno` gets its own clause: a handler may call functions that set `errno`, but must save it on
entry and restore it on exit, or the interrupted code's error report is destroyed.

## Key Properties

- **Thread-safe ⊅ reentrant.** A mutex-protected function is thread-safe; the same mutex makes
  it deadly to call from a handler.
- **The distinguishing test is static state.** Where does a second activation write? If the
  answer is "a buffer the first activation owns", the function is not reentrant.
- **Async-signal-safe is a whitelist, not a property you can eyeball** — though "no static
  state, no locks, no stdio, no memory allocation" is the reliable heuristic.
- **`sig_atomic_t` is the contract for handler-shared data**; anything larger or compound needs
  the signal blocked during access (`sigprocmask`), which is Sheet 2's own fix.

## Worked Example

Sheet 2's Problem 3(c) is the demonstration in miniature: `print1` and `print2` both call
`printf`, and a `SIGALRM` timer can preempt either thread-body *inside* `printf` — one
activation mid-way through filling a stdio buffer, the other starting on the same global
buffer state. The recorded runs in `study/homework/virtual-machines-and-runtime-systems/sheet-02/`
(`printf-race.c`, `check-printf-race.py`, `output-printf-race.txt`) capture the corruption. The
same sheet's Problem 1(a) shows the correct pattern: the handler writes with `write` into a
stack buffer and touches only a `volatile sig_atomic_t` counter, and Problem 2(b) answers the
`errno` clause.

## Common Pitfalls

- **Calling `printf`/`malloc`/`exit` from a handler** because "it compiles". Compilation says
  nothing; the whitelist is a runtime-corruption contract.
- **Forgetting the `errno` save/restore** in a handler that calls any runtime function.
- **Sharing a plain `int` between loop and handler** instead of `volatile sig_atomic_t`, or
  sharing anything compound without `sigprocmask` protection.
- **Equating "I added a mutex" with reentrancy** — the mutex is exactly what the nested
  activation cannot take.

## Connections

- [[unix-signals]] — the delivery mechanism that creates the nested activation.
- [[errno-error-handling]] — the global the handler must not clobber; the EINTR idiom.
- [[thread-emulation-longjmp]] — the user-space threads whose timer preemption makes 3(c) real.
- [[setjmp-longjmp]] — the jump primitive that performs the switch.
- [[exception-handling-implementation]] — the high-level-language counterpart of the same
  interruption problem.

## Open Questions

- The thread-local implementation of `errno` (it cannot be a plain global in a threaded program)
  is not discussed in the lecture material.
- Which fix the course prefers for non-reentrant calls under preemption — blocking signals
  around the call, or async-signal-safe substitutes — is not stated; Sheet 2 accepts the
  question as open ("how can printf be used correctly?").
