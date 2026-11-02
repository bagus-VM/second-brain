#include <stdio.h>
#include <stdlib.h>

extern int etext, edata, end;

/* initialized data */
int value = 42;

/* uninitialized data */
int arr[1000];

int main(void) {
    void *heap_begin;

    heap_begin = malloc(1);

    printf("end of text: %p\n", &etext);
    printf("end of data: %p\n", &edata);
    printf("end of bss:  %p\n", &end);
    printf("beginning of heap: %p\n", heap_begin);
    printf("top of stack: %p\n", &heap_begin);

    return 0;
}
