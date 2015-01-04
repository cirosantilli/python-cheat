#!/usr/bin/env python

"""
Embed tests into docstrings.

Serves mainly as good example for documentation.

Cannot replace unittest, specially for more complex functions.

The test format is exactly the same as seen in an interactive Python session.

This is a docstring for the module, so tests inside it will be run.

Pass:

>>> print 'abc'
abc

Fail:

>>> 1
2

Define names:

>>> a = 1
>>> print a
1

This is only works for stuff defined in current docstring:

>>> mod_doc = 1

Search for `mod_doc` elsewhere and see the fail.

Indent:

>>> if True:
...     print 'a'
a

Multiline output:

>>> for a in [1,2]:
...   print a
1
2

Unpredictable output:

>>> f # doctest: +ELLIPSIS
<function f at 0x...>

The comment `# doctest: +ELLIPSIS` is obligatory and is called a *directive*.

Exceptions:

>>> raise ZeroDivisionError
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ZeroDivisionError

Fails:

>>> raise ZeroDivisionError
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AnotherError
"""

def f():
    """
    Fail:

    >>> 1
    2

    Call itself:

    >>> print f()
    1

    Call other functions:

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
Not a docstring becaues there is stuff before it.

Not tested:

>>> 1+1
4
"""

def f2():
    return 2

def func_with_very_long_name():
    """
    To avoid typing large names several times, you could to as follows:

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

if __name__ == '__main__':
    if '##testmod':

        # Test current module:

        import doctest
        doctest.testmod()

        # Test given module:

        #doctest.testmod(doctest)

        # From the command line:

        #python -m doctest file.py
