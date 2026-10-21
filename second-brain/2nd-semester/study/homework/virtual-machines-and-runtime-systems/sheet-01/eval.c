/* eval.c — Exercise Sheet 1, Problem 2: a primitive JIT compiler.
 *
 * Reads an arithmetic expression in C syntax, writes it into a C function,
 * compiles that function into a shared library, loads the library with
 * dlopen, calls f(), and prints the value.
 *
 * The compiler is taken from the CC environment variable if set, otherwise
 * "gcc". Example:
 *     ./eval                       (uses gcc)
 *     CC="zig cc -target x86_64-linux-gnu.2.35" ./eval
 *
 * Relative filenames are used on purpose: the compiler and the loader must
 * see the same directory.
 */
#define _POSIX_C_SOURCE 200809L

#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SRC "expr_tmp.c"
#define LIB "./expr_tmp.so"

static int compile_and_eval(const char *expr) {
    FILE *fp = fopen(SRC, "w");
    if (fp == NULL) {
        perror("fopen");
        return -1;
    }
    fprintf(fp, "#include <math.h>\n");
    fprintf(fp, "double f(void) { return (%s); }\n", expr);
    fclose(fp);

    const char *cc = getenv("CC");
    if (cc == NULL) {
        cc = "gcc";
    }

    char cmd[4096];
    snprintf(cmd, sizeof cmd, "%s -fPIC -shared -o expr_tmp.so expr_tmp.c -lm", cc);

    if (system(cmd) != 0) {
        fprintf(stderr, "compilation failed: %s\n", cmd);
        return -1;
    }

    void *hdl = dlopen(LIB, RTLD_NOW | RTLD_LOCAL);
    if (hdl == NULL) {
        fprintf(stderr, "dlopen failed: %s\n", dlerror());
        return -1;
    }

    dlerror();
    double (*f)(void) = (double (*)(void))dlsym(hdl, "f");
    char *err = dlerror();
    if (err != NULL) {
        fprintf(stderr, "dlsym failed: %s\n", err);
        dlclose(hdl);
        return -1;
    }

    double result = f();
    dlclose(hdl);
    printf("%s = %g\n", expr, result);
    return 0;
}

int main(void) {
    char *line = NULL;
    size_t n = 0;

    for (;;) {
        printf("> ");
        fflush(stdout);
        if (getline(&line, &n, stdin) <= 0) {
            printf("quitting\n");
            break;
        }
        line[strcspn(line, "\n")] = '\0';
        if (line[0] == '\0') {
            continue;
        }
        compile_and_eval(line);
    }

    free(line);
    return 0;
}
