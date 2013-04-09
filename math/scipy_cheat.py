#!/usr/bin/env python

"""
current best maths package for python
"""

##numpy vs scipy

#scipy uses and extends numpy (think lapack blas)

#it offers all functions in numpy

#so just use scipy all the time to avoid confusion

##install

#pip may not work because of missing binary dependencies.

#on ubuntu, the best way to go is:

    #sudo aptitude install python-numpy
    #sudo aptitude install python-scipy

#which takes care of the dependencies.

#you may also try with pip, but it is not sure to work:

    #sudo pip install numpy
    #sudo pip install scipy

import scipy as sp
import scipy.linalg as la

def norm_m2( a ):
    """
    Mean squared norm
    """
    return la.norm( a )/sp.size(a)

def dist_m2( a, a2 ):
    return norm_m2( a - a2 )

def eqa( a, a2, err = 10e-6, dist = dist_m2 ):
    """
    states if two sp.arrays are equal according to some distance
    """
    return dist( a, a2 ) < err

#sources

#- <http://www.scipy.org/Tentative_NumPy_Tutorial>
#- <www.scipy.org/PerformancePython>


#all numpy funcs are available through scipy and much more.

#always use scipy so you don't have to think what is what.

##basic functions

#unlike math.sqrt, this works:

assert eqa( sp.sqrt(-1), 1j )

#so *always* use it

##arrays

#basic n-dimensional computational object

#are like c sp.arrays fixed length and efficient.

#to extend them, must make new one.

#allocate all at once with zeros

#$a*b$ and $a+b$ ARE MUCH MORE EFFICIENT THAN PYTHON LOOPS!
#because they are already compiled

#try to replace every loop with those operations

##datatypes

#there are explicit datatypes for sp.arrays.

#system dependant width (most efficient for system):

#- bool_ 	Boolean (True or False) stored as a byte
#- int_     Platform integer (normally either int32 or int64).
#- float_ 	Shorthand for float64.
#- complex_	Shorthand for complex128.

#those are the same as python types and may be interchanged.

#fixed widths:

#- int32 	Integer (-2147483648 to 2147483647)
#- uint32 	Unsigned integer (0 to 4294967295)
#- float32 	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
#- float64 	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
#- complex64 	Complex number, represented by two 32-bit floats (real and imaginary components)

#those have fixed width on all systems, and may not be compatible with the python types

#equivalent

assert sp.array_equal(
    sp.array( [1, 2, 3], dtype = sp.int_ ),
    sp.int_( [1, 2, 3] )
)

###different types evaluate to equal sp.arrays

assert sp.array_equal(
    sp.array( [1, 2, 3], dtype = sp.int_   ),
    sp.array( [1, 2, 3], dtype = sp.float_ )
)

###get type

v = sp.array([1,2], dtype = sp.int32)
assert v.dtype == sp.int32

###subtypes

sp.issubdtype(sp.int32, sp.int_)

##convert type

v = sp.array([1,2], dtype = sp.int32)
vf = v.astype(sp.float_)
assert vf.dtype == sp.float_

##create

###two equivalent methods

#type_ is the same as using the dtype arg:


#that said, *always use the sp.array* methods without dtye for uniformity

#and if you need explicit type, use the dtype arg.

###multidimensional

v = sp.array([
    [1, 2, 3],
    [4, 5, 6],
])

###dimensions must match

#TODO why does this work? type object

#try:
    #v = sp.array([
        #[1, 2, 3],
        #[4,5],
    #])
#except ValueError:
    #pass
#else:
    #assert False

###shape

#get/set size of each dimension

#think like this:

#the         most external list, has how many elements? this is the size of the first    dimension
#    seconde                                          ?                         second
#...

assert sp.array([1,2]).shape        == (2,)
assert sp.array([[1,2]]).shape      == (1,2)
assert sp.array([[1],[2]]).shape    == (2,1)

###change shape

#in place:

v = sp.arange(5.1)
v.shape = (2,3)
assert sp.array_equal( v, sp.array([[0,1,2],[3,4,5]]) )

