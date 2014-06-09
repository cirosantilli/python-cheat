#!/usr/bin/env python

"""
Change color and attributes of terminal output.

    sudo pip install termcolor

`cprint` kwargs are the `print_function` kwargs:

    from __future__ import print_function

The `color` is obsolete, exists only for backwards compatibility, don't use it.
"""

import sys

import termcolor

termcolor.cprint(
    'the content\n',
    'red',
    'on_green',
    attrs = ['bold', 'blink'],
    end = '',
    file = sys.stderr,
)
