#!/usr/bin/env python3

class Base:
    pass

class Derived(Base):
    pass

base = Base()
derived = Derived()

assert issubclass(Derived, Base)
assert not issubclass(Base, Derived)

# True for same object.
assert issubclass(Base, Base)

# Cannot use object of class.
try:
    issubclass(derived, Base)
except TypeError:
    pass
else:
    assert False

# Do this instead.
isinstance(derived, Base)
