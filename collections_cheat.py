#!/usr/bin/env python

import collections

if 'OrderedDict':

    # Ordered by insertion order, not natural key order.

    d = collections.OrderedDict()
    d[1] = 2
    d[0] = 0
    d[2] = 1

    # Iteration.
    i = iter(d)
    assert(next(i) == 1)
    assert(next(i) == 0)
    assert(next(i) == 2)

    # Other built-in methods.
    assert d.keys() == [1, 0, 2]
    assert d.items() == [(1, 2), (0, 0), (2, 1)]
