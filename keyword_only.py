#!/usr/bin/env python3

'''
https://www.python.org/dev/peps/pep-3102/
'''

# Basic example.
def f(a, *, b=1):
    return a + b

# Bad, b is not named. `*` does not act as *args.
try:
    f(1, 2)
except TypeError:
    pass
else:
    assert False

# Good, b is named.
assert f(1, b=2) == 3

# Example with **kwargs as well.
def g(a, *, b=1, **kwargs):
    return a + b + kwargs['c']

# Bad.
try:
    g(1, 2, c=3)
except TypeError:
    pass
else:
    assert False

# Good.
assert g(1, b=2, c=3) == 6

# Example with *args as well.
def h(a, *args, b=1, **kwargs):
    return a + b + kwargs['c'] - args[0]

# Impossible to set b without keyword, as that falls into *args instead.
assert h(1, 2, b=3, c=4) == 6
