#!/usr/bin/env python3

# Lambda is a function without name
#
# Lambda functions can only contain a single expression.
#
# This means in particular that they cannot contain assigments,
# so they are very limited.

f = lambda x, y: x + 2 * y + 1
assert f(1, 2) == 6
assert f(3, 4) == 12
assert f(3, 4) == 12

# Lambda that does nothing.
# https://stackoverflow.com/questions/22738412/a-suitable-do-nothing-lambda-expression-in-python
f = lambda *args: None
f()
