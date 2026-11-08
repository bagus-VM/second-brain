---
title: "Exercise Sheet 2 — Signals, Threads (Solutions)"
tags: [homework, virtual-machines, semester-2, signals, threads]
course: "Virtual Machines and Runtime Systems"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[unix-signals]]", "[[thread-emulation-longjmp]]"]
---

# Virtual Machines and Runtime Systems — Exercise Sheet 2

Sheet: `02.pdf` (Größlinger, WS 2026/27), *"Sheet 2 (Signals, Threads)"*, due Thursday 29 October
18:00, discussion 30 October 2026. Hand-in is optional and source files only.

**Everything below was compiled and executed**, with `zig cc` (clang 21,
`x86_64-linux-gnu.2.35`) cross-compiled on Windows and run under WSL — the host has no gcc in
either environment. Recorded runs: `output-sheet02.txt`, `output-printf-race.txt` and the raw
race captures `naive-1..3.txt`, `deferred-1..2.txt`.

Files in this folder: `printvar.c` (Problem 1, tasks a–d), `threads.c` (Problem 3, `schedule`
and `init` implemented), `printf-race.c` + `check-printf-race.py` (Problem 3(c) evidence),
`errno-demo.c` (Problem 2(b) evidence), plus the sheet's own `main.c`, `threads.h`, `timer.c`,
`Makefile` and the untouched skeleton as `printvar-orig.c`.

---

## Problem 1 — Signals

### (a) Print the counter on SIGINT

```c
static volatile sig_atomic_t counter;

static void sigint_handler(int sig) {
    (void)sig;
    char buf[64];
    int n = snprintf(buf, sizeof buf, "Counter is %d\n", (int)counter);
    if (n > 0 && (size_t)n < sizeof buf)
        (void)write(STDOUT_FILENO, buf, (size_t)n);
}
...
struct sigaction sa;
memset(&sa, 0, sizeof sa);
sa.sa_handler = sigint_handler;
sa.sa_flags = 0;                    /* no SA_RESTART */
sigemptyset(&sa.sa_mask);
sigaddset(&sa.sa_mask, SIGINT);     /* block SIGINT inside the handler */
sigaction(SIGINT, &sa, NULL);
```

Three choices, each with a reason:

- **`sigaction`, not `signal`.** `signal()`'s semantics differ between systems; `sigaction`
  gives you `sa_mask`, which is how SIGINT is blocked while its own handler runs so a second
  Ctrl+C cannot nest inside the first.
- **`write`, not `printf`.** The handler runs asynchronously; `printf` is not on the
  async-signal-safe list. Problem 3(c) on this same sheet is about exactly that, and
  `printf-race.c` is the demonstration.
- **`sig_atomic_t`, not plain `int`.** It is the only type the C standard guarantees can be read
  or written atomically with respect to a signal.

### (b) Protect the variable with `sigprocmask`

```c
sigset_t block_sigint, old_mask;
sigemptyset(&block_sigint);
sigaddset(&block_sigint, SIGINT);

while (true) {
    sigprocmask(SIG_BLOCK, &block_sigint, &old_mask);
    ++counter;                                    /* critical section */
    sigprocmask(SIG_SETMASK, &old_mask, NULL);
    ...
}
```

`++counter` is a read, an increment and a write. A signal delivered between the read and the write
gives the handler a value the loop never held; on a 32-bit target the handler can even read a
half-written word. `SIG_BLOCK`/`SIG_SETMASK` with the saved mask is the standard idiom —
`SIG_SETMASK` (restore exactly what was there) rather than `SIG_UNBLOCK` (which would clobber a
mask set by an outer context).

### (c) Terminate when two consecutive handler calls see the same value

```c
if (last_seen == counter) { write(1, "same value twice -> terminating\n", 31); _exit(0); }
last_seen = counter;
```

**What you observe when you press Ctrl+C several times is that it usually does not terminate** —
which is the sheet's own observation, and the point of task (d). The reason is worth stating
carefully, because it is not the one students reach for first.

### (d) The real reason — `nanosleep` and `EINTR`

The skeleton's loop is:

```c
struct timespec ts = {1, 0};
nanosleep(&ts, &ts);          /* return value ignored */
```

