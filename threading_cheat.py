#!/usr/bin/env python3

import threading

if 'it is asynchronous, I promise':

    def f():
        global ok
        lock.acquire()
        lock.release()
        ok = (x == 1)
    ok = False
    x = 0
    lock = threading.Lock()
    lock.acquire()
    thread = threading.Thread(target=f)
    thread.start()
    x = 1
    lock.release()
    thread.join()
    assert ok

if 'add parallel':

    '''
    Minimal educational threading.Thread example.

    This example does not give any performance gain and is useless:

    -   the GIL prevents SMP with import threading.
        import multiprocessing overcomes this multiple processes:
        https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
    -   in non-NUMA PCs RAM is the bottleneck and there is only one RAM access:
        https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean/33510470#33510470

    Making multiple network requests concurrently would be a real world use case however.
    '''

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
