#!/usr/bin/env python

"""
## NumPy and SciPy

Current best math package for Python.

## Install

On Ubuntu 12.04:

    sudo aptitude install python-scipy

Pip may not work because of missing binary dependencies.

    sudo pip install numpy
    sudo pip install scipy

## NumPy vs SciPy

SciPy uses and extends NumPy (think LAPACK BLAS).

It offers all functions in NumPy and many more conveient ones through the single `scipy` module.

Since NumPy is quite low level, just use SciPy all the time and avoid confusion.

## Sources

- <http://www.scipy.org/Tentative_NumPy_Tutorial>
- <www.scipy.org/PerformancePython>
- <https://github.com/rougier/numpy-100>
- <https://github.com/scipy-lectures/scipy-lecture-notes>
"""

import math
import StringIO

import scipy as sp
import scipy.constants
import scipy.stats
import scipy.linalg as la

def norm2(a):
    """
    Mean squared norm.
    """
    return la.norm(a) / sp.size(a)

def dist2(a, a2):
    return norm2(a - a2)

def array_equal(a, a2, err=10e-6, dist=dist2):
    """
    True iff two sp.arrays are equal within a given `err` precision for given `dist` distance.
    """
    return dist(a, a2) < err

if '## arrays':

    """
    Basic n-dimensional computational object.

    Are like C sp.arrays fixed length and efficient.

    To extend them, must make new one.

    Allocate all at once with zeros.

    $a*b$ and $a+b$ ARE MUCH MORE EFFICIENT THAN PYTHON LOOPS!
    because they are already compiled

    Try to replace every loop with those operations.
    """

if '## data types':

    """
    There are explicit data types for `sp.arrays`.

    System dependant width (most efficient for system):

    - bool_ 	Boolean (True or False) stored as a byte
    - int_     Platform integer (normally either int32 or int64).
    - float_ 	Shorthand for float64.
    - complex_	Shorthand for complex128.

    Those are the same as python types and may be interchanged.

    Fixed widths:

    - int32 	Integer (-2147483648 to 2147483647)
    - uint32 	Unsigned integer (0 to 4294967295)
    - float32 	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
    - float64 	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
    - complex64 	Complex number, represented by two 32-bit floats (real and imaginary components)

    Those have fixed width on all systems, and may not be compatible with the python types.
    """

    assert sp.array_equal(
        sp.array([1, 2, 3], dtype = sp.int_),
        sp.int_([1, 2, 3])
    )

    # Different types evaluate to equal sp.arrays

    assert sp.array_equal(
        sp.array([1, 2, 3], dtype = sp.int_  ),
        sp.array([1, 2, 3], dtype = sp.float_)
    )

    # Get type

    v = sp.array([1,2], dtype = sp.int32)
    assert v.dtype == sp.int32

    # Subtype:

    sp.issubdtype(sp.int32, sp.int_)

    # Convert type

    v = sp.array([1,2], dtype = sp.int32)
    vf = v.astype(sp.float_)
    assert vf.dtype == sp.float_

    ### type_ vs dtype

    # `type_` is the same as using the dtype arg.

    # That said, *always use the sp.array* methods without dtye for uniformity

    # And if you need explicit type, use the dtype arg.

