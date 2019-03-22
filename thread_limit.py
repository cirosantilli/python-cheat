#!/usr/bin/env python3

'''
https://stackoverflow.com/questions/19369724/the-right-way-to-limit-maximum-number-of-threads-running-at-once/55263676#55263676

Full docs and canonical version at: https://github.com/cirosantilli/linux-kernel-module-cheat/blob/287c83f3f99db8c1ff9bbc85a79576da6a78e986/thread_pool.py
'''

from typing import Any, Callable, Dict, Iterable, Union
import multiprocessing
import queue
import sys
import threading
import time

def run_in_parallel(
    func: Callable,
    works: Iterable[Dict[str,Any]],
    handle_output: Union[Callable[[Any,Any,Exception],Any],None] = None,
    nthreads: Union[int,None] = None
):
    error_output = None
    error_output_lock = threading.Lock()
    def func_runner(func, in_queue, handle_output):
        nonlocal error_output
        while True:
            work = in_queue.get(block=True)
            if work is None:
                break
            try:
                exception = None
                out = func(**work)
            except Exception as e:
                exception = e
            try:
                handle_output_return = handle_output(work, out, exception)
            except Exception as e:
                error_output_lock.acquire()
                error_output = (work, out, e)
                error_output_lock.release()
            else:
                if handle_output_return is not None:
                    error_output_lock.acquire()
                    error_output = handle_output_return
                    error_output_lock.release()
            finally:
                in_queue.task_done()
    if handle_output is None:
        handle_output = lambda input, output, exception: exception
    if nthreads is None:
        nthreads = multiprocessing.cpu_count()
    threads = []
    in_queue = queue.Queue(maxsize=nthreads)
    for i in range(nthreads):
        thread = threading.Thread(
            target=func_runner,
            kwargs={
                'func': func,
                'in_queue': in_queue,
                'handle_output': handle_output,
            }
        )
        threads.append(thread)
        thread.start()
    for work in works:
        in_queue.put(work)
        if error_output is not None:
            break
    for thread in range(nthreads):
        in_queue.put(None)
    for thread in threads:
        thread.join()
    return error_output

def my_func(i):
    '''
    The main function that will be evaluated.

    It sleeps to simulate an IO operation.
    '''
    time.sleep((abs(i) % 4) / 10.0)
    return 10.0 / i

def get_work(min_, max_):
    '''
    Generate simple range work for my_func.
    '''
    for i in range(min_, max_):
        yield {'i': i}

def handle_output_print(input, output, exception):
    '''
    Print outputs and exit immeditaly on failure.
    '''
    print('{!r} {!r} {!r}'.format(input, output, exception))
    return exception

def handle_output_print_no_exit(input, output, exception):
    '''
    Print outputs, don't exit on failure.
    '''
    print('{!r} {!r} {!r}'.format(input, output, exception))

out_queue = queue.Queue()
def handle_output_queue(input, output, exception):
    '''
    Store outputs in a queue for later usage.
    '''
    global out_queue
    out_queue.put((input, output, exception))
    return exception

def handle_output_raise(input, output, exception):
    '''
    Raise if input == 10, to test that execution
    stops nicely if this raises.
    '''
    print('{!r} {!r} {!r}'.format(input, output, exception))
    if input['i'] == 10:
        raise Exception

if __name__ == '__main__':
    # CLI arguments.
    argv_len = len(sys.argv)
    if argv_len > 1:
        nthreads = int(sys.argv[1])
        if nthreads == 0:
            nthreads = None
    else:
        nthreads = None
    if argv_len > 2:
        min_ = int(sys.argv[2])
    else:
        min_ = 1
    if argv_len > 3:
        max_ = int(sys.argv[3])
    else:
        max_ = 100
    if argv_len > 4:
        c = sys.argv[4][0]
    else:
        c = '0'
    if c == '1':
        handle_output = handle_output_print_no_exit
    elif c == '2':
        handle_output = handle_output_queue
    elif c == '3':
        handle_output = handle_output_raise
    else:
        handle_output = handle_output_print

    # Action.
    error = run_in_parallel(
        my_func,
        get_work(min_, max_),
        handle_output,
        nthreads
    )
    if error is not None:
        print('error: {!r}'.format(error))
    if handle_output == handle_output_queue:
        while not out_queue.empty():
            print(out_queue.get())
