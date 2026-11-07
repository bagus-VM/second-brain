#define _POSIX_C_SOURCE 200809L

/*
 * The addresses of labels and the values put on the stack
 * (e.g., the frame pointer) are sensitive to optimizations.
 * Therefore, this code should be compiled without optimizations
 * (i.e., with -O0) so the compiler keeps the order of the labels
 * in functions and we can rely on the default layout of the
 * activation records.
 *
 * This implementation of exceptions is far from perfect.
 * It is intended as a demonstration of the principles of
 * exception handling.
 */

#include <limits.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define UNW_LOCAL_ONLY
#include <libunwind.h>

typedef struct {
    void *start;
    void *end;
    void *catch;
} hdl;

/* Description of the exception handlers */
int n_handlers = 0;      /* number of installed handlers   */
hdl handlers[3];

/*
 * Register an exception handler at 'catch' for the try block
 * between 'start' and 'end'. The function returns 'start' because
 * we need to make an indirect jump to the try block to prevent
 * the compiler from rearranging the jump labels (e.g., when 'end'
 * moves to a different location, the try block may no longer
 * be exactly in the range start..end.)
 */
static void *register_handler(void *start, void *end, void *catch) {
    for (int i=0; i<n_handlers; ++i) {
        if (handlers[i].start == start && handlers[i].end == end) {
            exit(1);
            return start;
        }
    }
    handlers[n_handlers].start = start;
    handlers[n_handlers].end   = end;
    handlers[n_handlers].catch = catch;
    ++n_handlers;
    return start;
}

/* Handler for error signals (e.g., SIGFPE) */
void exception_handler(int sig) {
    unw_cursor_t cursor;
    unw_context_t uc;
    unw_word_t ip;

    hdl *handler = NULL;

    unw_getcontext(&uc);
    unw_init_local(&cursor, &uc);
    while (unw_step(&cursor) > 0) {
        unw_get_reg(&cursor, UNW_REG_IP, &ip);

        fprintf(stderr, "Looking for handler for IP=%p:\n", (void *)ip);

        /* Search through the registered handlers. */
        for (int i=0; i<n_handlers; i++) {
            hdl *h = &handlers[i];
            fprintf(stderr, "  handler %d (for %p ... %p): ",
                    i, h->start, h->end);

            /* Check if the instruction address is between the bounds
             * for the exception handler.
             */
            if (h->start <= (void*)ip && (void*)ip < h->end) {
                fprintf(stderr, "yes\n");
                if (handler == NULL || handler->start < h->start || handler->end > h->end) {
                    handler = h;
                }
            } else {
                fprintf(stderr, "no\n");
            }
        }

        if (handler != NULL) {
            fprintf(stderr, "Innermost handler is %p...%p, catch=%p\n",
                    handler->start, handler->end, handler->catch);

            /* Unblock the signal that activated this signal handler. */
            sigset_t sigs;
            sigemptyset(&sigs);
            sigaddset(&sigs, sig);
            sigprocmask(SIG_UNBLOCK, &sigs, NULL);

            /* Continue execution of the main program in the stack frame
             * to which the found handler belongs; before, we set the
             * instruction pointer (IP) to the address of the "catch"
             * block of the found handler.
             */
            unw_set_reg(&cursor, UNW_REG_IP, (unw_word_t)handler->catch);
            unw_resume(&cursor);

            fprintf(stderr, "Oops, unw_resume(...) did not work?!\n");
            abort();
        }
    }

    /* No exception handler handles the error.
     * So we call abort() to terminate the program.
     */
    fprintf(stderr, "Unhandled exception '%s'\n", strsignal(sig));
    abort();
}


volatile int zero = 0;
#define DIVIDE_BY_ZERO (2/zero)

void g() {
    goto *register_handler(&&try, &&catch, &&catch);  // jumps to label "try"

try:                                       // try {
    printf("%d\n", DIVIDE_BY_ZERO);
    goto cont;
catch:                                     // } catch (...) {
    printf("Exception caught in g()\n");
cont:                                      // }
    printf("%d\n", DIVIDE_BY_ZERO);
}

void f() {
    register_handler(&&try2, &&catch2, &&catch2);
    goto *register_handler(&&try, &&catch, &&catch);  // jumps to label "try"

try:                                           // try {
try2:                                          //     try {
    printf("%d\n", DIVIDE_BY_ZERO);
    goto cont2;
catch2:                                        //     } catch (...) {
    printf("Inner exception caught in f()\n");
cont2:                                         //     }
    g();
    goto cont;
catch:                                         // catch (...) {
    printf("Exception caught in f()\n");
cont:                                          // }
    printf("%d\n", DIVIDE_BY_ZERO);
}

int main(void) {
    struct sigaction sa;
    sa.sa_handler = exception_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;

    sigaction(SIGFPE,  &sa, NULL);

    f();

    return 0;
}
