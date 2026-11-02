/* Problem 2(b): does errno survive a signal handler? */
#define _POSIX_C_SOURCE 200809L
#include <time.h>
#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

static void handler_clobber(int sig) { (void)sig;
    /* a handler that calls a library function which sets errno */
    int fd = open("/definitely/not/here", O_RDONLY);
    if (fd >= 0) close(fd);
    /* no errno save/restore: whatever it just became is what it stays */
}
static void handler_safe(int sig) { (void)sig;
    int saved = errno;
    int fd = open("/definitely/not/here", O_RDONLY);
    if (fd >= 0) close(fd);
    errno = saved;                       /* restore */
}

static volatile sig_atomic_t fired;

int main(void) {
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = handler_clobber;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGALRM, &sa, NULL);

    /* create a distinctive errno value the caller will test afterwards */
    errno = EPIPE;
    printf("caller set errno = %d (%s)\n", errno, strerror(errno));

    raise(SIGALRM);      /* handler runs immediately, before the next statement */
    fired = 1;
    printf("after handler : errno = %d (%s)   <-- caller's value destroyed?\n",
           errno, strerror(errno));

    /* --- with the save/restore handler --- */
    sa.sa_handler = handler_safe;
    sigaction(SIGALRM, &sa, NULL);
    errno = EPIPE;
    printf("caller set errno = %d (%s)\n", errno, strerror(errno));
    raise(SIGALRM);
    printf("after handler : errno = %d (%s)   <-- saved and restored\n",
           errno, strerror(errno));

    /* the practical case: nanosleep interrupted, then errno tested */
    errno = 0;
    struct sigaction dagain;
    memset(&dagain, 0, sizeof dagain);
    dagain.sa_handler = handler_clobber;
    sigemptyset(&dagain.sa_mask);
    sigaction(SIGALRM, &dagain, NULL);
    alarm(1);
    struct timespec ts = {5, 0};
    int r = nanosleep(&ts, &ts);
    printf("nanosleep r=%d errno=%d (%s) -- the classic EINTR test\n",
           r, errno, strerror(errno));
    return 0;
}
