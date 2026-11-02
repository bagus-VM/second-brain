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

const char *temp_c_file = "__evaltemp.c";
const char *temp_so_file = "__evaltemp.so";
const char *compile_cmd =
    "gcc -Wall -fPIC -shared -o __evaltemp.so __evaltemp.c -lm";

/* Remove the temp files */
void cleanup(void) {
    unlink(temp_c_file);
    unlink(temp_so_file);
}

/* Handle Ctrl+C */
void intr_handler(int sig) {
    printf("interrupted\n");
    cleanup();
    exit(0);
}

int main(void) {
    char *line = NULL;
    size_t n;

    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = intr_handler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags   = 0;
    sigaction(SIGINT, &sa, NULL);

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

        FILE *f = fopen(temp_c_file, "wt");
        if (f == NULL) {
            perror("Could not open temp c file");
            continue;
        }
        int res = fprintf(f, "#include <math.h>\n"
                          "double f(void) { return %s; }",
                          line);
        if (res < 0) {
            perror("Could not write temp c file");
	    fclose(f);
            continue;
        }
        if (fclose(f) == EOF) {
            perror("Could not close temp c file");
            continue;
        }

        res = system(compile_cmd);
        if (res == -1) {
            perror("Could not run compiler");
            continue;
        } else if (!WIFEXITED(res) || WEXITSTATUS(res) != 0) {
            fprintf(stderr, "Compilation failed\n");
            continue;
        }
        void * hdl = dlopen(temp_so_file, RTLD_NOW | RTLD_LOCAL);
        if (hdl == NULL) {
            fprintf(stderr, "Could not load compiled code: %s\n", dlerror());
            continue;
        }
        dlerror(); /* clear dynamic loader error messages */
        double (*f_ptr)(void) = dlsym(hdl, "f");
        char *err = dlerror();
        if (err != NULL) {
            fprintf(stderr, "Could not find symbol in library: %s\n", err);
            dlclose(hdl);
            continue;
        }
        printf("%g\n", f_ptr());
        dlclose(hdl);
    } while(1);

    cleanup();

    return 0;
}
