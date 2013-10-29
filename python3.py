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

    x = 0
    def outer():
        x = 10
        def inner():
            #this x refers to the x that would be seen from just outside of the function
            #that is, the one on outer
            nonlocal x
            x += 1
        inner()
        assert x == 11

    outer()
    assert x == 0

    #note that a nonlocal *cannot* be a global:

        #x = 0
        #def outer():
        #    nonlocal x
        #    x += 1
        #outer()
        #assert x == 1

    #would give an error

    ####closure

    #nonlocal information is returned together with the function itself:

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
    #see how `inner1` and `inner2` have two separate versions of x:
    assert inner2() == 2

if "##super without args":

    class A(object):
        def __init__(self):
            self.member = 0

    class B(A):
        def __init__(self):
            super().__init__()

    b = B()
    assert b.member == 0
