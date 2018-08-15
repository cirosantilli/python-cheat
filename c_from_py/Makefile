.POSIX:

CFLGS := -Wall
CNAME := mylib

.PHONY: run clean

run: lib$(CNAME).so
	./main.py

lib$(CNAME).so: $(CNAME).c
	gcc $(CFLGS) -fPIC -c "$<" -o $(CNAME).o
	gcc $(CFLGS) -shared '$(CNAME).o' -o "$@"

clean:
	rm -rf *.o *.so
