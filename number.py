#!/usr/bin/env python

"""
## int

## long

## float

Implement the Number "interface": http://docs.python.org/2/library/numbers.html
"""

import numbers

assert isinstance(0, numbers.Integral)
assert isinstance(0, numbers.Rational)
assert isinstance(0, numbers.Real)
assert isinstance(0, numbers.Complex)
assert not isinstance(1j, numbers.Real)

# int, float and long are classes.
# It is just that `1` and `1.1` are nice looking literals.

assert (1).__add__(1) == 2
assert 1L.__add__(1L) == 2L
assert 1.1.__add__(1.1) == 2.2

# It is not possible to omit parenthesis because the lexer would treate
# the `1.` as a float causing an ambiguity.

#a = 1.__add__(1) # SyntaxError

# A less readable alternative is to use a space:

assert 1 .__add__(1) == 2

# As any built-in class, they have global constructor functions:

assert 1 == int(1)
assert 1 == long(1L)
assert 1.1 == float(1.1)

# The constructors also support construction from any numeric type
# or strings:

assert 1 == int(1.5)
assert 1.1 == float('1.1')

# Each of them has a class with the same name:

class myint(int):
    pass

assert myint(1) + myint(2) == myint(3)

if '# float':

    # Unlike int, has a maximum range, machine defined I suppose.
    # In orther words, no implicit arbitrary precision convertion.

    # How to get the max:
    # http://stackoverflow.com/questions/3477283/what-is-the-maximum-float-in-python

    # If you write a constant that is larger than that, it becomes infinity.
    #assert 9e99999999999999999999999999999999999999999 == float('inf')

    # Arbitrary precision feature request:
    # http://stackoverflow.com/questions/11522933/python-floating-point-arbitrary-precision-available

    pass

if 'inf':

    # Watch out for the max float, which then EQUALS infinity.
    assert(1e10 < float('inf'))

    assert(float('-inf') < -1e10)

    assert(float('inf') == float('inf'))
    assert(float('-inf') == float('-inf'))

    # int always works, even though float has limited size.
    # http://stackoverflow.com/questions/24587994/infinite-integer-in-python

    assert(999999999999999999999999999999999999999999999 < float('inf'))

    if 'nan':

        # float('inf')) * 0

        pass

if '## imaginary ## complex':

    """
    Imaginary numbers have built-in literals of the form `Nj`.
    """

    assert 1j * 1j == -1

    assert 1 + 2j == complex(1, 2)

    j = 2
    assert 1j * 1j == -1
    assert j * j   == 4

    assert 1j * 1j == -1
    assert (1 + 2j).real == 1
    assert (1 + 2j).imag == 2
    assert 1j.conjugate() == -1j
