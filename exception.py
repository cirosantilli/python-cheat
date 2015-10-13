#!/usr/bin/env python

"""
## Exception
"""

import sys

# They go up until something catches them:

def e():
    raise Exception

def d():
    e()

try:
    d()
except:
    pass
else:
    raise Exception

"""
If nothing catches them, they explode on stdX and stop program execution!

What gets printed:

    traceback: where the exception came from (modules, functions, lines)
        #this is useful for debug, so you can find where the problem comes from

    <Exception class>: <exception.__repr__>
        raise Exception("repr")
        print "cant reach here"
"""

if '## else':

    # Only execute if the exception did not happen.

    try:
        raise Exception()
    except:
        pass
    else:
        assert False

    e = False
    try:
        pass
    except:
        assert False
    else:
        e = True
    assert e

if '## finally':

    # Always executed, whether the exception happened or not.

    f = False
    try:
        raise Exception()
    except:
        pass
    else:
        assert False
    finally:
        f = True
    assert f

    f = False
    try:
        pass
    except:
        assert False
    else:
        pass
    finally:
        f = True
    assert f

if '## raise':

    # Parenthesis or not:
    # http://stackoverflow.com/questions/16706956/is-there-a-difference-between-raising-an-exception-and-exception

    if 'What can be raised':

        # Only old style classes or derived classes from exception can be raised.

        # In particular, strings cannot be raised, or that raises a `TypeError` instead of the string.

        # This was made possible around Python 2.5, but removed in Python 2.6.

        class Old: pass
        try:
            raise Old()
        except Old:
            pass
        else:
            assert False

        class New(object): pass
        try:
            raise New()
        except TypeError:
            pass
        else:
            assert False

        class New(Exception): pass
        try:
            raise New()
        except New:
            pass
        else:
            assert False

        # Since `'str'` is a new style object:

        try:
            raise 'str'
        except TypeError:
            pass
        else:
            assert False

        # A lightweight alternative is to raise Exception with a custom message:

        try:
            raise Exception('str')
        except Exception:
            pass
        else:
            assert False

    if '## Custom exception':

        class CustomException(Exception):
            def __init__(self, value):
                self.parameter = value
            def __str__(self):
                return repr(self.parameter)
        try:
            raise CustomException('msg')
        except CustomException, (instance):
            print instance.parameter

if '## except':

    # Except catches derived classes only:

    try:
        raise Exception()
    except ZeroDivisionError:
        print 'ZeroDivisionErrorOnly or derived classes'
    except Exception:
        print 'Exception, or its derived classes, therefore all exceptions'
    except:
        print 'same as above'

if '## Pass arguments to exceptions':

    try:
        raise Exception(1, 2)
        # Same as above, but more verbose and implicit. NEVER user this.
        #raise Exception, (1, 2)
    except Exception, e:
        print 'e is an instance of Exception'
        print 'Exception, e = ' + str(e)
        print e.args[0], e.args[1]

if '## reraise':

    # Can be used to add/modify info

    # It is hard to modify and reraise i python 2

    # It seems python 3 introduces the `raise from` statement which makes that much easier!

    #<http://stackoverflow.com/questions/696047/re-raising-exceptions-with-a-different-type-and-message-preserving-existing-inf>

    try:

        raise Exception('msg')

    except Exception, e:

        # You lose the traceback:

        #raise Exception("updated msg\n" + str(e))

        # To keep the traceback:

        #import traceback
        #traceback.print_exc(
            ##file = sys.stdout #stderr is the default
        #)

        # For more info on current exception:

        print 'sys.exc_info() = '
        print sys.exc_info()
        print 'sys.exc_type() = '
        print sys.exc_type
        print 'sys.exc_value() = '
        print sys.exc_value
        print 'sys.exc_traceback() = '
        print sys.exc_value

        # The following forms keep the traceback:

        #raise e
        #raise

if '## built-in exceptions':

    """
    Like other built-ins, the following exceptions are always available
    without any imports.

    <http://docs.python.org/2/library/exceptions.html>
    """

    try:
        print 1/0
    except ZeroDivisionError:
        pass
    else:
        raise

    try:
        int('a')
    except ValueError:
        print 'not a number'

    try:
        f = open("NONEXISTENT")
    except IOError, (err, msg):
        if err == 2:
            print "does not exist", msg
        else:
            print "no exception"

    if '## KeyboardInterrupt':

        # Program got a SIGINT, generated when user presses control c on Linux terminals.

        if False:
            try:
                for i in itertools.count():
                    pass
            except KeyboardInterrupt:
                print "had enough of waiting"
