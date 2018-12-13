#!/usr/bin/env python3
'''
Get stdout and sterr from process separately.
'''
import subprocess
process = subprocess.Popen(
    ['./stdout_stderr.py'],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
)
exit_status = process.wait()
assert exit_status == 0
stdout, stderr = process.communicate()
assert stdout == b'stdout\n'
assert stderr == b'stderr\n'
