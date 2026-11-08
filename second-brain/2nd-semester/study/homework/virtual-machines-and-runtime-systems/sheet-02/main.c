/* Define _POSIX_C_SOURCE for nanosleep() */
#define _POSIX_C_SOURCE 199309L
#include <errno.h>
#include <stdio.h>
#include <time.h>

#include "threads.h"

/* Sleep for the given number of milliseconds.
 */
void sleepmillis(int millis) {
    struct timespec ts = {.tv_sec = 0, .tv_nsec = millis * 1000000L};
    int res;
    do {
        /* When nanosleep is interrupted by a signal, it
         * returns the remaining time in the second argument,
         * so we repeat the call finish the waiting time.
         */
        res = nanosleep(&ts, &ts);
    } while (res == -1 && errno == EINTR);
}

/*
 * thread0 and thread1: Example for (a)
 */
void thread1(void) {
    printf("thread1: before schedule\n");
    schedule();
    printf("thread1: before 2nd schedule\n");
    schedule();
    printf("thread1: end\n");
}

void thread0(void) {
    printf("thread0: before new_thread\n");
    new_thread(thread1);
    printf("thread0: before schedule\n");
    schedule();
    printf("thread0: end\n");
}

/*
 * print0 and print1: Exmaple for (b) and (c)
 */
void print1(void) {
    int i;
    for (i = 0; i < 10; i++) {
        printf("print1: i=%d\n", i);
        sleepmillis(10);
    }
}

void print0(void) {
    int i;
    new_thread(print1);
    for (i = 0; i < 10; i++) {
        printf("print0: i=%d\n", i);
        sleepmillis(10);
    }
}

int main(void) {
    /* (a): thread0 (and thread1) without timer-based
     * context switches.
     */
    init(thread0, 0);

    /* (b): timer-based context switches every
     * 15 milliseconds betweed print0 and print1.
     */
    init(print0, 15);

    return 0;
}
