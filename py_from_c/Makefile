.POSIX:

CC = gcc
CFLGS = -ggdb3 -O0 -pedantic-errors -std=c99 -Wall -Wextra
IN_EXT = .c
OUT_EXT = .out
PYTHON_CONFIG = python-config
ifeq ($(PYTHON_CONFIG),python3-config)
	# https://askubuntu.com/questions/1169364/building-python-3-c-extension-modules-in-ubuntu-18-04-fails-with-relocation-r-x
	CONFIG_CFLAGS = -I/usr/include/python3.6m -I/usr/include/python3.6m  -Wno-unused-result -Wsign-compare -g -fdebug-prefix-map=/build/python3.6-PEMn0O/python3.6-3.6.8=. -fstack-protector -Wformat -Werror=format-security  -DNDEBUG -g -fwrapv -O3 -Wall
else
	CONFIG_CFLAGS = $$($(PYTHON_CONFIG) --cflags)
endif

OUTS = $(addsuffix $(OUT_EXT), $(basename $(wildcard *$(IN_EXT))))

.PHONY: all clean test

all: $(OUTS)

%$(OUT_EXT): %$(IN_EXT)
	@# UNDEBUG: https://stackoverflow.com/questions/4541565/how-can-i-assert-from-python-c-code
	$(CC) $(CFLGS) $(CONFIG_CFLAGS) $$($(PYTHON_CONFIG) --ldflags) -UNDEBUG -o '$@' '$<' $$($(PYTHON_CONFIG) --libs)

clean:
	rm -f *'$(OUT_EXT)'

test: all
	@\
	for t in *"$(OUT_EXT)"; do\
	  if ! ./"$$t"; then\
		echo "ASSERT FAILED: $$t";\
		exit 1;\
	  fi;\
	done;\
