#include <stdio.h>
#include <stdlib.h>
#ifdef USE_DLOPEN
#include <dlfcn.h>
#endif

extern int etext, edata, end;

/* initialized data */
int value = 42;

/* uninitialized data */
int arr[1000];

#ifdef USE_DLOPEN
void (*showaddrs)(void);
#else
void showaddrs(void);
#endif

int main(void) {
    void *heap_begin = malloc(1);

#ifdef USE_DLOPEN
    void *hdl = dlopen("libshowaddrs.so", RTLD_LAZY);
    if (hdl == NULL) {
        fprintf(stderr, "Could not open libshowaddrs.so: %s\n", dlerror());
        exit(1);
    }
    dlerror();
    showaddrs = dlsym(hdl, "showaddrs");
    char *err = dlerror();
    if (err != NULL) {
        fprintf(stderr, "Could not lookup showaddrs(): %s\n", err);
        exit(1);
    }
#endif

    printf("In main:\n");
    printf(" end of text: %p\n", &etext);
    printf(" end of data: %p\n", &edata);
    printf(" end of bss:  %p\n", &end);
    printf(" beginning of heap: %p\n", heap_begin);
    printf(" top of stack: %p\n", &heap_begin);

    showaddrs();
    
#ifdef USE_DLOPEN
    dlclose(hdl);
#endif
    
    return 0;
}
