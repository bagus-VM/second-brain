/* showaddrs.c — the library required by Exercise Sheet 1, Problem 1.
 *
 * It declares the same linker-provided symbols as addrs.c and prints their
 * addresses from *inside the library*, so the main program and the library
 * can be compared.
 */
#include <stdio.h>

extern int etext, edata, end;

void show_addrs(const char *who) {
    printf("[%s] end of text: %p\n", who, (void *)&etext);
    printf("[%s] end of data: %p\n", who, (void *)&edata);
    printf("[%s] end of bss:  %p\n", who, (void *)&end);
}
