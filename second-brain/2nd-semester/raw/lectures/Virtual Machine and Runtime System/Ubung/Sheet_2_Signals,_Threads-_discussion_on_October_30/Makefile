.PHONY: all
all: timer main

#
# -U_FORTIFY_SOURCE undefines _FORTIFY_SOURCE.
# With _FORTIFY_SOURCE (which may be enabled
# by default) gcc's longjmp checks whether
# the stack pointer moves in the right direction
# (upwards in the call chain) but in our threads
# example we also move the stack pointer down, so
# we must disable this check.
#
main: main.c threads.c
	gcc -Wall -U_FORTIFY_SOURCE -o $@ $^

timer: timer.c
	gcc -Wall -o $@ $^

.PHONY: clean
clean:
	/bin/rm -f main timer
