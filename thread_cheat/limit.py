#!/usr/bin/env python3

'''
https://stackoverflow.com/questions/19369724/the-right-way-to-limit-maximum-number-of-threads-running-at-once/55263676#55263676

Usage:

    ./limit.py [nproc [min [max]]

To see error handling in action, start from a negative integer, e.g.:

    ./limit.py 2 -10 1000

Notice how execution stops soon after the error.
'''

from typing import Any, Callable, Union
import multiprocessing
import queue
import sys
import threading
import time

def run_in_parallel(
        func: Callable,
        get_work: Callable[[], Any],
        handle_output: Union[Callable,None] = None,
        nthreads: Union[int,None] = None
    ):
    """
    Run a function in parallel.

    Design goals:

    - the input funcion does not need to be modified
    - limits the number of threads
    - queue sizes follow number of threads closely
    - if an error happens, stop soon afterwards

    :param func: main function to be evaluated. If an exception is raised,
                 stop submiting new work and exit as soon as currently
                 running work finishes.
    :param get_work: returns a kwargs dict with inputs for func
    :param handle_output: called on func return values as they
                 are returned
    :param nthreads: number of threads to use
    :return: if an error occurred: tuple(input, output, exception).
             Otherwise, None.
    """
    def func_runner(func, in_queue, out_queue):
        while True:
            work = in_queue.get(block=True)
            if work is None:
                break
            try:
                exception = None
                out = func(**work)
            except Exception as e:
                exception = e
                out = None
            in_queue.task_done()
            out_queue.put((work, out, exception))
    if handle_output is None:
        handle_output = lambda *args: None
    if nthreads is None:
        nthreads = multiprocessing.cpu_count()
    threads = []
    in_queue = queue.Queue(maxsize=nthreads)
    out_queue = queue.Queue()
    for i in range(nthreads):
        thread = threading.Thread(
            target=func_runner,
            kwargs={
                'func': func,
                'in_queue': in_queue,
                'out_queue': out_queue,
            }
        )
        threads.append(thread)
        thread.start()
    error_output = None
    for work in get_work():
        in_queue.put(work)
        if not out_queue.empty():
            output = out_queue.get()
            handle_output(output)
            _, _, error = output
            if error is not None:
                error_output = output
                break
    in_queue.join()
    for thread in range(nthreads):
        in_queue.put(None)
    for thread in threads:
        thread.join()
    while not out_queue.empty():
        handle_output(out_queue.get())
    return error_output

def my_func(i):
    # Simulate IO.
    time.sleep((abs(i) % 4) / 10.0)
    return 10.0 / i

def my_get_work(min_, max_):
    for i in range(min_, max_):
        yield {'i': i}

def my_handle_output(output):
    print(output)

if __name__ == '__main__':
    # CLI arguments.
    argv_len = len(sys.argv)
    if argv_len > 1:
        my_nthreads = int(sys.argv[1])
        if my_nthreads == 0:
            my_nthreads = None
    else:
        my_nthreads = None
    if argv_len > 2:
        min_ = int(sys.argv[2])
    else:
        min_ = 1
    if argv_len > 3:
        max_ = int(sys.argv[3])
    else:
        max_ = 100

    # Action.
    error = run_in_parallel(
        my_func,
        lambda: my_get_work(min_, max_),
        my_handle_output,
        my_nthreads
    )
    if error is not None:
        print('error: ' + str(error))
