---
title: "errno and C Error Handling"
tags: [concept, virtual-machines, semester-2, error-handling]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[runtime-system]]"]
---

## One-line Summary
C has no exceptions, so functions report failure through their return value and stash the reason in the global `errno` — and the two must be read in that order, or you will report errors that never happened.

## Core Intuition
Every error-handling design has to answer "what went wrong?" without a return channel for it. C's answer is a side channel: one global integer that the failing call writes. Because it is global and *not cleared* on success, it is a stale-value trap — a function can succeed and leave a non-zero `errno` behind from some internal probe.

So the discipline is: **check the return value first, `errno` second, and only inside the failure branch.** The `errno = 0` idiom exists, but only for functions whose failure value collides with a legal success value.

## Formal Definition / Statement

Because C does not have exceptions, most functions of the C runtime system signal errors through their return value. Often **-1 or NULL** indicates that an error has occurred. The cause can be determined from the global variable `int errno`.

```c
ssize_t res = read(fd, data, count);
if (res == -1) {
    fprintf(stderr, "Error number %d occurred.\n", errno);
}
```

Textual descriptions come from `char *strerror(int errnum)`, `void perror(const char *s)` (prints `s` plus the current message) and `void error(int status, int errnum, const char *fmt, ...)`.

**The wrong pattern** (seen in real code):

```c
errno = 0;
read(fd, ...);
write(fd, ...);
... /* more function calls that may set errno */
if (errno != 0) {
    /* some call has failed, handle errors */
}
```

This is **not correct**. `errno` can be set to a value other than 0 even when a function call succeeds. Therefore the return value almost always has to be checked *before* `errno` is inspected.

**The exception:** `getpriority` returns -1 both as an error indicator and as a legitimate scheduling priority of -1. There you must set `errno = 0` before the call, and check `errno` when -1 comes back. This is the one case where the "wrong" pattern is right — precisely because the return value is ambiguous.

**EINTR:** some runtime functions (those that call kernel functions) are interrupted when a signal arrives while they are executing. They exit with an error state and set `errno` to `EINTR` (interrupted system call). Such functions must (should) be called again:

```c
ssize_t res;
do {
    res = read(fd, buffer, count);
} while (res == -1 && errno == EINTR);
```

The loop condition retries only on `-1` **and** `EINTR`, so a genuine failure falls through and a short read is kept. When a handler is installed with `SA_RESTART`, some functions are restarted automatically when interrupted by that signal (`man 7 signal`).

## Key Properties

- **Return value is the signal, `errno` is the diagnosis.** Different information, not interchangeable.
- **`errno` is not reset by success.** Any function may leave a stale value; that is why "clear once, test at the end" fails.
- **EINTR is normal, not exceptional.** A signal during a blocking call is expected, so the retry belongs at the call site, not in the handler.
- **`SA_RESTART` trades control for convenience.** No retry loops, but also no chance to react to the interruption.

## Worked Example

```c
errno = 0;
int prio = getpriority(PRIO_PROCESS, pid);
if (prio == -1 && errno != 0)
    perror("getpriority");     /* -1 with errno == 0 is a real priority */
```

Two tests, both required: the return value alone cannot distinguish "error" from "priority -1", and `errno` alone is meaningless without the -1. This is the single documented case where the order is inverted.

For `read`, three outcomes need three branches: interrupted (retry, as in the loop above), failed (report with `perror`), and succeeded — possibly partially, so use `res`, not `count`. The anti-pattern `errno = 0; read(...); if (errno != 0)` collapses all three: it cannot separate "succeeded with dirty `errno`" from "failed", and it throws away the short-read information.

## Common Pitfalls

- **Setting `errno = 0` and testing it later.** The lecture calls this out explicitly as incorrect.
- **Ignoring the return value** and only inspecting `errno` — you cannot tell success from failure.
- **Not retrying on `EINTR`.** The call "fails" for a reason unrelated to your data.
- **Applying the `errno = 0` idiom everywhere** because `getpriority` needs it. It is the exception.

## Connections

- [[runtime-system]] — error handling is one of the C runtime's main tasks, and its weakest.
- [[unix-signals]] — `EINTR` is the interface between the signal mechanism and the `errno` convention.
- [[setjmp-longjmp]] — the non-local escape that `errno` cannot provide.
- [[exception-handling-implementation]] — what a language with real exceptions does instead.

## Open Questions

- The slide calls `errno` a global `int`. In a threaded program that cannot be literally true; the thread-local implementation is not discussed.
- `SA_RESTART` restarts "some functions" — which, and what happens to a partially completed `read`, is deferred to `man 7 signal`.