`nanosleep` returns **−1 with `errno == EINTR`** when a signal arrives, and *immediately* — it does
not finish the second. The return value is ignored, so the loop does not sleep at all on that
iteration: it increments `counter` and calls `nanosleep` again, which is interrupted again if
another signal is pending, and so on. Pressing Ctrl+C twice in quick succession therefore drives
the counter forward at memory speed between the two presses, and the two handler calls almost
never see the same value. The fix is the standard restart-on-`EINTR` loop:

```c
int r;
do {
    r = nanosleep(&ts, &ts);
} while (r == -1 && errno == EINTR);
```

Reusing `ts` matters: on `EINTR`, `nanosleep` writes the *remaining* time into the second
argument, so restarting with a fresh `{1, 0}` would slow the clock down by the interrupted
fraction every time. The sheet's own `main.c` `sleepmillis()` uses the same idiom.

**Careful with the diagnosis.** The `EINTR` loop fixes the *spin*, but the "two equal values"
test still depends on the counter not advancing between the two handler calls. The run recorded in
`output-sheet02.txt` shows the compiled program behaving correctly for (a) and (b); (c) and (d)
are argued from the man page and from the code path, and the busy-wait is visible in the original
skeleton rather than measured here.

---

## Problem 2 — Reentrancy and signals

### (a) Thread-safe but not reentrant

**Thread-safe** means safe to call from two threads *concurrently*. **Reentrant** means safe to
call again *while a call to it is still in progress* — including from a signal handler, which
interrupts the same thread in the middle of the outer call.

Functions that lock to be thread-safe are exactly the ones that stop being reentrant, because the
interrupted call holds the lock:

| Function | Why thread-safe but not reentrant |
|---|---|
| `printf` / `fprintf` | takes stdout's lock and mutates the stream's buffer state; interrupting it and re-entering corrupts both |
| `malloc` / `free` | internal arena locks; re-entering from a handler that interrupted a half-finished allocation corrupts the heap |
| `strtok` | static internal state — the *same* limitation, with no lock at all |
| `readdir`, `gethostbyname`, `localtime` | return pointers into a shared static buffer |
| `rand`, `strerror` | shared internal state |

The distinction that matters: a thread-safe function can be *proved* safe by a lock, and a lock
does nothing against a signal, because the signal is delivered to the thread that already owns it.
Reentrancy requires no mutable shared state at all.

### (b) `errno` is a global, and that is a real bug in the shape of Problem 1

`errno` is a global variable. A signal handler that calls any library function may therefore
**overwrite the interrupted code's `errno`**, and the interrupted code then makes a decision on a
value that belongs to somebody else.

This is not hypothetical on this sheet. Problem 1(d)'s loop is:

```c
int r = nanosleep(&ts, &ts);
if (r == -1 && errno == EINTR) ...
```

If the handler called `printf` and `printf` set `errno` to anything other than `EINTR`, the
restart test reads the wrong value. **Any handler that calls library functions must save and
restore `errno`.**

`errno-demo.c` demonstrates it, and the recorded run is:

```
caller set errno = 32 (Broken pipe)
after handler : errno = 2 (No such file or directory)   <-- caller's value destroyed?
caller set errno = 32 (Broken pipe)
after handler : errno = 32 (Broken pipe)   <-- saved and restored
nanosleep r=-1 errno=4 (Interrupted system call) -- the classic EINTR test
```

A handler that calls `open("/definitely/not/here", …)` leaves `errno = ENOENT` (2) where the
caller had `EPIPE` (32). Wrapping the same body in `int saved = errno; … errno = saved;` leaves the
caller's value intact.

**One correction to the sheet's framing.** On modern glibc, `errno` is thread-local, so two real
threads do not clobber each other's `errno`. But a signal handler runs *in the same thread* as the
code it interrupts, so the thread-local storage is the same object — and the clobber above is
real. Thread-locality fixes a problem this exercise does not have; it does not fix the one it
does.

---

## Problem 3 — Threads

The skeleton provides `new_thread()` and half of `init()`; `schedule()` and the tail of `init()`
are to be filled in.

### (a) `schedule()` and the termination path

```c
void schedule(void) {
    if (sigsetjmp(jmpbufs[curr], 1) == 0) {
        curr = (curr + 1) % numThreads;
        siglongjmp(jmpbufs[curr], 1);
    }
}
```

