#!/usr/bin/env python

"""
## datetime

Year month day minute sec milisec oriented time operations.
"""

import datetime

if '## datetime':

    now = datetime.datetime.now()
    print('now = ' + str(now))
    print('now.tzinfor = ' + str(now.tzinfo))

    # Get a datetime from a seconds since Epoch.
    # This is first passed to your timezone by default,
    # since timestamps are usually absolute, but datetimes are relative.
    # So it is likely to be 1970-01-01 offset by a few hours.
    print('fromtimestamp(0) = ' + str(datetime.datetime.fromtimestamp(0)))

    # This is guaranteed to be 1970-01-01
    print('utcfromtimestamp(0) = ' + str(datetime.datetime.utcfromtimestamp(0)))

    if 'Applications':

        if '# Midnight':

            # http://stackoverflow.com/questions/8361099/django-python-date-time-set-to-midnight

            today_midnight = datetime.datetime(year=now.year, month=now.month, day=now.day)
            tomorrow_midnight = today_midnight + datetime.timedelta(days=1)
            print('today midnight    = ' + str(today_midnight))
            print('tomorrow midnight = ' + str(tomorrow_midnight))

    if 'UTC':

        print('utcnow = ' + str(datetime.datetime.utcnow()))
        assert type(datetime.datetime.utcnow()) == datetime.datetime

if '## date':

    # Only up to day precision.

    print('today = ' + str(datetime.date.today()))

    # From datetime (OK, this assert *could* fail
    # if you're into learning Python at midnight):

    assert datetime.date.today() == datetime.datetime.now().date()

    # UTC today:
    # http://stackoverflow.com/questions/27587127/convert-datetime-date-today-to-utc-time
    # convert from utcnow.

    # How many days between two dates:

    assert (datetime.date(2000, 2, 1) - datetime.date(2000, 1, 1,)).days == 31

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

if '## naive ## offset':

    """
    TODO. create one of each.
    """
