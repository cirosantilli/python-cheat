#!/usr/bin/env python3

# https://docs.python.org/3/library/functions.html#sorted

if 'sorted':
    strings = ['b.2', 'a.12', 'c.1']
    assert sorted(['b.2', 'a.12', 'c.1'], key=lambda x: int(x.split('.')[1])) \
           == ['c.1', 'b.2', 'a.12']
