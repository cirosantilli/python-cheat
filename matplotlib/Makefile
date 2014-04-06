# Compiles all *.py files into *.svg files

# Can mkdir and output that dir.

override CC 		:= python shared.py
override FLAGS 		?=
override ID 		?=
override IN_EXT 	?= .py
override OUT_EXT 	?= .svg
override IN_DIR 	?= in/
override OUT_DIR 	?= out/
# Basename without extension of file to view (with firefox, okular, etc.)
override RUN_NOEXT 	?= a

# Files on which all other files depend (so that if that changes, all is rebuilt)
override ALL_DEPEND ?= shared.py

.PHONY: all mkdir firefox okular clean

INS 		:= $(wildcard $(IN_DIR)*$(IN_EXT))
INS_NODIR 	:= $(notdir $(INS))
OUTS_NODIR	:= $(patsubst %$(IN_EXT),%$(OUT_EXT),$(INS_NODIR))
OUTS		:= $(addprefix $(OUT_DIR),$(OUTS_NODIR))

all: mkdir $(OUTS)

$(OUT_DIR)%$(OUT_EXT): $(IN_DIR)%$(IN_EXT) $(ALL_DEPEND)
	$(CC) $< $(FLAGS)

clean:
	rm -rf "$(OUT_DIR)"

mkdir:
	mkdir -p $(OUT_DIR)
