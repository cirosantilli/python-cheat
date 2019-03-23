#!/usr/bin/env python3

'''
It is asynchronous, I promise.
'''

import threading

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
