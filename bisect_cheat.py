#!/usr/bin/env python

import bisect

l = [0, 2, 4]
bisect.insort_left(l, 1)
assert l == [0, 1, 2, 4]
