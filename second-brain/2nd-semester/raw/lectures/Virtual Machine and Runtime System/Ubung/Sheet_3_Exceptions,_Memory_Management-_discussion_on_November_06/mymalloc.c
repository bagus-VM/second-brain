/*
 * Compile this program with
 *    gcc -Wall -std=c99 -fPIC -shared -o libmymalloc.so mymalloc.c
 *
 * The resulting library can be used to replace 'malloc' and related
 * functions from the C library by using LD_PRELOAD, e.g.,
 *    LD_PRELOAD=./libmymalloc.so ls
 * runs 'ls' with 'malloc' etc. replaced by our custom versions.
 */

/*
 * For sbrk().
 */
#define _XOPEN_SOURCE 500

#include <errno.h>
#include <pthread.h>
#include <stdarg.h>
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

/*
 * Allocate 'size' bytes of storage.
 * Note that the returned pointer should be aligned
 * on a 16-byte boundary.
 */
void *malloc(size_t size) {
    myprintf("malloc(%zu);  program break = 0x%p\n", size, sbrk(0));
    pthread_mutex_lock(&lock);
    /* please implement */
    pthread_mutex_unlock(&lock);
    errno = ENOMEM;
    return NULL;
}

/*
 * Free storage that has been allocated with
 * malloc, calloc or realloc. According to the
 * documentation, free has to preserves errno.
 */
void free(void *ptr) {
    int saved_errno = errno;
    pthread_mutex_lock(&lock);
    myprintf("free(0x%p)\n", ptr);
    /* please implement */
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
    /* please implement */
    pthread_mutex_unlock(&lock);
    errno = ENOMEM;
    return NULL;
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
 */
void *realloc(void *ptr, size_t size) {
    myprintf("realloc(0x%p,%zu)\n", ptr, size);
    pthread_mutex_lock(&lock);
    /* please implement */
    pthread_mutex_unlock(&lock);
    errno = ENOMEM;
    return NULL;
}
