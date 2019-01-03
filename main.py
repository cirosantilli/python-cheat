#!/usr/bin/env python3

import concurrent.futures

def func_that_raises(do_raise):
    lock.acquire()
    lock.release()
    if do_raise:
        raise Exception()
    else:
        return 42 + i

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures = []
    futures.append(executor.submit(func_that_raises, True))
    for future in concurrent.futures.as_completed(futures):
        print(repr(future.exception()))
