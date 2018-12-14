#!/usr/bin/env python3

import concurrent.futures
import time

'''
https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures
'''

if 'Raise exception from thread':

    # https://stackoverflow.com/questions/2829329/catch-a-threads-exception-in-the-caller-thread-in-python/12808634#12808634

    def func_that_raises(do_raise):
        # Very likely that the main thread will set i before we go past this point.
        time.sleep(0.1)
        if do_raise:
            raise Exception()
        else:
            return 42 + i

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        # Ensure that it is asynchronous.
        i = 0
        future = executor.submit(func_that_raises, False)
        i = 1
        assert future.result() == 43

        # Check that exceptions are raised up.
        future = executor.submit(func_that_raises, True)
        try:
            future.result()
        except Exception:
            pass
        else:
            assert False
