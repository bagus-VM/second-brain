CC ?= gcc
CFLAGS = -Wall -std=c99 -D_DEFAULT_SOURCE -fPIC

all: libmymalloc-bump.so libmymalloc-freelist.so test-mymalloc

libmymalloc-bump.so: mymalloc-bump.c
	$(CC) $(CFLAGS) -shared -o $@ $^

libmymalloc-freelist.so: mymalloc-freelist.c
	$(CC) $(CFLAGS) -shared -o $@ $^

test-mymalloc: test-mymalloc.c
	$(CC) -Wall -std=c99 -o $@ $^

.PHONY: run clean
run: all
	./test-mymalloc
	LD_PRELOAD=./libmymalloc-bump.so     ./test-mymalloc
	LD_PRELOAD=./libmymalloc-freelist.so ./test-mymalloc
	LD_PRELOAD=./libmymalloc-bump.so     ls -1 .
	LD_PRELOAD=./libmymalloc-freelist.so ls -1 .

clean:
	/bin/rm -f *.so test-mymalloc
