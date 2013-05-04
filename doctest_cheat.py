#!/usr/bin/env python

"""
can be used for unittesting code

cannot replace unittest, specially for more complex functions

serves mainly as good example for documentation

you just copy and paste an interactive session

this is a docstring for the module, so it is tested:

pass:

>>> print 'abc'
abc

fail:

>>> 1
2

define names:

>>> a = 1
>>> print a
1

this is only works for stuff defined in current docstring:

>>> mod_doc = 1

search for ``mod_doc`` elsewhere and see the fail

indent:

>>> if True:
...     print 'a'
a

multiline output:

>>> for a in [1,2]:
...   print a
1
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

fails:

>>> raise ZeroDivisionError
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AnotherError
"""

def f():
    """
    fail:

    >>> 1
    2

    call itself:

    >>> print f()
    1

    call other funcs:

    >>> print f2()
    2

    >>> mod_doc
    Traceback (most recent call last):
        File "/usr/lib/python2.7/doctest.py", line 1289, in __run
            compileflags, 1) in test.globs
        File "<doctest __main__.f[4]>", line 1, in <module>
            mod_doc
    NameError: name 'mod_doc' is not defined
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

def func_with_very_long_name():
    """
    to avoid typing large names several times, you could to as follows:

    >>> a = func_with_very_long_name
    >>> a()
    1
    >>> a() + 1
    2
    >>> a() + 3
    4
    """
    return 1

class C():
    """
    >>> C().f()
    'C.f'
    """

    def f(self):
        """
        >>> C().f()
        'C.f'
        """
        return 'C.f'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
