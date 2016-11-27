#!/usr/bin/env python

import StringIO

import numpy as np

def norm2(a):
    """
    Mean squared norm.
    """
    return np.linalg.norm(a) / a.size

def dist2(a, a2):
    return norm2(a - a2)

def array_equal(a, a2, err=10e-6, dist=dist2):
    """
    True iff two np.arrays are equal within a given `err` precision for given `dist` distance.
    """
    return dist(a, a2) < err

if '## ndarray':

    if '## slicing':

        x = np.array([
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ])

        assert np.array_equal(
            x[:, 0],
            [0, 3, 6]
        )

        assert np.array_equal(
            x[0, :],
            [0, 1, 2]
        )

        assert np.array_equal(
            x[0:3:2, 0:3:2],
            [
                [0, 2],
                [6, 8],
            ]
        )

        # Pairwise list!
        assert np.array_equal(
            x[[0, 1], [1, 2]],
            [1, 5]
        )

        # Submtraix.
        assert np.array_equal(
            x[[[0], [1]], [1, 2]],
            [
                [1, 2],
                [4, 5],
            ]
        )

        # Transposed.
        assert np.array_equal(
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

        a = np.array([
            [0, 1,  1],
            [1, 1, -1],
            [0, 2,  2],
            [1, 2, -2],
            [0, 3,  3],
            [1, 3, -3],
        ])
        aa = np.array([
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

            assert np.array_equal(
                a[a[:, 0] == 0, :],
                np.array([
                    [0, 1, 1],
                    [0, 2, 2],
                    [0, 3, 3],
                ])
            )
            assert np.array_equal(
                a[a[:, 0] == 1, :],
                np.array([
                    [1, 1, -1],
                    [1, 2, -2],
                    [1, 3, -3],
                ])
            )

        if '## Unknown values':

            keys = list(set(a[:, 0]))
            for key in keys:
                assert np.array_equal(
                    a[a[:, 0] == key, :],
                    aa[key],
                )

    if '## sum':

        # Over all elements.
        assert array_equal(
            np.sum([
                [0, 1],
                [2, 3]
            ]),
            6
        )

        # Some dimensions only.
        assert array_equal(
            np.sum([[0, 1], [2, 3]], axis = 0),
            [2, 4]
        )
        assert array_equal(
            np.sum([[0, 1], [2, 3]], axis = 1),
            [1, 5]
        )

    if '## Structured array ## dtype':

        """
        Using dtype changes the form of the array.
        It becomes a list of tuples.
        Insane.

        Types specifiers at: http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
        """

        x = np.array([
                (0, 1),
                (2, 3),
            ],
            dtype=[
                ('a', 'i4'),
                ('b', 'f4')
            ]
        )
        assert type(x) == np.ndarray
        assert type(x[0]) == np.void
        assert type(x[0][0]) == np.int32
        assert type(x[0][1]) == np.float32
        assert type(x[1][0]) == np.int32
        assert type(x[1][1]) == np.float32
        assert np.array_equal(x['a'], [0, 2])
        assert np.array_equal(x['b'], [1.0, 3.0])
        assert x[0]['a'] == 0

        # Does not work with arrays here. Insane.
        # x = np.array([
                # [0, 1],
                # [2, 3],
            # ],
            # dtype=[('a','i4'),('b','f4')]
        # )

        # Cannot use two indexes.
        try:
            assert x[0, 0] == 1
        except IndexError:
            pass
        else:
            assert False

        # print type(a[0])
        # assert a[0] == (1, 2.0, 'ab')

if '## file io':

    # TODO: examples

    """
    a = np.zeros((2, 3))

    # Space separated.
    np.savetxt("a.tmp", a)

    np.savetxt("b.tmp", delimiter = ", ")

    # single width format
    np.savetxt("c.tmp", delimiter = 3)

    # multi width format
    np.savetxt("d.tmp", delimiter = (4, 3, 2))

    # strip trailing/starting whitespace
    np.savetxt("e.tmp", autostrip = True)

    # stop reading line when # is found
    np.savetxt("f.tmp", comments = '# ')

    # skip first line, and last two lines
    np.savetxt("g.tmp", skip_header = 1, skip_footer = 2)

    # only use first and last columns
    np.savetxt("h.tmp", usecols = (0, -1))

    # same, give names
    np.savetxt("b.tmp", names = "a, b, c", usecols = ("a", "c"))

    b = genfromtxt("a.tmp")

    b = loadtxt("a.tmp")
    """

    if 'loadtxt':

        assert np.array_equal(
            np.loadtxt(StringIO.StringIO("0 1\n2 3\n")),
            [
                [0.0, 1.0],
                [2.0, 3.0],
            ]
        )

        # Dtype works like for the array constructor.
        x = np.loadtxt(
            StringIO.StringIO("0 1\n2 3\n"),
            dtype=[('a', 'i4'), ('b', 'f4')]
        )
        assert type(x) == np.ndarray
        assert type(x[0]) == np.void
        assert type(x[0][0]) == np.int32
        assert type(x[0][1]) == np.float32
        assert type(x[1][0]) == np.int32
        assert type(x[1][1]) == np.float32


        # usecols

        assert array_equal(
            np.loadtxt(
                StringIO.StringIO("0 1\n2 3\n"),
                usecols=(1,)
            ),
            [
                [1.0, 3.0],
            ]
        )

        # It is slow for large files:
        # http://stackoverflow.com/questions/18259393/numpy-loading-csv-too-slow-compared-to-matlab
