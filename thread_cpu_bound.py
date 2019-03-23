#!/usr/bin/env python3

'''
CPU bound vs I/O bound in both threading and multiprocessing
to observe the GIL.

- https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
- https://stackoverflow.com/questions/1294382/what-is-the-global-interpreter-lock-gil-in-cpython
- https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean/33510470#33510470
'''

import multiprocessing
import threading
import time
import sys

def cpu_func(result, niters):
    '''
    A useless CPU bound function.
    '''
    for i in range(niters):
        result = (result * result * i + 2 * result * i * i + 3) % 10000000
    return result

class CpuThread(threading.Thread):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class CpuProcess(multiprocessing.Process):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class IoThread(threading.Thread):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)

class IoProcess(multiprocessing.Process):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)

if __name__ == '__main__':
    cpu_n_iters = int(sys.argv[1])
    sleep = 1
    cpu_count = multiprocessing.cpu_count()
    input_params = [
        (CpuThread, cpu_n_iters),
        (CpuProcess, cpu_n_iters),
        (IoThread, sleep),
        (IoProcess, sleep),
    ]
    header = ['nthreads']
    for thread_class, _ in input_params:
        header.append(thread_class.__name__)
    print(' '.join(header))
    for nthreads in range(1, 2 * cpu_count):
        results = [nthreads]
        for thread_class, work_size in input_params:
            start_time = time.time()
            threads = []
            for i in range(nthreads):
                thread = thread_class(work_size)
                threads.append(thread)
                thread.start()
            for i, thread in enumerate(threads):
                thread.join()
            results.append(time.time() - start_time)
        print(' '.join('{:.6e}'.format(result) for result in results))
