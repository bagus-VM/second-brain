/* Virtual Machines and Runtime Systems — Exercise Sheet 2, Problem 3(c)
 *
 *   "printf is called in both print1 and print2 but printf is not reentrant.
 *    Why is the program incorrect and how can printf be used correctly?"
 *
 * This is the sheet's own threads.c used as the vehicle: two emulated threads,
 * each printing a long fixed-width record in a loop, with the ITIMER_REAL
 * switch set to 1 ms so that the timer fires *inside* printf often.
 *
 *   ./printf-race naive      switch happens inside the SIGALRM handler
 *   ./printf-race deferred   handler only raises a flag; the switch is taken
 *                            at a safe point between printf calls
 *
 * Build:  gcc -Wall -U_FORTIFY_SOURCE -o printf-race printf-race.c
 */
#define _POSIX_C_SOURCE 200809L
#include <alloca.h>
#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>

#define MAX_THREADS 2

static volatile int curr, numThreads;
static sigjmp_buf newThread, jmpbufs[MAX_THREADS];
static void (*newThreadFn)(void);
static void *dummy;

static volatile sig_atomic_t switch_requested;  /* deferred mode only */
static int deferred;                            /* 0 = naive, 1 = deferred */

void schedule(void) {
    if (sigsetjmp(jmpbufs[curr], 1) == 0) {
        curr = (curr + 1) % numThreads;
        siglongjmp(jmpbufs[curr], 1);
    }
}

void new_thread(void (*fn)(void)) {
    newThreadFn = fn;
    if (sigsetjmp(jmpbufs[curr], 1) == 0)
        siglongjmp(newThread, 1);
}

static void alarm_handler(int sig) {
    (void)sig;
    if (deferred)
        switch_requested = 1;   /* the ONLY thing this handler does */
    else
        schedule();             /* non-local jump out of the middle of printf */
}

static void take_safe_switch(void) {       /* a point where no stdio call is in flight */
    if (switch_requested) {
        switch_requested = 0;
        schedule();
    }
}

static void init(void (*fn)(void), int millis) {
    curr = 0;
    numThreads = 1;

    if (sigsetjmp(newThread, 1) == 0) {
        struct sigaction sa;
        memset(&sa, 0, sizeof sa);
        sa.sa_handler = alarm_handler;
        sigemptyset(&sa.sa_mask);
        sigaction(SIGALRM, &sa, NULL);

        struct timeval tv = {millis / 1000, (millis % 1000) * 1000};
        struct itimerval itv = {tv, tv};
        setitimer(ITIMER_REAL, &itv, NULL);

        fn();
    } else {
        curr = numThreads++;
        dummy = alloca(65536 * curr);
        newThreadFn();
    }

    --numThreads;
    for (int i = curr; i < numThreads; i++)
        memcpy(&jmpbufs[i], &jmpbufs[i + 1], sizeof(jmpbufs[i]));
    if (numThreads > 0) {
        curr %= numThreads;
        siglongjmp(jmpbufs[curr], 1);
    }

    struct itimerval off;
    memset(&off, 0, sizeof off);
    setitimer(ITIMER_REAL, &off, NULL);
}

/* One record is far longer than the stdio buffer worth of a single write(),
 * so a switch taken mid-call is visible in the byte stream. */
static void record(const char *who, int i) {
    /* 400 bytes, written with many separate stdio calls: a switch taken
     * mid-call lands inside the record rather than between records. */
    char hdr[16];
    snprintf(hdr, sizeof hdr, "%s %03d ", who, i);
    fputs(hdr, stdout);
    for (int k = 0; k < 200; k++) putchar('<');
    for (int k = 0; k < 200; k++) putchar('>');
    putchar('\n');
}

static void work_a(void);
static void work_b(void);

static void body(const char *who) {
    for (int i = 0; i < 200; i++) {
        record(who, i);
        if (deferred)
            take_safe_switch();       /* switch only where it is safe */

        /* burn some time so the 1 ms timer lands inside the next printf */
        struct timespec ts = {0, 300000};
        nanosleep(&ts, NULL);
    }
}

static void work_b(void) { body("B"); }
static void work_a(void) { new_thread(work_b); body("A"); }

int main(int argc, char **argv) {
    deferred = (argc > 1 && strcmp(argv[1], "deferred") == 0);
    init(work_a, 1);      /* 1 ms timer */
    return 0;
}
