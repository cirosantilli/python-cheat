#!/usr/bin/env python

"""
## set

Unordered mutable set of unique elements.

Quick reference:

    len(s)                            cardinality of set s
    x in s                            test x for membership in s
    x not in s                        test x for non-membership in s
    s.issubset(t)                     s <= t  test whether every element in s is in t
    s.issuperset(t)                   s >= t  test whether every element in t is in s
    s.union(t)                        s | t   new set with elements from both s and t
    s.intersection(t)                 s & t   new set with elements common to s and t
    s.difference(t)                   s - t   new set with elements in s but not in t
    s.symmetric_difference(t)         s ^ t   new set with elements in either s or t but not both
    s.copy()                          new set with a shallow copy of s
    s.update(t)                       s |= t  return set s with elements added from t
    s.intersection_update(t)          s &= t  return set s keeping only elements also found in t
    s.difference_update(t)            s -= t  return set s after removing elements found in t
    s.symmetric_difference_update(t)  s ^= t  return set s with elements from s or t but not both
    s.add(x)                          add element x to set s
    s.remove(x)                       remove x from set s; raises KeyError if not present
    s.discard(x)                      removes x from set s if present
    s.pop()                           remove and return an arbitrary element from s; raises KeyError if empty
    s.clear()                         remove all elements from set s
"""

# Literals:

assert {0, 1} == set([0, 1])

# Empty set literal: nope, syntax conflict with dict:
# http://stackoverflow.com/questions/6130374/empty-set-literal-in-python

assert {} == dict()
assert set() == set([])

# List *without* order of unique elements:

assert {2, 1} == {1, 2}

# Iteration order undefined.

# Factory built-in method: takes any iteratorable.

assert set([1, 2]) == set((1, 2))

# Add new element:

s = {1, 2}
assert s.add(3) is None
assert s == {1, 2, 3}

# If already present, do nothing:

assert s.add(2) is None
assert s == {1, 2, 3}

# Remove an element:

s = {1, 2}
assert s.remove(2) is None
assert s == {1}

# If not present, raises `KeyError`:

try:
    s.remove(2)
except KeyError:
    pass
else:
    assert False

# Elements must implement `__hash__`. This *excludes* any mutable built-in type.

s = set()
try:
    s.add([1])
except TypeError:
    pass
else:
    assert False

