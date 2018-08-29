#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TODO: split this up into smaller files.

Major cheat on the Python language and stdlibs.

Contains every test that does not:

- produces too much stdout, or one that is too complex to assert, e.g. human readable
- takes a perceptible ammount of time to run
- cannot be contained on a single file
"""

import re
import sys
import shutil
import tempfile
import itertools

if '## whitespace':

    # Python forces certain indentations

    # Use backslash '\' for line continuation of long commands:

    assert \
    1+\
        1\
    == 2

    # Parenthesis also work:

    assert (
            1+
        1 ==
    2
    )

    if '## whitespace and functions':

        # Cannot separate `(` from function def:

        #def f
            #(x,y):
            #pass

        # Everything else works.

        # Good:

        def f(x,y):
            """
            docstrings must be indented
            """
            pass

        # My favorite format for lots of args:

        def f(
                x,
                y,
                z,
                w
            ):
            pass

        # Ugly but works:

        def f(
        x
                    ,y,
            z
            ):
            pass

        # Single line only

        def f(): pass

            #def f(): pass
                #pass

        def f(x,y):
            pass

        f(1,2)

        f(1,
        2)

        f(
        1,
        2
        )

        def f():
            g(
                    1,
        2
            )

        # Anything that has `:` like `if`, `while` and `class` works like function.

    if '## multiple commands on a single line':

        # <http://stackoverflow.com/questions/6167127/how-to-put-multiple-statements-in-one-line>

        # Only possible for multiple simple statements.

        i = 0; i += 1; assert i == 1

        # Only use this for bash one liners.

if '## built-in':

    """
    Python has three kinds of built-ins:

    - functions
    - constants
    - types

    Built-ins add insanity to the language, but allow us to write much shorter
    and more readable code. It is the classical sanity / sugarness tradeoff of language design.

    Those built-ins are mostly just like user defined types except for some points.

    Notable differences include:

    -   they do not need to be imported: they are always available on any scope.

    -   some (but not all) built-in types have nice looking literals such as `1`, `[1]` or `{1: 2}`
        It is however be possible to create any type with a built-in factory function.

    -   most built-in types are lower case words by convention, while classes usually start with Upper case.
    """

    if 'It is not possible to set attributes of built-in types.':

        class C: pass
        C.i = 1

        try:
            int.i = 1
        except TypeError:
            pass
        else:
            assert False

if '## built-in constants':

    """
    Python has the following built-in constants:

    -   `True`

    -   `False`

    -   `None`

    -   ##NotImplemented

        Vs. `NotImplementedError` built-in exception:

        <http://stackoverflow.com/questions/878943/why-return-notimplemented-instead-of-raising-notimplementederror>

    -   `Ellipsis`

    -   `__debug__`

    Besides those, there are also builtin exception objects.
    """

    # Can be reassigned in Python 2.

    def f():
        False = 10
        assert False == 10
    f()

if '## built-in functions':

    if '## help':

        """
        Intended for interactive usage documentation retrieval.

        If linked to a tty, opens the doc of the given object in a pager.

        Else, does nothing.
        """

        def f():
            """doc"""
        #help(f)

    if '## locals':

        # TODO

        pass

    if '## globals':

        # TODO

        pass

    # Built-in functions:

    assert abs(-1) == 1

    if '## max':

        # Returns the first max item according to some metric:

        assert max(1, -2, 0)   == 1
        assert max([1, -2, 0]) == 1
        assert max([1, -2, 0, 2], key=lambda x: x*x) == -2

        # TODO best way to get the value of key withtout recalculating?

        def f(x): return x*x
        assert f(max([1, -2, 0, 2], key=f)) == 4

    if '## exec':

        # Interpret a string at given point.

        a = 0
        exec('a = 1')
        assert a == 1

if '## built-in types ## types':

    """
    <http://docs.python.org/3.3/reference/datamodel.html>

    Types which are already defined by the interpreter,
    and do not need to be imported from the stdlib.

    They may have special (non-class-like) literals like ints `1` and lists: `[1, 2]`.
    All have global function constructors like `list()` or `set()`,

    The built-in types can be classified based on which ABCs they implement.

    All the Python 2 built-in types are:

    -   numbers: implement the `numbers.Number` ABC or its derived classes.

        All immutable.

        -   integers: `numbers.Integral`

            - int
            - long
            - bool

            -   real: `numbers.Real`

                -   float

                -   complex: `numbers.Complex`

                    - complex

    - sequences:

        It seems that in Python 2 there is not a fixed ABC for them.

        In Python 3 they implement `collections.abc.Sequence`. Much saner.

        -   immutable:

            - str
            - unicode
            - tuple

        -   mutable:

            - list
            - bytearray
            - memoryview

    -   sets: in Python 3 they implement `collections.abc.Set`

        - set
        - frozenset

    -   mappings:

        Only one:

        - dict

    - super
    """

    assert(type(int())      == type(0))
    assert(type(float())    == type(0.0))
    assert(type(long())     == type(0L))
    assert(type(complex())  == type(1j))

if '## bytearray':

    """
    Mutable version of `str`.
    """

    ba = bytearray(b'ab')
    ba2 = ba
    ba2[0] = ord(b'b')
    assert ba == bytearray(b'bb')

if '## branching':

    if '## if':

        if False:
            assert False
        elif False:
            assert False
        else:
            pass

        if '## multiline condition':

            # Multiline conditions must have parenthesis:

            if (a
                and b
                and c
                and d):
                pass

        if '## single line':

            # Behaves like the C question mark `?` operator.

            # Must have the else part:

            a = 1 if True  else 2
            assert a == 1
            a = 1 if False else 2
            assert a == 2

    if '## is':

        # `is` checks for equality of reference equality instead of using __equals__

        class C(object):
            def __eq__(self, other): True
        assert C() != C()
        assert not C() is C()
        c = C()
        assert c is c

        # In Python 2, not guaranteed because True and False can be reassigned.
        # In Python 3, guaranteed.
        # http://stackoverflow.com/questions/2764017/is-false-0-and-true-1-in-python-an-implementation-detail-or-is-it-guarante
        assert 1 == True
        assert not 1 is True

        assert 0 == False
        assert not 0 is False

        assert not None == False
        assert not None is False

        assert not '' == False
        assert not '' is False
        assert not '' == None

        assert not [] == False
        assert not [] is False

    if '## truth value testing for objects':

        """
        Any object can be used on an if or while.

        In Python 2, an object evaluates to false iff:

        - it implements `__nonzero__` and `__nonzero__()` if False.
        - else if it impements `__len__`, and `__len__() == 0`

        Any other object evaluates to True.

        For the built-in types, the only the following are test False:

        - None
        - False
        - zero of any numeric type, for example, 0, 0L, 0.0, 0j.
        - any empty sequence, for example, '', (), [], set().
        - any empty mapping, for example, {}.
        """

        if '':
            assert False

        if ' ':
            pass
        else:
            assert False

        if []:
            assert False

        if [False]:
            pass
        else:
            assert False

        if None:
            assert False

        """
        Truth value testing can differ from `__eq__` to True or false!

        Something that is not equal to True can still works for an if!
        """

        assert -1 != True

        if -1:
            pass
        else:
            assert False

    if '## while':

        i = 0
        while i < 10:
            print i
            i += 1

        i = 0
        while i < 10:
            print i
            if i == 5:
                break
            i += 1

        i = 0
        while i < 10:
            print i
            i += 1
            if i == 5:
                continue

    if '## for':

        for i in [1, 3, 2]:
            print i

        for i in [1, 3, 2]:
            print i
            if i == 3:
                break

        for i in [1, 3, 2]:
            print i
            if i == 3:
                continue

        """
        # Modify list while itearting it

            Just don't do it. Make a copy instead. There is no decent efficient way like in Java:
            http://stackoverflow.com/questions/1207406/remove-items-from-a-list-while-iterating-in-python/34238688#34238688
        """

    if '## and ## or':

        """
        And and or are actually branching instructions:
        analogous to ``&&`` and ``||`` in bash.

        - and evaluates the first expression. If False return it, if true return the second.
        - or evaluates the first expression. If True return it, if false return the second one.
        """

        assert (True  and 1) == 1
        assert (False and 1) == False

        assert (True  or 1) == True
        assert (False or 1) == 1

if '## Function':

    if '## Arguments':

        def f(a, b = 0, *args, **kwargs):
            """
            args is a tuple
            kwargs a dicdt

            those names are just a convention,
            any name can be used, ex:

                def g(*myArgs, **myEtraKwargs)
            """

            #args is a tuple.
            for arg in list(args):
                pass
            #you can iterate over it.

            #this is a standard way to give default values:
            kw1 = kwargs.get(1, "default1")
            kw2 = kwargs.get(2, "default2")
            kw2 = kwargs.get(3, "default3")

            return a, b, list(args), kwargs

        #ERROR: argument a has no value

            #f()

        assert f(1)                             == (1, 0, []   ,    {}              )
        assert f(1, 2)                          == (1, 2, []   ,    {}              )

        assert f(1, 2, 3)                       == (1, 2, [3],      {}              )
        assert f(1, 2, 3, 4)                    == (1, 2, [3, 4],   {}              )

        assert f(1, 2, 3, 4,    c=5, d=6)       == (1, 2, [3, 4],   {'c':5, 'd':6}  )
        assert f(1, 2,          c=5, d=6)       == (1, 2, [],       {'c':5, 'd':6}  )

        # If a named parameter exists already, it does not go into kwargs:

        assert f(a = 1)                 == (1, 0, [], {} )
        assert f(a = 1, b = 2)          == (1, 2, [], {} )
        assert f(b = 2, a = 1)          == (1, 2, [], {} )
        assert f(a = 1, b = 2, c = 5)   == (1, 2, [], {'c':5} )

        if '## Unpack argument lists ## Splat':

            # Splat is the Rubish term for it.

            # Transform list or dictionnaries into function arguments.

            assert f(*[0, 1]) == (0, 1, [], {})
            assert f(0, 1, *[2, 3]) == (0, 1, [2, 3], {})

            # Part of them may be named arguments, part may be *args.

            assert f(0, *[1, 2, 3]) == (0, 1, [2, 3], {})

            # ERROR: only named arguments may follow unpacked list

            assert f(0, 1, *[2, 3], c=4) == (0, 1, [2, 3], {'c':4})
            #assert f(0, 1, *[2, 3], 4) == (0, 1, [2, 3, 4], {})

            # Also possible with dictionnaries:

            assert f(1, 2, 3, 4, **{'c': 5, 'd': 6})    == (1, 2, [3, 4],   {'c': 5, 'd': 6}  )
            assert f(1, 2,       **{'c': 5, 'd': 6})    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # Can combine dict unpack with named arguments:

            assert f(1, 2,       d=6, **{'c': 5}   )    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # ERROR: dict unpack must be the last thing:

                #assert f(1, 2,       **{'c': 5}, d=6   )    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # Can use list unpack with dict unpack:

            assert f(1, *[2, 3, 4], d=6, **{'c': 5}) == (1, 2, [3, 4],   {'c': 5, 'd': 6}  )

        # ERROR: multiple values for `a`:

            #f(1, a = 1)

        # ERROR: can only pass dictionnaries if there is a kwargs

        #def g(a): pass
        #g(a = 1)

        # OK: we have kwargs:

        def g(a, **kwargs): pass
        g(a = 1)

        # ERROR: cannot change the order of normal args, *args and **kwargs:

        #def f(*args, a): pass
        #def f(**kwargs, a): pass
        #def f(**kwargs, *args): pass

        # ERROR: cannot use integer (5) as keyword for kwargs: must use strings

            #f(1, 2, *[3, 4], **{5:6})

        if '## overload':

            """there is no function overloading in python"""

            def f(a):
                """
                completely destroys last existing f
                """
                return a

            def f(a, b):
                return a + b

            "too many args:"

            #f(1, 2, 3)

        if 'default values for lots of kwargs':

            # If you have default values to a large number of them kwargs
            # this is a good way, which saves you from writting lots of ``gets``

            def f( **non_default_kwargs ):

                kwargs = {
                    'a':1,
                    'b':2,
                }
                kwargs.update( non_default_kwargs )

                f2( **kwargs )

        if 'variables can contain functions':

            def f(x):
                return x + 1
            g = f
            assert g(0) == 1

        if '## immutable types ## mutable types':

            """
            Literals like `1` and `1.1` are objects.

            Immutable type: there is no way (function, member, etc.) to modify the object itself.
            It is only possible to point to a different object of the same type.

            For all standard types, doing `a = b` always makes a point to a different thing,
            and does not change what `a` was pointing to.

            For other operators this may vary: `a += 1` may change what `a` points to, or the object pointed to
            depending on the type.

            Immutable types include:

            - numeric types like integers and floats
            - strings
            - tuples

            Mutable types include:

            - lists
            - dictionnaries
            """

            if 'immutable:':

                x = 1
                assert id(x) == id(1)

                y = x
                assert id(x) == id(y)

                y = 2
                assert x == 1
                assert id(y) == id(2)

            if 'mutable:':

                x = [1]
                assert id(x) != id([1])
                assert x == [1]

                x = [1]
                y = x
                assert id(y) == id(x)

                x = [1]
                y = x
                assert id(y) == id(x)

                y[0] = 2
                assert x == [2]
                assert id(x) == id(y)

                # For mutable types, `+=` may change the actuabl object, not just the address to which `y` points to.
                y += [3]
                assert id(x) == id(y)
                assert x == [2, 3]

                # Doing `y = ` however does change the address pointed to.
                y = [0]
                assert id(x) != id(y)

                def f(y):
                    y[0] = 2
                x = [1]
                f(x)
                assert x == [2]

            """
            Immutable built-in types all implement `__hash__`. Mutable built-in types are not.
            User defined types are all hashable.
            """

            s = set()
            s.add(1) # OK: hashable.
            try:
                s.add([1]) # KO: not hashable
            except TypeError:
                pass
            else:
                assert False

            """
            list constructor does shallow copies.
            """

            x = [0, [10]]
            y = list(x) # or x[:]
            y[0] = 1
            y[1][0] = 11
            assert x == [0, [11]]
            assert y == [1, [11]]

        if '## Pass by value ## Pass by reference':

            """
            Flamethrower battle: http://stackoverflow.com/questions/986006/python-how-do-i-pass-a-variable-by-reference

            Only modifications on mutable objects inside a function have effect outside it.
            """

            def f(a, b):
                a = a + b

            # integer: immutable

            a = 0
            f(a, 1)
            assert a == 0

            def g(i):
                return i + 1
            a = 0
            a = g(a)
            assert a == 1

            # string: immutable
            a = "a"
            f(a, "b")
            assert a == "a"

            def g(s):
                return s + "b"
            a = "a"
            a = g(a)
            assert a == "ab"

            # list: mutable
            a = [0]
            f(a, [1])
            assert a == [0]

            def g(a):
                a.append(1)
            a = [0]
            g(a)
            assert a == [0, 1]

    if '## Return value':

        if '## Multiple return values':

            """
            there is no real multiple return values,

            but you can return a single tuple of values and open it

            this is one of the major motivations for tuples existing in the language
            """

            def f():
                """
                returns multiple arguments
                """
                return 1, 2
                #SAME:
                    #return (1, 2)

            a, b = f()
            assert a == 1
            assert b == 2

        if '## can return nothing':

            """
            If a function does not end on a return statement, it returns `None`.
            """

            def f(b):
                if b:
                    return 1

            assert f(True)  == 1
            assert f(False) == None

    if '## redefine':

        # Like any python object, you can redfine functions whenever you want.

        def f():
            return 0

        def f():
            return 1

        assert f() == 1

        class f:
            pass

    if '## functions can have attributes':

        # Function attributes have no relation to local variables.

        def f():
            c = 1
            return c
        f.c = 2
        assert f() == 1
        assert f.c == 2

        # View all the function attributes:

        print 'dir(f) = ' + str(dir(f))

        # The most important attribute is `__call__` which allows us to call the function:

        assert f.__call__() == 1

    if '## scope':

        """
        If the value of a variable was not defined inside the function,
        the value in the currently executing scope is taken.
        """

        def f(b):
            return a == b

        a = 1
        assert f(1) == True

        a = 2
        assert f(1) == False

        if '## global':

            def global_inc_a_wrong():
                a = 2

            def global_inc_a():
                global a
                a = a + 1

            a = 1
            global_inc_a_wrong()
            assert a == 1
            global_inc_a()
            assert a == 2

            # If the variable was not yet defined on global scope,
            # it then gets defined once the function is called
            # and the assignement occurs:

            def global_def():
                global defined_in_global_def
                #This will define the variable on global scope:
                defined_in_global_def = 1

            try:
                print defined_in_global_def
            except NameError:
                pass
            else:
                assert False

            global_def()

            print defined_in_global_def

            # Global means *global*, and *not* inside another function:

            def outer():
                x = 1
                def inner():

                    #This x is not the same as the first one,
                    #but one on a global scope
                    global x

                    x = 2

                #Here we do not see the global x,
                #but the one inside outer:
                inner()
                assert x == 1

            #Here we see the global x defined inside inner:
            outer()
            assert x == 2

            # Compare this to what happens with nonlocal in Python 3.

    if '## nested functions':

        # This is the way to go:

        def ex8():
            ex8.var = 'foo'
            def inner():
                ex8.var = 'bar'
                print 'inside inner, ex8.var is ', ex8.var
            inner()
            print 'inside outer function, ex8.var is ', ex8.var
        ex8()

    if '## call function from its name on a string':

        #http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python

        pass

if '## class':

    """
    Python classes are designed such that some of its syntax is analogous to C++
    classes.

    However, Python classes are much more dynamic and allow for many things which C++
    classes do not.

    In most cases, Python classes are used with syntax similar to C++ syntax.

    However, there are practical cases where the full flexibility of Python classes are used,
    and your C++ knowledge breaks.

    The faster you learn about how exacly Python classes work, the faster the magic will go away.

    The key points are:

    - classes and everythin else in Python are objects
    - attributes and the dot `.` operator
    - __dict__
    - bound methods
    """

    if 'Classes are objects':

        class C(object):
            i = 1
            pass

        # You can assign it to a variable:

        D = C
        assert D.i == 1

        # You can add attributes to it:

        C.j = 2
        assert C.j == 2

        # You can return it from functions:

        def f(i):
            class C(object):
                if i == 0:
                    j = 0
                else:
                    j = 1
            return C
        assert f(0).j == 0
        assert f(1).j == 1

    if 'Everything is an object':

        # All built-in types like `int`, `string` and `list`:

        assert (1).__class__ == int
        assert "ab".__class__ == str
        assert [1, 2].__class__ == list

        # Functions:

        def f(): pass
        print f.__class__

        # Classes:

        class C(object): pass
        assert C.__class__ == type
        assert C().__class__ == C

        # Modules:

        import os
        print os.__class__

    if '## __metaclass__ ## __new__':

        """
        TODO
        """

    if '## Bound method ## Unbound method':

        """
        <http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static>
        """

        class C(object):
            def __init__(self, i):
                self.i = i
            def m(self):
                return self.i

        c = C(1)

        # When we call a bound method:

        assert c.m() == 1

        # Python executes exactly the following call to an unbound method:

        assert C.m(c) == 1

        # This is why methods without a `self` always fail.

    if '## Object':

        """
        Base type of all Python built-in types.

        In Python 2, it is possible for a user defined object not to
        inherit from `object` (old style class).

        In Python 3, user defined classes automatically inherit from it,
        so every type derives from `object`.
        """

        assert isinstance(1, object)
        assert isinstance("ab", object)

        def f(): pass
        assert isinstance(f, object)

        class C(object): pass
        assert isinstance(C, object)
        assert isinstance(C(), object)

        import os
        assert isinstance(os, object)

        # This is everything objects give to classes:
        print 'dir(object) = ' + str(dir(object))
        print 'dir(object()) = ' + str(dir(object()))

    if '## type':

        """
        Built-in function type does two things:

        - determine the type of an object
        - dynamically create classes from strings

        Important rules:

        - the type of any type (built-in or user defined) is `type`.
        - the type of any object is its type,
            also known as class for user defined types.
        """

        if 'determine type of value':

            """
            The `type` object is at the base of all the hierarchy.
            """

            assert type(type)   == type
            assert type(object) == type
            assert type(1)      == int
            assert type(1.0)    == float
            assert type('abc')  == str
            assert type(u's')   == unicode
            assert type([])     == list
            assert type({})     == dict

            print type(lambda:1)
            #<type 'function'>

            class C(object): pass
            assert type(C) == type
            assert type(C()) == C

            import os
            print type(os)
            #<type 'module'>

        if 'Make classes dynamically':

            class B(object): pass

            class C(B):
                a = 1

            # Same as above.

            C = type('C', (B,), {'a': 1})
            assert C.a == 1

    if '## __class__':

        """
        Corresponding class object of a object.

        The only difference from `type()` seems to be for old style classes:
        <http://stackoverflow.com/questions/1060499/difference-between-typeobj-and-obj-class>

        Therefore, there is no difference in Python 3.
        """

        assert object.__class__ == type
        assert (1).__class__    == int

        """
        `__class__` can be set to something else however.

        This has no special effect.
        """

        class D(object): pass

        class C(object):
            __class__ = D

        assert type(C()) == C
        assert C().__class__ == D

    if '## isinstance':

        """
        TODO: like type but also considers base types?
        """

        assert isinstance(object, type)
        assert isinstance(1, int)
        class C0(object): pass
        class C1(C0): pass
        assert isinstance(C1(), C1)
        assert isinstance(C1(), C0)

    if '## attributes':

        """
        Anything you can get from an object via a dot `.`, including methods and memebers.

        Good tutorial: <http://www.cafepy.com/article/python_attributes_and_methods/contents.html>

        How the dot searches for attributes on `obj.attr`:

        1) `obj.__dict__` itself
        2) `obj.__class__.__dict__`
        3) then searches all base classes via MRO.
        """

        class C:
            pass

        # Create a new attribute for class object C:

        C.i = 1

        c = C()
        c2 = C()

        # Attribute not found on object. Look at class:

        assert c.i == 1

        # Add attribute to object.

        c.i = 2

        # Attribute found on object. Ignore class attributes:

        assert c.i == 2

        # Can use __class__ to reach the class attribute:

        assert c.__class__.i == 1

        # Create a new function attribute for the class:

        def m(self):
            return 1
        C.m = m
        assert C().m() == 1

        if '## haSattr':

            class A:
                a = 1
                def f():
                    pass

            assert hasattr(A, 'a')
            assert hasattr(A, 'f')
            assert not hasattr(A, 'b')

            assert hasattr(A(), 'a')
            assert hasattr(A(), 'f')
            assert not hasattr(A(), 'b')

        if '## geAttr':

            class C:
                def __init__(self, i):
                    self.attribute = i
            c = C(1)
            c.attribute2 = 2
            assert getattr(c, "attribute") == 1
            assert getattr(c, "attribute2") == 2
            assert getattr(c, "notanattribute", "default") == "default"

        if '## seTattr':

            class A: pass

            setattr(A, 'name', 'value')
            assert A.name == 'value'

            ###any expression goes

            hasa = True
            class A:
                if hasa:
                    a = 1
                else:
                    a = 0

            assert A.a == 1

    if '## __dict__':

        """
        Contains all attributes of an object.

        Represents a base data structure for objects, and is used on the magic dot `.` attribute lookup.
        """

        if 'Does not contain attributes inherited through `__class__` and MRO.':

            class B(object):
                a = 1
                def __init__(self):
                    self.b = 1

            class C(B):
                c = 2
                def __init__(self):
                    self.d = 2
                    super(C, self).__init__()

            print 'C.__dict__ = ' + str(C.__dict__)

            C.__dict__
            assert C().__dict__ == {'b':1, 'd':2}

        if 'It is possible to write directly to it from both sides.':

            class C(object): pass
            c = C()
            c.__dict__['a'] = 1
            assert c.a == 1

            c.a = 2
            assert c.__dict__['a'] == 2

            class C(object): pass
            c = C()
            c.__dict__ = {'a':1, 'b':2}
            assert c.a == 1
            assert c.b == 2

            c.__dict__.update({'a':2, 'c':3})
            assert c.a == 2
            assert c.c == 3

            # TODO why not here:

            class C(object): pass
            try:
                C.__dict__['a'] = 1
            except TypeError:
                #'dictproxy' object does not support item assignment
                pass
            else:
                assert False

        # Built-in functions and types don't have a dict.
        # It is not possible to set their attributes.

        try:
            (1).__dict__
        except AttributeError:
            #'int' object has no attribute '__dict__'
            pass
        else:
            assert False

        try:
            (1).a = 2
        except AttributeError:
            #'int' object has no attribute 'a'
            pass
        else:
            assert False

        try:
            (len).a = 2
        except AttributeError:
            #'builtin_function_or_method' object has no attribute 'a'
            pass
        else:
            assert False

        # Functions:

        def f():
            """doc"""
            a = 1
        assert f.__dict__ == {}

        f.a = 1
        assert f.__dict__['a'] == 1

        f.__dict__['b'] = 2
        assert f.b == 2

        print 'f.__dict__ = ' + str(f.__dict__)

        # Sample output:

        #{'a': 1, '__module__': '__main__', '__doc__': 'doc', 'f': <function f at 0x9cb82cc>}

    if '## dir':

        """
        Returns a list of all attributes of an object.

        Includes attributes available through `__class__` and base classes.

        Does a search in the `__dict__` attributes in the same order as the dot `.` operator.
        """

        print 'dir(1) = ' + str(dir(1))
        class C(object): pass
        print 'dir(C) = ' + str(dir(C))
        print 'dir(C()) = ' + str(dir(C()))
        import os
        print 'dir(os) = ' + str(dir(os))

    if '## inspect':

        """
        Module that can do many introspective things on Python objects.
        """

    if '## reflection':

        # Get meta info objects.

        class C:
            """doc"""

            def __init__(self, name):
                """initdoc"""
                self.name = name

            def print_attrs(self):
                """print_attrs_doc"""
                for name in dir(self):
                    attr = getattr(self, name)
                    if not callable(attr):
                        print name, ':', attr


            def print_method_docs(self):
                """print_method_docs.doc"""
                for name in dir(self):
                    attr = getattr(self, name)
                    if callable(attr):
                        print name, ':', attr.__doc__

        c = C('the my object')
        c.print_attrs()

        # TODO: sane way to get only user defined attributes: http://stackoverflow.com/questions/4241171/inspect-python-class-attributes

    if '## vars':

        #list all available names in current scope and their string values:

        vars()

    if '## old style ## new style ## classic':

        """
        In Python 2 there are 2 types of classes:

        - classic classes. The only type that existed up to `2.1`.
            They are deprecated and existed only for backwards compatibility.

        - new-style classes. Appeared in 2.2. To create a new-style class
            it must derive from `object`.

        Always use new style classes for new code.

        In Python 3 classic classes disappear, and it is not necessary
        to derive from `object` anymore.

        <http://stackoverflow.com/questions/2399307/python-invoke-super-constructor>

        Behaviours that have changed between old and new style classes:

        - super added
        - MRO changed
        - descriptors added
        - `__slots__` added
        """

        class Old:
            pass

        class New(object):
            pass

        class New2(New):
            pass

    if '## members':

        # This shows how the concept of instance member variables are usually implemented.

        class A(object):

            def __init__(self, a):
                """
                Constructor.

                Members are defined in the constructor as `self.a = `
                """

                self.member = a

        a = A(0)
        assert a.member == 0
        a.member = 1
        assert a.member == 1

    if '## methods':

        # This shows how the concpet of instance methods variables are usually implemented.

        class A(object):

            def __init__(self, i):
                self.i = i

            def method(self):
                """
                Every non static method must receive self as the first arg.
                """
                return self.i

        assert A(1).method() == 1

    if '## private':

        """
        By convention the underline '_' indicates private varibales and methods.

        Nothing in the language prevents you from using it outside
        except your code breaking later on because you broke the convention.
        """

        class C:
            _private_static = 1
            def __init__(self):
                self._private_member = 2
            def _private_method(self):
                return 3

        assert C._private_static == 1
        assert C()._private_member == 2
        assert C()._private_method() == 3

    if '## static':

        class A(object):

            #static fields:
            static = 0
            static_refcount = 0

            def __init__(self, a=0, b=1):
                """
                Constructor
                """

                # Direct access fail:

                try:
                    static
                except NameError:
                    #global name 'static' is not defined
                    pass
                else:
                    assert False

                # The best way is to use `__class__`:

                self.__class__.static_refcount += 1

                # Also works but not DRY as it repeats the class name;

                A.static = 0

                # Since this is so verbose, just use `self.` instance attributes for singleton classes.
                # - memory is not duplicated because singleton

            @classmethod
            def class_method(cls, x):
                return cls, x

            @staticmethod
            def static_method(x):
                return x

        assert A.static == 0
        A.static = 1
        assert A.static == 1

        if '## classmethod and ## staticmethod':

            """
            The only difference between classmethod and staticmethod is that classmethod
            also gets a reference to the class as argument.

            This means that:

            - classmethod is more versatile and verbose.

                It is required if the method relies on static variables since `self.__class__` is not possible.

            - staticmethod is recommended if the method does not need to access the class,
                since using it serves as self documentation of that fact.

            <http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python>
            """

            a = A()
            assert a.class_method(0) == (A, 0)
            assert A.class_method(0) == (A, 0)
            assert a.static_method(0) == 0
            assert A.static_method(0) == 0

        if 'Static variables are attributes of the class.':

            """
            It is possible to read them as attributes of objects directly,
            if they are not already an attribute of the object, since attribute
            lookup looks at the object and then its class.

            It is not possible to assign to them, or you create a new attribute
            of the object which will shadow that of the class.
            """

            a = A()
            b = A()

            A.static = 0
            assert A.static == 0
            assert a.static == 0
            assert b.static == 0

            A.static = 1
            assert A.static == 1
            assert a.static == 1
            assert b.static == 1

            a.static = 2
            assert A.static == 1
            assert a.static == 2
            assert b.static == 1

            b.static = 3
            assert A.static == 1
            assert a.static == 2
            assert b.static == 3

            """
            You could however achieve that using `__class__`.

            This could be useful if you don't want to repeat the class name.
            """

            a = A()
            b = A()

            A.static = 0
            assert A.static == 0
            assert a.static == 0
            assert b.static == 0

            A.static = 1
            assert A.static == 1
            assert a.static == 1
            assert b.static == 1

            a.__class__.static = 2
            assert A.static == 2
            assert a.static == 2
            assert b.static == 2

            b.__class__.static = 3
            assert A.static == 3
            assert a.static == 3
            assert b.static == 3

    if '## abstract class ## pure virtual method':

        """
        Method that must be overridden on inheritting class.

        There is no language feature that implements that feature,
        since it is a restriction, and Python leaves out all features
        which are simple restrictions.

        There are however conventional idioms that translate it.
        """

        # NotImplementedError idiom.
        # Allows instantiation, but breaks if method is used.

        class C(object):
            def m(self):
                raise NotImplementedError

        c = C()
        try:
            c.m()
        except NotImplementedError:
            pass
        else:
            assert False

        # abstractmethod idiom.
        # Attempt to instantiate class raises `TypeError`.

        import abc

        class C(object):
            __metaclass__ = abc.ABCMeta

            @abc.abstractmethod
            def m(self, i):
                return

        try:
            c = C()
        except TypeError:
            pass
        else:
            assert False

    if '## inheritance':

        class A(object):

            static = 0
            static_overridden = 1

            def __init__(self):
                self.member = 0
                self.member_overridden = 1

            def method(self):
                return 0

            def method_overridden(self):
                return 1

        class B(A):
            """
            This class inherits from A
            """

            static_overridden = 2

            def __init__(self):

                # It is mandatory to call base class constructors explicitly if you want them called.
                super(B, self).__init__()

                # This must come after the base constructor to have an effect:
                self.member_overridden = 2

            def method_overridden(self):
                return 2

        a = A()
        b = B()

        assert B.static == 0
        assert b.member == 0
        assert b.method() == 0

        assert B.static_overridden == 2
        assert b.member_overridden == 2
        assert b.method_overridden() == 2

        #B.static and A.static are two different variables
        B.static = 2
        B.static_overridden = 2
        assert A.static == 0
        assert A.static_overridden == 1

        if '## super':

            """
            Both a:

            -   built-in type (seldom used directly)

            -   method that can only be used inside classes, commonly used to call
                constructors of base classes
                TODO what does it return? How does it work?
                http://www.artima.com/weblogs/viewpost.jsp?thread=236275

            Base class constructors are *not* called automatically!
            http://stackoverflow.com/questions/3782827/why-arent-pythons-superclass-init-methods-automatically-invoked
            """

            class A(object):
                def __init__(self, i):
                    self.i = i

            class B(A):
                def __init__(self, i):
                    # In Python 3 you can write just super().
                    super(B, self).__init__(i)
                    assert type(super(B, self)) == super

            assert B(1).i == 1

            """
            Only works for new style classes.
            """

            class A():
                pass

            class B(A):
                def __init__(self):
                    super(B, self)

            try:
                B()
            except TypeError:
                pass
            else:
                assert False


        if '## inheritance constructor combos':

            class B(A):
                def __init__(
                            self,
                            for_derived_only,
                            named_to_modify,
                            *args,
                            **kwargs
                        ): #note that other named args, before or after modified one will fall into args, so youre fine

                    self.for_derived_only = for_derived_only

                    named_to_modify = named_to_modify + 1

                    #modify args
                    args = [ a+1 for a in args ]

                    #kwargs
                    self.creator = kwargs.pop('arg_derived_only', "default")
                    kwargs['override'] = "new value"

                    #call base calss constructor
                    super(B, self).__init__(named_to_modify, *args, **kwargs)

        if '## __bases__':

            """
            Tuple of direct base classes.
            """

            class C00(object): pass
            class C01(object): pass
            class C02(object): pass
            class C1(C01, C00, C02): pass
            assert C1.__bases__ == (C01, C00, C02)

        if '## MRO ## method resolution order ## C3 linearization':

            """
            Order in which attributes (including methods) are searched for on its base classes.

            This has changed from old style classes to new style classes:

            - old style classes: search from left to right depth first. Stop at first match.
            - new style classes: [C3 linearization](http://en.wikipedia.org/wiki/C3_linearization)

                C3 MRO works as follows: <http://www.python.org/download/releases/2.3/mro/>

            C3 is also used on Perl 6.

            C3 is called C3 *linearization* because it takes as input an inheritance tree
            and outputs a linear list which represents the search order.

            ##__mro__ ##mro()

                The `__mro__` attribute is a tuple of class objects that contains the
                MRO order for the class.

                It only exists for new style classes.

                `mro()` is a method that returns an `__mro__` tuple.
                It can be overridden, and its result is sotored in `__mro__` at class
                instanciation.
            """

            # Old:

            class C: i = 0
            class C1(C): pass
            class C2(C): i = 2
            class C12(C1, C2): pass
            class C21(C2, C1): pass

            assert C12().i == 0
            assert C21().i == 2

            try:
                C12.__mro__
            except AttributeError:
                pass
            else:
                assert False

            # New:

            class C(object): i = 0
            class C1(C): pass
            class C2(C): i = 2
            class C12(C1, C2): pass
            class C21(C2, C1): pass

            assert C12().i == 2
            assert C21().i == 2

            assert C12.__mro__ == (C12, C1, C2, C, object)
            assert C21.__mro__ == (C21, C2, C1, C, object)

            """
            Some hierarchies do not admit linearization.

            In those cases, an exception is raised.
            """

            class C11(object): pass
            class C12(object): pass
            class C21(C11, C12): pass
            class C22(C11, C12): pass
            class C3(C21, C22): pass

    if '## special attributes':

        class A(object):
            """
            The methods here are often accessed via operators such as `<`,
            or are used by global functions such as `str()` (should be inheritance like Java).

            Full list:

            <http://docs.python.org/2/reference/datamodel.html#special-method-names>
            """

            def __init__(self, a=0, b=1):
                self.a = a
                self.b = b

            #def __cmp__(self, other):
                #"""
                #deprecated in 3., forget it!
                #"""

            def __eq__(self, other):
                """
                >>> a = A()
                >>> b = A()
                >>> a == b
                """
                return self.a == other.a

            def __ge__(self, other):
                """
                defines >=
                """
                return

            def __gt__(self, other):
                """
                defines  >
                """
                return

            def __le__(self, other):
                """
                defines <=
                """
                return

            def __lt__(self, other):
                """
                defines <
                """
                return

            def __ne__(self, other):
                """
                defines !=
                """
                return

            def __add__(self, other):
                """
                >>> A(1,2) + A(3,4)
                """

            def __hash__(self, other):
                """
                makes hashable, allowing it to be for example a dictionnary key
                """
                return

            def __str__(self):
                """should return bytes in some encoding,

                called string for compatibility, changed to __bytes__ in python 3"""
                return unicode(self).encode('utf-8')

            def __unicode__(self):
                """informal description, return (possibly unicode) chars

                http://stackoverflow.com/questions/1307014/python-str-versus-unicode

                changed to __str__ in python 3
                """
                return 'a'

            def __repr__(self):
                """
                Difference from str: formal and very precise string represenation of the object.

                What you get if you put an object on a interctive session directly:

                >>> A()
                class A()
                """
                return self.a + ' ' + self.b

            def __len__(self):
                """
                >>> len(a)
                """
                return len(self.a)

            d = {}

            def __setitem__(self, k, v):
                """
                >>> self[k] = v
                """
                d[k] = v

            def __getitem__(self, k):
                """
                >>> self[k]
                """
                return self.d[k]

            def __contains__(self, v):
                """
                >>> v in self
                """
                return v in d

            def __call__(self, n):
                """
                Allows object to be callable as:

                >>> a = A()
                >>> a(1) == 2
                >>> a.__call__(1) == 2
                """
                return n + 1

            """
            Special attributes which shall not be discussed in this class
            because they deserved a more involved discussion:

            - `__slots__`
            - `__get__`, `__set__` and `__delete__`
            """

        if '## equality operator for classes ## __eq__':

            """
            Default does not compare member by member,
            compares adress of object.
            """

            class C:
                def __init__(self,i):
                    self.a = i

            c = C(1)
            c2 = C(1)
            assert c != c2
            c = c2
            assert c == c2

            if '## compare by all members automatically do this':

                class C:
                    def __init__(self, i=0, j=1):
                        self.i = i
                        self.j = j

                    def __eq__(self, other):
                        """
                        all attributes of objects are equal
                        """
                        if type(other) is type(self):
                            return self.__dict__ == other.__dict__
                        return False

                c = C(1)
                c2 = C(1)
                assert c == c2
                c2 = C(2)
                assert c != c2

            if '## __eq__ and None':

                """
                always compare to `None` with is, never with `==`, because `==` can be overwriden by `__eq__`
                for example, to always true, while `is` cannot

                <http://jaredgrubb.blogspot.com.br/2009/04/python-is-none-vs-none.html>
                """

                class A(object):
                    def __eq__(self, other):
                        return True

                a = A()
                assert not a is None
                assert a == None

            if '## __ne__':

                # *Not* automatically deduced from __eq__.

                class C:
                    def __eq__(self, other):
                        return True

                assert C() == C()
                assert C() != C()

        if '## descriptors ## __get__ ## __set__ ## __delete__':

            """
            Allow to control what the dot `.` does on access, assignment and del
            of an attribute.

            Descriptor protocol:

                descr.__get__(self, obj, type=None) --> value

                descr.__set__(self, obj, value) --> None

                descr.__delete__(self, obj) --> None
            """

            class Desc(object):

                def __init__(self):
                    self.i = 0

                def __get__(self, obj, cls=None):
                    return self.i + 1

                def __set__(self, obj, val):
                    self.i = val*val

                def __delete__(self, obj):
                    self.i = 0

            class HasDesc(object):
                i = Desc()

            o = HasDesc()
            o.i = 2
            assert o.i == 5
            del o.i
            assert o.i == 1

            #TODO what do obj and cls do?


            """
            Only work for new style classes
            """

            class Desc():

                def __init__(self):
                    self.i = 0

                def __get__(self, obj, cls=None):
                    return self.i + 1

            class HasDesc():
                i = Desc()

            o = HasDesc()
            assert o.i != 1

            if '## property':

                """
                Allows to make descriptors with a single class.
                """

                assert type(property) == type

                class HasDesc(object):

                    def __init__(self):
                        self._i = 0

                    def geti(self):
                        return self._i + 1

                    def seti(self, val):
                        self._i = val * val

                    def deletei(self):
                        self._i = 0

                    i = property(geti, seti, deletei, "doc")

                o = HasDesc()
                o.i = 2
                assert o.i == 5
                del o.i
                assert o.i == 1

            if '## property as decorators':

                # It is very idiomatic to use property as a decorator as follows:

                class HasDesc(object):

                    def __init__(self):
                        self._i = 0

                    @property
                    def i(self):
                        return self._i + 1

                    @i.setter
                    def i(self, val):
                        self._i = val * val

                    @i.deleter
                    def i(self):
                        self._i = 0

                o = HasDesc()
                o.i = 2
                assert o.i == 5
                del o.i
                assert o.i == 1

            # Application: create a readonly value:

            class HasDesc(object):

                def __init__(self):
                    self._i = 0

                @property
                def i(self):
                    return self._i + 1

            o = HasDesc()
            assert o.i == 1
            try:
                o.i = 2
            except AttributeError:
                pass
            else:
                assert False

        if '## __slots__':

            """
            Only available in new style classes.

            Fixes exactly what attributes a class can have.

            Only to be used as a memory optimization tool when
            there are many many objects of a given type in a performance critical point.
            """

            class Foo(object):
                __slots__ = ['x']
                def __init__(self, n):
                    self.x = n

            y = Foo(1)
            assert y.x == 1
            y.x = 2
            assert y.x == 2

            # This would work for an object without `__slots__`.

            try:
                y.z = 3
            except AttributeError:
                pass
            else:
                assert False

        if '## operators that cannot be overloaded':

            """
            <http://stackoverflow.com/questions/3993239/python-class-override-is-behavior>

            -   is: always implements id compairison.

            -   not, and and or: only depend on the truth value assignment of objects,
                which depends on `__notzero__` and `__len__` in Python 2.

            - assignment: makes no sense since assignment always replaces one object for another.
            """

            class A(object):

                def __is__(self):
                    return True

                def __not__(self):
                    return True

                def __and__(self, other):
                    return True

                def __or__(self, other):
                    return True

            #assert not A()
            #assert A() and A()
            #assert A() or A()

        if '## automaticaly print all members of objects':

            class C:

                def __init__(self, i=0, j=1):
                    self.i = i
                    self.j = j

                def __str__(self):
                    out = '\n' + 30 * '-' + '\n'
                    for k in self.__dict__.keys():
                        out += k + ':\n'
                        out += str(self.__dict__[k]) + '\n\n'
                    return out

            print C()
            print C(1,2)

    if '## assignment operator for classes':

        """
        Objects are mutable, so assignment throws old object away,
        and a is a reference to b now!

        To get around this you can use the copy package.
        """

        class A(object):
            def __init__(self, i):
                self.i = i

        a = A(0)
        b = A(1)

        a = b
        assert a.i == 1
        assert a == b
        a.i = 2
        assert b.i == 2

    if '## copy':

        # Makes copies and deepcopies of objects.

        import copy

        class A(object):
            def __init__(self, i):
                self.i = i

        b = A(1)
        a = copy.copy(b)
        assert a.i == 1
        assert not a == b
        a.i = 2
        assert b.i == 1


    if '## classes can be made inside functions':

        def func(val):
            class A:
                a = val
            return A
        a = func(1)
        print a.a
        b = func(2)
        print b.a
        print a.a #unaltered

    if '## mixin':

        """
        Hard to say what it is in Python, people don't agree much.

        <http://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful>
        """

        if 'single inheritance definition':

            import abc

            class ComparableMixin(object):
                """This clas has methods which use `<=` and `==`,
                but this class does implement those methods."""
                def __ne__(self, other):
                    return not (self == other)
                def __lt__(self, other):
                    return self <= other and (self != other)
                def __gt__(self, other):
                    return not self <= other
                def __ge__(self, other):
                    return self == other or self > other

            class Integer(ComparableMixin):
                def __init__(self, i):
                    self.i = i
                def __le__(self, other):
                    return self.i <= other.i
                def __eq__(self, other):
                    return self.i == other.i

            assert Integer(0) <  Integer(1)
            assert Integer(0) != Integer(1)
            assert Integer(1) >  Integer(0)
            assert Integer(1) >= Integer(1)

            c = ComparableMixin()

            # This particular example could have been achieved via the `functools.total_ordering()` decorator.

            import functools

            @functools.total_ordering
            class Integer(object):
                def __init__(self, i):
                    self.i = i
                def __le__(self, other):
                    return self.i <= other.i
                def __eq__(self, other):
                    return self.i == other.i

            assert Integer(0) < Integer(1)
            assert Integer(0) != Integer(1)
            assert Integer(1) > Integer(0)
            assert Integer(1) >= Integer(1)

        if 'multiple inheritance definition':

            class HasMethod1(object):
                def method(self):
                    return 1

            class HasMethod2(object):
                def method(self):
                    return 2

            class UsesMethod10(object):
                def usesMethod(self):
                    return self.method() + 10

            class UsesMethod20(object):
                def usesMethod(self):
                    return self.method() + 20

            class C_1_10(HasMethod1, UsesMethod10): pass
            class C_1_20(HasMethod1, UsesMethod20): pass
            class C_2_10(HasMethod2, UsesMethod10): pass
            class C_2_20(HasMethod2, UsesMethod20): pass

            assert C_1_10().usesMethod() == 11
            assert C_1_20().usesMethod() == 21
            assert C_2_10().usesMethod() == 12
            assert C_2_20().usesMethod() == 22

if '## Docstring':

    """
    First string that comes after a function or class.

    It is possible to access them at runtime.

    This can be used by documentation generators.

    Their recommended style guide is documented at: <https://www.python.org/dev/peps/pep-0257/>

    Basically: use triple double quoted docstrings, either one-liners or multi-liners.

    For non-docstring string literals, use the same quote type as you use for single quoted strings.
    """

    # Good:

    def f():
        """One liner."""

    assert f.__doc__ == 'One liner.'

    # Good:

    def f():
        """
        Multi liner.
        """

    print repr(f.__doc__)
    assert re.match('\n *Multi liner.\n *', f.__doc__)

    # Bad style, but also works:

    def f():
        'a'

    assert f.__doc__ == 'a'

if '## with':

    """TODO"""

if '## __builtins__':

    #TODO

    #direct acess to all builtin functions:

    __builtins__.dir()

if '## streams':

    """
    Like in C, files and pipes are both similar objects
    meaning that you can do many operations to them transparently
    such as read/write

    The stdin, stdout and stderr streams are always open by default.

    There are however, as in POSIX, some operations may be only
    available to certain types of streams.

    For example, search operations can be done on files, but not on stdin/out.
    """

    if '## print statement':

        """
        In 2.X there is the `print` statement (not a regular function)
        which will be replaced by the print function in 3.X.
        This will make the interface more standard and support more options.

        In 2.X, the `print s` is exactly the same as `sys.stdout.write(s)`.

        ## Parenthesis and the print statement

            The fact that it is a statement, means that:

                print (object, object)

            prints a *tuple*, and it may differ from:

                print (object)

            which prints just object, since `tuple.str()`
            does `repr()` on their contents, not `str()`.

        ## print vs str

            print converts objects with str.

            Well, unless you make an insane C API like sqlite3.Row:
            http://stackoverflow.com/questions/7920284/how-can-printing-an-object-result-in-different-output-than-both-str-and-repr
        """

    if '## stdout':

        sys.stdout.write('stdout')
        print

        # Best way to print without a newline in 2.X:

        # Many shells don't show input immediately until the next newline. To force that use flush.

        import sys
        sys.stdout.write('no newline')
        sys.stdout.flush()
        print

    if '## stderr':

        sys.stderr.write('stderr')

    if '## stdin':

        # Read from stdin until an EOF, that is until:
        #
        # - program on other side of pipe terminates if pipe coming in
        # - user hits ctrl+d on linux (ctrl+z on windows)

        if False:
            sys.stdin.read()

        if '## isatty':

            #check if stdin has a pipe comming in or if its the user who is typing

            if False:

                #test.py
                if sys.stdin.isatty():
                    print True
                else:
                    print False
                print ins

                #echo asdf | test.py

            # prints False (is a pipe, not a terminal) and asdf (read from sdtin)

                #test.py

            # prints True is a user input terminal (no pipes) and waits for user input
            # after ^D, prints what was input by keyboard.

    if '## file IO':

        if 'binary':

            # Best way to open binary files:

            path = os.path.join(tempfile.gettempdir(), 'pythone_fileio.tmp')
            data = 'a\nb'
            try:
                with open(path, 'w') as f:
                    f.write(data)
            except IOError, e:
                print e
                raise
            try:
                with open(path, 'r') as f:
                    assert f.read() == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            # `with` is exception safe: on exception will first close file.

            #http://preshing.com/20110920/the-python-with-statement-by-example
            #http://effbot.org/zone/python-with-statement.htm

        if 'unicode':

            """
            If all you want to do is slurp read, then encoding manually is a fine option as shown here.

            There however operations which are non trivial to do, for example reading linewise,
            which requires knowledge about the encoding to be done. For this kind of operation, use `codecs`.
            """

            path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
            # Euro sign
            data = u"\u20AC"
            try:
                with open(path, "w") as f:
                    # Raises on most implemtatoins:
                    #     UnicodeEncodeError: 'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
                    #f.write(data)
                    f.write(data.encode('utf-8'))

                    # Might work because Python knows if its outputing to a terminal, and uses LC_CTYPE to determine encoding.
                    # May fail if you pipe however, even if output to terminal works fine. In that case Python uses None as encoding.
                    #sys.stdout.write(data)

                    # To automatically change the default encoding non non terminal output, use on you main imported file:
                    # http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python
                    #Output UTF-8 by default.
                    #import sys
                    #reload(sys)  # Reload is required.
                    #sys.setdefaultencoding('utf-8')
            except IOError, e:
                print e
                raise
            try:
                with open(path, "r") as f:
                    read = f.read()
                    assert type(read) == str
                    # Because str, only the first byte!
                    assert read[0] != data
                    assert read.decode('utf-8')[0] == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            if '## codecs':

                import codecs

                # Linewise read. Requires the encoding to be known, and is a non trival operation.

                path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
                # Two line terminated euro signs.
                data = u"\u20AC\n\u20AC\n"
                with open(path, "w") as f:
                    f.write(data.encode('utf-8'))
                # 'r' is the default
                f = codecs.open(path, encoding='utf-8', mode='r')
                lines = []
                for line in f:
                    lines.append(line)
                f.close()
                assert lines[0] == u"\u20AC\n"
                assert lines[1] == u"\u20AC\n"
                os.unlink(path)

    if '## read methods':

        # Read from handle until EOF:

            #sys.stdin.read()
            #f.read()

        # Appends a newline at the end!

        # Read up to 128 bytes:

            #f.read(128)

        # Read single ascii char:

            #f.read(1)

        # Read up to first \n or EOF:

            #f.readline()

        # Same as `f.read().split(\n)`. This is amost never useful because of `xreadlines`.

            #lines = f.readlines()
            #print lines[2];

        # Never do for loops with `readlines`, always user `xreadlines` instead
        # because that way you don't clutter memory, and you can read files larger
        # than memory.

        # Iterator based `readlines`:

            #for l in f.xreadlines():
                #print l

        # This is the way to go for looping over lines one at a time.

        pass

if '## shutil':

    """
    High level file operations based on `os`.
    """

    import shutil

    if '## rmtree ## rm -rf':

        # Recursive directory removal like rm -rf:

        temp = tempfile.mkdtemp()
        with file(os.path.join(temp, 'a'), 'a'): pass
        try:
            os.rmdir(temp)
        except OSError:
            pass
        else:
            assert False
        shutil.rmtree(temp)
        assert not os.path.exists(temp)

    if '## copyfile ## cp':

        # Not a base utility since it can be done naively with with open read write.

        #shutil.copyfile(src, dst)
        pass


    if '## Return value':

        if '## Multiple return values':

            """
            there is no real multiple return values,

            but you can return a single tuple of values and open it

            this is one of the major motivations for tuples existing in the language
            """

            def f():
                """
                returns multiple arguments
                """
                return 1, 2
                #SAME:
                    #return (1, 2)

            a, b = f()
            assert a == 1
            assert b == 2

        if '## can return nothing':

            """
            If a function does not end on a return statement, it returns `None`.
            """

            def f(b):
                if b:
                    return 1

            assert f(True)  == 1
            assert f(False) == None

    if '## redefine':

        # Like any python object, you can redfine functions whenever you want.

        def f():
            return 0

        def f():
            return 1

        assert f() == 1

        class f:
            pass

    if '## functions can have attributes':

        # Function attributes have no relation to local variables.

        def f():
            c = 1
            return c
        f.c = 2
        assert f() == 1
        assert f.c == 2

        # View all the function attributes:

        print 'dir(f) = ' + str(dir(f))

        # The most important attribute is `__call__` which allows us to call the function:

        assert f.__call__() == 1

    if '## lambda':

        """
        Lambda is a function without name

        Lambda functions can only contain a single expression.

        This means in particular that they cannot contain assigments,
        so they are very limited.
        """

        f = lambda x: x + 1
        assert f(0) == 1
        assert f(1) == 2

    if '## scope':

        """
        If the value of a variable was not defined inside the function,
        the value in the currently executing scope is taken.
        """

        def f(b):
            return a == b

        a = 1
        assert f(1) == True

        a = 2
        assert f(1) == False

        if '## global':

            def global_inc_a_wrong():
                a = 2

            def global_inc_a():
                global a
                a = a + 1

            a = 1
            global_inc_a_wrong()
            assert a == 1
            global_inc_a()
            assert a == 2

            # If the variable was not yet defined on global scope,
            # it then gets defined once the function is called
            # and the assignement occurs:

            def global_def():
                global defined_in_global_def
                #This will define the variable on global scope:
                defined_in_global_def = 1

            try:
                print defined_in_global_def
            except NameError:
                pass
            else:
                assert False

            global_def()

            print defined_in_global_def

            # Global means *global*, and *not* inside another function:

            def outer():
                x = 1
                def inner():

                    #This x is not the same as the first one,
                    #but one on a global scope
                    global x

                    x = 2

                #Here we do not see the global x,
                #but the one inside outer:
                inner()
                assert x == 1

            #Here we see the global x defined inside inner:
            outer()
            assert x == 2

            # Compare this to what happens with nonlocal in Python 3.

    if '## nested functions':

        # This is the way to go:

        def ex8():
            ex8.var = 'foo'
            def inner():
                ex8.var = 'bar'
                print 'inside inner, ex8.var is ', ex8.var
            inner()
            print 'inside outer function, ex8.var is ', ex8.var
        ex8()

    if '## call function from its name on a string':

        #http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python

        pass

if '## Docstring':

    """
    First string that comes after a function or class.

    It is possible to access them at runtime.

    This can be used by documentation generators.

    Their recommended style guide is documented at: <https://www.python.org/dev/peps/pep-0257/>

    Basically: use triple double quoted docstrings, either one-liners or multi-liners.

    For non-docstring string literals, use the same quote type as you use for single quoted strings.
    """

    # Good:

    def f():
        """One liner."""

    assert f.__doc__ == 'One liner.'

    # Good:

    def f():
        """
        Multi liner.
        """

    print repr(f.__doc__)
    assert re.match('\n *Multi liner.\n *', f.__doc__)

    # Bad style, but also works:

    def f():
        'a'

    assert f.__doc__ == 'a'

if '## with':

    """TODO"""

if '## __builtins__':

    #TODO

    #direct acess to all builtin functions:

    __builtins__.dir()

if '## streams':

    """
    Like in C, files and pipes are both similar objects
    meaning that you can do many operations to them transparently
    such as read/write

    The stdin, stdout and stderr streams are always open by default.

    There are however, as in POSIX, some operations may be only
    available to certain types of streams.

    For example, search operations can be done on files, but not on stdin/out.
    """

    if '## print statement':

        """
        In 2.X there is the `print` statement (not a regular function)
        which will be replaced by the print function in 3.X.
        This will make the interface more standard and support more options.

        In 2.X, the `print s` is exactly the same as `sys.stdout.write(s)`.

        ## Parenthesis and the print statement

            The fact that it is a statement, means that:

                print (object, object)

            prints a *tuple*, and it may differ from:

                print (object)

            which prints just object, since `tuple.str()`
            does `repr()` on their contents, not `str()`.

        ## print vs str

            print converts objects with str.

            Well, unless you make an insane C API like sqlite3.Row:
            http://stackoverflow.com/questions/7920284/how-can-printing-an-object-result-in-different-output-than-both-str-and-repr
        """

    if '## stdout':

        sys.stdout.write('stdout')
        print

        # Best way to print without a newline in 2.X:

        # Many shells don't show input immediately until the next newline. To force that use flush.

        import sys
        sys.stdout.write('no newline')
        sys.stdout.flush()
        print

    if '## stderr':

        sys.stderr.write('stderr')

    if '## stdin':

        # Read from stdin until an EOF, that is until:
        #
        # - program on other side of pipe terminates if pipe coming in
        # - user hits ctrl+d on linux (ctrl+z on windows)

        if False:
            sys.stdin.read()

        if '## isatty':

            #check if stdin has a pipe comming in or if its the user who is typing

            if False:

                #test.py
                if sys.stdin.isatty():
                    print True
                else:
                    print False
                print ins

                #echo asdf | test.py

            # prints False (is a pipe, not a terminal) and asdf (read from sdtin)

                #test.py

            # prints True is a user input terminal (no pipes) and waits for user input
            # after ^D, prints what was input by keyboard.

    if '## file IO':

        if 'binary':

            # Best way to open binary files:

            path = os.path.join(tempfile.gettempdir(), 'pythone_fileio.tmp')
            data = 'a\nb'
            try:
                with open(path, 'w') as f:
                    f.write(data)
            except IOError, e:
                print e
                raise
            try:
                with open(path, 'r') as f:
                    assert f.read() == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            # `with` is exception safe: on exception will first close file.

            #http://preshing.com/20110920/the-python-with-statement-by-example
            #http://effbot.org/zone/python-with-statement.htm

        if 'unicode':

            """
            If all you want to do is slurp read, then encoding manually is a fine option as shown here.

            There however operations which are non trivial to do, for example reading linewise,
            which requires knowledge about the encoding to be done. For this kind of operation, use `codecs`.
            """

            path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
            # Euro sign
            data = u"\u20AC"
            try:
                with open(path, "w") as f:
                    # Raises on most implemtatoins:
                    #     UnicodeEncodeError: 'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
                    #f.write(data)
                    f.write(data.encode('utf-8'))

                    # Might work because Python knows if its outputing to a terminal, and uses LC_CTYPE to determine encoding.
                    # May fail if you pipe however, even if output to terminal works fine. In that case Python uses None as encoding.
                    #sys.stdout.write(data)

                    # To automatically change the default encoding non non terminal output, use on you main imported file:
                    # http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python
                    #Output UTF-8 by default.
                    #import sys
                    #reload(sys)  # Reload is required.
                    #sys.setdefaultencoding('utf-8')
            except IOError, e:
                print e
                raise
            try:
                with open(path, "r") as f:
                    read = f.read()
                    assert type(read) == str
                    # Because str, only the first byte!
                    assert read[0] != data
                    assert read.decode('utf-8')[0] == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            if '## codecs':

                import codecs

                # Linewise read. Requires the encoding to be known, and is a non-trival operation.

                path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
                # Two line terminated euro signs.
                data = u"\u20AC\n\u20AC\n"
                with open(path, "w") as f:
                    f.write(data.encode('utf-8'))
                # 'r' is the default
                f = codecs.open(path, encoding='utf-8', mode='r')
                lines = []
                for line in f:
                    lines.append(line)
                f.close()
                assert lines[0] == u"\u20AC\n"
                assert lines[1] == u"\u20AC\n"
                os.unlink(path)

    if '## read methods':

        pass

        # Read from handle until EOF:

            #sys.stdin.read()
            #f.read()

        # Appends a newline at the end!

        # Read up to 128 bytes:

            #f.read(128)

        # Read single ascii char:

            #f.read(1)

        # Read up to first \n or EOF:

            #f.readline()

        # Same as `f.read().split(\n)`. This is amost never useful because of `xreadlines`.

            #lines = f.readlines()
            #print lines[2];

        # Never do for loops with `readlines`, always user `xreadlines` instead
        # because that way you don't clutter memory, and you can read files larger
        # than memory.

        # Iterator based `readlines`:

            #for l in f.xreadlines():
                #print l

        # This is the way to go for looping over lines one at a time.

        # Each line ends in a newline.

            # Python 2.x code

        # Get version of module installed with pip:

            #pkg_resources.get_distribution("blogofile").version

        # PEP 8 recommends that modules define `__version__`, but many packages don't do that.
        #http://legacy.python.org/dev/peps/pep-0008/#version-bookkeeping

if '## shutil':

    """
    High level file operations based on `os`.
    """

    import shutil

    if '## rmtree ## rm -rf':

        # Recursive directory removal like rm -rf:

        temp = tempfile.mkdtemp()
        with file(os.path.join(temp, 'a'), 'a'): pass
        try:
            os.rmdir(temp)
        except OSError:
            pass
        else:
            assert False
        shutil.rmtree(temp)
        assert not os.path.exists(temp)

    if '## copyfile ## cp':

        # Not a base utility since it can be done naively with with open read write.

        #shutil.copyfile(src, dst)
        pass
