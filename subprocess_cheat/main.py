#!/usr/bin/env python

"""
#sources

<http://docs.python.org/2/library/subprocess.html>

<http://www.doughellmann.com/PyMOTW/subprocess/>

<http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python>

#alternatives

Using the subprocess module is the best option.

##system ##os.system

The only alternative is `os.system`, which is less flexible (cannot get stdout),
and intelligent (does not do smart quoting for you)

#Popen

the main class of the module.

there are other convenience functions, but they are only shortcuts to `Popen`
so just *always* use `Popen` which is more versatile and less confugins.

##commands

Are automatically escaped for you for the target shell!

For example, note how 'arg 1' is converted to 'arg\ 1' on Linux.

##shell

If true, is exactly the same as pasting the command on a shell

never use this beucause:

- it is highly system dependant
- makes escaping ``insane a la shell''

as this example illustrates, the PATH variable is still used to find the `python`
executable even if we are not in a shell.

##subprocess.PIPE

you must use subprocess.PIPE for each pipe you want to communicate via python
for example via `process.communicate`

if you ommit those, they go/come from the default place: the terminal or pipes

##universal_newlines

if True, converts `os.linsep` to `\n` on stdout and stderr, and `\n` to `os.linesep` on stdin

default False.

it is up to the data creator do define if this should be on or off,
but almost always this should be on whenever the generator may generate
output fit for terminal consuption, and False otherswise.

#communicate

Set stdin, wait for process to termiate, get stdout and stderr.

#stdin

It `stdin = PIPE`, `Popen.stdin` represents the pipes stdin, and you can write to it with process.

TODO why can this fill buffers but not communicate?

TODO example

"""

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
