#include <stdio.h>
#include <stdlib.h>

extern int etext, edata, end;

void showaddrs(void) {
    void *heap_begin = malloc(1);

    printf("In libshowaddrs:\n");
    printf(" end of text: %p\n", &etext);
    printf(" end of data: %p\n", &edata);
    printf(" end of bss:  %p\n", &end);
    printf(" beginning of heap: %p\n", heap_begin);
    printf(" top of stack: %p\n", &heap_begin);
}
