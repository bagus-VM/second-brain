libmymalloc.so: mymalloc.c
	gcc -Wall -std=c99 -fPIC -shared -o $@ $^

.PHONY: clean
clean:
	/bin/rm -f libmymalloc.so
