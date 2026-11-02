/* Virtual Machines and Runtime Systems — Exercise Sheet 2, Problem 3
 * threads.c with schedule() and init() implemented.
 *
 * Build (needs -U_FORTIFY_SOURCE, see the sheet's Makefile):
 *   zig cc -U_FORTIFY_SOURCE -o main main.c threads.c      (or gcc)
 *
 * The filled-in parts are marked [3a] and [3b].
 */
#define _POSIX_C_SOURCE 200809L   /* sigsetjmp/siglongjmp, setitimer, _exit */
#include <alloca.h>
#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>

#include "threads.h"

#define MAX_THREADS 3

static volatile int curr;               /* number of current thread */
static volatile int numThreads;         /* total number of threads  */
static sigjmp_buf newThread;            /* where we create new threads in init() */
static sigjmp_buf jmpbufs[MAX_THREADS]; /* saves the contexts of the threads */
static void (*newThreadFn)(void);       /* helper to pass the entry function to init() */

/*
 * Save the context of the current thread in 'jmpbufs' and
 * activate the next thread.
 *
 * [3a] Round-robin. sigsetjmp(..., 1) saves the signal mask too, and the
 * matching siglongjmp restores it, so a switch that happens inside the
 * SIGALRM handler does not leave SIGALRM blocked in the thread it resumes.
 * This is why the skeleton uses sigjmp_buf and not plain jmp_buf.
 */
void schedule(void) {
    /* The guard is the whole trick. sigsetjmp returns 0 when the context is
     * saved and 1 when it is resumed; without the `if`, a resumed thread would
     * fall straight through into the switch below and immediately schedule
     * again, so the program ping-pongs forever and never returns to its
     * callers.
     */
    if (sigsetjmp(jmpbufs[curr], 1) == 0) {
        curr = (curr + 1) % numThreads;     /* next thread, wrapping */
        siglongjmp(jmpbufs[curr], 1);       /* resume the next thread */
    }
    /* resumed: return to the caller of schedule() */
}

/*
 * Start a new thread with entry point 'threadFn'.
 */
void new_thread(void (*threadFn)(void)) {
    newThreadFn = threadFn;
    if (sigsetjmp(jmpbufs[curr], 1) == 0) {
        siglongjmp(newThread, 1);
    }
}

/* Dummy variable for the stack allocation in 'init'. */
static void *dummy;

/*
 * SIGALRM handler: the timer is what makes the switch automatic.
 * [3b] Nothing but schedule() here — it is a signal handler, so it must be
 * async-signal-safe, and schedule() itself already saves/restores the mask.
 */
static void alarm_handler(int sig) {
    (void)sig;
    schedule();
}

/*
 * Initialize the thread scheduler. The first thread
 * starts at 'threadFn'.
 * If 'timerMillis' is greater than 0, a timer is started
 * which calls schedule() every 'timerMillis' milliseconds.
 */
void init(void (*threadFn)(void), int timerMillis) {
    /* There is only one thread for now with ID 0. */
    curr = 0;
    numThreads = 1;

    if (sigsetjmp(newThread, 1) == 0) {
        if (timerMillis > 0) {
            /* [3b] Install the SIGALRM handler. SA_NODEFER would let SIGALRM
             * nest inside its own handler; we do NOT want that, the default
             * (SIGALRM blocked while the handler runs) is exactly right.
             * No SA_RESTART: unnoticed here, but consistent with nanosleep().
             */
            struct sigaction sa;
            memset(&sa, 0, sizeof sa);
            sa.sa_handler = alarm_handler;
            sa.sa_flags = 0;
            sigemptyset(&sa.sa_mask);
            if (sigaction(SIGALRM, &sa, NULL) == -1) {
                perror("sigaction");
                _exit(1);
            }

            /* [3b] ITIMER_REAL counts real time and delivers SIGALRM.
             * it_interval = period (automatic re-arm), it_value = first expiry.
             */
            struct timeval tv;
            tv.tv_sec = timerMillis / 1000;
            tv.tv_usec = (timerMillis % 1000) * 1000;
            struct itimerval itv;
            itv.it_interval = tv;
            itv.it_value = tv;
            if (setitimer(ITIMER_REAL, &itv, NULL) == -1) {
                perror("setitimer");
                _exit(1);
            }
        }

        /* We start the first thread. */
        threadFn();
    } else {
        /* new_thread() has been called to create a new thread,
         * so assign the next thread ID to 'curr'.
         */
        curr = numThreads++;

        /* To avoid overlaps in the stacks of the threads,
         * we let the stack pointers of different threads
         * point to locations 64k apart. (No thread should
         * use more than 64k stack, of course.)
         * We save the returned pointer in a dummy global variable
         * to prevent the compiler from optimizing the stack
         * allocation away.
         */
        dummy = alloca(65536 * curr);

        /* Run the new thread. */
        newThreadFn();
    }

    /* Remove current thread and continue scheduling
     * until only one thread remains.
     *
     * [3a] The thread's entry function returned: it is finished. Decrement
     * the thread count, SHIFT the surviving contexts down over the dead slot,
     * and hand the CPU to the next thread. When only one thread is left, there
     * is nobody to hand over to, so we fall through and return from init().
     *
     * The shift is not cosmetic. Slot indices and thread identity coincide, so
     * dropping the count without compacting makes `curr % numThreads` name a
     * *different* live thread than the one that just exited — and resuming it
     * means a siglongjmp into a frame that is no longer on the stack. That is
     * the segfault this program has if you skip the loop. memcpy, not
     * assignment: jmp_buf is an array type and the sheet says so explicitly.
     */
    --numThreads;
    for (int i = curr; i < numThreads; i++)
        memcpy(&jmpbufs[i], &jmpbufs[i + 1], sizeof(jmpbufs[i]));

    if (numThreads > 0) {
        curr %= numThreads;                 /* past-the-end wraps to slot 0 */
        siglongjmp(jmpbufs[curr], 1);
    }

    /* All other threads have finished. */
    if (timerMillis > 0) {
        /* Disable timer by setting its interval to 0. */
        struct itimerval off;
        memset(&off, 0, sizeof off);        /* it_interval = it_value = 0 */
        setitimer(ITIMER_REAL, &off, NULL);
    }
}