#define _POSIX_C_SOURCE 199309L
#include <errno.h>
#include <signal.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

static int counter;

static void sigint_handler(int sig) {
    printf("Counter is %d\n", counter);
}

int main() {
    counter = 0;

    // install sigint_handler() as signal handler for SIGINT (Ctrl+C)

    while (true) {
        ++counter;

        // sleep for one second
        struct timespec ts;
        ts.tv_sec = 1;  // 1 second
        ts.tv_nsec = 0; // 0 nanoseconds
        nanosleep(&ts, &ts);
    }

    return 0;
}
