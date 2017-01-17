#!/usr/bin/env python

"""
In python everything is an object.

There is operator overload: every operator has a correponding method

In Python, methods that can become operators are prefixed and suffixed by `__`.

For example:

- `==` and `__eq__()`
- `+` and `__add__()`
- `**` and `__pow__()`
- `//` and `__TODO__()`

Built-in classes like `int` simply implement those methods.
"""

assert 0 == 0

assert 2 * 3 == 6

# C like division arithmetic:

assert 1 / 2        == 0
assert 1 / 2.0      == 0.5
assert 1 / float(2) == 0.5

# Floor division:

assert 9.0 // 2.0 == 4

# pow:

assert 2 ** 3

if '## boolean operator':

    assert not True         == False
    assert True and False   == False
    assert True or  False   == True

if '## chained comparison':

    # Insane sugar:
    # http://stackoverflow.com/questions/24436150/how-does-interval-comparison-work

    assert 1 < 2 < 3 < 4 < 5
