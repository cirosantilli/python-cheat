#!/usr/bin/env python

"""
## time
"""

import time

if '## time()':

    # Get number of seconds since 1970:

    print('time.time() = ' + str(time.time()))

if '## clock':

    # Quoting the man: "This is the function to use for benchmarking Python or timing algorithms."

    start_time = time.clock()
    "-".join(str(n) for n in range(10000))
    elapsed_time = time.clock() - start_time
    print('clock elapsed = {0:.6f}s'.format(elapsed_time))

    # Not accurate for wall time. Does not measure time of external programs.

if '## timeit':

    # Benchmark code snippets from strings. Relies internally on either time or clock.

    import timeit
    print('timeit time of all iterations= {0}s'.format(
            timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)))

    # From the command line:

        #python -m timeit '"-".join(str(n) for n in range(100))'

if '## sleep':

    """Sleep for the given number of seconds"""

    #time.sleep(3)
