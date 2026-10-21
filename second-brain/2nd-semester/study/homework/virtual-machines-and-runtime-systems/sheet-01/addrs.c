/* addrs.c — Exercise Sheet 1, Problem 1.
 *
 * Prints the segment boundaries of the program itself, then asks the library
 * to print its own view of the same symbols.
 *
 * Three builds (see Makefile):
 *   make static   -> linked against libshowaddrs.a
 *   make dynamic  -> linked against libshowaddrs.so at link time
 *   make dlopen   -> not linked at all; loaded at run time with dlopen/dlsym
 */
#include <stdio.h>
#include <stdlib.h>

#include "showaddrs.h"

#ifdef USE_DLOPEN
#include <dlfcn.h>
#endif

extern int etext, edata, end;

/* initialized data */
int value = 42;

/* uninitialized data */
int arr[1000];

static void print_own(void) {
    printf("[main] end of text: %p\n", (void *)&etext);
    printf("[main] end of data: %p\n", (void *)&edata);
    printf("[main] end of bss:  %p\n", (void *)&end);
}

int main(void) {
    void *heap_begin = malloc(1);

    print_own();
    printf("[main] beginning of heap: %p\n", heap_begin);
    printf("[main] top of stack: %p\n", (void *)&heap_begin);

#ifdef USE_DLOPEN
    void *hdl = dlopen("./libshowaddrs.so", RTLD_LAZY | RTLD_LOCAL);
    if (hdl == NULL) {
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        return 1;
    }
    dlerror(); /* clear any previous error */
    void (*fn)(const char *) = (void (*)(const char *))dlsym(hdl, "show_addrs");
    char *err = dlerror();
    if (err != NULL) {
        fprintf(stderr, "dlsym failed: %s\n", err);
        dlclose(hdl);
        return 1;
    }
    fn("lib");
    printf("[main] library function at: %p\n", (void *)fn);
    dlclose(hdl);
#else
    printf("[main] show_addrs (library code): %p\n", (void *)show_addrs);
    show_addrs("lib");
#endif

    return 0;
}
