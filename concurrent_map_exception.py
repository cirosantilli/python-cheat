#!/usr/bin/env python3

'''
https://stackoverflow.com/questions/19369724/the-right-way-to-limit-maximum-number-of-threads-running-at-once/55263676#55263676

Usage:

    ./concurrent_map_exception.py [nproc [min [max]]

e.g.:

    ./concurrent_map_exception.py 2 -10 100

Outcome:

- all input is read immediately
- iteration stops on exception
'''

import concurrent.futures
import sys
import time

def my_func(i):
    time.sleep((abs(i) % 4) / 10.0)
    return 10.0 / i

def my_get_work(min_, max_):
    for i in range(min_, max_):
        print('my_get_work: {}'.format(i))
        yield i

# CLI.
argv_len = len(sys.argv)
if argv_len > 1:
    nthreads = int(sys.argv[1])
    if nthreads == 0:
        nthreads = None
else:
    nthreads = None
if argv_len > 2:
    min_ = int(sys.argv[2])
else:
    min_ = 1
if argv_len > 3:
    max_ = int(sys.argv[3])
else:
    max_ = 100

# Action.
with concurrent.futures.ProcessPoolExecutor(max_workers=nthreads) as executor:
    for input, output in zip(
        my_get_work(min_, max_),
        executor.map(my_func, my_get_work(min_, max_))
    ):
        print('result: {} {}'.format(input, output))
