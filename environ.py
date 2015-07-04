#!/usr/bin/env python

"""
## environ

## Environment variables
"""

import os

# A dictionnary that contains all environment variables:

print('os.environ = ' + str(os.environ))

# Get one from the dict:

if 'PATH' in os.environ:
    print('PATH = ' + os.environ['PATH'])

# Always check if it is defined before using it.

# Loop over them all:

#for v in os.environ:
    #print(v + ' = ' + os.environ[v])

if '## set values':

    if 'Good':

        os.environ['SOME_VAR'] = 'abc'
        assert os.environ['SOME_VAR'] == 'abc'

        # Subprocess will inherit this, for example those opened with `Popen`.

    # if 'Bad':

        # Does *not* work!:

        #os.environ = {'a':'b'}

        # Child process will not inherit it.
