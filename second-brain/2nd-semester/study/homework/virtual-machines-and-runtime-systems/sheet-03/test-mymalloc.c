/*
 * Test driver for the sheet-03 allocators. Built once, run three times:
 *
 *    ./test-mymalloc                                   (system malloc, baseline)
 *    LD_PRELOAD=./libmymalloc-bump.so      ./test-mymalloc
 *    LD_PRELOAD=./libmymalloc-freelist.so  ./test-mymalloc
 *
 * Checks: 16-byte alignment, calloc zeroing, realloc data preservation when
 * growing (the case the lecture's own libmemory.c gets wrong) and shrinking,
 * block reuse after free, and a mixed workload with interleaved frees.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int failures = 0;
static int checks = 0;

static void check(int ok, const char *what) {
    ++checks;
    if (!ok) {
        ++failures;
        printf("FAIL: %s\n", what);
    }
}

int main(void) {
    /* 1. alignment for a spread of sizes */
    int align_ok = 1;
    for (size_t s = 1; s <= 200; ++s) {
        void *p = malloc(s);
        if (p == NULL || ((uintptr_t)p & 15) != 0) {
            align_ok = 0;
            printf("  misaligned: size=%zu ptr=%p\n", s, p);
        }
    }
    check(align_ok, "every size 1..200 is 16-byte aligned");

    /* 2. calloc returns zeroed memory */
    unsigned char *z = calloc(64, 4);
    int zero_ok = 1;
    for (int i = 0; i < 256; ++i)
        if (z[i] != 0) { zero_ok = 0; break; }
    check(zero_ok, "calloc(64,4) is fully zeroed");

    /* 3. realloc growing far past the old block: min(size, old_size) must be
     *    copied -- and the read must stay inside the old block */
    char *a = malloc(96);
    memset(a, 'A', 96);
    char *c = realloc(a, 200000);
    check(c != NULL && c[0] == 'A' && c[95] == 'A', "realloc grow keeps the 96 bytes");

    /* 4. shrink in place: prefix survives, and where it matters the pointer
     *    is unchanged (the free-list build can shrink in place, part (a) cannot) */
    c[31] = 'B';
    char *d = realloc(c, 32);
    check(d[0] == 'A' && d[31] == 'B', "realloc shrink keeps the first 32 bytes");

    /* 5. free then malloc the same size: the free-list build must hand the
     *    same block back, part (a) must not (it never reuses) */
    void *x = malloc(4096);
    free(x);
    void *y = malloc(4096);
    printf("reuse after free: x=%p y=%p same=%s\n", x, y, x == y ? "yes" : "no");

    /* 6. mixed workload: interleaved alloc/free, then verify every block's
     *    contents survived */
    enum { N = 64 };
    unsigned char *p[N];
    for (int i = 0; i < N; ++i) {
        p[i] = malloc((size_t)(i + 1) * 7);
        memset(p[i], (unsigned char)(i & 0xff), (size_t)(i + 1) * 7);
    }
    for (int i = 0; i < N; i += 2)
        free(p[i]);
    unsigned char *q[N / 2];
    for (int i = 0; i < N / 2; ++i)
        q[i] = malloc(64);
    int survive = 1;
    for (int i = 1; i < N; i += 2) {
        for (size_t k = 0; k < (size_t)(i + 1) * 7; ++k) {
            if (p[i][k] != (unsigned char)(i & 0xff)) { survive = 0; break; }
        }
    }
    check(survive, "untouched blocks survive an interleaved alloc/free round");

    free(z);
    free(d);
    free(y);
    for (int i = 0; i < N / 2; ++i)
        free(q[i]);
    for (int i = 1; i < N; i += 2)
        free(p[i]);

    printf("%d checks, %d failure(s)\n", checks, failures);
    return failures != 0;
}
