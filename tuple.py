#!/usr/bin/env python

"""
## tuple

# Immutable list of elements of any type
"""

# Special constructor notation:

t = (1, 2, 3)
t = 1, 2, 3

# For a single element, a trailing comma is needed to differentiate from numeric expressions:

assert (1) == 1
assert type((1,)) == tuple

# Also works without parenthesis on some cases:

a = 1,

# Global factory method from list:

assert tuple([1, 2, 3]) == (1, 2, 3)

# Doest not exist:

    #t = tuple(1, 2, 3)

t2 = (4, 5, 6)
t3 = (4, 5, 1)
tb = (False, False, True)
tm = (1, 1.1, True, 'asdf')

# Index access:

t = (1, 2, 3)
assert t[0] == 1
assert t[1] == 2
assert t[2] == 3

# Unpack:

a, b, c = (1, 2, 3)
assert a == 1
assert b == 2
assert c == 3

if 'tuples are immutable':

    t = (0)
    try:
        t[0] = 'a'
    except TypeError:
        pass
    else:
        assert False

# Concatenate:

assert (0, 1) + (2, 3) == (0, 1, 2, 3)

t = (0, 1)
assert t * 2  == (0, 1, 0, 1)
assert 2 * t  == (0, 1, 0, 1)

# Compare: does alphabetical like compare from left to right.

assert (0, 1)  == (0, 1)
assert (0, 1)  < (1, 2)
assert (0, 10) < (1, 1)
# TODO why:
#assert (0, 1)  > (1)

# The list global functions also work on tuples:

assert len((0,1)) == 2
assert max((0,1)) == 1
assert min((0,1)) == 0
assert any((True, False)) == True
assert all((True, False)) == False
