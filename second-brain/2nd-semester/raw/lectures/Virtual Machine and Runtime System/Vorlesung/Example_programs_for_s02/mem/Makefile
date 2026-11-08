
libmemory.so: libmemory.c
	gcc -std=c99 -Wall -shared -fPIC -o $@ $^

.PHONY: clean
clean:
	rm -rf libmemory.so
