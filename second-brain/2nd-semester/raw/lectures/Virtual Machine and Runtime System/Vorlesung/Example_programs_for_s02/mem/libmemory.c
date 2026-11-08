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

void *calloc(size_t nmemb, size_t size) {
    size_t s = nmemb * size;
    void *p = malloc(s);
    if (p != NULL)
        memset(p, 0, s);
    return p;
}

void *malloc(size_t size) {
    static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

    myprintf("malloc(%zu)\n", size);
    size = (size + 0x3f) & ~0x3fUL; /* alignment on 64-byte boundary */
    pthread_mutex_lock(&lock);
    void *p = sbrk(size);
    pthread_mutex_unlock(&lock);
    return p;
}

void free(void *ptr) {
    // free() has to preserve "errno".
    int saved_errno = errno;
    myprintf("free(%p)\n", ptr);
    errno = saved_errno;
}

void *realloc(void *ptr, size_t size) {
    myprintf("realloc(%p,%zu)\n", ptr, size);
    if (size == 0) {
        free(ptr);
        return malloc(0);
    } else {
        void *p = malloc(size);
        if (ptr != NULL) {
            memcpy(p, ptr, size); // wrong, should be min(size,old_size);
            free(ptr);
        }
        return p;
    }
}

/*
 * Implement
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
    posix_memalign(&ptr, alignment, size);
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
 * Implementation of myprintf()
 */

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
