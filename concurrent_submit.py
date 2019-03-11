#!/usr/bin/env python3

'''
Outcome:

    [sleep 1]
    1
    [sleep 1]
    2
    [sleep 2]
    4
    2
    5
    3
'''

import concurrent.futures
import time

ints = [1, 4, 2]

def myfunc(i):
    time.sleep(i)
    print(i)
    return i + 1

futures = []
with concurrent.futures.ProcessPoolExecutor() as executor:
    for i in ints:
        futures.append(executor.submit(myfunc, i))
for future in futures:
    print(future.result())
