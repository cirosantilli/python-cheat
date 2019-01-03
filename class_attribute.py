#!/usr/bin/env python3

'''
# __class__

The only difference from `type()` seems to be for old style classes:
http://stackoverflow.com/questions/1060499/difference-between-typeobj-and-obj-class
Therefore, there is no difference in Python 3.
'''

assert object.__class__ == type
assert (1).__class__    == int

'''
`__class__` can be set to something else however.

This seems to have no special effect.
'''

class D(): pass

class C():
    __class__ = D

assert type(C()) == C
assert C().__class__ == D

'''
__class__ and inheritance: self determines class.
'''

class C:
    def get_class(self):
        return self.__class__

class D(C):
    def get_class_2(self):
        return self.get_class()

assert C().get_class() == C
assert D().get_class() == D
assert D().get_class_2() == D