if '## Create arrays':

    ### multidimensional

    v = sp.array([
        [1, 2, 3],
        [4, 5, 6],
    ])

    ### dimensions must match

    # TODO why does this work? type object

    #try:
        #v = sp.array([
            #[1, 2, 3],
            #[4,5],
        #])
    #except ValueError:
        #pass
    #else:
        #assert False

    if '## zeros':

        assert sp.array_equal(
            sp.zeros((1, 2)),
            sp.array([[0,0]])
        )

        assert sp.array_equal(
            sp.zeros((2, 1)),
            sp.array([[0],[0]])
        )

        assert sp.array_equal(
            sp.zeros((1, 2, 3)),
            sp.array([[[0,0,0],
                        [0,0,0]]])
        )

    if '## ones':

        assert sp.array_equal(
            sp.ones((1, 2)),
            sp.array([[1,1]])
        )

    if '## arange':

        # BAD idea:

        '''
        assert array_equal(
            sp.arange(3),
            sp.array([0, 1, 2])
        )
        '''

        # May fail because of precision.

        # Good idea:

        assert array_equal(
            sp.arange(2.1),
            [0, 1, 2]
        )

        assert array_equal(
            sp.arange(2, 5.1),
            [2, 3, 4, 5]
        )

        assert array_equal(
            sp.arange(0.1, 2.2),
            [0.1, 1.1, 2.1]
        )

        assert array_equal(
            sp.arange(0, 5, 2),
            [0, 2, 4]
        )

    if '## linspace':

        assert array_equal(
            sp.linspace(0, 1, 6),
            [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        )

    if '## meshgrid':

        x = sp.arange(0, 2.1)
        y = sp.arange(0, 3.1)
        (X, Y) = sp.meshgrid(x, y)

        assert array_equal(
            X,
            sp.array([
            [ 0.,  1.,  2.],
            [ 0.,  1.,  2.],
            [ 0.,  1.,  2.],
            [ 0.,  1.,  2.]])
        )

        assert array_equal(
            Y,
            sp.array([
            [ 0.,  0.,  0.],
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 3.,  3.,  3.]])
        )

    if '## indices':

        assert array_equal(
            sp.indices((2, 3)),
            sp.array([
                [
                    [0, 0, 0],
                    [1, 1, 1]
                ],
                [
                    [0, 1, 2],
                    [0, 1, 2]
                ]
            ])
        )

if '## size':

    # Get total number of elements:

    assert sp.zeros((2, 3, 4)).size == 24
    assert sp.size(sp.zeros((2, 3, 4))) == 24
    assert sp.size(1) == 1

    # 2 vs 1x2 vs 1x2:

    assert not sp.array_equal(
        [1, 2],    # number of dimensions: 1. size of dimension 1: 2
        [[1, 2]]   #                       2.                    : 1 size of dimension 2: 2
    )

if '## shape':

    # Get / set size of each dimension.

    # Think like this:

    # > The Nth most external list, has how many elements? this is the size of the Nth dimension.

    assert sp.array([1,2]).shape == (2,)
    assert sp.array([[1,2]]).shape == (1,2)
    assert sp.array([[1],[2]]).shape == (2,1)

    ### Change shape

    # In place:

    v = sp.arange(5.1)
    v.shape = (2, 3)
    assert sp.array_equal(
        v,
        [
            [0, 1, 2],
            [3, 4, 5]
        ]
    )

    # Create new:

    assert sp.array_equal(
        sp.arange(5.1).reshape((2, 3)),
        [
            [0, 1, 2],
            [3, 4, 5]
        ]
    )

    # Make into one dimension (create new):

    x = sp.arange(6).reshape(2, 3)
    assert sp.array_equal(
        sp.ravel(x),
        sp.arange(6)
    )

if '## file io':

    # TODO: examples

    """
    a = sp.zeros((2, 3))

    # Space separated.
    sp.savetxt("a.tmp", a)

    sp.savetxt("b.tmp", delimiter = ", ")

    # single width format
    sp.savetxt("c.tmp", delimiter = 3)

    # multi width format
    sp.savetxt("d.tmp", delimiter = (4, 3, 2))

    # strip trailing/starting whitespace
    sp.savetxt("e.tmp", autostrip = True)

    # stop reading line when # is found
    sp.savetxt("f.tmp", comments = '# ')

    # skip first line, and last two lines
    sp.savetxt("g.tmp", skip_header = 1, skip_footer = 2)

    # only use first and last columns
    sp.savetxt("h.tmp", usecols = (0, -1))

    # same, give names
    sp.savetxt("b.tmp", names = "a, b, c", usecols = ("a", "c"))

    b = genfromtxt("a.tmp")

    b = loadtxt("a.tmp")
    """

    if 'loadtxt':

        assert array_equal(
            sp.loadtxt(StringIO.StringIO("0 1\n2 3")),
            [
                [0, 1],
                [2, 3],
            ]
        )

        assert array_equal(
            sp.loadtxt(
                StringIO.StringIO("0 1\n2 3"),
                usecols = (1,)
            ),
            [
                [1, 3],
            ]
        )

        # It is slow for large files:
        # http://stackoverflow.com/questions/18259393/numpy-loading-csv-too-slow-compared-to-matlab

