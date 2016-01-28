#!/usr/bin/env python

import csv
import itertools

if '## Basic example':
    # Takes anything that can be iterated linewise, e.g. file.
    # But here we use arrays to mimize.
    assert list(csv.reader(['1,2', '3,4'])) == [['1', '2'], ['3', '4']]

if '## Escaping':
    # Escape the comma.
    assert list(csv.reader(['","'])) == [[',']]
    # Escape the quote.
    assert list(csv.reader(['"\""'])) == [['"']]
    # Escaped quotes must be quoted.
    assert list(csv.reader(['\"'])) == [['']]

if '## DictReader':
    # If not given at creation time
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
