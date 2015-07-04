#!/usr/bin/env python

"""
## datetime

Year month day minute sec milisec oriented time operations.
"""

import datetime

now = datetime.datetime.now()
print('now = ' + str(now))
# timedelta(0)
print('now - now = ' + str(now - now))
# One day.
print(now - datetime.timedelta(1))
print(now - datetime.timedelta(
    #years       = 1, # Not a valid argument.
    weeks        = 2,
    days         = 3,
    hours        = 4,
    minutes      = 5,
    seconds      = 6,
    milliseconds = 7,
    microseconds = 8
))
    #get a datetime from a seconds after 1970 time.time()
print(datetime.datetime.fromtimestamp(0))
