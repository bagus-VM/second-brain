/* Virtual Machines and Runtime Systems — Exercise Sheet 2, Problem 1
 * printvar.c with tasks (a)-(d) solved.
 *
 * Build:  gcc -Wall -std=c99 -o printvar printvar.c
 * Run:    ./printvar      then press Ctrl+C
 *
 * Changes from the sheet's skeleton are marked [a] [b] [c] [d].
 */
#define _POSIX_C_SOURCE 200809L
#include <errno.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

static volatile sig_atomic_t counter;      /* [b] sig_atomic_t: the only type safe to share with a handler */
static volatile sig_atomic_t last_seen = -1;  /* [c] value the handler saw on the previous call */

/* [a] print the counter on SIGINT.
 * [c] terminate when two consecutive calls see the same value.
 * Only async-signal-safe calls belong here: write(2), not printf(3) — see
 * Problem 3(c) on this same sheet for why that distinction matters.
 */
static void sigint_handler(int sig) {
    (void)sig;

    char buf[64];
    int n = snprintf(buf, sizeof buf, "Counter is %d\n", (int)counter);
    if (n > 0 && (size_t)n < sizeof buf)
        (void)write(STDOUT_FILENO, buf, (size_t)n);   /* async-signal-safe */

    if (last_seen == counter) {                       /* [c] same value twice */
        static const char msg[] = "same value twice -> terminating\n";
        (void)write(STDOUT_FILENO, msg, sizeof msg - 1);
        _exit(0);                                     /* _exit, not exit: no atexit handlers */
    }
    last_seen = counter;
}

int main(void) {
    counter = 0;

    /* [a] install sigint_handler() as signal handler for SIGINT.
     * sigaction(), not signal(): defined semantics, and sa_mask lets us block
     * SIGINT inside the handler so a second Ctrl+C cannot nest inside it.
     */
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = sigint_handler;
    sa.sa_flags = 0;              /* no SA_RESTART: nanosleep must return EINTR */
    sigemptyset(&sa.sa_mask);
    sigaddset(&sa.sa_mask, SIGINT);
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    /* [b] the mask used to protect the increment */
    sigset_t block_sigint, old_mask;
    sigemptyset(&block_sigint);
    sigaddset(&block_sigint, SIGINT);

    while (true) {
        /* [b] critical section: block SIGINT, touch counter, unblock.
         * Without this the handler can fire between the load and the store of
         * ++counter and read a value the loop never held — and on a 32-bit
         * target it can read a half-written word.
         */
        if (sigprocmask(SIG_BLOCK, &block_sigint, &old_mask) == -1) {
            perror("sigprocmask");
            return 1;
        }
        ++counter;
        if (sigprocmask(SIG_SETMASK, &old_mask, NULL) == -1) {
            perror("sigprocmask");
            return 1;
        }

        struct timespec ts;
        ts.tv_sec = 1;
        ts.tv_nsec = 0;

        /* [d] nanosleep returns -1 with errno == EINTR when a signal arrives,
         * and writes the REMAINING time into the second argument. Restarting
         * with a fresh 1 s would lose that remainder and slow the clock down;
         * reusing ts keeps the period honest. The restart is also what stops
         * Ctrl+C from turning the loop into a busy-wait: without it, every
         * interrupt returns immediately and the counter races ahead — which is
         * why "press Ctrl+C twice quickly" never produced two equal values.
         */
        int r;
        do {
            r = nanosleep(&ts, &ts);
        } while (r == -1 && errno == EINTR);
    }

    return 0;
}