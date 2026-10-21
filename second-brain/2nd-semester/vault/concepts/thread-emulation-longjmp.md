---
title: "Thread Emulation with longjmp"
tags: [concept, virtual-machines, semester-2, threads]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[setjmp-longjmp]]"]
---

## One-line Summary
Threads can be emulated in plain C by keeping one `jmp_buf` per thread and jumping between them — the hard part is not the jump but giving each thread its own stack area, which `alloca` does by moving the stack pointer.

## Core Intuition
A context switch saves and restores registers and changes stack. `setjmp`/`longjmp` do the first two. The missing third: if two "threads" share one stack, their frames interleave and the first to return destroys the other's locals.

So: give each thread a region of stack, point RSP at it when the thread starts, and store each thread's `jmp_buf` in a table. `schedule()` becomes "save me into my slot, restore the next one" — a `longjmp` into a stack that was never unwound because it was never left.

## Formal Definition / Statement

`longjmp` allows non-local jumps. This makes it possible to **emulate threads (and co-routines) by jumping between the threads using `longjmp`**. The challenge lies in providing each thread with its own stack area.

```c
void *alloca(size_t size);
```

`alloca` allocates space dynamically **on the stack**; the allocation is valid until the end of the current function. Note: `alloca` is **not standardized** and its implementation is **compiler-dependent**.

The threads get separate stacks by having the stack pointer point to a different area of the stack (using `alloca`) when creating the threads — the slide's `alloca(65536*curr)` reserves a distinct 64 KiB block per thread index.

Threads are created with `new_thread`, and calling `schedule` switches execution between them. Some setup in `init` is necessary first.

## Key Properties

- **Green, not native.** The runtime system implements the context switch itself; the OS sees one thread. Such threads cannot use the concurrency of multicore processors — the lecture makes this the defining trade-off of green threads.
- **Stack per thread is mandatory.** Without it, frames of different threads overwrite each other.
- **`alloca` is the trick and the weakness.** It moves the stack pointer without a standard, so the program is compiler-dependent by construction.

## Worked Example

The slide's skeleton:

```c
int main(void) {
    init(thread0);
}

volatile int curr, numThreads;
jmp_buf newThread, jmpbufs[N];
void (*newThreadFn)(void);

void new_thread(void (*tFn)(void)) {
    newThreadFn = tFn;
    if (setjmp(jmpbufs[curr]) == 0)
        longjmp(newThread, 1);
}

void schedule(void) {
    /* save current thread to jmpbufs
     * and activate next thread */
}

void thread0(void) {
    ...
    new_thread(thread1);
    ...
    schedule();
    ...
}

void init(void (*threadFn)(void)) {
    curr = 0; numThreads = 1;
    if (setjmp(newThread) == 0)
        threadFn();
    else {
        curr = numThreads++;
        alloca(65536*curr);
        newThreadFn();
    }
    /* remove current thread from jmpbufs and activate one of
     * the remaining threads if the current thread is not the
     * last thread. */
}

void thread1(void) {
    ...
    schedule();
    ...
    schedule();
    ...
}
```

Read `init` as the thread factory. `setjmp(newThread)` marks the point every new thread returns to. The first time, it returns 0 and `threadFn()` (i.e. `thread0`) runs on the original stack. When `thread0` calls `new_thread(thread1)`, that saves the *current* thread into `jmpbufs[curr]` and `longjmp`s to `newThread` — so `init` resumes with return value 1, increments `numThreads`, calls `alloca(65536*curr)` to move the stack pointer into a fresh region, and enters `newThreadFn()`, which is `thread1`. `thread1` now runs on its own stack.

`curr` and `numThreads` are `volatile` for exactly the reason from [[setjmp-longjmp]]: they are modified between a `setjmp` and the matching `longjmp`, so they must stay in memory rather than in registers.

**Automatic scheduling:** the explicit `schedule()` calls can be automated by calling `schedule()` from a **signal handler for a timer event**. `setitimer` (`man 2 setitimer`) requests a periodic trigger of the timer signal. When signals are involved one should use `sigsetjmp`/`siglongjmp` so that blocking and unblocking of the timer signal after the jumps is handled correctly.

## Common Pitfalls

- **Forgetting `volatile` on `curr`/`numThreads`.** The scheduler then reads a stale register copy.
- **Sharing one stack.** The classic failure: threads appear to work until one returns.
- **Plain `setjmp` with a timer signal.** The mask state after the jump is wrong; use `sigsetjmp` with `savesigs`.
- **Assuming real parallelism.** Emulated threads on one stack-switching runtime run one at a time.
- **Relying on `alloca` portability.** The slide flags it as non-standard and compiler-dependent.

## Connections

- [[setjmp-longjmp]] — the mechanism, including the `volatile` trap that reappears here verbatim.
- [[unix-signals]] — the timer signal, the handler, and why `sigsetjmp` is required.
- [[process-memory-layout]] — the stack region each thread carves a slice out of.
- [[runtime-system]] — thread scheduling is the canonical *implicit* runtime service.
- [[virtual-machines-and-runtime-systems]] — course index.

## Open Questions

- `alloca(65536*curr)` grows with the thread index, so thread *n* reserves *n*×64 KiB — intended layout or slide simplification is not stated ("Details in the tutorial").
- The slide's `schedule()` body is elided. How the "next thread" is chosen — round robin, and what happens when a thread finishes — is left to the tutorial.
- Green threads block the whole process on a blocking syscall; the lecture's fix is non-blocking I/O with `SIGPOLL`. Whether the emulation here would need the same treatment is implied but not shown.
