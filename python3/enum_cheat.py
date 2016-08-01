#!/usr/bin/env python

from enum import Enum

# http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python

Animal = Enum('Animal', 'ant bee cat')
assert Animal.ant == Animal.ant
assert Animal.ant != Animal.bee

# The main advantage of the enum class,
# is that enums are diferent from any other value.
assert Animal.ant != 1
