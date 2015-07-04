#!/usr/bin/env python

"""
Run all scripts.

They should exit 0.
"""

import subprocess
import sys

ext = '.py'
# TODO: remove this and run all .py files
scripts = [
    'datetime_cheat',
    'decorator',
    'environ',
    'exception',
    'format_method',
    'hello_world',
    'list',
    'logging_cheat',
    'main',
    'math_cheat',
    'os_cheat',
    'path_cheat',
    'random_cheat',
    're_cheat',
    'time_cheat',
    'tempfile_cheat',
]
command = ['python', 'a.py', 'arg 1', 'arg 2']
for script in scripts:
    process = subprocess.Popen(
        ['python'] + [script + ext],
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
