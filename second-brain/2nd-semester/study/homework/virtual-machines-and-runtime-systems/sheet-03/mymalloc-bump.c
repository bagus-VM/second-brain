/*
 * Exercise Sheet 3 (VMs and Runtime Systems), Problem 2(a):
 * malloc / calloc / realloc / free on top of sbrk(), disregarding freeing.
 *
 * Compiled as:
 *    gcc -Wall -std=c99 -fPIC -shared -o libmymalloc-bump.so mymalloc-bump.c
 * Used as:
 *    LD_PRELOAD=./libmymalloc-bump.so ls
 *
 * The skeleton (mymalloc.c, Stud.IP) has been filled in as follows.
 *
 * Block layout:
 *
 *    block -> +----------------+ <- 16-byte header, block itself 16-byte aligned
 *             | size (size_t)  |    the *requested* size, so realloc() can copy
 *             +----------------+    min(size, old_size) instead of guessing
 *    payload  | ...            | <- returned pointer, 16-byte aligned
 *
 * free() does nothing (part (a) never reuses memory) but still preserves errno.
 * The requested size is kept in the header purely so that realloc() can copy the
 * right number of bytes -- the naive memcpy(p, ptr, size) reads past the old
 * block (a bug the lecture's own libmemory.c flags in a comment).
 */

/*
 * For sbrk().
 */
#define _XOPEN_SOURCE 500

#include <errno.h>
#include <pthread.h>
#include <stdarg.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/*
 * We cannot use printf() to write outputs because printf()
 * may call malloc(). Therefore, we implement our own (very limited)
 * version of printf. Supported conversion specifiers:
 *   %p    pointer (hexadecimal address)
 *   %u    unsigned int
 *   %zu   size_t
 */
static void myprintf(const char *fmt, ...) __attribute__((format(printf, 1, 2)));

/* convert uintptr_t to string */
static void uptoa(uintptr_t val, char *buf, unsigned base) {
    uintptr_t v;
    if (val == 0) {
        buf[0] = '0';
        buf[1] = '\0';
        return;
    }

    v = val;
    while (v != 0) {
        v = v / base;
        ++buf;
    }
    *buf-- = '\0';

    v = val;
    while (v != 0) {
        int r = v % base;
        *buf-- = r < 10 ? ('0' + r) : ('A' + r - 10);
        v = v / base;
    }
}

/*
 * Write a NUL-terminated string to standard error.
 */
static void writestr(const char *str) {
    write(STDERR_FILENO, str, strlen(str));
}

/* Very simple printf (to standard error).
 * Only %p, %u and %zu (and no other modifiers) are supported.
 */
static void myprintf(const char *fmt, ...) {
    const char *p;
    va_list argp;
    char fmtbuf[20];

    va_start(argp, fmt);

    for (p = fmt; *p != '\0'; ++p) {
        if (*p != '%')
            write(2, p, 1);
        else if (p[1] != '\0') {
            ++p;
            switch (*p) {
            case 'z':
                if (p[1] == 'u') {
                    ++p;
                    uptoa(va_arg(argp, size_t), fmtbuf, 10);
                    writestr(fmtbuf);
                }
                break;
            case 'u':
                uptoa(va_arg(argp, unsigned), fmtbuf, 10);
                writestr(fmtbuf);
                break;
            case 'p':
                uptoa((uintptr_t)va_arg(argp, void *), fmtbuf, 16);
                writestr(fmtbuf);
                break;
            case '%':
                writestr("%");
                break;
            }
        }
    }
    va_end(argp);
}

/*
 * Implementations of
 *   posix_memalign(), memalign(), aligned_alloc(), valloc(), pvalloc()
 * using malloc().
 */

int posix_memalign(void **memptr, size_t alignment, size_t size) {
    myprintf("posix_memalign(..., %zu, %zu)\n", alignment, size);
    if (size == 0) {
        *memptr = NULL;
        return 0;
    }

    void *p = malloc(size + alignment);
    if (p == NULL)
        return ENOMEM;
    *memptr = (void *)((((uintptr_t)p + alignment - 1) / alignment) * alignment);
    return 0;
}

void *memalign(size_t alignment, size_t size) {
    void *ptr;
    myprintf("memalign(%zu, %zu)\n", alignment, size);
    errno = posix_memalign(&ptr, alignment, size);
    return ptr;
}

void *aligned_alloc(size_t alignment, size_t size) {
    myprintf("aligned_alloc(%zu, %zu)\n", alignment, size);
    return memalign(alignment, size);
}

void *valloc(size_t size) {
    myprintf("valloc(%zu)\n", size);
    return memalign(sysconf(_SC_PAGESIZE), size);
}

