#include <alloca.h>
#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>

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
 */
void schedule(void) { /* PLEASE IMPLEMENT */
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
            /* Install signal handler for SIGALRM here and
             * start timer (ITIMER_REAL with setitimer()).
             */
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
     */
    /* PLEASE IMPLEMENT */

    /* All other threads have finished. */
    if (timerMillis > 0) {
        /* Disable timer by setting its interval to 0. */

        /* PLEASE IMPLEMENT */
    }
}
