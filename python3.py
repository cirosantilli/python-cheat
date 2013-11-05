#!/usr/bin/env python3

"""
This discusses only features present in python 3 that are not in python 2.
"""

import sys

if "##print function":

    """
    Python 3.x removes the print operator and introduces the print function.

    This is a saner than having an statement just for that,
    but still less sane than Java's class strucutring `System.out.print`.

    As part of the sanity, options are available!
    """

    print(1, 2, 3, sep = ' ', end = '\n', file = sys.stdout)
    print(1, 2, 3, sep = ' ', end = '\n', file = sys.stderr)

if "##nonlocal":

    # Allows for closures. Closures are functions + a context.

    def outer():
        x = 1
        def inner():
            nonlocal x
            x += 1
            return x
        return inner

    inner1 = outer()
    inner2 = outer()

    assert inner1() == 2
    assert inner1() == 3
    assert inner1() == 4

    # `inner1` and `inner2` have two separate versions of x:

    assert inner2() == 2

    # The minimal example of nonlocal usage is with a funciton inside a function.

    #nonlocal i

    # Gives:

        # SyntaxError: nonlocal declaration not allowed at module level

    # Globals cannot be declared as nonlocal:

    i = 0
    #def f(): nonlocal i

    # Gives:

        # SyntaxError: no binding for nonlocal 'i' found

    # The nonlocal variable can come after the nonlocal statement:

    def outer():
        def inner():
            nonlocal x
            x += 1
            return x
        # This comes after the nonlocal:
        x = 1
        return inner

    inner1 = outer()
    inner2 = outer()

    assert inner1() == 2
    assert inner1() == 3
    assert inner1() == 4

if "##super without args":

    class A(object):
        def __init__(self):
            self.member = 0

    class B(A):
        def __init__(self):
            super().__init__()

    b = B()
    assert b.member == 0
