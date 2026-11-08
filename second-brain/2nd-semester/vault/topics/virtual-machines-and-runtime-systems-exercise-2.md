---
title: "Virtual Machines and Runtime Systems — Exercise Sheet 2 Overview (Signals, Threads)"
tags: [topic, virtual-machines, semester-2, exercise, signals, threads]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-30
prerequisites: ["[[unix-signals]]", "[[thread-emulation-longjmp]]"]
---

## One-line Summary
Three problems that turn the runtime-system lectures into running code: a signal-safe counter
program, the reentrancy rules that decide what a signal handler may call, and a user-space
thread package built on `longjmp` and driven by a `SIGALRM` timer.

## Core Map

```
Exercise Sheet 2 (due 29.10.2026 18:00, discussion 30.10.2026) — Signals, Threads
│
├── Problem 1 — Signals (printvar.c)
│   ├── (a) print the counter on SIGINT (Ctrl+C)
│   ├── (b) protect counter with sigprocmask — deactivate interruptions
│   │       temporarily around the loop's access
│   ├── (c) terminate when the counter is unchanged across two handler
│   │       calls — and observe why Ctrl+C twice usually fails
│   └── (d) the culprit is nanosleep's EINTR semantics — read the man
│           page and fix it
│       └── → [[unix-signals]]
│
├── Problem 2 — Reentrancy and Signals
│   ├── (a) functions that are thread-safe but NOT reentrant
│   └── (b) errno is a global variable — what does that imply for
│           signal handlers calling C runtime functions?
│       └── → [[errno-error-handling]]
│
└── Problem 3 — Threads (threads.c)
    ├── (a) implement schedule and init in the longjmp skeleton
    ├── (b) install a SIGALRM timer (timer.c example) calling schedule —
    │       automatic switching; pay attention to the signal mask
    └── (c) printf in both print1 and print2 — printf is not reentrant:
            why is the program incorrect, and how can printf be used
            correctly?
        └── → [[thread-emulation-longjmp]] [[setjmp-longjmp]]
```

## Key Concepts at a Glance

| Page | What the sheet exercises |
|------|--------------------------|
| [[unix-signals]] | Delivery, handlers, masks — and the async-signal-safe rules Problem 1 lives under |
| [[errno-error-handling]] | The global `errno` and why a handler that disturbs it corrupts the interrupted code |
| [[setjmp-longjmp]] | The non-local jump primitive the thread skeleton is built from |
| [[thread-emulation-longjmp]] | The lecture's user-space threads: `jmp_buf` contexts, cooperative `schedule`, preemptive timer |
| [[runtime-system]] | The C runtime surface (stdio, errno, sleep) whose reentrancy rules the sheet probes |

## Exercise Structure

**Problem 1 — signals around a counter.** `printvar.c` increments a counter once per second.
(a) add a `SIGINT` handler that prints the current counter. (b) the loop and the handler both
touch `counter` — protect it by blocking interruptions temporarily with `sigprocmask`
(`man sigprocmask`, `man sigsetops`). (c) extend the handler so the program terminates when the
counter has the *same* value in two consecutive handler calls — i.e. two quick Ctrl+C should
kill it — and observe what actually happens. (d) the observation is explained by `nanosleep`'s
**EINTR** semantics: the sleep is interrupted, the loop continues, the counter moves on — so the
second Ctrl+C usually arrives during a fresh second. The fix comes from the man page.

