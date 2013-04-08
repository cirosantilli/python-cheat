#!/usr/bin/env python

#cannot replace unittest, specially for more complex functions

#serves mainly as good example for documentation

def f():
    """
    pass:

    >>> print 'abc'
    abc

    fail:

    >>> print 1
    2

    define stuff:

    >>> a = 1
    >>> print a
    1

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

    the comment `# doctest: +ELLIPSIS` is obligatory and is called a directive.

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

def f2():
    return 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
