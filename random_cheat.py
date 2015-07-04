#!/usr/bin/env python

"""
## random
"""

import random

if '## uniform':

    # Real on interval:

    n = 1000
    su = 0
    l = 0
    r = 1
    for i in xrange(n):
        rand = random.uniform(l,r)
        #print(rand)
        assert rand >= l and rand <= r
        su += random.uniform(0,1)

    # Check average:

    assert su/float((r - l)) - n < 1

if '## randint':

    # Uniform int on interval.

    print(random.randint(0, 3))

if '## choice':

    # Take one element at random from an iterable.

    assert random.choice([0, 1]) in [0, 1]

if '## sample':

    # Takes n *different* elements at random from iterable. Returns an iterable.

    vals = {1:0, 2:0, 3:0}
    n = 2
    for i in random.sample(vals.keys(), 2):
        assert i in vals.keys()
        vals[i] += 1

    for i in vals.keys():
        assert vals[i] == 0 or vals[i] == 1

    assert sum(vals[k] for k in  vals.keys()) == n