if '## indexing':

    x = sp.arange(5.1)
    x.shape = (2, 3)
    assert x[0, 0] == 0
    assert x[0, 1] == 1
    assert x[1, 0] == 3

    x[0,0] = 1
    assert x[0,0] == 1

    # With array

    x = sp.arange(2.0, 5.1)
    assert sp.array_equal(
        x[[1, 1, 0, 3]],
        [3, 3, 2, 5]
    )

    # TODO:

    x = sp.arange(5.1)
    x.shape = (2,3)
    # assert sp.array_equal(
        # x[ sp.array([[1,0], [0,1]]) ],
        # sp.array([3, 1])
    # )

if '## slicing':

    x = sp.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ])

    assert sp.array_equal(
        x[:, 0],
        [0, 3, 6]
    )

    assert sp.array_equal(
        x[0, :],
        [0, 1, 2]
    )

    assert sp.array_equal(
        x[0:3:2, 0:3:2],
        [
            [0, 2],
            [6, 8]
        ]
    )

if '## broadcasting':

    """
    Means to decide the right operation based on input types.
    """

if '## sum':

    # Arrays of same size:

    assert array_equal(
        sp.arange(5.1).reshape((2,3)) +
        [
            [0, 1, 0],
            [1, 0, 1]
        ],
        [
            [0, 2, 2],
            [4, 4, 6]
        ],
    )

    # Arrays of different size:

    assert array_equal(
        sp.arange(5.1).reshape(2,3) +
        sp.arange(2.1),
        [
            [0, 2, 4],
            [3, 5, 7]
        ]
    )

    # Broadcasting for scalars:

    assert array_equal(
        sp.arange(5.1) + 1,
        sp.arange(1,6.1)
    )

    # Over all elements:

    assert array_equal(
        sp.sum([
            [0, 1],
            [2, 3]
        ]),
        6
    )

    # Some dimensions only:

    assert array_equal(
        sp.sum([[0, 1], [2, 3]], axis = 0),
        sp.array([2, 4])
    )

    assert array_equal(
        sp.sum(
            [
                [0, 1],
                [2, 3]
            ],
            axis = 1
        ),
        [1, 5]
    )

if '## multiplication':

    # Scalar broadcast:

    assert array_equal(
        sp.arange(3.1) * 2,
        sp.arange(0, 6.1, 2.0)
    )

    # Between arrays of same dimensions:

    assert array_equal(
        sp.arange(3.1) *
        sp.arange(3.1),
        sp.array([0, 1, 4, 9])
    )

    # Between arrays of different size:

    assert array_equal(
        sp.arange(5.1).reshape(2,3) *
        sp.arange(2.1),
        [
            [0, 1,  4],
            [0, 4, 10]
        ]
    )

    # Dot product;

    A = sp.array([
        [1, 2],
        [3, 4]
    ])
    x = sp.array([[1, 2]]).T
    assert array_equal(
        A.dot(x),
        sp.array([[5],
                [11]])
    )

if '## vectorize':

    # vectorize a function that was meant for scalar use
    # making it more efficient? TODO confirm.

    def add(a, b):
        return a + b

    vec_add = sp.vectorize(add)
    assert array_equal(
        vec_add(sp.array([0,1,2]), sp.array([3,4,5])),
        sp.array([3,5,7])
    )

## linalg

# matrices, vectors and norms

#### matrix vs 2D arrays

# summary: *prefer 2D arrays*

# everything that can be done with matrix can be done with 2d arrays

# matrix only allows for some shortcuts.

# but in the end, this brings confusion, and gives less flexibility, so prefer arrays.

# just for reference

A = sp.mat('[1 2;3 4')
A = sp.mat('[1, 2; 3, 4')
A = sp.mat([[1, 2], [3, 4]])
b = sp.mat('[5;6]')

A.T # transpose
A.H # conjugate transpose
A.I # inverse
A*b # matrix multiplication
A*A # matrix multiplication

# we will forget the matrix class from now on.

## without mat

### transpose

assert sp.array_equal(
    sp.array([[1,2],[3,4]]).T,
    sp.array([[1,3],[2,4]]),
)

assert sp.array_equal(
    sp.array([[1,2]]).T,
    sp.array([[1],[2]]),
)

# But *watch out*!!!:

assert sp.array_equal(
    sp.array([1,2]).T,
    sp.array([1,2])
)

# T only works as expected on nxm objects, not on n objects!

