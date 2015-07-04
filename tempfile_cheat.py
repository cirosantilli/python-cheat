#!/usr/bin/env python

"""
## tempfile

 Create temporary files and directories.

<http://www.doughellmann.com/PyMOTW/tempfile/
"""

import shutil
import tempfile

# The filename is given by dir + prefix + random + suffix.
#
# - dir defaults to gettempdir()
# - prefix defaults to gettempprefix()
#
# Does not return a string, but an object.
# Use `.name` to get the path string.

temp = tempfile.NamedTemporaryFile(
    #dir = '/tmp',
    prefix = 'prefix_',
    suffix = '_suffix',
)

try:
    print('temp = ' + str(temp))
    print('temp.name = ' + temp.name)
    temp.write('asdf')
    temp.flush()
finally:
    # File is deleted on close!
    temp.close()

# Make a temporary directory instead of file.
# Returns a path string.

directory_name = tempfile.mkdtemp(
    dir = '/tmp',
    prefix = 'prefix_',
    suffix = '_suffix',
)
print('mkdtemp = ' + directory_name)
shutil.rmtree(directory_name)

# The default directory that will hold all of the temporary files:

print('gettempdir() = ' + tempfile.gettempdir())

# The basename prefix for new file and directory names:

print('gettempprefix() = ' + tempfile.gettempprefix())
