#!/usr/bin/env python

import ctypes
import os
import os.path

# Standard library call.
libc = ctypes.CDLL('libc.so.6')
assert libc.strlen('abcde') == 5

# Load our custom library.
libtest = ctypes.CDLL(os.path.join(os.path.split(os.path.realpath(__file__))[0], 'libtest.so'))
# Does not know how to convert floats.
assert libtest.f(1,               ctypes.c_float(1.0)) == 2
# Same as above, but explicit int.
assert libtest.f(ctypes.c_int(1), ctypes.c_float(1.0)) == 2