**Problem 2 — reentrancy, in two questions.** (a) name functions that are thread-safe but not
reentrant (the classic family: functions returning pointers into static state — `readdir`,
`strtok`, `localtime` — thread-safe only via locks or TLS, not reentrant because a second
activation clobbers the first's state). (b) `errno` is a global variable: a signal handler that
calls any runtime function may overwrite it, so the interrupted code's error report is destroyed
unless the handler saves and restores `errno`.

**Problem 3 — threads by `longjmp`.** The Stud.IP skeleton emulates threads with `setjmp`/
`longjmp` as presented in the lecture. (a) fill in `schedule` and `init` in `threads.c`. (b)
install a timer in `init` and a `SIGALRM` handler (pattern in `timer.c`) that calls `schedule`,
giving automatic preemption — *"pay attention to the signal mask"*. (c) both thread bodies call
`printf`, which is not reentrant: the program can interleave a `printf` call mid-flight with
another one switching in at the timer signal, so buffered state is used from two activations at
once. The sheet asks why that is incorrect and how `printf` can be used correctly. A stated
note: never assign `jmp_buf`s (`jmpbufs[0] = jmpbufs[1]`); use `memcpy`.

Hand-in is **optional**, via the "Submissions" folder in Stud.IP, source files only.

The full worked solutions — compiled with `zig cc`, run under WSL, with recorded output — are in
`study/homework/virtual-machines-and-runtime-systems/sheet-02/` (`solution.md`, `printvar.c`,
`threads.c`, `printf-race.c` with `check-printf-race.py` as the Problem 3(c) evidence,
`errno-demo.c` for 2(b), and the raw race captures `naive-*.txt`, `deferred-*.txt`).

## Exam-Relevant Points

1. **`sigaction` vs `signal`, and `sa_mask`** — blocking SIGINT inside its own handler so a
   second Ctrl+C cannot nest is (b)'s mechanism, and it is examinable as a pattern.
2. **`sig_atomic_t`** — the only type the C standard guarantees can be read/written atomically
   with respect to a signal; the handler/loop shared variable must use it.
3. **EINTR semantics** — interrupted system calls are the entire content of 1(c)→1(d): the
   observation (Ctrl+C twice usually fails to terminate) follows from `nanosleep` returning
   early, and the man page is the named source.
4. **Thread-safe ≠ reentrant** — 2(a) is the definitional question; static state is the
   distinguishing factor.
5. **`errno` in handlers** — save and restore it, or call nothing that touches it; 2(b) is a
   one-sentence answer with real consequences.
6. **The `longjmp` thread skeleton is the lecture, made code** — `schedule`'s context switch,
   the timer-driven preemption, and the signal-mask bookkeeping around it are the examinable
   core of Problem 3.
7. **Why `printf` breaks under timer preemption** — it is the concrete instance of 2(a)/2(b):
   non-reentrant, buffered, global state. "How can printf be used correctly" points at
   synchronisation/blocking signals around the call (or async-signal-safe alternatives such as
   `write`).

## Connections

- [[virtual-machines-and-runtime-systems-exercise-1]] — the previous sheet: dynamic linking and
  the mini-JIT; same folder convention in `study/homework/`.
- [[virtual-machines-and-runtime-systems-lecture-2]] — the C runtime system lecture this sheet
  applies.
- [[thread-emulation-longjmp]], [[setjmp-longjmp]] — the lecture material Problem 3 implements.
- [[unix-signals]], [[errno-error-handling]] — the concept pages behind Problems 1 and 2.
- `study/homework/virtual-machines-and-runtime-systems/sheet-02/` — the worked solutions and
  their recorded output.
- The sheet's own materials live in
  `raw/lectures/Virtual Machine and Runtime System/Ubung/Sheet_2_Signals,_Threads-_discussion_on_October_30/`
  (`02.pdf` plus the Stud.IP skeleton: `main.c`, `printvar.c`, `threads.c`/`threads.h`,
  `timer.c`, `Makefile`).

## Open Questions

- **1(c)'s "what do you observe"** is a measurement question — the answer depends on timing, and
  the sheet gives no expected output; the homework's recorded race captures fill that gap.
- **2(a) asks for "examples" without naming any** — which functions count as thread-safe but not
  reentrant is left to the student's C library knowledge.
- **3(c)'s "how can printf be used correctly"** admits several answers (block signals around the
  call, lock, use `write`); the sheet does not say which level of fix it expects.
- **The hand-in is optional and ungraded**, so the tutorial discussion on 30.10 is the only
  feedback channel.
