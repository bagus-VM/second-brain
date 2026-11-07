#define _POSIX_C_SOURCE 200809L

/*
 * This implementation of exceptions is far from perfect.
 * It is intended as a demonstration of the principles of
 * exception handling.
 */

#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* Description of the exception handlers */
int n_handlers = 0;      /* number of installed handlers   */
sigjmp_buf handlers[3];  /* jmp_buf for jumping to handler */


/* Handler for error signals (e.g., SIGFPE) */
void exception_handler(int sig) {
    if (n_handlers > 0) {
        /* Remove the handler from the stack of handlers
         * and jump to the error handling routine.
         */
        n_handlers--;
        siglongjmp(handlers[n_handlers], 1);
    }

    fprintf(stderr, "Unhandled exception '%s'\n", strsignal(sig));
    abort();
}


/* Register a handler by appending it to the array of
 * registered handlers. Since we call 'sigsetjmp', we cannot implement
 * 'handle' as a function because there would be the additional
 * activation record for 'handle' on the stack (i.e.,
 * 'siglongjmp' would jump to a non-existing activation record
 * later).
 */
#define handle() (sigsetjmp(handlers[n_handlers++], 1))

/* Remove a handler from the stack of handers.
 * This function must be called at the end of each try block and
 * must not be called in the catch block (when an exception occurs,
 * the handler is removed automatically).
 */
void remove_handler(void) {
    n_handlers--;
}


volatile int zero = 0;
#define DIVIDE_BY_ZERO (2/zero)

void g() {
    if (handle() == 0) {                       // try {
         printf("%d\n", DIVIDE_BY_ZERO);
         remove_handler();
    } else {                                   // } catch (...) {
         printf("Exception caught in g()\n");
    }                                          // }
    printf("%d\n", DIVIDE_BY_ZERO);
}

void f() {
    if (handle() == 0) {                    // try {
        if (handle() == 0) {                //     try {
            printf("%d\n", DIVIDE_BY_ZERO);
            remove_handler();
        } else {                            //     } catch (...)
            printf("Inner exception caught in f()\n");
        }

        g();

        remove_handler();
    } else {                              // } catch (DivisionByZeroException e)
        printf("Exception caught in f()\n");
    }

    printf("%d\n", DIVIDE_BY_ZERO);
}

int main(int argc, char *argv[]) {
    struct sigaction sa;
    sa.sa_handler = exception_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    sigaction(SIGFPE,  &sa, NULL);

    f();

    return 0;
}
