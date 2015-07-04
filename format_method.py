#!/usr/bin/env python

import sys

"""
## Format method

The percent format operator becomes deprecated in Python 3.1,

The `format` method is introduced and backported to Python 2,

On one hand, this is saner since we now have a method instead of a magic operator `%`.

On the other, C printf format strings are gone, and that is a shame.
Yet another format syntax to learn.

<http://www.python.org/dev/peps/pep-3101/>

Only operators `[]` and `.` are supported inside the formats.
"""

assert '{1} {0} {1} {2[0]} {a}'.format(0, 1, [0, 1], a=2 ) == '1 0 1 0 2'

# Escape, literals:

assert '{{}}{{a}}'.format(0) == '{}{a}'

assert '{} {}'.format(0, 1) == '0 1'

# Cannot use both automatic numbering and numbered references:

try:
    '{} {0}'.format(0)
except ValueError:
    pass
else:
    assert False

# Does not work like in Ruby where strings are magic: only the format method interprets anything.

a = 2
assert '{a}' != '2'

if 'format_spec':

    # The entire format is of the form:

    #{<id>[:<format-string>]}

    # It is C printf like, but **NOT** the same!

    # Default for integers if not given.
    assert '{:d}'.format(20) == '20'
    assert '{:x}'.format(20) == '14'

    # Fill to minimum width with spaces:

    assert '{:2d}'.format(1)  == ' 1'

    # With zeroes:

    assert '{:02d}'.format(1) == '01'

    # Align left:

    assert '{:<2d}'.format(1) == '1 '

    # Decimal places:

    assert '{:.2f}'.format(1.0)    == '1.00'
    assert '{0:.2f}'.format(1.0)   == '1.00'
    assert '{x:.2f}'.format(x=1.0) == '1.00'

    # Format via an argument combo:

    assert '{0:.{1}f}'.format(1.23456, 4) == '1.2346'
    assert '{number:.{digits}f}'.format(number=1.23456, digits=4) == '1.2346'

if '## Table printing':

    # There seems to be no built-in one liner.

    # Two rows built-in solution:

    print 'Label value table combo:'
    labels = ['label 0', 'very long label 1', 'l 2']
    values = [0, 1, 2]
    sys.stdout.write('{:<{l}}{}\n{:<{l}}{}\n{:<{l}}{}\n'.format(
        *[x for t in zip(labels,values) for x in t],
        l=len(max(labels, key=len)) + 2
    ))

    """
    Output:

        label 0            0
        very long label 1  1
        l 2                2

    Many solutions with external libraries since Python is so scientific based:
    - http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
    - http://stackoverflow.com/questions/17279059/print-list-in-table-format-in-python
    """
