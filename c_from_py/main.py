#!/usr/bin/env python

import ctypes
import os
import os.path

libc = ctypes.CDLL('libc.so.6')
assert libc.strlen('abcde')

libtest = ctypes.CDLL( os.path.join( os.getcwd(), 'libtest.so' ) )
assert libtest.f( 1,               ctypes.c_float(1.0) ) == 2
assert libtest.f( ctypes.c_int(1), ctypes.c_float(1.0) ) == 2
