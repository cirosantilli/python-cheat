#!/usr/bin/env python

import subprocess

##just args
    
process = subprocess.Popen(
    ['python','main.py','a','b'],
    shell  = False,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines = True
)
stdout, stderr = process.communicate()
exit_status = process.wait()
assert stdout == 'a\na2\nb\nb2\n'

#input order is used:

process = subprocess.Popen(
    ['python','main.py','b','a'],
    shell  = False,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines = True
)
stdout, stderr = process.communicate()
exit_status = process.wait()
assert stdout == 'b\nb2\na\na2\n'

##just stdin

process = subprocess.Popen(
    ['python','main.py'],
    shell  = False,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines = True
)
stdout, stderr = process.communicate('c\nc2\n')
exit_status = process.wait()
assert stdout == 'c\nc2\n'

##stdin and args

#only args are used, so don't do this.

process = subprocess.Popen(
    ['python','main.py','a','b'],
    shell  = False,
    stdin  = subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
    universal_newlines = True
)
stdout, stderr = process.communicate('c\nc2\n')
exit_status = process.wait()
assert stdout == 'a\na2\nb\nb2\n'
