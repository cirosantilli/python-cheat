#!/usr/bin/env python

"""
## Iterator

## yield
"""

"""
Iterators are more memory efficent for iterations than lists
since there is no need to store the entire sequence!

However, if you must calculate each new item, so more time expensive if
you are going to use it more than once

It is a classic space/time tradeoff.
"""

if '## create':

    # An iterator is just a function with a `yield` method:

    def count():
        """this is already built-in"""
        i = 0
        yield i
        i = i+1

    # Raise exception when over:

        def myxrange(n):
            i = 0
            yield i
            i = i+1
            if i > n:
                raise StopIteration

    if '## generator expressions':

        # Shorthand way to create iterators

        it = (i for i in xrange(10))
        for i in it:
            print i

        # Parenthesis can be ommited for single argument func call:

        def mysum(vals):
            total = 0
            for val in vals:
                total += val
            return total

        assert mysum(i for i in [0, 2, 5]) == 7

    if '## iter':

        # Converts various types to iterators.

        iter('abc')
        iter([1, 2, 3])

if '## next':

    # Will not work with `xrange`! <http://late.am/post/2012/06/18/what-the-heck-is-an-xrange>

    #next(xrange(1))

    i = iter(xrange(2))
    assert next(i) == 0
    assert i.next() == 1
    try:
        next(i)
    except StopIteration:
        pass
    else:
        assert False

    # Use default value if over:

    it = iter(xrange(1))
    assert next(it) == 0
    assert next(it, 3) == 3
    assert next(it, 3) == 3

    # There is no has_next method.
    # The only way is to catch the `StopIteration` exception:
    # <http://stackoverflow.com/questions/1966591/hasnext-in-python-iterators>

if '## iterators can\'t be rewinded':

    # Either store a list on memory or recalculate.

    # Recalculate:

    it = iter('asdf')
    for i in it:
        print 'first'
        print i
    it = iter('asdf')
    for i in it:
        print 'second'
        print i

    # Store on memory:

    it = list(iter('asdf'))
    for i in it:
        print 'first'
        print i
    for i in it:
        print 'second'
        print i

if 'Built-in iterator functions':

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

    Most important ones:

    - imap: map for iterators
    - izip: count to infinity
    - count: count to infinity
    """

    # Cartesian product:

    for i, j in itertools.product(xrange(3), xrange(3)):
        print i, j

    # Join two iterators:

    assert [i for i in itertools.chain(xrange(2), xrange(2))] == [0, 1, 0, 1]

if '## Applications':

    if 'Merge two lists of same length odd / even elements':

        # http://stackoverflow.com/questions/18041840/python-merge-two-lists-even-odd-elements

        # Same length:

        x = [0, 1]
        y = [2, 3]
        assert [ x for t in zip(x,y) for x in t ] == [0, 2, 1, 3]
