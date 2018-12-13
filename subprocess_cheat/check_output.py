#!/usr/bin/env python3
'''
Reads stdout from program.
'''
import subprocess
assert subprocess.check_output(['./stdout_stderr.py']) == b'stdout\n'
try:
    subprocess.check_output(['./false.py'])
except subprocess.CalledProcessError:
    pass
else:
    assert False
