#!/usr/bin/env python
import ctypes
import os
libtest = ctypes.CDLL(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'libtest.so'))
assert libtest.f(1, ctypes.c_float(1.0)) == 2
assert libtest.f(ctypes.c_int(1), ctypes.c_float(1.0)) == 2
