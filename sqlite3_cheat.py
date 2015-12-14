#!/usr/bin/env python

"""
## sqlite

https://docs.python.org/2/library/sqlite3.html

Oh, the Python stdlib is so overblown!

## Fetch methods

Fetch results that came from previous SELECT queries.

Results can only be fetched once, and then the next ones are fetched.

TODO example of multiple fetchone.

### commit

Saves to queries disk.

Beware: this slows things down a lot if you are doing bulk queries!

TODO ever needed for :memory:?
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

    """
    # print(row) is different than print(str(row))

        Either a horrible API choice, or a bug:
        http://stackoverflow.com/questions/7920284/how-can-printing-an-object-result-in-different-output-than-both-str-and-repr

        Consider instead:

            print(row)
    """

    #print row
    #print(str(row))

if '## cursor':

    """
    The second execute on a cursor erases previous results.
    """

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('SELECT 1')
    cursor.execute('SELECT 2')
    assert cursor.fetchone()[0] is 2
    assert cursor.fetchone() is None
    connection.close()

    if '## Query without cursor':

        """
        sqlite3 has some convenience methods so that you
        don't need to create an useless cursor for simple queries.
        """

        connection = sqlite3.connect(':memory:')
        assert next(connection.execute('SELECT 1'))[0] is 1
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
    so it can be run on huge databases. TODO: how is that possible?

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

if '## Memory database #:memory:':

    """
    A database with name :memory: only exists in memory.

    Each connection creates a new separate database.
    """

    connection1 = sqlite3.connect(':memory:')
    connection2 = sqlite3.connect(':memory:')
    cursor1 = connection1.cursor()
    cursor2 = connection2.cursor()
    cursor1.execute('CREATE TABLE t (i INT)')
    connection1.commit()
    # This works. Therefore `t` did not exist. So this is a separate DB.
    cursor2.execute('CREATE TABLE t (i INT)')
    connection2.commit()
    connection1.close()
    connection2.close()

    """
    How to bootstrap in memory from DB file and write it back to the file afterwards:

    - http://stackoverflow.com/questions/3850022/python-sqlite3-load-existing-db-file-to-memory
    - http://stackoverflow.com/questions/31191727/moving-back-and-forth-between-an-on-disk-database-and-a-fast-in-memory-database?lq=1
    """

if '# Iterate search results':

    """
    execute returns the cursor.

    Cursors are iterable over the set of rows.

        for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print row

    Can deal with large result sets, so it must be actually doing several queries in the backend?
    """

    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    execute_return = cursor.execute('SELECT 1 UNION ALL SELECT 2')
    assert type(execute_return) is sqlite3.Cursor
    assert list(execute_return) == [(1,), (2,)]
    connection.close()

if '# Transactions # Locking # timeout':

    """
    - https://docs.python.org/2/library/sqlite3.html#sqlite3.connect
    - https://docs.python.org/2/library/sqlite3.html#sqlite3-controlling-transactions

    Interesting quote:

    > When a database is accessed by multiple connections, and one of the processes modifies the database,
    the SQLite database is locked until that transaction is committed.
    The timeout parameter specifies how long the connection should wait
    for the lock to go away until raising an exception.
    The default for the timeout parameter is 5.0 (five seconds).
    """

    if '# Locking error example with double insert':

        connection1 = sqlite3.connect(db_path, timeout=0)
        connection2 = sqlite3.connect(db_path, timeout=0)
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()
        cursor1.execute('DROP TABLE IF EXISTS t')
        cursor1.execute('CREATE TABLE t (i INT)')
        connection1.commit()
        # Implicitly starts a transaction.
        cursor1.execute('INSERT INTO t VALUES (1)')
        try:
            # Cannot start a new transaction while the other one is going on.
            cursor2.execute('INSERT INTO t VALUES (1)')
        except sqlite3.OperationalError:
            pass
        else:
            raise
        # Finish the transaction.
        connection1.commit()
        # This time it is fine, because we have already finished the previous one.
        cursor2.execute('INSERT INTO t VALUES (1)')
        connection1.close()
        connection2.close()

    if '# Locking error example with SELECT + INSERT':

        connection1 = sqlite3.connect(db_path, timeout=0)
        connection2 = sqlite3.connect(db_path, timeout=0)
        cursor1 = connection1.cursor()
        cursor2 = connection2.cursor()
        cursor1.execute('DROP TABLE IF EXISTS t')
        cursor1.execute('CREATE TABLE t (i INT)')
        # If we comment this out and use an empty database, then no exception occurs. TODO Why?
        cursor1.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])
        connection1.commit()
        # TODO why does this SELECT lead to the lock error?
        cursor1.execute('SELECT * FROM t')
        # TODO why does this make no difference? What should I do to fix things now?
        connection1.commit()
        cursor2.execute('INSERT INTO t VALUES (1)')
        # TODO why do we blow up at the commit, instead of execute as in the INSERT INSERT example?
        try:
            connection2.commit()
        except sqlite3.OperationalError:
            pass
        else:
            raise
        connection1.close()
        connection2.close()

if 'iterate updating search results':

    """
    This is an oversimplified example:
    we could do this with a single update query of course.

    TODO how?

    - multiple connections gives: database is locked
    - multiple cursors with a single connection messes things up in a way I don't understand
    """

    # One connection and multiple cursors.

    connection = sqlite3.connect(':memory:')
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor1.execute('CREATE TABLE t (i INT)')
    cursor1.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])
    connection.commit()
    for row in cursor1.execute('SELECT * FROM t'):
        # On a real example, we do a very time consuming operation here.
        cursor2.execute('UPDATE t SET i = ? WHERE i = ?', (row[0] + 10, row[0]))
        # Because the operation is time consuming, we would like to commit here,
        # before doing the time consuming operation many more times.
        # Why can't we do this?
        connection.commit()
    # Committing here instead would works:
    #connection.commit()
    # TODO This assert should pass but fails. Why?
    #assert list(cursor1.execute('SELECT * FROM t ORDER BY i ASC')) == [(11,), (12,)]
    connection.close()

    # Two connections.

    connection1 = sqlite3.connect(db_path, timeout=0)
    connection2 = sqlite3.connect(db_path, timeout=0)
    cursor1 = connection1.cursor()
    cursor2 = connection2.cursor()
    cursor1.execute('DROP TABLE IF EXISTS t')
    cursor1.execute('CREATE TABLE t (i INT)')
    cursor1.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])
    connection1.commit()
    for row in cursor1.execute('SELECT * FROM t'):
        cursor2.execute('UPDATE t SET i = ? WHERE i = ?', (row[0] + 10, row[0]))
        # TODO Raises database is locked. I have minimized this elsewhere.
        #connection2.commit()
    #assert list(cursor1.execute('SELECT * FROM t ORDER BY i ASC')) == [(11,), (12,)]
    connection1.close()
    connection2.close()

    # Get all the data out first.

    connection = sqlite3.connect(db_path, timeout=0)
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS t')
    cursor.execute('CREATE TABLE t (i INT)')
    cursor.executemany('INSERT INTO t VALUES (?)', [(1,), (2,)])
    connection.commit()
    cursor.execute('SELECT * FROM t')
    rows = cursor.fetchall()
    for row in rows:
        cursor.execute('UPDATE t SET i = ? WHERE i = ?', (row[0] + 10, row[0]))
        connection.commit()
    assert list(cursor.execute('SELECT * FROM t ORDER BY i ASC')) == [(11,), (12,)]
    connection.close()
    connection.close()
