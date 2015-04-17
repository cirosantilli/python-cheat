# Subprocess

`subprocess` is a standard module that allows to call external programs/scripts.

Run `./main.py` for the tests.

## Sources

<http://docs.python.org/2/library/subprocess.html>

<http://www.doughellmann.com/PyMOTW/subprocess/>

<http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python>

## Alternatives

Using the subprocess module is the best option.

### system

### os.system

Subset: cannot get stdout, no quoting, etc.

## Popen

The fully blown interface.

There are other convenience functions, but they are only shortcuts to `Popen`
so just *always* use `Popen` which is more versatile and explicit.

### commands

Are automatically escaped for you for the target shell!

For example, `['arg 1']` would be converted to `['arg\ 1']` on Linux.

### shell

If true, is exactly the same as pasting the command on a shell

Never use this because:

- it is highly system dependant
- makes escaping "insane a la shell"

As this example illustrates, the `PATH` variable is still used to find the `python` executable even if we are not in a shell.

### subprocess.PIPE

You must use `subprocess.PIPE` for each pipe you want to communicate via Python for example via `process.communicate`

If you omit those, they go/come from the default place: the terminal or pipes.

How to ignore the output: <http://stackoverflow.com/questions/5495078/how-do-you-discard-subprocess-output-in-python>

### universal_newlines

If `True`, converts `os.linsep` to `\n` on stdout and stderr, and `\n` to `os.linesep` on stdin

Default: `False`.

It is up to the data creator do define if this should be on or off, but almost always this should be on whenever the generator may generate output fit for terminal consumption, and False otherwise.

## communicate

Set stdin, wait for process to terminate, get stdout and stderr.

## stdin

It `stdin = PIPE`, `Popen.stdin` represents the pipes stdin, and you can write to it with process.

## call

TODO vs `Popen`

Convenient subset of `Popen` that ignores stdin, stdout and stderr, waits automatically and returns the exit status.
