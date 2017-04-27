#!/usr/bin/env python

if 'Single string':

    # Works with a single string, until you start doing serialization loops.
    # So never do it, always use tuples of strings.

    class C(object):
        # Bad.
        # __slots__ = "ab"
        # Good.
        __slots__ = ("ab",)
        def __init__(self):
            self.ab = 1
        def __getstate__(self):
            return (None, {k:getattr(self, k) for k in C.__slots__})
    assert C().ab == 1
    import pickle
    assert pickle.loads(pickle.dumps(C(), -1)).ab == 1
