#!/usr/bin/env python

#put input to stdout

import sys
import fileinput

for line in fileinput.input():
    sys.stdout.write(line)
