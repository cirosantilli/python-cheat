#!/usr/bin/env python3

import concurrent.futures
import threading
import time

'''
https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures
'''

if 'Raise exception from thread':

    # https://stackoverflow.com/questions/2829329/catch-a-threads-exception-in-the-caller-thread-in-python/12808634#12808634

    def func_that_raises(do_raise):
        lock.acquire()
        lock.release()
        if do_raise:
            raise Exception()
        else:
            return 42 + i

    # Check that result() raises.
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # Ensure that it is asynchronous.
        i = 0
        lock = threading.Lock()
        lock.acquire()
        future = executor.submit(func_that_raises, False)
        i = 1
        lock.release()
        assert future.result() == 43

        # Check that exceptions are raised up.
        future = executor.submit(func_that_raises, True)
        try:
            future.result()
        except Exception:
            pass
        else:
            assert False

    # Check raising from as_completed.
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = []
        futures.append(executor.submit(func_that_raises, False))
        futures.append(executor.submit(func_that_raises, True))
        for future in concurrent.futures.as_completed(futures):
            # TODO assert something.
            print(repr(future.result()))
