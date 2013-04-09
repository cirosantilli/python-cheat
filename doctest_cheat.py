#!/usr/bin/env python

#cannot replace unittest, specially for more complex functions

#serves mainly as good example for documentation

"""
this is a docstring for the module, so it is tested:

>>> 1+1
3
>>> mod_doc = 1
"""

def f():
    """
    pass:

    >>> print 'abc'
    abc

    fail:

    >>> print 1
    2

    define names:

    >>> a = 1
    >>> print a
    1

    only works for stuff defined in current docstring:

    >>> mod_doc
    Traceback (most recent call last):
        File "/usr/lib/python2.7/doctest.py", line 1289, in __run
            compileflags, 1) in test.globs
        File "<doctest __main__.f[4]>", line 1, in <module>
            mod_doc
    NameError: name 'mod_doc' is not defined

    indent:

    >>> if True:
    ...     print 'a'
    a

    multiline output:

    >>> for a in [1,2]:
    ...   print a
    1
    2

    call itself:

    >>> print f()
    1

    call other funcs:

    >>> print f2()
    2

    unpredictable output:

    >>> f # doctest: +ELLIPSIS
    <function f at 0x...>

    the comment `# doctest: +ELLIPSIS` is obligatory and is called a *directive*

    exceptions:

    >>> raise ZeroDivisionError
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ZeroDivisionError

    >>> raise ZeroDivisionError
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AnotherError

    """
    return 1

"""
not a docstring becaues there is stuff before it.

not tested:

>>> 1+1
4
"""

def f2():
    return 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
