#!/usr/bin/env python

"""
mathematical and scientific libraries and functions
"""

##stdlib

assert abs(-1) == 1
assert abs( sin(0) - 0.0 ) < 0.01 
assert abs( cos(0) - 1.0 ) < 0.01 
assert abs( exp(0) - 1.0 ) < 0.01 

import math

assert abs( math.pi     - 3.14 ) < 0.01 
assert abs( math.exp(0) - 1.0  ) < 0.01 
assert abs( math.exp(1) - 2.71 ) < 0.01 

##numpy

#install:

    #sudo pip install numpy

#import:

import numpy as np

#sources:

#- <http://www.scipy.org/Tentative_NumPy_Tutorial>
#- <www.scipy.org/PerformancePython>


#all numpy funcs are available through scipy and much more,
#so always use scipy so you don't have to think what is what

###arrays

    #are like c arrays fixed length and efficient.

    #to extend them, must make new one.

    #allocate all at once with zeros

    #$a*b$ and $a+b$ ARE MUCH MORE EFFICIENT THAN PYTHON LOOPS!
    #because they are already compiled

    #try to replace every loop with those operations

#there are explicit datatypes:

#- bool 	Boolean (True or False) stored as a byte
#- int 	Platform integer (normally either int32 or int64)
#- int32 	Integer (-2147483648 to 2147483647)
#- uint32 	Unsigned integer (0 to 4294967295)
#- float 	Shorthand for float64.
#- float32 	Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
#- float64 	Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
#- complex 	Shorthand for complex128.
#- complex64 	Complex number, represented by two 32-bit floats (real and imaginary components)

            #arrays

                #create
                    np.float_([1, 2, 3])

                    np.array([1, 2, 3], dtype = float32)
                    np.array([1, 2, 3], dtype = 'f32')

                    np.zeros((2, 3))
                    np.ones((2, 3))

                    #arange
                        >>> np.arange(10)
                        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                        >>> np.a'ro'range(2, 10, dtype = np.float)
                        array([ 2., 3., 4., 5., 6., 7., 8., 9.])
                        >>> np.arange(2, 3, 0.1)
                        array([ 2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])

                    #linspace
                        >>> np.linspace(1., 4., 6)
                        array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])

                    #meshgrid
                        >>> x = arange(0., 2.1)
                        >>> y = arange(0., 3.1)
                        >>> (X, Y) = meshgrid(x, y)
                        >>> X
                        array([[ 0.,  1.,  2.],
                            [ 0.,  1.,  2.],
                            [ 0.,  1.,  2.],
                            [ 0.,  1.,  2.]])
                        >>> Y
                        array([[ 0.,  0.,  0.],
                            [ 1.,  1.,  1.],
                            [ 2.,  2.,  2.],
                            [ 3.,  3.,  3.]])

                    #indices
                    >>> np.indices((3, 3))
                    array([[[0, 0, 0], [1, 1, 1], [2, 2, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]])

                    #from/to file
                        try:
                            a = np.zeros((3, 3))
                            np.savetxt("a.txt", a)
                        except Exception, e:
                            logging.error(e)

                        try:
                            print genfromtxt("myfile.txt")
                            print np.savetxt("b.txt", delimiter = ", ")
                            print np.savetxt("b.txt", delimiter = 3) #single width format
                            print np.savetxt("b.txt", delimiter = (4, 3, 2)) #multi width format
                            print np.savetxt("b.txt", autostrip = True) #strip trailling/starting whitespace
                            print np.savetxt("b.txt", comments = '#') #stop reading line when # is found
                            print np.savetxt("b.txt", skip_header = 1, skip_footer = 2) #skip first line, and last two lines
                            print np.savetxt("b.txt", usecols = (0, -1) ) #only use first and last columns
                            print np.savetxt("b.txt", names = "a, b, c", usecols = ("a", "c") ) #same, give names
                        except Exception, e:
                            logging.error(e)


                #get type
                    z.dtype
                    np.issubdtype(np.dtype(int))

                #convert type
                    z.astype(float)

                #modify dimension
                    >>> x = np.arange(6)
                    >>> x
                    array([ 0.,  1.,  2.,  3.,  4.,  5.])
                    >>> x.shape = (2, 3)
                    >>> x
                    array([[ 0.,  1.,  2.],
                        [ 3.,  4.,  5.]])
                    >>> x = np.array([[1, 2, 3], [4, 5, 6]])
                    >>> print np.ravel(x)
                    [1 2 3 4 5 6]


                #indexing
                    >>> x = arange(6)
                    >>> x.shape = (2, 3)
                    >>> x[1, 0]
                    3
                    >>> x[0]
                    array([0, 1, 2])

                    #array indexing
                        >>> x = np.arange(10, 1, -1)
                        >>> x
                        array([10,  9,  8,  7,  6,  5,  4,  3,  2])
                        >>> x[np.array([3, 3, 1, 8])]
                        array([7, 7, 9, 2])

                #slicing
                    #same as python, except ::
                    >>> y = np.arange(35).reshape(5, 7)
                    >>> y[1:5:2, ::3]
                    array([[ 7, 10, 13],
                        [21, 24, 27]])

                #operations
                    #broadcasting
                    #means to decide the right operation based on types
                    >>> a = np.array([1.0, 2.0, 3.0])
                    >>> b = 2.0
                    >>> a * b
                    array([ 2.,  4.,  6.])

                    >>> a = np.array([1.0, 2.0, 3.0])
                    >>> b = np.array([2.0, 2.0, 2.0])
                    >>> a + b
                    array([ 3.,  4.,  5.])
                    >>> a * b
                    array([ 2.,  4.,  6.])

                    >>> x = arange(6)
                    >>> x.shape = (2, 3)
                    >>> y = int_([1, 2, 3])
                    >>> x*y
                    array([[ 0,  2,  6],
                        [ 3,  8, 15]])

                #sum
                    >>> np.sum([0.5, 1.5])
                    2.0
                    >>> np.sum([0.5, 0.7, 0.2, 1.5], dtype = np.int32)
                    1
                    >>> np.sum([[0, 1], [0, 5]])
                    6
                    >>> np.sum([[0, 1], [0, 5]], axis = 0)
                    array([0, 6])
                    >>> np.sum([[0, 1], [0, 5]], axis = 1)
                    array([1, 5])

        #constants. simple mathematical
            #http://docs.scipy.org/doc/numpy/reference/c-api.coremath.html

###scipy

        #higher level operations

        #uses numpy, and givew view to all numpy objects are available here

        #therefore only use this and forget what is what.

        #sudo aptitude install python-scipy

        #create arrays

            r_[3, [0]*5, -1:1:10]
            #row concat

            c_ #TODO
            #2d array concat

            #polynomials
                >>> p = poly1d([3, 4, 5])
                >>> print p
                2
                3 x + 4 x + 5
                >>> print p*p
                4      3      2
                9 x + 24 x + 46 x + 40 x + 25
                >>> print p.integ(k = 6)
                3     2
                x + 2 x + 5 x + 6
                >>> print p.deriv()
                6 x + 4
                >>> p([4, 5])
                array([ 69, 100])

            #vectorize a func that was meant for scalar use
                >>> @vecorize
                ... def addsubtract(a, b):
                ...    if a > b:
                ...        return a - b
                ...    else:
                ...        return a + b
                >>> vec_addsubtract([0, 3, 6, 9], [1, 3, 5, 7])

        #linalg
            #numpy.linalg vs scipy.linalg
                #numpy also has a linalg package, but scipy.linalg
                #implements all the functions in numpy and more
                #so just use scipy.linalg

            #numpy.matrix vs 2D ndarrays
                #matrix is just for convenience!
                #use ndarrays always
                #if you insist no using np.matrix..
                    A = mat('[1 2;3 4']) 
                    A = mat('[1, 2; 3, 4']) 
                    A = mat([[1, 2], [3, 4]])
                    b = mat('[5;6]'])

                    A*b #matrix multiplication
                    A.I #inverse
                    A.H #conjucate transpose


            #matrix multiplication and transpose
                #are done with numpy

            #transpose and multiply
                >>> import numpy as np
                >>> from scipy import linalg
                >>> A = np.array([[1, 2], [3, 4]])
                >>> A
                array([[1, 2],
                    [3, 4]])
                >>> linalg.inv(A)
                array([[-2. ,  1. ],
                    [ 1.5, -0.5]])
                >>> b = np.array([[5, 6]]) #2D array
                >>> b
                array([[5, 6]])
                >>> b.T
                array([[5],
                    [6]])
                >>> A*b #not matrix multiplication!
                array([[ 5, 12],
                    [15, 24]])
                >>> A.dot(b.T) #matrix multiplication
                array([[17],
                    [39]])
                >>> b = np.array([5, 6]) #1D array
                >>> b
                array([5, 6])
                >>> b.T  #not matrix transpose!
                array([5, 6])
                >>> A.dot(b)  #does not matter for multiplication
                array([17, 39])

            #conjugate transpose
                A.conjugate()

            #identity
                >>> eye(2)
                array([[ 1.,  0.],
                    [ 0.,  1.]])

            #determinant
                linalg.det(A)

            #inverse
                linalg.inv(A)

            #solve linear system. not only shortcut: better algorithm
                A = mat('[1 3 5; 2 5 1; 2 3 8]')
                b = mat('[10;8;3]')
                linalg.solve(A, b)

            #eigenvalues and vectors
                >>> from scipy import linalg
                >>> A = mat('[1 5 2; 2 4 1; 3 6 2]')
                >>> la, v = linalg.eig(A)
                >>> l1, l2, l3 = la
                >>> print l1, l2, l3
                (7.95791620491+0j) (-1.25766470568+0j) (0.299748500767+0j)

                >>> print v[:, 0]
                [-0.5297175  -0.44941741 -0.71932146]
                >>> print v[:, 1]
                [-0.90730751  0.28662547  0.30763439]
                >>> print v[:, 2]
                [ 0.28380519 -0.39012063  0.87593408]
                >>> print sum(abs(v**2), axis = 0)
                [ 1.  1.  1.]

            #norms
                >>> A = mat('[1, 2; 3, 4]')
                >>> A
                matrix([[1, 2],
                        [3, 4]])
                >>> linalg.norm(A)
                5.4772255750516612
                >>> linalg.norm(A, 'fro') #'fro' is default
                5.4772255750516612
                >>> linalg.norm(A, 1)
                6
                >>> linalg.norm(A, -1)
                4
                >>> linalg.norm(A, inf)
                7

        #statistics
            from numpy.random import normal

            normal(1, 2)
            #mean 1, standard deviation 2

            normal(1, 2, (2, 3))
            #2 per 3 random variables 

        #constants. many physical
            #http://docs.scipy.org/doc/scipy/reference/constants.html

