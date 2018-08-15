#!/usr/bin/env python
# Standard library call.
import ctypes
libc = ctypes.CDLL('libc.so.6')
assert libc.strlen('abcde') == 5
