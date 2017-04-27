#!/usr/bin/env python

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
    http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python/19950198#19950198
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

    if '## implicit __init__ of base class':

        # Parent __init__ is used.

        class C(object):
            def __init__(self, a):
                self.b = a + 1
        class D(C):
            pass
        assert D(1).b == 2

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

if '## double underscore mangling':

    class C(object):
        __x = 1
        def __f(self):
            return 2
        def __g(self):
            # Self automatically unmangles?
            return self.__f() + 1
    try:
        C.__x
    except AttributeError:
        pass
    else:
        assert False
    assert C._C__x == 1
    assert C()._C__f() == 2
    assert C()._C__g() == 3

if '## Iterate over all user defined class variables':

    # http://stackoverflow.com/questions/11371933/are-there-any-other-ways-to-iterate-through-the-attributes-of-a-custom-class-ex

    class C(object):
        x = 1
        y = 2
        def f(self):
            return 1
        @classmethod
        def iter_attributes(cls):
            vars_ = vars(cls)
            for key in vars_:
                val = vars_[key]
                if not key.startswith('__') and not callable(val):
                    yield key, val
    # Yes, class methods are not callable...
    # http://stackoverflow.com/questions/11058686/classmethod-object-is-not-callable
    assert set(x for x,y in C.iter_attributes()) == set(['x', 'y', 'iter_attributes'])

if '## __slots__':

    # Only in new style classes.

    class C(object):
        __slots__ = ('x')
        def __init__(self):
            x = 1;

    # Cannot set any new attributes on class.
    # Great for performance, and sanity!
    try:
        C().y = 2
    except AttributeError:
        pass
    else:
        assert False

if '## __getitem__':

    class C(object):
        def __getitem__(self, x):
            return x + 1
    assert C()[1] == 2
    C()[1] = 2
