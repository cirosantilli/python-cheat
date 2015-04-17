#!/usr/bin/env python

import os
import subprocess
import sys

commands = ['python', 'a.py', 'arg 1', 'arg 2']

try:
    process = subprocess.Popen(
        commands,
        shell  = False,
        stdin  = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines = True
    )
except OSError:
    #typically gets here if the executable is not found
    sys.stderr.write(' '.join(commands) + '\nfailed')

stdin = "stdin1\nstdin2"
stdout, stderr = process.communicate(stdin)
assert stdout == 'stdout:\nstdin1\nstdin2\n'
assert stderr == 'stderr:\narg 1\narg 2\n'

# Wait for process to end and get exit statut:
exit_status = process.wait()
assert exit_status == 0

#does not wait for process to end, None if process not yet terminated:
    #return_code = process.poll()

if "#check method present":

    # http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python

    def command_present(command):
        import distutils.spawn
        # Only in path:
        return distutils.spawn.find_executable(command)

    print "command_present"
    commands = ['ls', 'not-present']
    for command in commands:
        sys.stdout.write(command + ': ')
        if command_present(command):
            print "yes"
        else:
            print "no"
