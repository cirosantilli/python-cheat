#!/usr/bin/env python3
'''
Count to stdout at 10Hz:
./count.py [n=2 [dt=1]]
Write the latest number to the count.tmp file.
'''
import sys
import time
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 2
if len(sys.argv) > 2:
    dt = float(sys.argv[2])
else:
    dt = 1
for i in range(n):
    print(i)
    sys.stdout.flush()
    with open('count.tmp', 'w') as f:
        f.write(str(i))
    time.sleep(dt)
