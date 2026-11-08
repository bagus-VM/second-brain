#define _POSIX_C_SOURCE 199309L
#include <errno.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>

volatile int finished;

void sig_handler(int sig) {
    switch (sig) {
    case SIGINT:
        printf("Interrupt received, quitting.\n");
        finished = 1;
        break;
    case SIGALRM:
        printf("2 seconds have passed...\n");
        break;
    }
}

int main(void) {
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = sig_handler;
    sa.sa_flags = 0;

    /* Register sig_handler() as handler for SIGINT and SIGALRM.
     * Block signal while each handler is active.
     */
    sigemptyset(&sa.sa_mask);
    sigaddset(&sa.sa_mask, SIGALRM);
    sigaction(SIGINT, &sa, NULL);

    sigemptyset(&sa.sa_mask);
    sigaddset(&sa.sa_mask, SIGINT);
    sigaction(SIGALRM, &sa, NULL);

    /* Start a timer (ITIMER_REAL, see  man 2 setitimer) which
     * fires SIGALRM every 2 seconds.
     */
    struct timeval tv = {.tv_sec = 2, .tv_usec = 0};
    struct itimerval itv = {.it_interval = tv, .it_value = tv};
    setitimer(ITIMER_REAL, &itv, NULL);

    while (!finished) {

        /* Sleep for 10 seconds; print a message every
         * time nanosleep() is interrupted by a signal.
         */
        struct timespec ts = {.tv_sec = 10, .tv_nsec = 0};
        int res;
        do {
            res = nanosleep(&ts, &ts);
            if (res == -1 && errno == EINTR)
                printf("nanosleep interrupted\n");
        } while (res == -1 && errno == EINTR && !finished);
    }

    return 0;
}