The `if` is the whole trick. `sigsetjmp` returns 0 when the context is *saved* and 1 when it is
*resumed*; without the guard a resumed thread falls straight through into the switch below and
schedules again, so the program ping-pongs forever and never returns to its callers. With the
guard, a resumed thread simply returns from `schedule()` to whoever called it.

`sigsetjmp(..., 1)` / `siglongjmp` rather than plain `setjmp`/`longjmp` because the timer handler
switches threads from inside a signal handler: the saved-and-restored signal mask is what stops
SIGALRM from arriving still-blocked in the thread that gets resumed.

And the tail of `init()` — this is where the first version of this solution segfaulted:

```c
--numThreads;
for (int i = curr; i < numThreads; i++)
    memcpy(&jmpbufs[i], &jmpbufs[i + 1], sizeof(jmpbufs[i]));

if (numThreads > 0) {
    curr %= numThreads;
    siglongjmp(jmpbufs[curr], 1);
}
```

**The `memcpy` loop is not cosmetic.** Slot index and thread identity coincide, so decrementing
the count without compacting makes `curr % numThreads` name a *different* live thread than the one
that just exited — and resuming it means a `siglongjmp` into a frame that is no longer on the
stack. The first run of this solution printed

```
thread0: before new_thread
thread1: before schedule
thread0: before schedule
thread1: before 2nd schedule
thread0: end
timeout: the monitored command dumped core
```

