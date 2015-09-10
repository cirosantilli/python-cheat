#!/usr/bin/env python

"""
## format operator

## %

Deprecated in favor of `format` and `str.format`, so never use it in new code.

Mostly like C printf.

There are two forms: tuple or dict.

Single value form: only works for a single input.
"""

assert '%d' % 1 == '1'

try:
    assert '%d %d' % 1, 2 == '1 2'
except TypeError:
    pass
else:
    assert False

# Tuple form: works for any number of arguments.

assert '%d'    % (1)     == '1'
assert '%d %d' % (1, 2)  == '1 2'
assert '%.2f'  % (1.2)   == '1.20'
assert '%5.2f' % (1.2)   == ' 1.20'
assert '%s'    % ('abc') == 'abc'

# Map form:

assert '%(v1)s %(#)03d %(v1)s %(#)03d' % {'v1':'asdf', '#':2} == 'asdf 002 asdf 002'
