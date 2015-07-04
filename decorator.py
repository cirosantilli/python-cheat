#!/usr/bin/env python

"""
## decorator

Decorators are syntaxical sugar syntax that allows to write functions or classes in the forms:

    @decorator
    def f():
        pass

    @decorator
    class C:
        pass

Where `decorator` is any callable such as a function of a class that implements `__call__`.

They are documented together with function and class definition syntax.
"""

if 'Create a function based function decorator':

    def decorator(func):
        def wrapper(i, *args, **kwargs):
            return func(i, *args, **kwargs) + 1
        return wrapper

    # Decorator sugar

    @decorator
    def f(i):
        return i

    assert f(1) == 2

    # Exact same but without decorator sugar:

    def f(i):
        return i

    decorated = decorator(f)
    assert decorated(1) == 2

if 'Multiple decorators':

    def decorator(func):
        def wrapped(i):
            return func(i) + 2
        return wrapped

    def decorator2(func):
        def wrapped(i):
            return func(i) * 2
        return wrapped

    @decorator
    @decorator2
    def f(i):
        return i

    assert f(0) == 2

if 'Create a callable class based function decorator':

    class Decorator:
        def __init__(self, j):
            self.j = j

        def __call__(self, func):
            def wrapper(i, *args, **kwargs):
                return func(i, *args, **kwargs) + self.j
            return wrapper

    # Decorator sugar

    @Decorator(2)
    def f(i):
        return i

    assert f(1) == 3

if 'Create a function based ## class decorator':

    def decorator(cls):
        def f(self):
            return 1
        cls.f = f
        return cls

    @decorator
    class C(object):
        pass

    assert C().f() == 1

if 'It is only possible to decorate functions or classes, not variables.':

    def d():
        pass
    #@d #SyntaxError
    a = 1

if 'Decorators can take multiple arguments.':

    def decorator(func, j):
        def wrapper(i, *args, **kwargs):
            return func(i, *args, **kwargs) + j
        return wrapper

    # Decorator sugar

    #@decorator
    def f(i):
        return i

    # TODO get working
    #assert f(1) == 3

if 'Decorator must take at least one argument to not raise a TypeError.':

    def d():
        pass
    try:
        @d
        def f():
            pass
    except TypeError:
        pass
    else:
        assert False

if 'Decorator functions of __call__ methods must take at exactly one argument.':

    """
    If you want to pass parameters to a decorator, make a class based decorator
    and use its __init__ method for the arguments.
    """

    # Direct function approach fails.

    def decorator(func, j):
        def wrapper(i, *args, **kwargs):
            return func(i, *args, **kwargs) + j
        return wrapper

    try:
        @decorator(2)
        def f(i):
            return i
    except TypeError:
        pass
    else:
        assert False

if 'The decorator call is only made at function / class definition.':

    def decorator(func):
        global i
        i += 1
        def wrapper(*args, **kwargs):
            pass
        return wrapper

    i = 0
    @decorator
    def f():
        pass
    assert i == 1
    f()
    assert i == 1

if 'Decorators can return anything.':

    def d(g):
        return 1

    @d
    def f():
        pass

    assert f == 1

