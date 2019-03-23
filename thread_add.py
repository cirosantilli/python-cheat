#!/usr/bin/env python

'''
TODO parametrize.

Minimal educational threading.Thread example.

This example does not give any performance gain and is useless:

-   the GIL prevents SMP with import threading.

    Using multiprocessing overcomes this with multiple processes:

    - https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
    - https://stackoverflow.com/questions/1294382/what-is-the-global-interpreter-lock-gil-in-cpython

-   in non-NUMA PCs RAM is the bottleneck and there is only one RAM access:

    https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean/33510470#33510470

Making multiple network requests concurrently would be a real world use case however.
'''

import threading

class SummingThread(threading.Thread):
    def __init__(self, values):
        super(SummingThread, self).__init__()
        self.values = values
        self.total = 0
    def run(self):
        for i in self.values:
            self.total += i

thread1 = SummingThread([1, 2, 3])
thread2 = SummingThread([4, 5, 6])
thread1.start()
thread2.start()
thread1.join()
thread2.join()
assert thread1.total == 6
assert thread2.total == 15
