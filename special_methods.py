#!/usr/bin/env python

"""
The methods here are of form __XXX__ and are often accessed via operators such as `<`,
or are used by global functions such as `str()` (should be inheritance like Java...).

Full list:

http://docs.python.org/2/reference/datamodel.html#special-method-names
"""

class A(object):
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

        http://jaredgrubb.blogspot.com.br/2009/04/python-is-none-vs-none.html
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
