# Compiles all *.py files into *.svg files

# Can mkdir and output that dir.

override CC := python shared.py
override FLAGS ?=
override ID ?=
override IN_EXT ?= .py
override OUT_EXT ?= .png
override IN_DIR ?= in/
override OUT_DIR ?= out/
override ALL_DEPEND ?= shared.py

.PHONY: all mkdir firefox okular clean

OUTS := $(addprefix $(OUT_DIR),$(patsubst %$(IN_EXT),%$(OUT_EXT),$(notdir $(wildcard $(IN_DIR)*$(IN_EXT)))))

all: mkdir $(OUTS)

$(OUT_DIR)%$(OUT_EXT): $(IN_DIR)%$(IN_EXT) $(ALL_DEPEND)
	$(CC) $< $(FLAGS)

clean:
	rm -rf '$(OUT_DIR)'

mkdir:
	mkdir -p '$(OUT_DIR)'
