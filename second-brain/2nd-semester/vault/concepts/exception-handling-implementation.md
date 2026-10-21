---
title: "Exception Handling Implementation"
tags: [concept, virtual-machines, semester-2, exceptions]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[setjmp-longjmp]]"]
---

## One-line Summary
Exceptions are implemented so that code which never throws pays nothing: hardware and kernel raise `SIGSEGV`/`SIGFPE`, and the runtime finds the handler — via a dynamic stack of handlers, or a static table keyed on the faulting address.

## Core Intuition
The naive implementation tests before every risky operation: check the divisor, check the pointer — taxing code that never faults. Instead, let the *hardware* check for free — dereferencing NULL or dividing by zero traps by itself, the kernel turns the trap into a signal, and only then does the runtime pay. So the question is not "how do we detect the error" but "**given a fault at address x and type τ, which catch block owns it?**"

## Formal Definition / Statement

Many higher languages offer exceptions; they must be implemented efficiently by the runtime or virtual machine. "Efficiently" means **code which does not cause exceptions should not be slowed down by tests for possible exceptions** — no explicit check that a divisor is not 0, no explicit check that a pointer is not NULL. Compiler optimizations cover the rest — a pointer never changed needs a NULL check only at first dereference.

**Hardware** detects such faults; the kernel/runtime system delegates a signal to the process (`SIGSEGV`, `SIGFPE`); the jump is done with `longjmp` or similar.

**The responsible handler** has been installed last for the thrown type (**dynamic**), or is determined by the faulting instruction's address and the exception type (**static**).

**Dynamic stack of handlers.** Try blocks nest, so they form a stack at run time (last entered, first exited):

1. Entering try block *t*: for every catch block *cᵢ* push (τᵢ, αᵢ) — type handled, handler address.
2. Exiting *t*: pop its elements.
3. On an exception: search from the top for (τ, α) with matching type τ; let *t* be its try block; remove every handler above *t*'s and continue at α, removing the runtime stack frames too.

It grows and shrinks with try blocks and integrates into the runtime stack: each frame carries an "exception link" plus its (τ, α) pairs.

**Static table.** All handlers are listed in one table *E* of tuples (τ, α, β, ε): τ the handled type, α the handler address, [β, ε] the instruction-address range of the try block. For an exception of type *t* at address *x*, let

```
H := { h | h = (τ, α, β, ε) ∈ E, β ≤ x ≤ ε, t ≤ τ }
```

If H ≠ ∅, the handler is **min_τ max_β (H)** — innermost try block by max β, most specific type by min τ. If H = ∅ and *x* is in `main`, there is no handler. Otherwise let *x′* be the call site of the method containing *x* and repeat with *x := x′*.

## Key Properties

| runtime cost | dynamic | static |
|---|---|---|
| entry into try block | naïve O(c), optimized O(1) | none |
| exit from try block | O(k) | none |
| finding a handler | O(1) | naïve O(d·n), optimized (cf. tutorial) |
| jump to handler | O(1) | O(1) |

Parameters — static: *n* = total handlers. Dynamic: *k* = active catch blocks at the exception, *c* = catch blocks of the current try block, *d* = call-stack depth.

## Worked Example

```java
void f() { try { g() } catch(E e) { } catch(F f) { } }
void g() { try { ... } catch(E e) { } }
```

Dynamic: the stack reads, top down, `(E, g_catch_E)`, then `(F, f_catch_F)`, `(E, f_catch_E)`. If `g` throws `F`, the search skips `g`'s `E`, finds `(F, f_catch_F)` in `f`, and must pop `g`'s handler *and* frame before jumping.

Static: the throw at *x* in `g` is outside every try range of `g` handling `F`, so H is empty and the search repeats at *x′*, the call site of `g` inside `f`. There *x′* lies in `f`'s try range and F ≤ F, so `f_catch_F` is found. How to find it without walking the handler stack? The call-site chain in the return addresses.

## Common Pitfalls

- **Testing on the normal path.** The whole point is that non-throwing code carries no checks.
- **Confusing the two searches.** Dynamic walks a *stack of handlers*; static walks *call sites* through the table.
- **Forgetting frame removal.** Both schemes must unwind the runtime stack, not just the handler list.

## Connections

- [[setjmp-longjmp]] — the jump primitive; exception dispatch is a typed wrapper around it.
- [[unix-signals]] — where `SIGSEGV`/`SIGFPE` come from, and why only one handler per signal hurts.
- [[runtime-system]] — implementing this is a runtime-system job, not a compiler-only one.

## Open Questions

- The comparison slide's PDF text interleaves its cells; the rows above account for every cell once, but placing **O(k)** on "exit from try block" is a reconstruction.
- The optimised static variant is deferred to the tutorial ("optimized (cf. Tutorial)"); its cost is not given. Type matching uses "t ≤ τ", a subtype relation whose lattice is not discussed.
