#!/usr/bin/env python

try:
    # ImportError: dynamic module does not define init function (initlibctypes_cheat)
    import libctypes_cheat
except:
    pass
else:
    assert False

# TODO
#import libimport_cheat
# assert libimport_cheat.f(1, ctypes.c_float(1.0)) == 2
