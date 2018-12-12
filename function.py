#!/usr/bin/env python3

if '## Arguments':

    def f(a, b = 0, *args, **kwargs):
        """
        args is a tuple
        kwargs a dicdt

        those names are just a convention,
        any name can be used, ex:

            def g(*myArgs, **myEtraKwargs)
        """

        # args is a tuple.
        for arg in list(args):
            pass
        # you can iterate over it.

        # This is a standard way to give default values:
        kw1 = kwargs.get(1, "default1")
        kw2 = kwargs.get(2, "default2")
        kw2 = kwargs.get(3, "default3")

        return a, b, list(args), kwargs

    # ERROR: argument a has no value
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

        # There is no function overloading in python.

        def f(a):
            """
            Completely destroys last existing f.
            """
            return a

        def f(a, b):
            return a + b

        # Too many args.
        #f(1, 2, 3)

    if 'Default values for lots of kwargs':

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

if '## Redefine a function':

    # Like any python object, you can redfine functions whenever you want.

    def f():
        return 0

    def f():
        return 1

    assert f() == 1

    class f:
        pass

if '## Functions can have attributes':

    # Function attributes have no relation to local variables.

    def f():
        c = 1
        return c
    f.c = 2
    assert f() == 1
    assert f.c == 2

    # View all the function attributes:

    print('dir(f) = ' + str(dir(f)))

    # The most important attribute is `__call__` which allows us to call the function:

    assert f.__call__() == 1

if '## Function scope':

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
            print(defined_in_global_def)
        except NameError:
            pass
        else:
            assert False

        global_def()

        print(defined_in_global_def)

        # Global means *global*, and *not* inside another function:

        def outer():
            x = 1
            def inner():

                # This x is not the same as the first one,
                # but one on a global scope
                global x

                x = 2

            # Here we do not see the global x,
            # but the one inside outer:
            inner()
            assert x == 1

        # Here we see the global x defined inside inner:
        outer()
        assert x == 2

        # Compare this to what happens with nonlocal in Python 3.

if '## Nested functions':

    # This is the way to go:

    def ex8():
        ex8.var = 'foo'
        def inner():
            ex8.var = 'bar'
            print('inside inner, ex8.var is ', ex8.var)
        inner()
        print('inside outer function, ex8.var is ', ex8.var)
    ex8()

if '## call function from its name on a string':

    # http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python

    pass
