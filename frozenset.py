#!/usr/bin/env python

"""
## frozenset

Immutable version of set.

As a consequence, it is hashable.
"""

fs = frozenset([0, 1])
try:
    fs.add(2)
except AttributeError:
    pass
else:
    assert False

assert fs == set([0, 1])
