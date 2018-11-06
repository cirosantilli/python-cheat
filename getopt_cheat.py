#!/usr/bin/env python3

import getopt

short = "ho:v"
longs = ["help", "output="]
opts, args = getopt.getopt(['-h', '-o', 'foo', '-v', 'asdf', 'qwer'], short, longs)
assert(opts == [('-h', ''), ('-o', 'foo'), ('-v', '')])
assert(args == ['asdf', 'qwer'])
opts, args = getopt.getopt(['--help', '--output', 'foo', 'asdf', 'qwer'], short, longs)
assert(opts == [('--help', ''), ('--output', 'foo')])
assert(args == ['asdf', 'qwer'])
