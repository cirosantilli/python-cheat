#!/usr/bin/env python

"""
## sqlite

https://docs.python.org/2/library/sqlite3.html

Oh, the Python stdlib is so overblown!

## Fetch methods

Fetch results that came from previous SELECT queries.

Results can only be fetched once, and then the next ones are fetched.

TODO example of multiple fetchone.

### Fetch type

By default strings are retrieved for every type:

- http://stackoverflow.com/questions/14047303/how-to-make-fetch-methods-return-original-types-like-int-instead-of-only-strings
- http://stackoverflow.com/questions/1829872/read-datetime-back-from-sqlite-as-a-datetime-in-python

### commit

Saves to queries disk.

Beware: this slows things down a lot if you are doing bulk queries!
"""

import datetime
import os
import sqlite3

if 'Basic example':

    db_path = 'sqlite.tmp'

    data = [
        ('one', 1),
        ('two', 2)
    ]
    data.sort()

    # Create table and add some data.
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS t')
    cursor.execute('CREATE TABLE t (t TEXT, i INT)')
    cursor.executemany('INSERT INTO t VALUES (?, ?)', data)
    connection.commit()
    connection.close()

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM t ORDER BY t ASC')
    result = cursor.fetchall()
    # Strings are returned by default.
    assert result == [('one', 1), ('two', 2)]
    connection.close()

if '## row_factory':

    """
    Parses row outputs into sqlite3.Row objects which are much more flexible.

    In particular, this allows:

    - map access to the row by column name: http://stackoverflow.com/questions/3300464/how-can-i-get-dict-from-sqlite-query

    I recommend that you use this always.
    """

    connection = sqlite3.connect(':memory:')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE t (i INT)')
    cursor.execute('INSERT INTO t VALUES (?)', (1,))
    cursor.execute('SELECT * FROM t')
    row = cursor.fetchone()
    assert type(row) is sqlite3.Row
    assert row['i'] is 1
    assert type(row['i']) is int
    connection.close()

if '## NULL':

    """
    Becomes None.
    """

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('SELECT NULL')
    row = cursor.fetchone()
    assert row[0] is None
    connection.close()

if '## execute on large tables':

    """
    execute SELECT statements don' bring all the data to memory,
    so it can be run on huge databases.

    It does take a long time however, if you don't have an index.
    There is of course no solution to that except creating the index.
    """

if '## DATE ## DATETIME ## TIMESTAMP':

    """
    Comes out as strings by default.
    http://stackoverflow.com/questions/1829872/how-to-read-datetime-back-from-sqlite-as-a-datetime-instead-of-string-in-python
    """

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE t (c DATE, d DATETIME, e TIMESTAMP)')
    today = datetime.date.today()
    now = datetime.datetime.now()
    cursor.execute('INSERT INTO t VALUES (?, ?, ?)', (today, now, now))
    cursor.execute('SELECT * FROM t')
    row = cursor.fetchone()
    assert [type(x) for x in row] == [unicode] * 3
    assert row == (unicode(today), unicode(now), unicode(now))
    connection.close()

    if '## PARSE_DECLTYPES':

        connection = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE t (c DATE, d DATETIME, e TIMESTAMP)')
        today = datetime.date.today()
        now = datetime.datetime.now()
        cursor.execute('INSERT INTO t VALUES (?, ?, ?)', (today, now, now))
        cursor.execute('SELECT * FROM t')
        row = cursor.fetchone()
        # TODO why only datetime comes out as a string?
        assert [type(x) for x in row] == [datetime.date, unicode, datetime.datetime]
        assert row == (today, unicode(now), now)
        connection.close()

if '## Memory database':

    """
    How to bootstrap in memory from DB file and write it back to the file afterwards:

    - http://stackoverflow.com/questions/3850022/python-sqlite3-load-existing-db-file-to-memory
    - http://stackoverflow.com/questions/31191727/moving-back-and-forth-between-an-on-disk-database-and-a-fast-in-memory-database?lq=1
    """

    # TODO example.

if 'iterate search results':

    """
    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print row
    """

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    print type(cursor.execute('SELECT '))
    row = cursor.fetchone()
    assert row[0] is None
    connection.close()

