#!/usr/bin/env python
import ctypes
libctypes_cheat = ctypes.CDLL('libctypes_cheat.so')
assert libctypes_cheat.f(ctypes.c_int(1), ctypes.c_float(1.0)) == 2
