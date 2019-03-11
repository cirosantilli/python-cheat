#!/usr/bin/env python3

'''
Extremely likely outcome:

    [sleep 1]
    1
    1 2
    [sleep 1]
    2
    [sleep 2]
    4
    4 5
    2 3

Interpretation:

-   threads run in parallel, runtime is just 4 seconds

    All threads started running immediately from beginning.

-   threads return immediately when done, but only in order.

    If something slow comes up, e.g. the 4s wait, the following
    ones only return when that is done.
'''

import concurrent.futures
import time

ints = [1, 4, 2]

def myfunc(i):
    time.sleep(i)
    print(i)
    return i + 1

with concurrent.futures.ProcessPoolExecutor() as executor:
    for input, output in zip(ints, executor.map(myfunc, ints)):
        print('{} {}'.format(input, output))