void *pvalloc(size_t size) {
    myprintf("pvalloc(%zu)\n", size);
    long pagesize = sysconf(_SC_PAGESIZE);
    return valloc(((size + pagesize - 1) / pagesize) * pagesize);
}

/*
 * Calls to sbrk(), etc. and output with myprintf()
 * must be synchronized in case the executing program
 * is multithreaded.
 */
static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

/* 16-byte header (one size_t in use, the rest padding) keeps the payload
 * 16-byte aligned as long as every block starts 16-byte aligned. */
#define HEADER 16

static size_t round16(size_t n) {
    return (n + 15) & ~(size_t)15;
}

/*
 * Allocate one block from the top of the heap and return its payload.
 * Never reuses memory: the program break only ever moves up.
 * The caller must hold `lock`.
 */
static void *bump_alloc(size_t size) {
    if (size == 0)
        size = 1; /* malloc(0) still returns a unique pointer */

    uintptr_t brk = (uintptr_t)sbrk(0);
    if (brk == (uintptr_t)-1)
        return NULL;

    /* Align the program break once; every request below is a multiple of 16,
     * so it stays aligned afterwards. */
    if (brk & 15) {
        if (sbrk((ptrdiff_t)(16 - (brk & 15))) == (void *)-1)
            return NULL;
    }

    void *block = sbrk((ptrdiff_t)(HEADER + round16(size)));
    if (block == (void *)-1)
        return NULL;

    *((size_t *)block) = size; /* requested size, for realloc() */
    return (char *)block + HEADER;
}

/*
 * Allocate 'size' bytes of storage.
 * Note that the returned pointer should be aligned
 * on a 16-byte boundary.
 */
void *malloc(size_t size) {
    myprintf("malloc(%zu);  program break = 0x%p\n", size, sbrk(0));
    pthread_mutex_lock(&lock);
    void *p = bump_alloc(size);
    pthread_mutex_unlock(&lock);

    if (p == NULL)
        errno = ENOMEM;
    return p;
}

/*
 * Free storage that has been allocated with
 * malloc, calloc or realloc. According to the
 * documentation, free has to preserves errno.
 *
 * Part (a): freeing is disregarded -- the block is simply abandoned.
 */
void free(void *ptr) {
    int saved_errno = errno;
    pthread_mutex_lock(&lock);
    myprintf("free(0x%p) -- ignored, part (a) never reuses memory\n", ptr);
    /* deliberately no-op */
    pthread_mutex_unlock(&lock);
    errno = saved_errno;
}

/*
 * Allocate storage for 'nmemb' elements of size 'size'
 * and initialize the memory with zeros.
 */
void *calloc(size_t nmemb, size_t size) {
    myprintf("calloc(%zu, %zu)\n", nmemb, size);
    pthread_mutex_lock(&lock);

    size_t total = nmemb * size;
    /* multiplication overflow: fail instead of handing out a short block */
    if (size != 0 && total / size != nmemb) {
        pthread_mutex_unlock(&lock);
        errno = ENOMEM;
        return NULL;
    }

    void *p = bump_alloc(total);
    if (p != NULL)
        memset(p, 0, total);

    pthread_mutex_unlock(&lock);

    if (p == NULL)
        errno = ENOMEM;
    return p;
}

/*
 * Change the size of an allocation at 'ptr' to new
 * size 'size'. If the resizing cannot be done in-place,
 * move the data to a new location. Returns a pointer
 * to the new location (or 'ptr' if data has not
 * been moved).
 *
 * Note:  realloc(NULL, size)  is equivalent to  malloc(size)
 * and  realloc(ptr, 0)  is equivalent to  free(ptr).
 * (see  man 3 realloc).
 *
 * Part (a) cannot resize in place (there is no way back), so it always
 * allocates; the copy is min(size, old_size), taken from the header.
 */
void *realloc(void *ptr, size_t size) {
    myprintf("realloc(0x%p,%zu)\n", ptr, size);
    pthread_mutex_lock(&lock);

    if (ptr == NULL) {
        void *p = bump_alloc(size);
        pthread_mutex_unlock(&lock);
        if (p == NULL)
            errno = ENOMEM;
        return p;
    }

    if (size == 0) {
        /* == free(ptr); in part (a) that means "return everything to nobody" */
        pthread_mutex_unlock(&lock);
        return NULL;
    }

    size_t old_size = *((size_t *)((char *)ptr - HEADER));
    void *p = bump_alloc(size);
    if (p != NULL)
        memcpy(p, ptr, old_size < size ? old_size : size);

    pthread_mutex_unlock(&lock);

    if (p == NULL)
        errno = ENOMEM;
    return p;
}
