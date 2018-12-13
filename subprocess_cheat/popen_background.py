#!/usr/bin/env python3
'''
proc.stdout.read() blocks:
https://stackoverflow.com/questions/1196074/how-to-start-a-background-process-in-python/53751896#53751896
'''
import subprocess
import os
path = 'count.tmp'
if os.path.exists(path):
    os.unlink(path)
with subprocess.Popen(
        ['./count.py', '2', '0.1'],
        # This makes the read wait.
        stdout=subprocess.PIPE,
    ) as proc:
        stdout = proc.stdout.read()
        if os.path.exists(path):
            with open(path, 'r') as f:
                s = f.read()
                # Counted until the end.
                assert s == '1'