#create new:

assert sp.array_equal(
    sp.arange(5.1).reshape((2,3)),
    sp.array([[0,1,2],[3,4,5]])
)

#make into one dimension (create new):

x = sp.arange(6).reshape(2,3)
assert sp.array_equal(
    sp.ravel(x),
    sp.arange(6)
)

###size

#get total number of elements

assert sp.zeros((2,3,4)).size == 24
assert sp.size(sp.zeros((2,3,4))) == 24
assert sp.size(1) == 1

####2 vs 1x2 vs 1x2

assert not sp.array_equal(
    sp.array([1,2]),    #number of dimensions: 1. size of dimension 1: 2
    sp.array([[1,2]])   #                      2.                    : 1 size of dimension 2: 2
)

###zeros

assert sp.array_equal(
    sp.zeros((1, 2)),
    sp.array( [[0,0]] )
)

assert sp.array_equal(
    sp.zeros((2, 1)),
    sp.array( [[0],[0]] )
)

assert sp.array_equal(
    sp.zeros((1, 2, 3)),
    sp.array( [[[0,0,0],
                [0,0,0]]] )
)

###ones

assert sp.array_equal(
    sp.ones((1, 2)),
    sp.array( [[1,1]] )
)

###arange

#BAD idea:

    #assert eqa(
            #sp.arange(3),
            #sp.array([0, 1, 2])
        #)

#mail fail because of precision

#good idea:

assert eqa(
    sp.arange(2.1),
    sp.array([0, 1, 2])
)

assert eqa(
    sp.arange(2, 5.1),
    sp.array([ 2, 3, 4, 5])
)

assert eqa(
    sp.arange(0.1, 2.2),
    sp.array([ 0.1, 1.1, 2.1])
)

assert eqa(
    sp.arange(0, 5, 2),
    sp.array([0, 2, 4])
)

###linspace

