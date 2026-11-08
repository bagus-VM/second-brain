# Add the flag "-m32" (if supported) to CC to compile for
# the 32 bit target (instead of the 64 bit target).
CC=gcc -Wall -std=c99
AR=ar

BINARIES=addrs addrs-dlopen addrs-static eval

.PHONY: all
all: $(BINARIES)

addrs: addrs.c libshowaddrs.so
	$(CC) -o $@ $< -L. -lshowaddrs -Wl,-rpath,'$${ORIGIN}'

addrs-dlopen: addrs.c libshowaddrs.so
	$(CC) -DUSE_DLOPEN -o $@ $< -ldl -Wl,-rpath,'$${ORIGIN}'

addrs-static: addrs.c libshowaddrs.a
	$(CC) -o $@ $< -L. -l:libshowaddrs.a

eval: eval.c
	$(CC) -o $@ $< -ldl -Wl,-rpath,'$${ORIGIN}'

libshowaddrs.so: showaddrs.c
	$(CC) -fPIC -shared -o $@ $<

showaddrs.o: showaddrs.c
	$(CC) -c -o $@ $<

libshowaddrs.a: showaddrs.o
	$(AR) r $@ $<

.PHONY: clean
clean:
	/bin/rm -f $(BINARIES) libshowaddrs.so libshowaddrs.a showaddrs.o
