#!/usr/bin/env python

"""
## datetime

Year month day minute sec milisec oriented time operations.
"""

import datetime

now = datetime.datetime.now()
print('now = ' + str(now))

if '## timedelta':

    # Time differences are of timedelta class.

    diff = now - now
    assert type(diff) == datetime.timedelta
    assert diff == datetime.timedelta()

    # One day.

    date = datetime.datetime(2000, 1, 2)
    assert date + datetime.timedelta(1) == datetime.datetime(2000, 1, 3)

    print('timedelta full costructor = ' + str(datetime.timedelta(
        # Not possible:
        #years       = 1,
        #months      = 1,
        weeks        = 2,
        days         = 3,
        hours        = 4,
        minutes      = 5,
        seconds      = 6,
        milliseconds = 7,
        microseconds = 8
    )))

    # Get a datetime from a seconds since Epoch.
    print('epoch = ' + str(datetime.datetime.fromtimestamp(0)))
