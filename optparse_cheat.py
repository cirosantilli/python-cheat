#!/usr/bin/env python3

import optparse

# action append
parser = optparse.OptionParser()
parser.add_option("-a", action='append')
options, args = parser.parse_args()
assert(options == {'a': None})
options, args = parser.parse_args(['-a', 'b'])
assert(options == {'a': ['b']})
