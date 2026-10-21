---
title: "setjmp / longjmp"
tags: [concept, virtual-machines, semester-2, control-flow]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[process-memory-layout]]"]
---

## One-line Summary
`setjmp` snapshots the processor registers; `longjmp` restores them — giving C an untyped, uncontrolled non-local goto that works by moving RSP/RBP back and discarding the stack frames in between.

## Core Intuition
The valuable part of an exception is not the error object. It is the ability to leave several nested calls at once and land in a place that knows how to recover. C has no exceptions, but it does have the machine state, so it can offer the jump without the typing or the discipline.

The mechanism is almost embarrassingly direct: save the registers at the landing site, and later write them back. Because RSP and RBP are among them, the stack pointer returns to where it was — every frame pushed after that point becomes unreachable garbage. This is why the frame containing `setjmp` must still be alive: you are jumping *into* it.

## Formal Definition / Statement

The big advantage of exceptions is — in addition to typing of error classes — the possibility to perform **controlled non-local jumps** in the control flow. The C runtime system also offers non-local jumps, but these are **neither typed nor controlled**.

```c
int setjmp(jmp_buf env);            /* save execution context to env   */
int longjmp(jmp_buf env, int val);  /* restore it                      */
```

Execution returns to the `setjmp` call. `setjmp` returns **0** when `env` is initialised and **`val`** when it is reached again through a call to `longjmp`.

The execution context contains (mostly) the **processor registers**, but **not the program memory**.

**How it works:** `longjmp` resets the processor registers to the values they had when `setjmp` was called — in particular the instruction pointer (RIP on x86_64) and the stack-management registers (RBP and RSP). So execution jumps back to the `setjmp` call with the stack in the layout it had there, and the stack records of functions called between `setjmp` and `longjmp` are removed.

**Constraint:** the stack frame in which `setjmp` was called must still exist when `longjmp` is used, i.e. the function that called `setjmp` must not have ended.

## Key Properties

- **Untyped.** `val` is an `int`; there is no notion of an exception class or a matching `catch`.
- **Uncontrolled.** Nothing checks that the jump target is still valid or that the destination expects this error.
- **Stack-destructive.** Intermediate frames are not unwound — no destructors, no cleanup, no `fclose`.
- **Cheap.** Saving registers is a handful of stores; nothing is paid on the normal path.
- **The basis for everything else in this lecture.** Thread switching, signal-based error recovery and exception implementation are all built on this primitive.

## Worked Example

The slide's escape hatch:

```c
jmp_buf env;

void f(int arg) {
    ...
    if (some_error)
        longjmp(env, 1);
    ...
}

int main(void) {
    ...
    if (setjmp(env) == 0) {
        for (int i=0; i<10; i++)
            f(i);
    } else
        printf("Oops, f() failed\n");
    ...
}
```

`setjmp` runs once and returns 0, so the loop starts. On the third iteration `f` calls `longjmp(env, 1)`: RIP jumps back to the `setjmp` line, RSP/RBP are restored, `f`'s frame is gone, and `setjmp` now returns **1** — so the `else` branch runs. No `if` after each `f(i)` call, no error return threaded through the signature. The cost is that you cannot tell *which* failure happened except through `val`, and you cannot tell the compiler to check that you jumped to the right place.

**The local-variable trap:**

```c
int main(void) {
    jmp_buf env;
    int i = 42;
    if (setjmp(env) == 0) {
        i = 23;
        longjmp(env, 1);
    } else {
        printf("i = %d\n", i);
    }
}
```

Both **23 and 42** are possible. If the compiler keeps `i` in a processor register, `longjmp` resets that register to 42. If `i` lives on the stack, the memory cell still holds 23. Rule: **local variables modified between `setjmp` and `longjmp` must be declared `volatile`**, which keeps them in memory and out of registers.

## Common Pitfalls

- **Returning from the function that called `setjmp`.** The frame is gone; the jump lands in reused stack. Undefined.
- **Forgetting `volatile`.** The 42/23 ambiguity is a real, compiler-dependent bug, not a curiosity.
- **Using `longjmp` to leave a function with cleanup.** No stack unwinding happens, so every acquired resource leaks.
- **Passing `val == 0`.** `setjmp` returning 0 means "initialised"; a `longjmp(env, 0)` would be indistinguishable, so pass a non-zero value.

## Connections

- [[process-memory-layout]] — the stack region and RSP/RBP are the mechanism.
- [[unix-signals]] — a handler can `longjmp` out of a `SIGSEGV`, but the signal mask then needs explicit repair.
- [[thread-emulation-longjmp]] — jumping between stacks is exactly `longjmp` plus a relocated stack pointer.
- [[exception-handling-implementation]] — how a typed, controlled version is built on this primitive.
- [[virtual-machines-and-runtime-systems]] — course index.

## Open Questions

- The slide says the context contains "mostly" the registers. Which pieces are not registers (signal mask, floating-point state) is left open — and the answer decides whether `longjmp` after a signal is safe.
- Is the 42/23 outcome unspecified by the language, or only at `-O0`? The lecture says compiler-dependent without naming a flag.
