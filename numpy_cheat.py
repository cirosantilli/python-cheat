#!/usr/bin/env python

import numpy

def norm2(a):
    """
    Mean squared norm.
    """
    return numpy.linalg.norm(a) / a.size

def dist2(a, a2):
    return norm2(a - a2)

def array_equal(a, a2, err=10e-6, dist=dist2):
    """
    True iff two sp.arrays are equal within a given `err` precision for given `dist` distance.
    """
    return dist(a, a2) < err

if '## ndarray':

    if '## Split by value of column':

        """
        http://stackoverflow.com/questions/21757680/python-separate-matrix-by-column-values
        """

        # Known values.
        a = numpy.array([
            [0, 1,  1],
            [1, 1, -1],
            [0, 2,  2],
            [1, 2, -2]
        ])
        a0 = a[a[:, 0] == 0, :]
        a1 = a[a[:, 0] == 1, :]
        assert numpy.array_equal(
            a0,
            numpy.array([
                [0, 1, 1],
                [0, 2, 2]
            ])
        )
        assert numpy.array_equal(
            a1,
            numpy.array([
                [1, 1, -1],
                [1, 2, -2]
            ])
        )

        a = numpy.array([
            [1, 0, 0],
            [2, 0, 0],
            [1, 1, 1],
            [2, 1, 1],
            [1, 2, 2],
            [2, 2, 4],
        ])
        i = numpy.array([1, 2])
        b = a[numpy.array([True, False, True, False, True, False]), :]
        b = a[numpy.array([True, False, True, False, True, False]), i]
        print(b)
        print(b[:, i])

        # Unknown key values.
        a = numpy.array([
            [0, 1,  1],
            [1, 1, -1],
            [2, 1,  2],
            [0, 2,  2],
            [1, 2, -2],
            [2, 2,  4],
            [0, 3,  3],
            [1, 3, -3],
            [2, 3,  6],
        ])
        keys = list(set(a[:, 0]))
        for key in keys:
            print(a[a[:, 0] == key, [1, 2]])

        a = numpy.array([
            [1, 0, 0],
            [2, 0, 0],
            [1, 1, 1],
            [2, 1, 1],
            [1, 2, 2],
            [2, 2, 4],
        ])
        keys = list(set(a[:, 0]))
        for key in keys:
            print(a[a[:, 0] == key, [1, 2]])
