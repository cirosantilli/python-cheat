#!/usr/bin/env python

#use as quick and dirty testing for simpler functions
#cannot replace really unit tests, specially for more complex functions
#serves as good example documentation

def local_search(self, query, numresults=_LOCAL_RESULTS_PER_PAGE, **kwargs):
    """
    Searches Google Local for the string `query` and returns a
    dictionary of the results.

    >>> print "asdf"
    adsf
    >>> for a in [1,3,2]:
    ...   print a
    1
    3
    2
    >>> function_defined_on_this_module():
    out
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#unpredictable output
    class MyClass(object):
        pass

    def unpredictable(obj):
        """Returns a new list containing obj.

        >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
        [<doctest_ellipsis.MyClass object at 0x...>]
        """
        return [obj]

###exceptions

def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')
