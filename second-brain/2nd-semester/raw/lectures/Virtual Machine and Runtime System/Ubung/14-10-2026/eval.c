/*
 * Remember to use the flags
 *    -ldl -Wl,-rpath,.
 * when compiling/linking. "-ldl" is necesarry to make dlopen() available,
 * "-rpath,." to make dlopen() look in the current directory
 * for the generated library.
 */

/* Define _POSIX_C_SOURCE to make getline() available.
 */
#define _POSIX_C_SOURCE 200809L

#include <dlfcn.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void) {
    char *line = NULL;
    size_t n;
    do {
        if (line != NULL) {
            free(line);
            line = NULL;
        }
        printf("> ");
        fflush(stdout);
        if (getline(&line, &n, stdin) <= 0) {
            printf("quitting\n");
            break;
        }
        /* 'line' contains the user's input as a 0-termined C string.
         */

        /*
         *  - open a file (e.g. using fopen(<file>, "w")),
         *  - write to the file
         *       #include <math.h>
         *       double f(void) { return <user input>; }
         *    e.g., using fprintf(),
         *  - close the file,
         *  - call the compiler to obtain a dynamic library, e.g.,
         *    with system() and a command
         *        gcc -fPIC -shared -o <file>.so <file> -lm
         *  - open the library with dlopen(),
         *  - look for the symbol "f" in the library,
         *  - call "f" and print the result,
         *  - close the library.
         */


    } while(1);

    return 0;
}
