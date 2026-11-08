CC=gcc

.PHONY: all
all: static_ex dyn_ex

static_ex: static_ex.c
	$(CC) -Wall -std=c99 -O0 -o $@ $^ -lunwind

dyn_ex: dyn_ex.c
	$(CC) -Wall -std=c99 -O0 -o $@ $^

.PHONY: clean
clean:
	/bin/rm -f static_ex dyn_ex
