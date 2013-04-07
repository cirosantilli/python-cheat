#!/usr/bin/env python

#http://docs.python.org/2/library/unittest.html
#http://www.diveintopython.net/unit_testing/index.html

import sys
import unittest 

class SomeInput:
    pass

class SomeOutput:

    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __eq__(self, other):
        """
        all attributes of objects are equal
        """
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

class SomeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        called once before all test methods
        """
        print 'test.setUpClass'

    @classmethod
    def tearDownClass(self):
        """
        called once before all test methods
        """
        print 'test.tearDownClass'

    def setUp(self):
        """
        called before each test method
        """
        print 'test.setUp'

    def tearDown(self):
        """
        called after each test method
        """
        print 'test.tearDown'

    ##tests have 3 possible outcomes

    #- OK       The test passes.
    #- FAIL     The test does not pass, and raises an AssertionError exception.

        #this is raised by unit test `assert*` methods as well as the built in `assert`.

    #- ERROR    The test raises an exception other than AssertionError.

    def test_pass(self):
        """
        this test passes
        """
        self.assertEqual( 1, 1 )

    def test_fail(self):
        """
        basic
        """
        self.assertEqual( 1, 2 )

        #stops after first fail because fails raise exceptions:
        assert(False)

    def test_fail2(self):
        """
        any assertion error gives a fail
        """
        raise AssertionError

    def test_error(self):
        """
        this is an error, not a fail!
        """
        raise ZeroDivisionError

    def test_fail_message(self):
        """
        fail message can be explicitly set:
        """
        self.assertEqual( 1, 2, 'message' )

    ##assertEqual

    #with assertTrue() you could make all the others.

    #so why use `assertEqual`?

    #one reason: in case of fail `assertEqual(v,v2)`,
    #it automatically prints a nice message `v + ' != ' v2` for you

    #furthermore, assert equal recognizes the types of inputs
    #and automatically uses one of the nice formattings if available:

    #- assertItemsEqual(a, b) 	sorted(a) == sorted(b) and works with unhashable objs 	2.7
    #- assertMultiLineEqual(a, b) 	strings 	2.7
    #- assertSequenceEqual(a, b) 	sequences 	2.7
    #- assertListEqual(a, b) 	lists 	2.7
    #- assertTupleEqual(a, b) 	tuples 	2.7
    #- assertSetEqual(a, b) 	sets or frozensets 	2.7

    def test_assertEqual_int(self):
        """
        """
        self.assertEqual(1,2)

    def test_assertEqual_dict(self):
        """
        notice the nice formatting that only shows differences!
        """
        self.assertEqual({1:1,2:2},{1:2,3:3})


    def test_objects(self):
        """
        there is no assertEqual for objects.

        there are two alternatives to get the nice formatting

        IMHO, the best way to get this for formatting is:

        1) if the objects are equal iff __dict__ are equal,
            use assertEqual + explicit __dict__ so you get the nice dict formatting.

        2) if the equality is more complex, implement, it
        """
        self.assertEqual( SomeOutput(1,1).__dict__, SomeOutput(1,2).__dict__ )

    def test_because_starts_with_test(self):
        self.assertEqual(1,1)
        self.assertEqual(1,2,'test.another')

    def not_a_test_because_does_not_start_with_test(self):
        print 'test.not_a_test_because_starts_with_test'
        self.assertEqual(1,1)
        self.assertEqual(1,2,'test.another')

class SomeTest2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print 'test2.setUpClass'

    @classmethod
    def tearDownClass(self):
        print 'test2.tearDownClass'

    def setUp(self):
        print 'test2.setUp'

    def tearDown(self):
        print 'test2.tearDown'

    def tearDown(self):
        print 'test2.tearDown'

    def test(self):
        print 'test2.test'
        self.assertEqual(1,1)
        self.assertEqual(1,2,'message')

if __name__ == '__main__':

    ##run tests from a single class

    suite = unittest.TestLoader().loadTestsFromTestCase(SomeTest)
    unittest.TextTestRunner().run(suite)

    ##main

    #finds every class derived from `unittest.TestCase`
    #in cur module and calls their `runTest()` methods

    ##runTest

    #the default is to:
    
    #- call setUpClass
    
    #- search for every method in the class that
    #starts with the string `test` then call in order the class':

        #- setUp
        #- test*
        #- tearDown

    #- call tearDownClass

    #in this order.

    #you could override this method, but the default is pretty good
    #and standard already

    ###exit

    #if True (default), exits program immediately.
    #exit status = 0 if all pass, 1 otherwise.

    #else continue

    unittest.main( exit = False )

    unittest.main()
    assert False
