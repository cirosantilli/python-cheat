#!/usr/bin/env python

"""
Run all scripts.

They should exit 0.
"""

import subprocess
import sys
import os
import os.path

# Either:
#
# - requires user input
# - takes too long
# - dependencies that are complicated to install
# - uses network resources
# - simply broken
#
blacklist = [
    # Broken.
    'main',
    # Large download.
    'nltk_cheat',
    # pip build takes too long.
    'numpy_cheat',
    'scipy_cheat',
    # Networking.
    'smtplib_cheat',
    # infinite loop!
    'test',
    # Meant to fail.
    'unittest_cheat',
    # Networking.
    'urllib2_cheat',
    # Interactive.
    'wsgi',
]

ext = '.py'
# TODO: remove this and run all .py files
scripts = []
for f in os.listdir(u'.'):
    if os.path.isfile(f) and os.access(f, os.X_OK):
        noext, ext = os.path.splitext(f)
        if ext == '.py' and not noext in blacklist:
            scripts.append(f)
scripts.sort()
for script in scripts:
    print script
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
print 'ALL ASSERTS PASSED'
