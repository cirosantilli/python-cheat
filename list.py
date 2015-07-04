#!/usr/bin/env python

"""
## list

    List of any mixture of types.
"""

if '## Create new list':

    # List have literals:

    l = [1, 2, 'a', 'b']

    # List have a global factory method that takes an iterable.
    # Therefore they can be built from anything that is iterable:

    # From tuples:

    assert list((1, 2)) == [1, 2]

    # From iterators:

    assert list(xrange(0, 3)) == [0, 1, 2]

    if '## range':

        # Creates lists directly:

        assert range(3) == [0, 1, 2]
        assert range(1, 3) == [1, 2]
        assert range(1, 6, 2) == [1, 3, 5]

    if 'n copies of given element':

        # <http://stackoverflow.com/questions/8528178/list-of-zeros-in-python>

        # The best method for immutable objects is `*`:

        assert [0] * 4 == [0, 0, 0, 0]

    if '## List comprehension':

        assert [i for i in xrange(4) if i != 2] == [0, 1, 3]

        # Multilevel / nested: TODO parenthise this to understand it better.

        assert [i for j in [1, 2] for i in [j, -j]] == [1, -1, 2, -2]

    if '## map method':

        assert map(lambda i: 2 * i, xrange(3)) == [0, 2, 4]

    if '## + for lists ## plus for lists':

        l = range(2)
        assert l + [2, 3] == [0, 1, 2, 3]
        assert l == range(2)

    if '## += for lists':

        """
        Same as extend.

        http://stackoverflow.com/questions/3653298/concatenating-two-lists-difference-between-and-extend

        And `a = a + b` is different from `a += b`, take `b = [a]`:
        `+=` generates a list that contains itself, `+` does not.
        """

    if '## ... ## Elipses in a list that contains itself':

        # Python can deal with lists that contain a refernce to itself.

        # This ugly thing can only happen in dynamically typed languages:
        # on template based languages like C++ and Java, the outter list must always be one level above:

            #List<List<Integer>> l.append(List<Integer>);

        a = []
        a += [a]
        assert str(a) == '[[...]]'

    if '## slice':

        l = range(4)
        assert l[:2] == [0, 1]
        assert l[2:] == [2, 3]
        assert l[:-2] == [0, 1]
        assert l[-2:] == [2, 3]

        l = range(5)
        assert l[::2]   == [0, 2, 4]
        assert l[:3:2]  == [0, 2]
        assert l[2::2]  == [2, 4]
        assert l[0:3:2] == [0, 2]
        assert l[::-1]  == [4, 3, 2, 1, 0] #invert list!

        if '## ellipsis #...':

            """
            TODO
            """

    if '## sorted':

        l = [2, 1]
        assert sorted(l) == [1, 2]
        assert l == [2, 1]

    if '## remove dupes':

        assert list(set([1, 2, 1])) == [1, 2]

if '## len ## size ## length':

    # Get list length.

    pass

if 'Modify inplace':

    l = range(3)
    l[0] = 10
    assert l == [10, 1, 2]

    if '## append':

        # Append a single element to the end.

        l = range(3)
        assert l.append(3) == None
        assert l == [0, 1, 2, 3]

    if '## extend':

        # Same as `+=`.

        # Append all elements of a given list to another.

        # Similar to `+` but in-place.

        l = range(3)
        assert l.extend([3, 4]) == None
        assert l == [0, 1, 2, 3, 4]

    l = range(3)
    assert l.insert(0, 3) == None
    assert l == [3, 0, 1, 2]

    if '## pop':

        l = range(3)
        assert l.pop(1) == 1
        assert l == [0, 2]

        l = range(3)
        assert l.pop() == 2
        assert l == [0, 1]

    if '## remove':

        # Remove first occurence of value.

        l = [0, 1, 0]
        assert l.remove(0) == None
        assert l == [1, 0]

        # If not present, exception:

        l = [0, 1]
        try:
            l.remove(2)
        except ValueError:
            pass
        else:
            assert False

    if '## del':

        """
        Remove element from list.

        Is a statement.

        You *cannot* get a return value from it:

            a = del l[0]

        Rather insane: why is this not a list method? Why a language *statement*?
        I'd rather use `pop(i)`.
        """

        l = range(3)
        del l[1]
        assert l == [0, 2]

    if '## sort':

        l = [2, 1, 3]
        assert l.sort() == None
        assert l == [1, 2, 3]
        assert None == l.sort(reverse=True)
        assert l == [3, 2, 1]

if '## Items are references, not copies':

    l0 = [0]
    l1 = l0
    l1[0] = 1
    assert l0 == [1]

    l0 = [0]
    l1 = [l0]
    l1[0][0] = 1
    assert l0 == [1]

if '## access':

    l = [0, 1, 2]
    assert l[0] == 0
    assert l[1] == 1
    assert l[2] == 2

    assert l[-1] == 2
    assert l[-2] == 1

    if '## out of bounds':

        l = [0, 1]
        try:
            l[3]
        except IndexError:
            pass
        else:
            assert False

        # Use default value if out of bounds:

        l = range(3)
        i = 1
        assert l[i] if i < len(l) else 'default' == 1
        i = 3
        assert l[i] if i < len(l) else 'default" == "default'

if '## concatenate':

    assert [0, 2] + [1, 3] == [0, 2, 1, 3]

if '## find item':

    # First match for criteria with generator expression:

    assert next(pair for pair in [(1, 1), (2, 1), (2, 2)] if pair[0] == 2) == (2, 1)

    # Uses the given default if not found:

    assert next((pair for pair in [(1, 1), (2, 1), (2, 2)] if pair[0] == 3), None) == None

    # If no default, exception:

    try:
        next(pair for pair in [(1, 1), (2, 1), (2, 1)] if pair[0] == 3) == (2, 1)
    except StopIteration:
        pass
    else:
        assert False

if '## filter':

    # Leave only elements for which a function is True.

    l = range(4)
    assert filter(lambda x: x % 2 == 1, l) == [1, 3]
    assert l == range(4)

    ##ifilter

        # `itertools.ifilter` for iterators.
        # https://docs.python.org/2/library/itertools.html#itertools.ifilter
