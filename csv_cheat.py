#!/usr/bin/env python

import StringIO
import csv
import itertools

if '## reader basic example':

    """
    Takes anything that can be iterated linewise, e.g. file.
    But here we use arrays to mimize.

    Returns another iterator, but over lists.
    """

    assert list(csv.reader(['1,2', '3,4'])) == [['1', '2'], ['3', '4']]

if '## writer':

    """
    No, not the inverse of the reader.
    First argument must have the write() method.
    """

    rows = [['1', '2'], ['3', '4']]
    sio = StringIO.StringIO()
    csv_writer = csv.writer(sio, lineterminator='\n')
    for row in rows:
        csv_writer.writerow(row)
    assert sio.getvalue() == '1,2\n3,4\n'
    sio.close()

if '## Escaping':
    # Escape the comma.
    assert list(csv.reader(['","'])) == [[',']]
    # Escape the quote.
    assert list(csv.reader(['"\""'])) == [['"']]
    # Escaped quotes must be quoted.
    assert list(csv.reader(['\"'])) == [['']]

if '## DictReader':

    assert (list(csv.DictReader(['a,b', '1,2', '3,4'])) ==
            [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}])
    assert (list(csv.DictReader(['1,2', '3,4'], fieldnames=['a', 'b'])) ==
            [{'a': '1', 'b': '2'}, {'a': '3', 'b': '4'}])

if '## Ignore comment lines starting with #':

    # http://stackoverflow.com/questions/14158868/python-skip-comment-lines-marked-with-in-csv-dictreader

    assert (list(csv.reader(itertools.ifilter(
                lambda row: row[0] != '#',
                ['1,2', '#3,4', '5,6']))) ==
            [['1', '2'], ['5', '6']])
    assert (list(csv.reader(itertools.ifilter(
                lambda row: row[0] != '#',
                ['1,2', '"#3",4', '5,6']))) ==
            [['1', '2'], ['#3', '4'], ['5', '6']])