### conjugate

assert array_equal(
    sp.array([[1j,2j]]).conjugate(),
    sp.array([[-1j,-2j]]),
)

### conjugate transpose

assert array_equal(
    sp.array([[1j,2j]]).conjugate().T,
    sp.array([[-1j],[-2j]]),
)

### identity

assert sp.array_equal(
    sp.eye(2),
    sp.array([[ 1.,  0.],
            [ 0.,  1.]])
)

### determinant

assert array_equal(
    la.det(sp.array([[1,2],[3,4]])),
    -2
)

### inverse

# **DO NOT USE THIS TO SOLVE LINEAR SYSTEMS**

# use <# solve> instead, or an explicit LU decomposition.

# (solve likely uses LU it under the hood)

# This will be faster and more stable.

# Learn what LU decomposition is now if you don't know so.

A = sp.array([[1, 2], [3, 4]])
assert array_equal(
    la.inv(A).dot(A),
    sp.eye(2)
)

### solve

# solve linear system:

A = sp.array([[1, 2], [3, 4]])
b = sp.array([[5, 11]]).T
x = la.solve(A, b)
assert array_equal(
    A.dot(x),
    b
)

# Solve multiple linear systems:

# TODO

A = sp.array([[1, 2], [3, 4]])
b = sp.array([[5, 11],[5,11]])
x = la.solve(A, b)
assert array_equal(
    A.dot(x),
    b
)

# Singular raises exception:

A = sp.zeros((2,2))
b = sp.array([[5, 11]]).T
try:
    x = la.solve(A, b)
except la.LinAlgError:
    pass
else:
    assert False

### eigenvalues and vectors

A = sp.array([[1, 1], [0, 2]])
vals, vecs = la.eig(A)
n = A.shape[0]

# Check they are eigenvectors:

for i in xrange(0,n):
    assert array_equal(
        A.dot(vecs[:,i].T),
        vals[i] * vecs[:,i]
   )

# Check that they are normalized:

assert array_equal(
    sp.sum(abs(vecs**2), axis = 0),
    sp.ones((1,n))
)

### norms

# \max |Ax|_y, |x| = 1, |x|_y = \sqrt{\sum (|x_i|)^y}{y}

# the choice of y gives rise to the different norms

# often they have a simple interpretation for matrices

A = sp.array([[0, 1], [2, 3]])

# sum squares and take square root:

assert array_equal(
    la.norm(A),
    sp.sqrt(sp.sum(A*A))
)
assert array_equal(
    la.norm(A,'fro'),
    sp.sqrt(sp.sum(A*A))
)

# norm inf == max row sum:

assert array_equal(
    la.norm(A,sp.inf),
    max(sp.sum(A, axis = 1))
)

# norm 1 == max column sum:

assert array_equal(
    la.norm(A,1),
    max(sp.sum(A, axis = 0))
)

# norm -1 == min column sum:

assert array_equal(
    la.norm(A,-1),
    min(sp.sum(A, axis = 0))
)

if '## polynomials':

    # 1x^2 + 2x + 3

    p = sp.poly1d([1, 2, 3])

    if '## get info':

        assert sp.array_equal(
            p.coeffs,
            sp.array([1,2,3])
        )

        assert sp.array_equal(
            p.order,
            2
        )

    # Evaluate:

    assert array_equal(p([1,2]), sp.array([6,11]))

    # Roots:

    assert array_equal(p(p.r), sp.zeros(p.order))

    # Operations:

    p**2 + p*p + p
    p.integ(k = 6)
    p.deriv()

if '## random':

    # Mean 1, standard deviation 2:

    sp.random.normal(1, 2)

    # 2 x 3 random sp.arrays:

    assert sp.random.normal(1, 2, (2, 3)).shape == (2,3)

if '## constants':

    # Many physical ones.

    # http://docs.scipy.org/doc/scipy/reference/constants.html

    assert array_equal(scipy.constants.pi, math.pi)

if '## stats':

    if '## pearsonr':

        # https://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient

        assert array_equal(
            scipy.stats.pearsonr(
                [1, 2, 3],
                [2, 4, 6],
            )[0],
            1
        )

        assert array_equal(
            scipy.stats.pearsonr(
                [1, 2, 3],
                [-2, -4, -6],
            )[0],
            -1
        )
