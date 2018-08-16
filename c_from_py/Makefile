.POSIX:

CFLGS := -Wall
CNAME := ctypes_cheat

.PHONY: clean

lib$(CNAME).so: $(CNAME).c
	gcc $(CFLGS) -fPIC -c "$<" -o $(CNAME).o
	gcc $(CFLGS) -shared '$(CNAME).o' -o "$@"

clean:
	rm -rf *.o *.so
