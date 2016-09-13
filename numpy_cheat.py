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
    True iff two numpy.arrays are equal within a given `err` precision for given `dist` distance.
    """
    return dist(a, a2) < err

if '## ndarray':

    if '## slicing':

        x = numpy.array([
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ])

        assert numpy.array_equal(
            x[:, 0],
            [0, 3, 6]
        )

        assert numpy.array_equal(
            x[0, :],
            [0, 1, 2]
        )

        assert numpy.array_equal(
            x[0:3:2, 0:3:2],
            [
                [0, 2],
                [6, 8],
            ]
        )

        # Pairwise list!
        assert numpy.array_equal(
            x[[0, 1], [1, 2]],
            [1, 5]
        )

        # Submtraix.
        assert numpy.array_equal(
            x[[[0], [1]], [1, 2]],
            [
                [1, 2],
                [4, 5],
            ]
        )

        # Transposed.
        assert numpy.array_equal(
            x[[0, 1], [[1], [2]]],
            [
                [1, 4],
                [2, 5],
            ]
        )

    if '## Split by value of column':

        """
        http://stackoverflow.com/questions/21757680/python-separate-matrix-by-column-values
        """

        a = numpy.array([
            [0, 1,  1],
            [1, 1, -1],
            [0, 2,  2],
            [1, 2, -2],
            [0, 3,  3],
            [1, 3, -3],
        ])
        aa = numpy.array([
            [
                [0, 1,  1],
                [0, 2,  2],
                [0, 3,  3],
            ],
            [
                [1, 1, -1],
                [1, 2, -2],
                [1, 3, -3],
            ],
        ])

        if '## Known keys':

            assert numpy.array_equal(
                a[a[:, 0] == 0, :],
                numpy.array([
                    [0, 1, 1],
                    [0, 2, 2],
                    [0, 3, 3],
                ])
            )
            assert numpy.array_equal(
                a[a[:, 0] == 1, :],
                numpy.array([
                    [1, 1, -1],
                    [1, 2, -2],
                    [1, 3, -3],
                ])
            )

        if '## Unknown values':

            keys = list(set(a[:, 0]))
            for key in keys:
                assert numpy.array_equal(
                    a[a[:, 0] == key, :],
                    aa[key],
                )
