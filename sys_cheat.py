#!/usr/bin/env python

import sys

if '## command line arguments ## argv':

    print 'sys.argv[0]  = ' + repr(sys.argv[0])
    print 'sys.argv[1:] = ' + repr(sys.argv[1:])

if '## version_info':

    import sys
    print 'sys.version_info = ' + str(sys.version_info)
    print 'sys.version_info.major = ' + str(sys.version_info.major)

    # Check for Python 2.x code.
    if sys.version_info.major == 2:
        pass

if '## exit':

    # Raises an exception instead of realy exiting...
    # http://stackoverflow.com/questions/10166686/how-do-i-exit-program-in-try-except

    try:
        sys.exit(1)
    except SystemExit, e:
        pass
    else:
        assert False

    # If no call is made to sys.exit, exit code is 0.

    #sys.exit()
    #sys.exit(0)
    #sys.exit(1)
