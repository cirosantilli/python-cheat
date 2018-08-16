#!/usr/bin/env python

import ctypes
import os

libctypes_cheat = ctypes.CDLL(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'libctypes_cheat.so'))
# Knows how to convert integers, but not floats.
assert libctypes_cheat.f(1, ctypes.c_float(1.0)) == 2
# Same as above, but more explicit.
assert libctypes_cheat.f(ctypes.c_int(1), ctypes.c_float(1.0)) == 2

# Standard library test.
libc = ctypes.CDLL('libc.so.6')
assert libc.strlen('abcde') == 5
