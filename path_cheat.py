#!/usr/bin/env python

"""
## path

os.path vs os:
http://stackoverflow.com/questions/2724348/should-i-use-import-os-path-or-import-os
"""

import os.path
import tempfile

if '## join':

    assert os.path.join('a', 'b', 'c') == 'a{s}b{s}c'.format(s=os.sep)
    os.path.join('a//', '/b')

if '## split ## splitext':

    path = os.path.join('a', 'b', 'c.e')
    root, basename = os.path.split(path)
    basename_noext, ext = os.path.splitext(basename)
    assert root == os.path.join('a', 'b')
    assert basename_noext == 'c'
    assert ext == '.e'

if '## exists':

    # Returns False for broken symlinks.
    # lexists returns True in that case.

    temp = tempfile.NamedTemporaryFile()
    assert os.path.exists(temp.name)
    temp.close()
    assert not os.path.exists(temp.name)

    temp = tempfile.mkdtemp()
    assert os.path.exists(temp)
    os.rmdir(temp)

if '## isfile':

    # Exists and is file, not directory.

    temp = tempfile.NamedTemporaryFile()
    assert os.path.isfile(temp.name)
    temp.close()
    assert not os.path.isfile(temp.name)

    temp = tempfile.mkdtemp()
    assert not os.path.isfile(temp)
    os.rmdir(temp)

if '## isdir':

    # Exists and is directory.

    temp = tempfile.NamedTemporaryFile()
    assert not os.path.isdir(temp.name)
    temp.close()

    temp = tempfile.mkdtemp()
    assert os.path.isdir(temp)
    os.rmdir(temp)
    assert not os.path.isdir(temp)

if '## islink':

    # Detect if given path is a symbolic link.

    # TODO example.

    os.path.islink('/a')

if '## abspath':

    # Absolute path:

    print('os.path.abspath(u\'.\') = ' + os.path.abspath(u'.'))

if '## relpath':

    # Absolute path resolving links recursively:

    os.path.relpath(u'/a')

if '## commonprefix':

    assert os.path.commonprefix([
        '{s}a{s}b{s}c{s}d'.format(s=os.sep),
        '{s}a{s}b{s}e{s}d'.format(s=os.sep)
    ]) == '{s}a{s}b{s}'.format(s=os.sep)

    def isparent(path1, path2):
        return os.path.commonprefix([path1, path2]) == path1

    def ischild(path1, path2):
        return os.path.commonprefix([path1, path2]) == path2
