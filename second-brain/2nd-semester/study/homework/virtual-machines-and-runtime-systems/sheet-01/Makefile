# Exercise Sheet 1 — Virtual Machines and Runtime Systems
#
#   make static   (a) link against libshowaddrs.a
#   make dynamic  (b) link against libshowaddrs.so, resolved at run time via $ORIGIN
#   make dlopen   (c) no link at all; dlopen/dlsym at run time
#   make jit      build the primitive JIT compiler
#   make all
#   make clean
#
# Note: $ORIGIN must be written as $$ORIGIN inside a Makefile so that make does
# not treat it as its own variable.
CC      ?= gcc
CFLAGS  ?= -Wall -Wextra -O2

all: static dynamic dlopen jit

static: addrs_static

addrs_static: addrs.c libshowaddrs.a showaddrs.h
	$(CC) $(CFLAGS) addrs.c libshowaddrs.a -o $@

libshowaddrs.a: showaddrs.o
	ar rcs $@ $^

showaddrs.o: showaddrs.c showaddrs.h
	$(CC) $(CFLAGS) -c showaddrs.c -o $@

dynamic: addrs_dynamic

libshowaddrs.so: showaddrs.c showaddrs.h
	$(CC) $(CFLAGS) -fPIC -shared showaddrs.c -o $@

addrs_dynamic: addrs.c libshowaddrs.so showaddrs.h
	$(CC) $(CFLAGS) addrs.c -L. -lshowaddrs -Wl,-rpath,'$$ORIGIN' -o $@

dlopen: addrs_dlopen

addrs_dlopen: addrs.c libshowaddrs.so showaddrs.h
	$(CC) $(CFLAGS) -DUSE_DLOPEN addrs.c -ldl -o $@

jit: eval

eval: eval.c
	$(CC) $(CFLAGS) eval.c -ldl -o $@

clean:
	rm -f *.o *.a *.so addrs_static addrs_dynamic addrs_dlopen eval expr_tmp.c

.PHONY: all static dynamic dlopen jit clean