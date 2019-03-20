#!/usr/bin/env python

"""
Minimal threading.Thread example.

Note that this example does not give any performance gain in non-NUMA PCs
because RAM is the bottleneck and there is only one RAM access.

Making multiple network requests concurrently would be a real world use case however.
"""

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
