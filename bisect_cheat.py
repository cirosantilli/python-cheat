#!/usr/bin/env python

import bisect

# Insert into sorted list.
# https://stackoverflow.com/questions/8024571/insert-an-item-into-sorted-list-in-python

l = [0, 2, 4]
bisect.insort_left(l, 1)
assert l == [0, 1, 2, 4]

# Find in sorted list.

l = [0, 0, 2]
assert bisect.bisect_left(l, -1) == 0
assert bisect.bisect_left(l, 0) == 0
assert bisect.bisect_right(l, 0) == 2
assert bisect.bisect_left(l, 1) == 2
assert bisect.bisect_left(l, 2) == 2

# Slice sorted list.
# https://stackoverflow.com/questions/13631720/python-optimized-method-of-cutting-slicing-sorted-lists/47477642#47477642

def get_slice(list_, left, right):
    return list_[bisect.bisect_left(list_, left):bisect.bisect_left(list_, right)]
assert get_slice([0, 1, 1, 3, 4, 4, 5, 6], 1, 5) == [1, 1, 3, 4, 4]
