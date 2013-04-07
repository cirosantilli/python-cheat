CFLGS := -Wall
CNAME := test

.PHONY: run clean 

run: libtest.so
	./main.py

lib$(CNAME).so: $(CNAME).c
	gcc $(CFLGS) -fPIC -c "$<" -o $(CNAME).o
	gcc $(CFLGS) -shared "$(CNAME).o" -o "$@"

clean:
	rm -rf *.o *.so
