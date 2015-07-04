#!/usr/bin/env python

"""
## math

There are also some math built-in functions like abs and max.
"""

import math

assert abs(math.sin(0) - 0.0) < 0.01
assert abs(math.cos(0) - 1.0) < 0.01
assert abs(math.exp(0) - 1.0) < 0.01

if '## sqrt':

    assert abs(math.sqrt(4) - 2.0 ) < 0.01

    try:
        math.sqrt(-1)
    except ValueError:
        pass
    else:
        assert False

assert abs(math.pi     - 3.14) < 0.01
assert abs(math.exp(0) - 1.0 ) < 0.01
assert abs(math.exp(1) - 2.71) < 0.01
assert math.floor( 1.5 ) == 1
