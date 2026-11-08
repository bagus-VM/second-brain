/*
 * Exercise Sheet 3 (VMs and Runtime Systems), Problem 2(b) (the optional,
 * more complex part): the same malloc / calloc / realloc / free, but with a
 * real memory manager.
 *
 * Compiled as:
 *    gcc -Wall -std=c99 -fPIC -shared -o libmymalloc-freelist.so mymalloc-freelist.c
 * Used as:
 *    LD_PRELOAD=./libmymalloc-freelist.so ls
 *
 * Design
 * ------
 * Every block carries a 16-byte header:
 *
 *    +---------------------------+ <- block start, 16-byte aligned
 *    | size | free flag (bit 0)   |    size is a multiple of 16, so bits 0-3
 *    +---------------------------+    are free for flags
 *    | next                      |    next block in the heap list (address order)
 *    +---------------------------+ <- payload, 16-byte aligned
 *    | ...                       |
 *
 * All blocks ever handed out from sbrk() are kept in one singly linked list in
 * address order; free() only clears a flag, malloc() does a first-fit scan of
 * that list and reaches for sbrk() only when no block fits.  A block that is
 * much larger than requested is split; the remainder becomes a new free block.
 *
 * Known limitation (deliberate, and noted in solution.md): neighbouring free
 * blocks are NOT coalesced, so repeated alloc/free of different sizes
 * fragments the heap.  The sheet asks for marking + searching, which this is.
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

typedef struct header {
    size_t size;         /* payload size, multiple of 16; bit 0 = free flag */
    struct header *next; /* next block in address order */
} header_t;              /* 16 bytes, so the payload stays 16-byte aligned */

#define HDR ((size_t)sizeof(header_t))
#define MIN_PAYLOAD 16

static header_t *head = NULL; /* first block ever handed out from sbrk() */
static header_t *tail = NULL; /* last  block ever handed out from sbrk() */

static size_t round16(size_t n) {
    return (n + 15) & ~(size_t)15;
}

static size_t get_size(header_t *b) {
    return b->size & ~(size_t)15;
}

static int is_free(header_t *b) {
    return (int)(b->size & 1);
}

static void set_free(header_t *b, int free) {
    b->size = get_size(b) | (size_t)(free ? 1 : 0);
}

/*
 * Request a fresh block from the operating system and append it to the list.
 * The caller must hold `lock`.
 */
static header_t *heap_extend(size_t need) {
    uintptr_t brk = (uintptr_t)sbrk(0);
    if (brk == (uintptr_t)-1)
        return NULL;

    /* keep the payload (block + header) 16-byte aligned */
    if ((brk + HDR) & 15) {
        size_t pad = 16 - ((brk + HDR) & 15);
        if (sbrk((ptrdiff_t)pad) == (void *)-1)
            return NULL;
        brk += pad;
    }

    header_t *b = sbrk((ptrdiff_t)(HDR + need));
    if (b == (void *)-1)
        return NULL;

    b->size = need; /* free flag clear: the block is handed out */
    b->next = NULL;
    if (tail != NULL)
        tail->next = b;
    else
        head = b;
    tail = b;
    return b;
}

/*
 * First-fit search: the first free block whose size is at least `need`.
 * The caller must hold `lock`.
 */
static header_t *first_fit(size_t need) {
    for (header_t *b = head; b != NULL; b = b->next) {
        if (is_free(b) && get_size(b) >= need)
            return b;
    }
    return NULL;
}

/*
 * Give back the unused tail of an oversized block as a new free block.
 * Only worthwhile if the remainder can hold a header plus a minimal payload.
 * The caller must hold `lock`.
 */
static void split(header_t *b, size_t need) {
    size_t have = get_size(b);
    if (have < need + HDR + MIN_PAYLOAD)
        return;

    header_t *rest = (header_t *)((char *)b + HDR + need);
    rest->size = (have - need - HDR) | 1; /* the remainder is free */
    rest->next = b->next;
    b->next = rest;
    b->size = need;
    if (tail == b)
        tail = rest;
}

/*
 * Allocate (or reuse) a block of at least `size` usable bytes.
 * The caller must hold `lock`.
 */
static void *alloc_locked(size_t size) {
    if (size == 0)
        size = 1;

    size_t need = round16(size);

    header_t *b = first_fit(need);
    if (b != NULL)
        split(b, need);
    else
        b = heap_extend(need);

    if (b == NULL)
        return NULL;

    set_free(b, 0);
    return (char *)b + HDR;
}

/*
 * Allocate 'size' bytes of storage.
 * Note that the returned pointer should be aligned
 * on a 16-byte boundary.
 */
void *malloc(size_t size) {
    myprintf("malloc(%zu);  program break = 0x%p\n", size, sbrk(0));
    pthread_mutex_lock(&lock);
    void *p = alloc_locked(size);
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
 * Part (b): the block is only marked as available.  No coalescing --
 * see the note at the top of the file.
 */
void free(void *ptr) {
    int saved_errno = errno;
    pthread_mutex_lock(&lock);
    myprintf("free(0x%p)\n", ptr);
    if (ptr != NULL) {
        header_t *b = (header_t *)((char *)ptr - HDR);
        set_free(b, 1);
    }
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
    if (size != 0 && total / size != nmemb) {
        pthread_mutex_unlock(&lock);
        errno = ENOMEM;
        return NULL;
    }

    void *p = alloc_locked(total);
    if (p != NULL)
        memset(p, 0, total); /* reused blocks carry the previous contents */

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
 */
void *realloc(void *ptr, size_t size) {
    myprintf("realloc(0x%p,%zu)\n", ptr, size);
    pthread_mutex_lock(&lock);

    if (ptr == NULL) {
        void *p = alloc_locked(size);
        pthread_mutex_unlock(&lock);
        if (p == NULL)
            errno = ENOMEM;
        return p;
    }

    if (size == 0) {
        header_t *b = (header_t *)((char *)ptr - HDR);
        set_free(b, 1); /* == free(ptr) */
        pthread_mutex_unlock(&lock);
        return NULL;
    }

    header_t *b = (header_t *)((char *)ptr - HDR);
    size_t need = round16(size);

    if (get_size(b) >= size) {
        /* shrinking in place: hand the tail back to the heap */
        split(b, need);
        pthread_mutex_unlock(&lock);
        return ptr;
    }

    /* growing: find a new block, copy, mark the old one available */
    header_t *n = first_fit(need);
    if (n != NULL)
        split(n, need);
    else
        n = heap_extend(need);

    if (n == NULL) {
        pthread_mutex_unlock(&lock);
        errno = ENOMEM;
        return NULL;
    }

    set_free(n, 0);
    size_t old = get_size(b); /* rounded up, so never below the old request */
    memcpy((char *)n + HDR, ptr, old < need ? old : need);
    set_free(b, 1);

    pthread_mutex_unlock(&lock);
    return (char *)n + HDR;
}
