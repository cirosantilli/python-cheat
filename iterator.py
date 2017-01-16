#!/usr/bin/env python

"""
## Iterator

Iterators are more memory efficent for iterations than lists
since there is no need to store the entire sequence!

However, if you must calculate each new item, so more time expensive if
you are going to use it more than once

It is a classic space/time tradeoff.
"""

if '## __getitem__':

    # The thing used for dictionnary lookup.

    class C(object):
        def __getitem__(self, index):
            return index + 1
    assert C()[0] == 1
    assert C()[1] == 2

    # For loops use it if `__iter__` is not present, ans passes index to it.

    class C(object):
        def __init__(self):
            self.l = [1, 2, 3]
        def __getitem__(self, index):
            if index < len(self.l):
                return self.l[index]
            else:
                # TODO which exceptions can be used? All of the following work:
                raise StopIteration
                raise IndexError
    l = []
    c = C()
    for d in c:
        l.append(d)
    assert l == [1, 2, 3]

if '__iter__':

    """
    If present:

    - gets called by for loop instead of __getitem__
    - the object is called an iterable object
    """

    class C(object):
        def __init__(self):
            self.l = [1, 2, 3]
            self.i = 0
        def next(self):
            if self.i < 3:
                ret = self.l[self.i]
                self.i += 1
                return ret
            else:
                raise StopIteration
        def __iter__(self):
            return self
        def __getitem__(self, index):
            # Never called in this example.
            raise Exception
    l = []
    c = C()
    for d in c:
        l.append(d)
    assert l == [1, 2, 3]

    if '# len() of iterable':

        # http://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-pythonhttp://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-pythonhttp://stackoverflow.com/questions/3345785/getting-number-of-elements-in-an-iterator-in-python

        # __iter__ and next() Does not imply len().
        # len(C())

        # Best method:

        assert sum(1 for _ in C()) == 3

    if '# Must return an "iterator type"':

        """
        # Iterator type

        A type that has a `next` method.
        """

        class C(object):
            def __iter__(self):
                return 13
        try:
            iter(C())
        except TypeError:
            pass
        else:
            assert False

if '## next':

    """
    Calls the `next` method of the class. __next__ in python 3.

    An iterator is an object that defines this method.

    There is no has_next method.
    The only way is to catch the `StopIteration` exception:
    http://stackoverflow.com/questions/1966591/hasnext-in-python-iterators
    """

    class C(object):
        def __init__(self):
            self.l = [1, 2, 3]
            self.i = 0
        def next(self):
            if self.i < 3:
                ret = self.l[self.i]
                self.i += 1
                return ret
            else:
                raise StopIteration
    c = C()
    assert next(c) == 1
    assert next(c) == 2
    assert next(c) == 3
    try:
        next(c)
    except StopIteration:
        pass
    else:
        assert False

    # Not iterable.

    c = C()
    try:
        for d in c:
            pass
    except TypeError:
        pass
    else:
        assert False

if 'Generators':

    """
    Object that:
    - is returned by yield
    - has literal of form "(i for i in ble)"
    - implements __iter__ (and is thus iterable)
    """

    if '## yield':

        """
        Syntax sugar magic.

        Function is magically pre-parsed, and now returns a generator.

        When yield calls, function is put into magic suspended state.

        A generator object implements __iter__ and can be used in for loop.
        """

        def f():
            l = [1, 2, 3]
            i = 0
            while i < len(l):
                ret = l[i]
                i += 1
                yield ret
        l = []
        mygenerator = f()
        for d in mygenerator:
            l.append(d)
        assert l == [1, 2, 3]

        if '# send (yield)':

            """
            http://stackoverflow.com/questions/19302530/python-generator-send-function-purpose
            """

    if '## generator expression':

        """
        Quick way to make generators.

        TODO: no generator constructor?
        """

        genexpr = (i for i in [1, 2, 3])
        l = []
        mygenerator = f()
        for d in mygenerator:
            l.append(d)
        assert l == [1, 2, 3]

        def f():
            yield 1
        genexpr_f = f()
        assert type(genexpr) == type(genexpr_f)

    if 'No random access':

        genexpr = (i for i in [1, 2, 3])
        try:
            genexpr[0]
        except TypeError:
            pass
        else:
            assert False

if 'Built-in iterator functions':

    # Random stuff, might as well be in itertools.

    if '## enumerate':

        assert list(enumerate(['a', 'c', 'b']) ) == [(0, 'a'), (1, 'c'), (2, 'b'), ]

    if '## reduce':

        """
        - take two leftmost, apply func
        - replace the two leftmost by the result
        - loop

        On the example below:

        - 2*3 - 1 = 5
        - 2*5 - 3 = 8
        """

        assert reduce(lambda x, y: 2*x - y, [3, 1, 2]) == 8

if '## itertools':

    import itertools

    """
    Hardcore iterator patterns.
    http://docs.python.org/2/library/itertools.html#recipes
    """

    # Cartesian product:

    l = [x for x in itertools.product(xrange(2), xrange(3))]
    assert l == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
    ]

    # Join two iterators:

    assert [i for i in itertools.chain(xrange(2), xrange(2))] == [0, 1, 0, 1]

if '## Applications':

    if 'Merge two lists of same length odd / even elements':

        # http://stackoverflow.com/questions/18041840/python-merge-two-lists-even-odd-elements

        # Same length:

        x = [0, 1]
        y = [2, 3]
        assert [ x for t in zip(x,y) for x in t ] == [0, 2, 1, 3]
