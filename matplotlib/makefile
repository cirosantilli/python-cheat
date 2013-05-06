#compiles all *.py files into *.svg files

#can mkdir and output that dir.

override CC 		:= python shared.py
override FLAGS 		?=
override ID 		?=
override IN_EXT 	?= .py
override OUT_EXT 	?= .svg
override IN_DIR 	?= in/
override OUT_DIR 	?= out/
override RUN_NOEXT 	?= a 			#basename without extension of file to view (with firefox, okular, etc.)

override ERASE_MSG 	?= 'DONT PUT ANYTHING IMPORTANT IN THOSE DIRECTORIES SINCE `make clean` ERASES THEM!!!'

	#files on which all other files depend (so that if that changes, all is rebuilt)
override ALL_DEPEND ?= shared.py

.PHONY: all mkdir firefox okular clean

INS 		:= $(wildcard $(IN_DIR)*$(IN_EXT))
INS_NODIR 	:= $(notdir $(INS))
OUTS_NODIR	:= $(patsubst %$(IN_EXT),%$(OUT_EXT),$(INS_NODIR))
OUTS		:= $(addprefix $(OUT_DIR),$(OUTS_NODIR))

all: mkdir $(OUTS)
	@echo 'OUTPUT FILES WERE BE PUT INTO: $(OUT_DIR)'
	@echo $(ERASE_MSG)

$(OUT_DIR)%$(OUT_EXT): $(IN_DIR)%$(IN_EXT) $(ALL_DEPEND)
	$(CC) $< $(FLAGS)

mkdir:
	mkdir -p $(OUT_DIR)
	@echo "MADE DIRS: $(OUT_DIR)"
	@echo $(ERASE_MSG)

clean:
	rm -r "$(OUT_DIR)"
	@echo "REMOVED DIRS: $(OUT_DIR)"
	@echo $(ERASE_MSG)
