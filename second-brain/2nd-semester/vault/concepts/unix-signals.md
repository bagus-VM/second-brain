---
title: "Unix Signals"
tags: [concept, virtual-machines, semester-2, signals]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[errno-error-handling]]"]
---

## One-line Summary
A signal is an asynchronous message to a process that an event occurred; you ignore it, die from it, or run a handler — and if the handler must not return, it has to `longjmp`, which drags the signal mask along as a complication.

## Core Intuition
`longjmp` is a jump the program *asks for*. Signals are jumps the world inflicts: a timer fires, a child exits, a pointer dereferences NULL. The program has no say in when.

The tension is in the return path. A handler that returns puts control back at the interrupted instruction — right for a timer, absurd for `SIGSEGV`, where the instruction just faults again. So error signals must escape, and the escape (`longjmp`) does not restore the mask the kernel blocked on entry. That mismatch is the exam-relevant subtlety.

## Formal Definition / Statement

`longjmp` is for an **explicitly requested** non-local change of control flow. For **implicit** exceptions there is the signal mechanism: **a signal is a message to a process that a certain event has occurred.**

Typical signals: `SIGSEGV` (illegal memory access / segmentation fault), `SIGBUS` (bus error), `SIGILL` (illegal instruction), `SIGFPE` (arithmetic error), `SIGINT` (Ctrl+C), `SIGHUP` (connection loss to the terminal), `SIGTERM`/`SIGKILL` (termination by "term"/"kill"), `SIGALRM` (timer interrupt), `SIGCHLD` (child process exit), `SIGPIPE` (broken pipe).

**Three responses:** the signal is ignored; it causes program termination (sometimes with a core dump); a user-defined handler is called. The default for most signals is **termination** — only `SIGCHLD` is ignored by default. Stop and continue signals halt or resume execution (e.g. a shell stopping the foreground process on Ctrl+Z).

**Blocking:** signals can be blocked temporarily, delaying handling until unblocked — `sigprocmask`. Details: `man 7 signal`.

**Installing handlers:** `signal()` has different semantics on different systems. Better:

```c
struct sigaction {
    void  (*sa_handler)(int);
    void  (*sa_sigaction)(int, siginfo_t *, void *);
    sigset_t sa_mask;
    int   sa_flags;
};

int sigaction(int signum, const struct sigaction *act,
              struct sigaction *oldact);
```

`sigaction` installs the handler for `signum`: `sa_sigaction` when `SA_SIGINFO` is set in `sa_flags`, `sa_handler` otherwise. `sa_mask` lists signals to block *in addition to* `signum` while the handler runs; sets are manipulated with `sigemptyset`, `sigaddset`, etc.

```c
void intr_handler(int sig) {
    printf("Interrupt received, exiting.\n");
    exit(0);
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = intr_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    sigaction(SIGINT, &sa, NULL);
    while(1) { }
    return 0;
}
```

## Key Properties

- **Asynchronous.** The handler can run between any two instructions of the main program.
- **One handler per signal.** This is the root of the interaction problems: a C library and a high-level runtime may both want `SIGFPE`.
- **Blocked while handled.** The handled signal (and anything in `sa_mask`) is blocked during the handler; on a normal return the mask is restored automatically.
- **Not necessarily restartable.** A blocking call interrupted by a signal fails with `EINTR` unless `SA_RESTART` was set.

## Worked Example

When a handler exits normally, control returns to the interrupted instruction — sensible for timers, not for `SIGSEGV`: the handler should redirect control flow to an error routine via `longjmp`, after which normal operation resumes.

**The caveat:** the handled signal (and possibly others) is blocked while the handler executes. On a normal return the mask is unblocked automatically. When the handler uses `longjmp`, **the mask must be repaired explicitly** — with `sigprocmask` or `siglongjmp`.

```c
int sigsetjmp(sigjmp_buf env, int savesigs);
int siglongjmp(sigjmp_buf env, int val);
```

POSIX does not specify whether plain `longjmp` resets the mask to its state at `setjmp`. `sigsetjmp` makes it explicit: `savesigs = 0` leaves the mask unchanged, `savesigs ≠ 0` restores it.

**Reentrancy vs. thread safety.** A signal can enter a function in an overlapped fashion: main calls `malloc`; a signal arrives; the handler also calls `malloc`. POSIX does not guarantee this works — `malloc` manipulates global heap-management data, so behaviour is undefined. Handlers may use only **reentrant** functions.

- **Reentrant:** enterable several times *by the same thread*; implies no global modifiable data (except by atomic operations), no self-modifying code, no calls to non-reentrant functions.
- **Thread-safe:** callable *at the same time by different threads*.
- **Reentrant ⇒ thread-safe** (when resources such as files are handled like global data). **Thread-safe does not imply reentrant.**

## Common Pitfalls

- **Calling `printf`/`malloc` in a handler.** Not reentrant; undefined behaviour.
- **Assuming `longjmp` fixes the mask.** It does not; use `siglongjmp` or `sigprocmask`.
- **Using `signal()` for portability.** Semantics differ per system.
- **Equating thread safety with reentrancy.** A mutex-protected function is thread-safe and still not reentrant.

## Connections

- [[errno-error-handling]] — `EINTR` and `SA_RESTART` are where signals meet the return-value convention.
- [[setjmp-longjmp]] — the escape primitive handlers use.
- [[thread-emulation-longjmp]] — timer signals drive automatic scheduling; `sigsetjmp` is required there.
- [[exception-handling-implementation]] — `SIGSEGV`/`SIGFPE` are the hardware-detected exceptions.

## Open Questions

- Only `SIGCHLD` is ignored by default, yet stop/continue signals are also listed — where they sit in the "three responses" taxonomy is not spelled out.
- If `longjmp`'s effect on the mask is unspecified, what does a conforming program do where it happens to restore? "Always use `sigsetjmp`" is a safe rule, not a proof.
