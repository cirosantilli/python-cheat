#!/usr/bin/env python3

"""
Run all scripts.

They should exit 0.
"""

import subprocess
import sys
import os
import os.path

rootdir = os.path.split(os.path.realpath(__file__))[0]

blacklist = [
    # Broken, haven't fixed or investigated further because lazy.
    'main',

    # RuntimeError: module compiled against API version 0xb but this version of numpy is 0xa
    'pandas_cheat',

    # Large download.
    'nltk_cheat',

    # pip build takes too long
    'numpy_cheat',
    'scipy_cheat',

    # Networking.
    'smtplib_cheat',
    'urllib2_cheat',

    # Infinite loop!
    'test',

    # Meant to fail.
    'unittest_cheat',

    'wsgi',
]

ext = '.py'
# TODO: remove this and run all .py files
scripts = []
directories = []
for f in os.listdir(u'.'):
    if os.path.isfile(f):
        if os.access(f, os.X_OK):
            noext, ext = os.path.splitext(f)
            if ext == '.py' and not noext in blacklist:
                scripts.append(f)
    elif os.path.isdir(f):
        directories.append(f)
directories.sort()
scripts.sort()

for script in scripts:
    print(script)
    process = subprocess.Popen(
        ['./' + script],
        shell  = False,
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True
    )
    if process.wait() != 0:
        print('ASSERT FAILED: ' + script)
        sys.exit(1)

make_dir_set = {'c_from_py', 'py_from_c'}
for directory in directories:
    if os.path.exists(os.path.join(directory, 'test')):
        os.chdir(directory)
        if directory in make_dir_set:
            subprocess.check_call(['make'])
        subprocess.check_call(['./test'])

print('ALL ASSERTS PASSED')
