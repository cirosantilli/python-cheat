#!/usr/bin/env python3

"""
Features present in Python 3. Some may h

Source: <http://docs.python.org/3.0/whatsnew/3.0.html>
"""

import sys

if "##print function":

    """
    Python 3.x removes the print statement and introduces the print function.

    This is a saner than having an statement just for that,
    but still less sane than Java's class strucutring `System.out.print`.

    As part of increased sanity, extra options are available via standard
    keyword arguments.
    """

    print(1, 2, 3, sep=' ', end='\n', file=sys.stdout)
    print(1, 2, 3, sep=' ', end='\n', file=sys.stderr)

if "#new syntax":

    # Integer division breaks the ancestral C int floor type conversion.
    # Use explicit floor division for that instead.

    assert 1 / 2  == 0.5
    assert 1 // 2 == 0

    # Octal literals change for uniformity with hexadecimal and binary literals.

    assert 0o12 == 10

    # Extended unpacking:

    a, *bs, c = range(0, 4)
    assert a == 0
    assert bs == [1, 2]
    assert c == 3

if "##args":

    if "Keyword argument after args":

        def f(*args, after_args):
            assert args == (0, 1)
            assert after_args == 2

        f(0, 1, after_args=2)

        try:
            f(0, 1, 2)
        except TypeError:
            pass
        else:
            assert False

    if "empty args to ignore args":

        def f(a, *, b):
            assert a == 0
            assert b == 1

        # TODO stopped working
        #f(0, 10, 11, b=1)

if "##annotations":

    '''
    Complement docstrings for doc generation.
    '''

    def foo(a: 'x', b: 5 + 6, c: list) -> max(2, 9):
        pass

    def f(a: "doc a",
          b: "doc b",
          c: 1,
          d: 1 + 1,
          e: [1, 2],
          has_default: "doc has_default" = "default_val",
          *args: 'doc args',
          **kwargs: 'doc kwargs'
          ) -> 'doc return':
        pass

    assert f.__annotations__ == {
        'a': 'doc a',
        'b': 'doc b',
        'c': 1,
        'd': 2,
        'e': [1, 2],
        'args': 'doc args',
        'kwargs': 'doc kwargs',
        'has_default': 'doc has_default',
        'return': 'doc return',
    }

if "##view objects":

    '''
    dict keys, values and items return view instead of lists.

    Those views are updated with the dict.
    '''

    d = {0: 'zero', 1: 'one'}
    keys = d.keys()
    assert set(keys) == {0, 1}
    d[2] = 'two'
    assert set(keys) == {0, 1, 2}

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

if "##built-in types":

    if "##numbers":

        '''
        long does not exist anymore.

        int is the same as long.
        '''

        #1L # SyntaxError

        try:
            long(1)
        except NameError:
            pass
        else:
            assert False

    if "##sequence built-ins":

        if "##str ##unicode ##bytes":

            '''
            The default source encoding is UTF-8. No need to add the
            infamous `-*- coding: utf-8 -*-`, unless you want yet another encoding
            (which you don't do you? =)).
            '''

            assert u'\u4E2D\u6587' == u'中文'

            '''
            In Python 3, the unicode situation changes drastically:

            - Python 2 `unicode` becomes Python 3 `str`

            - Python 3 `str` (Python 2 `unicode`) literals are writen either like Python 2 `str`: `'\uAAAA'`.
                or old Python 2 `unicode` literals: `u'\uAAAA'`

            - Python 2 `str` is Python 3 `byte`.

                This is more intuitive, since in natural language terms,
                a string like `é` is considered to contain one character only.

                It is also more coherent with the `bytearray` type.

            - Python 3 `byte` literals start with `b`: `b'\xAA\xBB'`
            '''

            assert '中'.encode('UTF-8') == b'\xE4\xB8\xAD'
            assert '中' == b'\xE4\xB8\xAD'.decode('UTF-8')

            s = str('\u4E2D\u6587')
            s2 = '\u4E2D\u6587'
            s3 = u'\u4E2D\u6587'
            assert s == s2
            assert s == s3
            assert s[0] == '\u4E2D'

            '''
            TODO what do u escapes mean inside `b` literals? `\u0000` and `\U00000000` escapes.
            '''

            u = bytes(b'\u4E2D')
            #print("%x" % u[0])
            #assert u[0] == b'\x4E'

            # `[]` takes and gives integer or `TypeError` is raised.

            ba = b'a'
            try:
                ba[0] = b'b'
            except TypeError:
                pass
            else:
                assert False

            # `bytes` is immutable like `str`.

            b = b'a'
            try:
                b[0] = ord(b'b')
            except TypeError:
                pass
            else:
                assert False

            '%d' % 1

        if "##range ##xrange":

            '''
            In Python 3, the Python 2 `xrange` gloabal function and built-in types disappear
            and are replaced by the `range()` function and Range `built-in` type.

            Old Python 2 `range()` method disappears. It can be easily emulated via `list(range())`.

            Since this object is iterable, it can be used in the similar situations as `xrange` in Python 2,
            but it also supports more operations than simple iterators, for example efficient
            presence test for integers.

            Objects of type range have the advantage that the memory size of the object
            does not depend on the range size since only the edges and the step need to be stored.
            '''

            assert list(range(0, 6, 2)) == [0, 2, 4]

            '''
            Inclusion tests for integers is `O(1)` since they can be made in via modulos.
            '''

            assert 4 in range(0, 6, 2)

            '''
            You can make a range out of anything that implements TODO
            '''

            class Myrange:
                def __init__(self, i):
                    self.i = i

if "##truth value testing for objects":

    '''
    What if evaluates to True depends now only on the `__bool__()` value of an object.

    In Python 2 this was a mixture of `__nonzero__` and `__len__`, much less neat.
    '''

if "##super without args":

    class A(object):
        def __init__(self):
            self.member = 0

    class B(A):
        def __init__(self):
            super().__init__()

    b = B()
    assert b.member == 0