assert eqa(
    sp.linspace(0, 1, 6),
    sp.array([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
)

###meshgrid

x = sp.arange(0, 2.1)
y = sp.arange(0, 3.1)
(X, Y) = sp.meshgrid(x, y)

assert eqa(
    X,
    sp.array([
    [ 0.,  1.,  2.],
    [ 0.,  1.,  2.],
    [ 0.,  1.,  2.],
    [ 0.,  1.,  2.]])
)

assert eqa(
    Y,
    sp.array([
    [ 0.,  0.,  0.],
    [ 1.,  1.,  1.],
    [ 2.,  2.,  2.],
    [ 3.,  3.,  3.]])
)

###indices

assert eqa(
    sp.indices((2, 3)),
    sp.array(
        [[[0, 0, 0],
          [1, 1, 1]],

         [[0, 1, 2],
          [0, 1, 2]]])
)

###file io

#a = sp.zeros((2, 3))
#sp.savetxt( "a.tmp", a )
#sp.savetxt("b.tmp", delimiter = ", ")
#sp.savetxt("c.txt", delimiter = 3)                              #single width format
#sp.savetxt("d.txt", delimiter = (4, 3, 2))                      #multi width format
#sp.savetxt("e.txt", autostrip = True)                           #strip trailling/starting whitespace
#sp.savetxt("f.txt", comments = '#')                             #stop reading line when # is found
#sp.savetxt("g.txt", skip_header = 1, skip_footer = 2)           #skip first line, and last two lines
#sp.savetxt("h.txt", usecols = (0, -1) )                         #only use first and last columns
#sp.savetxt("b.txt", names = "a, b, c", usecols = ("a", "c") )   #same, give names
#b = genfromtxt("a.tmp")

###indexing

x = sp.arange(5.1)
x.shape = (2, 3)
assert x[0,0] == 0
assert x[0,1] == 1
assert x[1,0] == 3

x[0,0] = 1
assert x[0,0] == 1

####indexing with array

x = sp.arange(2.0, 5.1)
assert sp.array_equal(
    x[ sp.array([1, 1, 0, 3]) ],
    sp.array([3, 3, 2, 5])
)

#TODO:

x = sp.arange(5.1)
x.shape = (2,3)
#assert sp.array_equal(
    #x[ sp.array([[1,0], [0,1]]) ],
    #sp.array([3, 1])
#)

###slicing

x = sp.arange(8.1).reshape(3, 3)
assert sp.array_equal(
    x[0:3:2, 0:3:2],
    sp.array([[0,2],
              [6,8]])
)

assert sp.array_equal(
    x[:, 0],
    sp.array([0,3,6])
)

###broadcasting

#means to decide the right operation based on input types

###sum

#arrays of same size:

assert eqa(
    sp.arange(5.1).reshape((2,3)) +
    sp.array([[0,1,0],[1,0,1]]),
    sp.array([[0,2,2],[4,4,6]]),
)

#between arrays of different size:

assert eqa(
    sp.arange(5.1).reshape(2,3) +
    sp.arange(2.1),
    sp.array([[ 0,  2, 4],
              [ 3,  5, 7]])
)

#broadcasting for scalars:

assert eqa(
    sp.arange(5.1) + 1,
    sp.arange(1,6.1)
)

#over all elements:

assert eqa(
    sp.sum([[0, 1], [2, 3]]),
    6
)

#some dimensions only:

assert eqa(
    sp.sum([[0, 1], [2, 3]], axis = 0),
    sp.array([2, 4])
)

assert eqa(
    sp.sum([[0, 1], [2, 3]], axis = 1),
    sp.array([1, 5])
)

###multiplication

#scalar broadcast:

assert eqa(
    sp.arange(3.1) * 2,
    sp.arange( 0, 6.1, 2.0 )
)

#elementwise:

assert eqa(
    sp.arange(3.1) * 2,
    sp.arange( 0, 6.1, 2.0 )
)

#between arrays of same dimensions:

assert eqa(
    sp.arange(3.1) *
    sp.arange(3.1),
    sp.array( [0, 1, 4, 9] )
)

#between arrays of different size:

assert eqa(
    sp.arange(5.1).reshape(2,3) *
    sp.arange(2.1),
    sp.array([[ 0,  1,  4],
              [ 0,  4, 10]])
)

###vectorize

#vectorize a func that was meant for scalar use
#making it more efficient? TODO confirm

def add(a, b):
    return a + b

vec_add = sp.vectorize(add)
assert eqa(
    vec_add( sp.array([0,1,2]), sp.array([3,4,5])),
    sp.array([3,5,7])
)

##linalg

#matrices, vectors and norms

####matrix vs 2D arrays

#summary: *prefer 2D arrays*

#everything that can be done with matrix can be done with 2d arrays

#matrix only allows for some shortcuts.

#but in the end, this brings confusion, and gives less flexibility, so prefer arrays.

#just for reference

A = sp.mat('[1 2;3 4') 
A = sp.mat('[1, 2; 3, 4') 
A = sp.mat([[1, 2], [3, 4]])
b = sp.mat('[5;6]')

A.T #transpose
A.H #conjugate transpose
A.I #inverse
A*b #matrix multiplication
A*A #matrix multiplication

#we will forget the matrix class from now on.

##without mat

###transpose

assert sp.array_equal(
    sp.array([[1,2],[3,4]]).T,
    sp.array([[1,3],[2,4]]),
)

assert sp.array_equal(
    sp.array([[1,2]]).T,
    sp.array([[1],[2]]),
)

#but *whatch out*!!! :

assert sp.array_equal(
    sp.array([1,2]).T,
    sp.array([1,2])
)

#T only works as expected on nxm objcts, not on n objcts!

###conjugate

assert eqa(
    sp.array([[1j,2j]]).conjugate(),
    sp.array([[-1j,-2j]]),
)

###conjugate transpose

assert eqa(
    sp.array([[1j,2j]]).conjugate().T,
    sp.array([[-1j],[-2j]]),
)

###identity

assert sp.array_equal(
    sp.eye(2),
    sp.array([[ 1.,  0.],
            [ 0.,  1.]])
)

###determinant

assert eqa(
    la.det(sp.array([[1,2],[3,4]])),
    -2
)

###matrix multiplication

A = sp.array([[1, 2], [3, 4]])
x = sp.array([[1, 2]]).T
assert eqa(
    A.dot(x),
    sp.array([[5],
              [11]])
)

#I insist, this is **not** matrix multiplication!!!!!!!!!!:

A = sp.array([[1, 2], [3, 4]])
x = sp.array([[1, 2]]).T
assert eqa(
    A*x,
    sp.array([[1, 2],
              [6, 8]])
)

###inverse

#please note: **DO NOT USE THIS TO SOLVE LINEAR SYSTEMS**

#use <#solve> instead, or an explicit LU decomposition.

#( solve likelly uses LU it under the hood )

#this will be faster and more stable.

#Learn what LU decomposition is now if you don't know so.

A = sp.array([[1, 2], [3, 4]])
assert eqa(
    la.inv(A).dot(A),
    sp.eye(2)
)

###solve

#solve linear system:

A = sp.array([[1, 2], [3, 4]])
b = sp.array([[5, 11]]).T
x = la.solve(A, b)
assert eqa(
    A.dot(x),
    b
)

#solve many linear systems:

#TODO

A = sp.array([[1, 2], [3, 4]])
b = sp.array([[5, 11],[5,11]])
x = la.solve(A, b)
assert eqa(
    A.dot(x),
    b
)

#singular raises exception:

A = sp.zeros((2,2))
b = sp.array([[5, 11]]).T
try:
    x = la.solve(A, b)
except la.LinAlgError:
    pass
else:
    assert False


###eigenvalues and vectors

A = sp.array([[1, 1], [0, 2]])
vals, vecs = la.eig(A)
n = A.shape[0]

#check they are eigenvectors:

for i in xrange(0,n):
    assert eqa(
        A.dot(vecs[:,i].T),
        vals[i] * vecs[:,i]
    )

#check that they are normalized:

assert eqa(
    sp.sum( abs(vecs**2), axis = 0),
    sp.ones( (1,n) )
)

###norms

#\max |Ax|_y, |x| = 1, |x|_y = \sqrt{\sum (|x_i|)^y}{y}

#the choice of y gives rise to the different norms

#often they have a simple interpretation for matrices

A = sp.array([[0, 1], [2, 3]])

#sum squares and take squre root:

assert eqa(
    la.norm(A),
    sp.sqrt( sp.sum(A*A) )
)
assert eqa(
    la.norm(A,'fro'),
    sp.sqrt( sp.sum(A*A) )
)

#norm inf == max row sum:

assert eqa(
    la.norm(A,sp.inf),
    max( sp.sum( A, axis = 1) )
)

#norm 1 == max column sum:

assert eqa(
    la.norm(A,1),
    max( sp.sum( A, axis = 0) )
)

#norm -1 == min column sum:

assert eqa(
    la.norm(A,-1),
    min( sp.sum( A, axis = 0) )
)

##polynomials

#1x^2 + 2x + 3

p = sp.poly1d([1, 2, 3])

###get info

assert sp.array_equal(
    p.coeffs,
    sp.array([1,2,3])
)

assert sp.array_equal(
    p.order,
    2
)

###evaluate

assert eqa(
    p([1,2]),
    sp.array([6,11])
)

###roots

assert eqa(
    p( p.r ),
    sp.zeros(p.order)
)

###operations

#can sum, multiply, integrated, derive

p**2+p*p+p
p.integ(k = 6)
p.deriv()

##random

#mean 1, standard deviation 2:

sp.random.normal(1, 2)

#2 x 3 random sp.arrays:

assert sp.random.normal(1, 2, (2, 3)).shape == (2,3)

##constants

#many physical

#<http://docs.scipy.org/doc/scipy/reference/constants.html>
