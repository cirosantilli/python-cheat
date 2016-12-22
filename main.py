#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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

if '## memoryview':

    """
    TODO
    """

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

                # Unlike `=`, for immutable types `x += 1` makes `x` point to another address.
                x = 1
                x += 1
                assert id(x) == id(2)

                def f(y):
                    # Same as y = x
                    y += 1
                x = 1
                f(x)
                assert x == 1

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