— `thread1: end` never printed, and the program died in the handover. The `memcpy` (not
assignment: `jmp_buf` is an array type, which is exactly what the sheet's note warns about) fixes
it.

### (b) The timer

```c
static void alarm_handler(int sig) { (void)sig; schedule(); }

/* in init(), before starting the first thread */
struct sigaction sa;
memset(&sa, 0, sizeof sa);
sa.sa_handler = alarm_handler;
sa.sa_flags = 0;
sigemptyset(&sa.sa_mask);
sigaction(SIGALRM, &sa, NULL);

struct timeval tv = {timerMillis / 1000, (timerMillis % 1000) * 1000};
struct itimerval itv = {tv, tv};        /* it_interval = it_value = the period */
setitimer(ITIMER_REAL, &itv, NULL);
```

`ITIMER_REAL` counts real time and delivers SIGALRM. `it_interval` re-arms the timer
automatically, `it_value` is the first expiry. The default disposition of a blocked signal while
its handler runs is exactly what is wanted here — no `SA_NODEFER`, or the switch would re-enter
itself.

And at the end of `init()`, when every other thread has finished:

```c
struct itimerval off;
memset(&off, 0, sizeof off);            /* it_interval = it_value = 0 */
setitimer(ITIMER_REAL, &off, NULL);
```

The recorded run (`output-sheet02.txt`) shows both halves working:

```
thread0: before new_thread
thread1: before schedule
thread0: before schedule
thread1: before 2nd schedule
thread0: end
thread1: end
print1: i=0
print1: i=1
print0: i=0
print0: i=1
print1: i=2
print0: i=2
...
print1: i=9
print0: i=9
```

Both threads run, the round-robin switches where the calls ask for it, the timer interleaves the
rest, and the program exits cleanly with code 0. Note the *imperfect* interleaving —
`print1: i=3, print1: i=4` in a row — which is expected: the 15 ms timer and the 10 ms sleeps do
not line up, and a context switch only happens when the timer fires.

### (c) Why `printf` in both threads is incorrect, and what to do about it

`printf` is *thread-safe* (it takes a lock) but **not reentrant** and not async-signal-safe. The
switch is taken from inside the SIGALRM handler, so the handler can jump away **while a `printf`
call is in progress**, leaving stdio's internal state — the buffer write pointer, the stream's
lock, the `FILE` flags — mid-update. The resumed thread then calls `printf` on the same stream.
Because both emulated threads are the same OS thread, the lock provides no protection at all: it
is already held, by the very context that was interrupted.

**The measurement.** `printf-race.c` runs two emulated threads, each writing 400-byte records,
with the timer at 1 ms, in two modes. `check-printf-race.py` counts complete records, torn records
and duplicated work. Two threads × 200 records means 400 records and 162,800 bytes for a correct
run:

```
file                    bytes  complete  markers   torn  dup pairs  max rep
---------------------------------------------------------------------------
naive-1.txt            277281       676      742     66        362        2
naive-2.txt            274813       670      735     65        362        2
naive-3.txt            278069       674      741     67        361        2
deferred-1.txt         162800       400      400      0          0        1
deferred-2.txt         162800       400      400      0          0        1
```

Read the naive rows: **742 markers where 400 were written**, **66 records torn apart mid-write**,
and **362 records emitted twice** — the emulated threads ran their loops roughly twice over. The
extra work is the giveaway: a `siglongjmp` out of the middle of stdio, followed later by a
`schedule()` that re-saves a `jmp_buf` while a jump into it is in flight, resurrects a stale
context and re-runs code. On glibc the damage is duplicated and interleaved output rather than a
crash; on another libc, or at another optimisation level, the same window is a corrupted stream.

**The fix that the measurement confirms — defer the switch to a safe point:**

```c
static volatile sig_atomic_t switch_requested;

static void alarm_handler(int sig) { (void)sig; switch_requested = 1; }   /* and nothing else */

/* between operations, where no stdio call is in flight */
static void take_safe_switch(void) {
    if (switch_requested) { switch_requested = 0; schedule(); }
}
```

Exactly 400 complete records, no torn records, no duplicated work, and **byte-identical across
runs** — determinism is the point: the switch can no longer land in an unpredictable place.

**The two other correct answers**, for completeness:

- **Use only async-signal-safe output.** `write(2)` instead of `printf`, which is what Problem
  1(a)'s handler does. This does not make the *thread* logic safe; it removes stdio from the
  interrupted region.
- **Block the timer around the stdio call.** `sigprocmask` SIGALRM blocked, `printf`, unblock.
  This works but is easy to get wrong (the mask must be restored, and the pending signal is
  delivered the moment it is unblocked, which just moves the switch), so the deferred-flag version
  is preferred.

What must *not* be concluded from the "thread-safe" label is that `printf` is safe here. Thread
safety is about concurrency; this is about interruption of the same thread.

## Connections

- [[unix-signals]] — the signal mechanism, handlers, and the mask complication with `longjmp`.
- [[thread-emulation-longjmp]] — the `alloca`-based stack trick the skeleton's `init()` uses.
- [[setjmp-longjmp]] — `sigsetjmp`/`siglongjmp` and why the mask is saved here.
- [[signal-safety-and-async-reentrancy]] — thread-safe versus reentrant, and the
  async-signal-safe rules.
- [[errno-error-handling]] — `errno` and the `EINTR` idiom this sheet's tasks (b) and (d) turn on.
- [[exception-handling-implementation]] — the high-level-language counterpart of the signal
  mechanism.
- [[virtual-machines-and-runtime-systems-exercise-2]] — the session page.

## Open Questions

- **Tasks (c) and (d) were not exercised interactively.** "(c) what do you observe when you press
  Ctrl+C several times" needs a terminal and real key presses; the compiled program is in this
  folder and the diagnosis is from the code path and the `nanosleep` man page, not from a recorded
  Ctrl+C sequence. This is flagged rather than papered over.
- **The damage in 3(c) is noisy because it is timing-dependent, and the numbers are presented as
  three runs, not as a rate.** 66 torn records out of 742 markers is not a probability; the window
  depends on where the 1 ms timer lands. The deferred version's byte-identical runs are the solid
  half of the evidence.
- **The `-U_FORTIFY_SOURCE` flag in the sheet's `Makefile` is explained by a comment but not
  tested here.** The comment says gcc's `longjmp` hardening checks that the stack pointer moves
  upwards and this program moves it downwards. The build here used clang via `zig cc`, which does
  not implement that check; the flag was passed anyway, and the program runs.
- **The sheet asks for `memcpy` when copying `jmp_buf` values but does not say why**, beyond "not
  guaranteed to work". The reason is that `jmp_buf` is an array type, arrays are not assignable in
  C, and what looks like assignment is a struct copy whose validity depends on the
  implementation's internal layout.
- **The skeleton's `sigjmp_buf newThread` is a single shared buffer**, so `new_thread()` can only
  be called from one thread at a time. This is fine for the sheet's examples and would break for
  nested thread creation; the sheet does not discuss it.
