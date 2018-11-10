#!/usr/bin/env python

"""
## dict

## Map

Unordered map of hashable keys and to values of any type.
"""

if '## create':

    # Built-in constructor syntax:

    d = {1: 'a', 'b': 2, 1.1: 2}

    # Global factory function.

    # From list of pairs:

    assert dict([(0, 'zero'), (1, 'one')]) == {0: 'zero', 1: 'one'}

    # From kwargs (keys can only be strings):

    assert dict(zero=0, one=1) == {'zero': 0, 'one': 1}

    # dict comprehension:

    assert {key: value for (key, value) in [(1, 2), (3, 4)]} == {1: 2, 3: 4}

    # Keys must be hashable. This excludes all mutable built-in types like lists.

    try:
        d = {[1]: 2}
    except TypeError:
        pass
    else:
        assert False

    if '## fromkeys':

        # <https://docs.python.org/2/library/stdtypes.html#dict.fromkeys>

        # Create a dictionary with keys from a list, and a single value.

        # `dict` here is the `dict` type.

        assert dict.fromkeys([1, 2, 3]) == {1: None, 2: None, 3: None}
        assert dict.fromkeys([1, 2, 3], 0) == {1: 0, 2: 0, 3: 0}

        # Note however that this is not usually what you want for mutable objects:
        # http://stackoverflow.com/questions/8174723/dictionary-creation-with-fromkeys-and-mutable-objects-a-surprise

# To list of pairs:

d = {1: 'one', 2: 'two'}
assert set(d.items()) == set([(1, 'one'), (2, 'two')])

# Get list of keys (undefined order)

d = {1: 'one', 2: 'two'}
assert set(d.keys()) == set([1, 2])

# Why a list is returned by keys() instead of set():
# http://stackoverflow.com/questions/13886129/why-does-pythons-dict-keys-return-a-list-and-not-a-set
# set() didn't exist yet!

# To string:

print "dict str() = "
print d

# Undefined output because undefined key order.

# Get value of key:

d = {1: 'one', 2: 'two'}
assert d[1] == 'one'

# If not in dict, `KeyError` exception:

d = {}
try:
    d['not-a-key']
except KeyError:
    pass
else:
    assert False

# Check if key is in dict:

d = {1: 2}

if 1 in d:
    pass
else:
    assert False

if 2 in d:
    assert False

# Get default value if not present:

assert d.get('not-a-key', 'default value') == 'default value'

# Add new pair:

d= {}
d[0] = 'zero'
assert d == {0: 'zero'}

# Remove pair:

d= {0: 'zero'}
del d[0]

# If key not present, KeyError:

try:
    del d[0]
except KeyError:
    pass
else:
    assert False

# Add new pair if key not present:

d = {1: 2}
assert d.setdefault(1, 3) == 2
assert d == {1: 2}

d = {}
assert d.setdefault(1, 3) == 3
assert d == {1: 3}

if '## update':

    # https://stackoverflow.com/questions/577234/python-extend-for-a-dictionary

    # Add update all keys on d0 with those of d1:

    d0 = {0: 'zero', 1: 'one'}
    d1 = {0: 'zero2', 2: 'two'}
    assert d0.update(d1) is None
    assert d0 == {0: 'zero2', 1: 'one', 2: 'two'}

    # Create a new dict that is the union of two other dicts:

    d0 = {0: 'zero', 1: 'one'}
    d1 = {0: 'zero2', 2: 'two'}
    d01 = d0.copy()
    assert d01.update(d1) is None
    assert d01 == {0: 'zero2', 1: 'one', 2: 'two'}

if 'Iterate / loop over dict':

    # Unspecified order. Python 3 has `collections.OrderedDict` (backported to 2.7).

    # Keys only:

    assert sorted([i for i in {1:-1, 2:-2}]) == [1, 2]

    if '##iteritems':

        # Keys value pairs:

        assert sorted([(i,j) for i,j in {1:-1, 2:-2}.iteritems()]) == [(1, -1), (2, -2)]

    # Iteritems sorted by key. Must pull all into memory first.

    assert [(i,j) for i,j in sorted({2:-2, 1:-1}.iteritems())] == [(1, -1), (2, -2)]

    # Iteritems is out of Python3. Items is present in both 2 and 3
    # but returns a list, not an iterator. 2to3 converts it automatically.

if '## filter':

    """
    Only keys in a list:
    http://stackoverflow.com/questions/6827834/how-to-filter-a-dict-to-contain-only-keys-in-a-given-list

    Arbitrary function:
    http://stackoverflow.com/questions/2844516/python-filter-a-dictionary

    Comprehensions are the only way it seems.
    """
