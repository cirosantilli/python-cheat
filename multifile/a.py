a = 'a.a'

def f():
    return "a.f()"

def g():
    return "a.g()"

#imports on child and stuff defined in the import are not passed to parent

import imported_from_a
assert imported_from_a.n == 1

##__name__

#it is visible to the imported file

#assuming this was imported from .main:

    #assert __name__ == 'a'

#assuming this was imported as

    #b = imp.load_source('c','a.py')

#from .main:

    #assert __name__ == 'c'

#imports from the importing file are not put into this namespace

try:
    imported_from_main.f()
except NameError:
    pass
else:
    assert False

# This does not work:

def __call__():
    return "a.__call__()"

import sys
syspath = sys.path
import contains_list
print 'contains_list.l = ' + str(contains_list.l)
assert contains_list.l == [1]
