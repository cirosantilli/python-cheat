#!/usr/bin/env python

"""
## os

Wrappers for os specific stuff.

Lots of important file and directory operations.
"""

import tempfile
import os
import shutil

if '## sep':

    # Path separator ('/' linux/mac '\' on windows):

    print('os.sep = ' + os.sep.encode('string-escape'))

if '## linesep':

    # System newline separator ('\n' Linux, '\r' Mac, '\n\r' Windows):

    print('os.linesep = ' + os.linesep.encode('string-escape'))

if '## listdir ## ls':

    # **Always** use Unicode input since the output gets the same encoding as this input
    # and filenames may contain non ASCII chars!

    print('os.listdir(u".") = ' + str(os.listdir(u'/')))

if '## unlink ## rm':

    path = "open.tmp"
    f = open(path, "w")
    assert os.path.isfile(path)
    os.unlink(path)
    assert not os.path.exists(path)

if '## touch': pass

    # http://stackoverflow.com/questions/12654772/create-empty-file-using-python
    # open('/path/to/file', 'a').close()

if '## mkdir ## rmdir':

    # Only works if directory is empty.
    # For recursive directory removal, see `shutil.rmtree`.

    path = 'dir.tmp'
    os.mkdir(path)
    assert os.path.isdir(path)
    os.rmdir(path)
    assert not os.path.exists(path)

if '## makedirs':

    path0 = 'tmp0'
    path1 = 'tmp1'
    path2 = 'tmp2'
    path = os.path.join(path0, path1, path2)

    os.makedirs(path)
    assert os.path.isdir(path)
    os.removedirs(path)

if '## getcwd #pwd #chdir #cd':

    # Get current working dir (each process has a cwd)

    print('os.getcwd() = ' + os.getcwd())

if '## symlink':

    """
    os.symlink(name, origin)
    Where name is the place the symlinke will be created at,
    and origin what it points to.
    """

if '## listdir ## ls':

    # List basenames in a directory, excluding `.` and `..`.

    d = tempfile.mkdtemp()
    open(os.path.join(d, 'a'), 'a').close()
    open(os.path.join(d, 'b'), 'a').close()
    print(os.listdir(d))
    assert sorted(os.listdir(d)) == ['a', 'b']
    shutil.rmtree(d)

if '## walk ## find':

    """
    Walk all subdirectories recursively.

    Out of the box options:

    - up down or down up
    - onerror callback function
    - followlinks or not

    For input like:

        for root, dirs, files in os.walk(u"tests"):
            print(root)
            print(dirs)
            print(files)
            print()

    The output is of the form:

        directory path
        [basename of directories inside it]
        [basename of files inside it]

    It loops over all directories.

    **Be paranoid and always use unicode `u"."` in Python 2.7**, since the output has the same encoding as that input,
    and paths are primary examples of things that may contain unicode characters.
    """

    # Get relative paths to all non-directory files:

    for root, dirs, files in os.walk(u'.'):
        for basename in files:
            path = os.path.join(root, basename)
            #print(path)

    # Get relative paths to all directories:

    for root, dirs, files in os.walk(u'.'):
        for basename in dirs:
            path = os.path.join(root, basename)
            #print(path)

    # Does not include current directory dot `.` nor upper directory two dots `..`.

    # Get relative paths to all files and directories:

    for root, dirs, files in os.walk(u'.'):
        for basename in dirs + files:
            path = os.path.join(root, basename)
            #print(path)

    # To do all of Bash `find` filtering, jus use regular ifs. Sanity!

    for root, dirs, files in os.walk(u'.'):
        for basename in dirs + files:
            path = os.path.join(root, basename)
            if os.path.splitext(path)[1] == '.pdf':
                #print(path)
                pass

    # The order and choice of directories which will be descended into is determined by `dirs`.

    # If you modify if in-place, you can alter the descent order! Typical applications include:

    # - `sort` to fix descent order

        # Only sorts each level and the descent order:

        # - files come after directories
        # - shallow come before deep

    for root, dirs, files in os.walk(u'.'):
        dirs.sort()
        files.sort()
        for basename in dirs + files:
            path = os.path.join(root, basename)
            #print(path)

        # For a full sort, the only way is to put all paths in a list and sort the list.

        # That is less efficient because 2n log 2n > 2(n log n and rarely necessary.

    # - `remove` to prune any directories with a given basename:

    for root, dirs, files in os.walk(u'.'):
        try:
            dirs.remove(u'prune_me')
        except ValueError:
            pass
        for basename in dirs + files:
            path = os.path.join(root, basename)
            #print(path)

if '## devnul.':

    print('os.devnull = ' + os.devnull)

if '## system':

    # https://docs.python.org/2/library/os.html#os.system

    # Run command from default shell.

    # Return the exit status.

    # See subprocess for a better option.

    pass

if '## glob':

    """
    Searches directories using POSIX glob patterns.

    Applications:

    - list files at a given level: os.glob('*/*/*')
    """
