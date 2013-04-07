#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!note=8

"""
#sources

#- <http://www.diveintopython.net/index.html>

    #good beginners tutorial
"""


##learning path

#std or not that everyone should know about
#sys, os
    
import timedate

###tox

#sudo pip install tox

#TODO

###package macking
#http://guide.python-distribute.org/creation.html
import setup

###sphinx

#generate python documentation from docstrings

#- <http://packages.python.org/an_example_pypi_project/sphinx.html>
#- <http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>

###web

####django

#most used python web framework.

#not documented here.

####trac

#top django bugtracker.

#not django based.

####free django friendly web hosts

#you need to deploy some day

#####openshift
                
#ssh

##whitespace

#python forces certain indentations

#use backslash '\' for line continuation of long commands

assert \
1+\
    1\
== 2

#or parenthesis

assert (
        1+
    1 ==
2
)

###operators

1+\
1

(1+
1)

#cannot separate them over lines:

    #1+
    #1

    #1
    #+1

###functions

#cannot separate `(` from function def:

    #def f
        #(x,y):
        #pass

#everything else works!

#good:

def f(x,y):
    """
    docstrings must be indented
    """
    pass

#my favorite for lots of args:

def f(
        x,
        y,
        z,
        w
    ):
    pass

#ugly but works:

def f(
x
            ,y,
    z
    ):
    pass

#single line only

def f(): pass

    #def f(): pass
        #pass

def f(x,y):
    pass

f(1,2)

f(1,
2)

f(
1,
2
)

def f():
    g(
            1,
2
    )

#anything that has `:` like `if`, `while` and `class` works like function


##types and operators

###arithmetic operators

a = b = 1
assert a == 1
assert b == 1
assert 2 * 3 == 6
assert 1 / 2 == 0
assert 1. / 2. == 5
assert 5 % 3            #mod == 2
assert 2 ** 3           #pow == 8
assert 9 // 2           #floor division == 4
assert 1.1 // 1.0 == 0

####complex

assert 1j*1j == -1
assert (1+2j).real == 1
assert (1+2j).imag == 2
assert 1j.conjugate() == -1j

###boolean operator

assert not True         == False
assert True and False   == False
assert True or  False   == True

###strings

#2 classes: *str* and *unicode*
#*basestring* is their common ancestor 

####single vs double quotes

#no difference:

assert "abc" == 'abc'

#except for excaping quotes themselves:

assert "'" == '\''
assert '"' == "\""

####multiline

assert \
    'ab' \
    'cd' == 'abcd'

assert """a
b""" == "a\nb"

assert '''a
b''' == 'a\nb'

def f():
    assert """a
b""" == "a\nb"

####backslash escapes
            
#like c =)

print "a\tb\nc"

####format strings

#####list

#%s recieves strings, %d integegers (decimal), %f formatted floats:

assert "a%db"   % ( 1 )     == "a1b"
assert "%d %d"  % ( 1, 2 )  == "1 2"

#- lengh at least 2, left padded with spaces:

print "%f"      % ( 1.2 )   == " 1.10"
assert "%.2f"   % ( 1.2 )   == "1.10"
assert "%5.2f"  % ( 1.2 )   == " 1.10"

assert "%s"     % ( "abc" )     == "abc"

#####map

"%(v1)s %(#)03d %(v1)s %(#)03d" % {'v1':"asdf", "#":2}

####cat

assert "ab" + "cd" == "abcd"

#implicit: only works for strings
assert "ab" "cd" == "abcd"
assert "ab" * 3 == "ababab"

####replace

#1 replace max 

assert "aabbcc".replace("b", "0")   == "aa00cc"
assert "aabbcc".replace("bb", "0")  == "aa0cc"
assert "aabbcc".replace("b", "0", 1) == "aa0bcc"

####split

assert "0ab1ab2".split("ab") == ['0', '1', '2']
assert "0abab2".split("ab")  == ['0', '', '2']

#if string not given *splits at ``\s*`` regex*!!:

assert "0 1\t \n2".split()                  == ['0', '1', '2']
assert "0 1\t \n2".split(string.whitespace) == ['0', '1', '2']

#very confusing.

#split at ``[\n\r]+`` regex:

assert "0\n1\r2\r\n3".splitlines()  == ['0', '1', '2', '3']

####strip

#strip chars:

assert "0a1cba2".strip("abc") == "012"

#whitespace by default:

assert "0 1\t \n2".strip() == "012"

####query

assert "abc".startswith("ab") == True
assert "abc".startswith("bc") == False

####string to number

assert int("123") == 123
assert float("12.34e56") = = 12.34e56

#char to int:

assert ord('a') == 97

####encode

assert '\n'.encode('string-escape') == '\\n'

###unicode

#the second line of the file *must* be:

    # -*- coding: utf-8 -*-

#to be able to use utf8 directly in python source!!

#*bad*:

s = "åäö"
print s

#this works for for the terminal, where python recognizes the terminla encoding
#ALWAYS, I MEAN, ALWAYS encode unicdoe stuff that may be piped out and unicode!

#*good*:

s = u"中文"
print s.encode('utf-8')

##data structures

###lists

####create

[ 1, 2, "a", "b" ]  

#####from tuple

assert list( (1, 2) ) == [1, 2]

#####range

#xrange for the interator version

assert range(3) == [0, 1, 2, 3]
assert range(1, 3) == [1, 2, 3]
assert range(1, 5, 2) == [1, 3, 5]

#####list comprehentions

assert [ i for i in xrange(3) if i != 2 ] == [ 0, 1, 3 ]

#####map

assert map( lambda i: 2 * i, xrange(3) ) == [ 0, 2, 4 ]

####access

l = [0, 1, 2]
assert l[0] == 0
assert l[1] == 1
assert l[2] == 2

assert l[-1] == 2
assert l[-2] == 1

#####overflow

try:
    l[3]
except IndexError:
    pass
else:
    assert False

#####slice

l = range(3)
assert l[:2]  == [0, 1]
assert l[2:]  == [2, 3]
assert l[-2:] == [0, 1]
assert l[:-2] == [2, 3]

#####default value if overflow

l[i] if len(l) > i else default

####modify

l = range(2)
l[0] = 10
assert  == [10, 1, 2]

l = range(2)
assert del l[1] == None
assert l == [0, 2]

l = range(2)
assert l + 3 == [0, 1, 2, 3]
assert l == range(2)

l = range(2)
assert l.append(3) == None
assert l == [0, 1, 2, 3]

l = range(2)
assert l.extend( [3, 4] ) == None
assert l == [0, 1, 2, 3, 4]

l = range(2)
assert l.insert(0, 3) == [3, 0, 1, 2]
assert l == range(2)

####sort

l = [2, 1, 3]
assert l.sort() == None
assert l == [1, 2, 3]
assert l.sort(inverse = True == None
assert l == [3, 2, 1]
#modifies l1
    #returns NONE!!!

l = [2, 1]
assert sorted( l ) == [1, 2]
assert l == [2, 1]
#creates new list and returns it
#l is untouched

####find item

#first match for criteria with generator expression
assert next( pair for pair in [(1, 1), (2, 1), (2, 1)] if pair[0] == 2 ) == (2, 1)

#uses the given default if not found:

assert next( pair for pair in [(1, 1), (2, 1), (2, 1)] if pair[0] == 3, None ) == None

#if no default, exception:

try:
    next( pair for pair in [(1, 1), (2, 1), (2, 1)] if pair[0] == 3 ) == (2, 1)
except StopIteration:
    pass
else:
    assert False

####remove dupes

assert list( set( [1, 2, 1] ) ) == [1, 2]

###tuple

t = (1, 2, 3)
t = tuple( [1, 2, 3] ) #from list
t2 = (4, 5, 6)
t3 = (4, 5, 1)
tb = (False, False, True)
tm = (1, 1.1, True, "asdf")

t = (1, 2, 3)
assert t[0] == 1
assert t[1] == 2
assert t[2] == 3

a, b, c = (1, 2, 3)
assert a == 1
assert b == 2
assert c == 3

#tuples are immutable:

t = (0)
try:
    t[0] = "a"
except TypeError:
    pass
else:

t = (0, 1)
t = (2, 3)
assert t + t2 == (0, 1, 2, 3)

t = (0, 1)
assert t * 2  == (0, 1, 0, 1)
assert 2 * t  == (0, 1, 0, 1)

print t < t2
print t < t3

print len(t)
print max(t)
print min(t)
print any(tb)
print all(tb)
print divmod(5, 2)

###dictionnary

d = {1:"a", "b":2, 1.1:2}
print d
print d[1] #order is undefied!
print d["b"]

#print d["c"] #exception!
print d.get("c", "default value")

print d.keys() #list, undefined order.

#modify value
d["b"] = 3
print d

#add new value
d["c"] = 4
print d

del d["b"]
print d

d  = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#dict from list of pairs

d = dict(sape = 4139, guido = 4127, jack = 4098)
#string only keys

print d.items() 
#dict to list of pairs

c = a.copy()
c.update(b)
#create a new dict that is the sum of b and c

d1.update(d2)
d1.update({'as':12})
d1.update(1 = 2, 3 = 4)
#update d1 to add/update values of dict d2 and d3 and as key

#dictionnary comprehentions
print {key: value for (key, value) in [(1, 2), (3, 4)] } 

###set

#list without order of unique elements

#- len(s) 	  	cardinality of set s
#- x in s 	  	test x for membership in s
#- x not in s 	  	test x for non-membership in s
#- s.issubset(t) 	s <= t 	test whether every element in s is in t
#- s.issuperset(t) 	s >= t 	test whether every element in t is in s
#- s.union(t) 	s | t 	new set with elements from both s and t
#- s.intersection(t) 	s & t 	new set with elements common to s and t
#- s.difference(t) 	s - t 	new set with elements in s but not in t
#- s.symmetric_difference(t) 	s ^ t 	new set with elements in either s or t but not both
#- s.copy() 	  	new set with a shallow copy of s 
#- s.update(t) 	s |= t 	return set s with elements added from t
#- s.intersection_update(t) 	s &= t 	return set s keeping only elements also found in t
#- s.difference_update(t) 	s -= t 	return set s after removing elements found in t
#- s.symmetric_difference_update(t) 	s ^= t 	return set s with elements from s or t but not both
#- s.add(x) 	  	add element x to set s
#- s.remove(x) 	  	remove x from set s; raises KeyError if not present
#- s.discard(x) 	  	removes x from set s if present
#- s.pop() 	  	remove and return an arbitrary element from s; raises KeyError if empty
#- s.clear() 	  	remove all elements from set s

assert set( [2, 1] ) == set( [1, 2] )
assert set( [1, 2] ).add(3) == set([1, 2, 3])
assert set( [1, 2] ).add(2) == set([1, 2])
assert set( [1, 2] ).remove(2) == set([1])

##branching

###if

if False:
    assert False
elif False:
    assert False
else:
    pass

####non booleans

if 1:
    pass
else:
    assert False

#very confusing:

assert 1 == True
assert not 1 is True

if -1:
    pass
else:
    assert False

#but then:

assert not -1 == True
assert not -1 is True

if 0:
    assert False

assert 0 == False
assert not 0 is False

if None:
    assert False

assert not None == False
assert not None is False

if "":
    assert False

assert not "" == False
assert not "" is False

if []:
    assert False

assert not [] == False
assert not [] is False

####multiline conditions must have parenthesis

if ( a
    and b
    and c
    and d ):

####single line

#like c ``?`` operator

#*must* have the else part

assert 1 if True  else 2 == 1
assert 1 if False else 2 == 2

###while

i = 0
while i<10:
    print i
    i = i+1

i = 0
while i<10:
    print i
    if i == 5:
        break

i = 0
while i<10:
    print i
    if i == 5:
        continue

###for

for i in [1, 3, 2]:
    print i

for i in [1, 3, 2]:
    print i
    if i == 3:
        break

for i in [1, 3, 2]:
    print i
    if i == 3:
        continue

###and or

#and and or are actually branching instructions:

assert ( True  and 1 ) == 1
assert ( False and 1 ) == False

assert ( True  or 1 ) == True
assert ( False or 1 ) == 1

#they simply eval the last expression,

#for and if it is True or not None, return last,
#else return second.

#or does the same negated.

#this is the analogous to ``&&`` and ``||`` in bash.

##functions

###multiple return values

#there is no real multiple return values,

#but you can return a tuple and open it

#this is one of the major motivations of tuples

def f():
    """
    returns multiple arguments
    """
    return 1, 2
    #SAME:
        #return (1, 2)
a, b = f()

###arguments

def f(a, b = 0, *args, **kwargs):
    """
    args is a tuple
    kwargs a dicdt
    
    those names are just a convention,
    any name can be used, ex:

        def g(*myArgs, **myEtraKwargs)
    """
    
    #args is a tuple.
    for arg in list(args):
        pass
    #you can iterate over it.
    
    #this is a standard way to give default values:
    kw1 = kwargs.get(1, "default1")
    kw2 = kwargs.get(2, "default2")
    kw2 = kwargs.get(3, "default3")

    return a, b, list(args), kwargs

#ERROR
    #f()
#argument a vas no value
assert f(1)                       == (1, 0, []   , {}            )
assert f(1, 2)                     == (1, 2, []   , {}            )

assert f(1, 2, 3)                   == (1, 2, [3]  , {}            )
assert f(1, 2, 3, 4)                 == (1, 2, [3, 4], {}            )
assert f(1, 2, *[3, 4])              == (1, 2, [3, 4], {}            )

assert f(1, 2, 3, 4,   c = 5, d = 6)      == (1, 2, [3, 4], {'c':5, 'd':6} )
assert f(1, 2, *[3, 4], c = 5, d = 6)      == (1, 2, [3, 4], {'c':5, 'd':6} )
assert f(1, 2,       c = 5, d = 6)      == (1, 2, [],    {'c':5, 'd':6} )
assert f(1, 2, 3, 4, **{'c':5, 'd':6}) == (1, 2, [3, 4], {'c':5, 'd':6} )
assert f(1, 2,    **{'c':5, 'd':6}) == (1, 2, [],    {'c':5, 'd':6} )

#note how a removed from the kwargs:
assert f(a = 1)         == (1, 0, [], {} )
assert f(a = 1, b = 2)     == (1, 2, [], {} )
assert f(b = 2, a = 1)     == (1, 2, [], {} )
assert f(a = 1, b = 2, c = 5) == (1, 2, [], {'c':5} )
#ERROR:
    #f(1, a = 1)
#multiple values for value a

#this only works because we have a **kwargs:
#ERROR:
    #def g(a):
        #None
    #g(a = 1)
#does not work because there are no kwargs!

####cannot change order

#cannot change the order of normal args, *args and **kwargs:

#ERRORS:
    #def f(*args, a):
    #def f(**kwargs, a):
    #def f(**kwargs, *args):


#ERROR:
#f(1, 2, *[3, 4], **{5:6})
#cannot use integer (5) as keword for kwargs: must use strings

####there is no function overloading

def f(a):
    """
    completely destroys last existing f
    """
    print "newf"

#def f(a, b):

#f(1, 2, 3)
#too many args

####default values for lots of kwargs

#if you have default values to a large number of them kwargs
#this is a good way, which saves you from writting lots of ``gets``
def f(**non_default_kwargs):

    kwargs = {
        'default':False,
        'action':'store_true',
        'help':"if given, do not ignore case (enabled by default)",
    }
    kwargs.update(non_default_kwargs)

    other_func(**kwargs)

###variables can contain functions

def f(x):
    return x + 1
g = f
assert g(0) == 1

#lambda
    g(lambda x: x, x)
    #lambda is faunction without name
    #lambda cannot contain assignments

###functions can return nothing

def f(b):
    if b:
        return 1

assert f(True)  == 1
assert f(False) == None

###function names are symbols

#like any other python object, you can reassign function names as you wish:

def f():
    pass
f()
def f():
    pass
f()
f = 1
class f
    pass

###functions can have attributes

def f():
    c = 1
f.c = 2
f()
assert f.c == 2

###scope

def f(b):
    return a == b

a = 1
assert f(1) == True

a = 2
assert f(2) == False

####global

def setA_wrong(b):
    a = b

def setA_right(b):
    global a
    a = b

a = 1
setA_wrong(2)
assert a == 1
setA_right(2)
assert a == 2

###nested functions

#this is the way to go
def ex8():
    ex8.var = 'foo'
    def inner():
        ex8.var = 'bar'
        print 'inside inner, ex8.var is ', ex8.var
    inner()
    print 'inside outer function, ex8.var is ', ex8.var
ex8()

##class

###fields

class A():
    """
    comment
    """

    static = None
    _static_private = None
    #static field!

    def __init__(self, a):
        self.member = a
        #object field!

        A.static = a
        self.__class__.static = a
        #set the static variable
        print self.static

        self._private = b
        #by convention, '_' indicates private varibales and methods.
        #nothing in the language prevents you from using it outside
        #except your code breaking later on

a = A(1)
b = A(2)

print a.member
a.member = 3
print a.member

print a.static
a.static = 3
print a.static

print a._private
a._private = 4
print a._private

print A.static
A.static = 5
print A.static

print a.__class__.static
print b.__class__.static
#ERROR
    #print a.non_existent
#ERROR
    #a.non_existent = 6
    #must use setattr()

###inheritance

class B(A):
    def __init__(
                self,
                for_derived_only,
                named_to_modify,
                *args,
                **kwargs
            ): #note that other named args, before or after modified one will fall into args, so youre fine

        self.for_derived_only = for_derived_only

        named_to_modify = named_to_modify + 1

        #modify args
        args = [ a+1 for a in args ]

        #kwargs
            self.creator = kwargs.pop('arg_derived_only', "default")

            kwargs['override'] = "new value"

        #call base calss constructor
        super(B, self).__init__(named, named_to_modify, *args, **kwargs)
        #super().__init__(*args, **kwargs) #python 3

        print "Constructor B was called"

###special methods

class A():
    """
    comment
    """

    def __init__(self, a, b):
        print "Constructor A was called"
        self.a = a 


    #def __cmp__(self, other):
        #"""
        #deprecated in 3., forget it!
        #"""

    def __eq__(self, other):
        """
        >>> a = A()
        >>> b = A()
        >>> a == b
        """
        return self.a == other.a

    def __ge__(self, other):
        """
        defines >=
        """
        return

    def __gt__(self, other):
        """
        defines  >
        """
        return

    def __le__(self, other):
        """
        defines <=
        """
        return

    def __lt__(self, other):
        """
        defines <
        """
        return

    def __ne__(self, other):
        """
        defines !=
        """
        return

    def __hash__(self, other):
        """
        makes hashable, allowing it to be for example a dictionnary key
        """
        return

    def __str__(self):
        """should return bytes in some encoding,
        
        called string for compatibility, changed to __bytes__ in python 3"""
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        """informal description, return (possibly unicode) chars
        
        http://stackoverflow.com/questions/1307014/python-str-versus-unicode

        changed to __str__ in python 3
        """
        return 'a'

    def __repr__(self):
        """formal and very precise

        what you get if you put an object on a interctive session directly:

        >>> A()
        class A()
        """
        return 'class A()'

    def __len__(self):
        """
        >>> len(a)
        """
        return len(self.a)

    d = {}

    def __setitem__(self, k, v):
        """
        >>> self[k] = v
        """
        d[k] = v

    def __getitem__(self, k):
        """
        >>> self[k]
        """
        return self.d[k]

    def __contains__(self, v):
        """
        >>> v in self
        """
        return v in d

    def __call__(self, n):
        """
        >>> a = A()
        >>> a(1) == 2
        """
        return n + 1

a = A()
assert a.__class__.__name__ == 'A'

####__str__

#automaticaly print all members of objects:

class C:

    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __str__(self):
        out = '\n' + 30 * '-' + '\n'
        for k in self.__dict__.keys():
            out += k + ':\n'
            out += str(self.__dict__[k]) + '\n\n'
        return out

#designed to look good even if values have multiline representations

####__eq__

#defalut does not compare element by element!

#compares adress of object.

class C:
    def __init__(self,i):
        self.a = i

c = C(1)
c2 = C(1)
assert c != c2
c = c2
assert c == c2

#to compare by element do this:

class C:

    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __eq__(self, other):
        """
        all attributes of objects are equal
        """
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

c = C(1)
c2 = C(1)
assert c == c2
c2 = C(2)
assert c != c2

###None

a = A()
a is None
#a == None #bad
#always compare with is, never = = , because == can be overwriden by __eq__
    #for example, to always true, while is cannot
    #http://jaredgrubb.blogspot.com.br/2009/04/python-is-none-vs-none.html

###hasattr

class A:
    a = 10
if hasattr(A, 'a'): 
    print True

###geattr

value = obj.attribute
value = getattr(obj, "attribute")

#of a module

### settings.py ###
PARAM = True

### otherfile.py
param = getattr(settings, "PARAM", False) #default to False

###setattr

class A:
    pass #empty class
setattr(A, 'name', 'value')

###any expression goes

hasa = True
class A:
    if hasa:
        a = 1
    else:
        a = 0
assert A.a == 1

###classes can be made inside functions

def func(val):
    class A:
        a = val
    return A
a = func(1)
print a.a
b = func(2)
print b.a
print a.a #unaltered

###@classmethod and @staticmethod

class A():
    def m(self, x):
        print "m(%s, %s)"%(self, x)

    @classmethod
    def c(cls, x):
        print "c(%s, %s)"%(cls, x)

    @staticmethod
    def s(x):
        print "s(%s)"%(x)

a = A()
a.m(1)
a.c(2)
A.c(3)
a.s(4)
A.s(5)

###reflection

#you can get info about objects easily

class C:
    """doc"""

    def __init__(self, name):
        """initdoc"""
        self.name = name

    def print_attrs(self):
        """print_attrs_doc"""
        for name in dir(self):
            attr = getattr(self, name)
            if not callable(attr):
                print name, ':', attr


    def print_method_docs(self):
        """print_method_docs.doc"""
        for name in dir(self):
            attr = getattr(self, name)
            if callable(attr):
                print name, ':', attr.__doc__

c = C('the my object')
c.print_all()

##__dict__

#readonly

###function

def f():
    """doc"""
    a = 1

assert f.__dict__ == {}

f.a = 1
assert f.__dict__ == { 'a' : 1 }

###object

class C:
    def __init__(self):
        self.a = 1
        self.b = "abc"

assert C().__dict__ == { 'a':1, 'b':"abc" }

###class

class C:
    """doc"""
    a = 1
    def f():
        b = 2

###type

#make classes dynamically

class C(B):
    a = 1
print C.a

assert set( C.__dict__.keys() ) == set( ['a', 'f', '__module__', '__doc__'] )
assert C.__dict__['a'] == 1
assert C.__dict__['__module__'] == '__main__'
assert C.__dict__['__doc__'] == 'doc'

##exceptions

###prerequisites

        #<#class>

###they go up until somthing catches them

def e():
    raise Exception

def d():
    e()

try:
    d()
except:
    print "exception!"

#if nothing catches them, they explode on stdX and stop program excecution!

#what is printed:
#1) traceback: where the exception came from (modules, functions, lines)
    #this is userful for debug, so you can find where the problem comes from
#2) <Exception class>: <exception.__repr__>
    raise Exception("repr")
    print "cant reach here"

###raise and catch

try:
    print "try"
except:
    print "any exception"
else:
    print "no exceptions happened"
finally:
    print "this is *always* executed, with or without exception"

###except catches derived classes only

try:
    raise Exception()
except ZeroDivisionError:
    print "ZeroDivisionErrorOnly or derived classes"
except Exception:
    print "Exception, or its derived classes, therefore all exceptions"
except:
    print "same as above"

###passing args to exceptions

try:
    raise Exception(1, 2)
    #raise Exception, (1, 2) #same as above, but more verbose and implicit. NEVER user this
except Exception, e:
    print "e is an instance of Exception"
    print Exception, e
    print e.args[0], e.args[1]
    print e

###reraise

#to add/modify info
try:
    raise Exception("msg")

except Exception, e:

    raise Exception("updated msg")
    #YOU LOSE THE TRACEBACK!!

    #to print you traceback
    import traceback
    traceback.print_exc(
        #file = sys.stdout #stderr is the default
    )

    #for more info
    print sys.exc_info()
    print sys.exc_type
    print sys.exc_value
    print sys.exc_traceback

    raise e
    raise
    #same thing

###standard exceptions

#http://docs.python.org/2/library/exceptions.html

try:
    print 1/0
except ZeroDivisionError:
    print "division by zero"
else:
    print "no exception"

try:
    int("a")
except ValueError:
    print "not a number"

try:
    f = open("NONEXISTENT")
except IOError, (err, msg):
    if err == 2:
        print "does not exist", msg
    else:
        print "no exception"

###custom exception

class CustomException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

try:
    raise CustomException("msg")
except CustomException, (instance):
    print instance.parameter

##iterators

#are more memory effiicent for iterations than lists
#no need to store the entire sequence!
#but you must calculate each new item, so more time expensive if
#you are going to use it more than once
#classic space/time tradeoff

###create

def count():
    """this is already builtin"""
    i = 0
    yield i
    i = i+1

#no need to store all items
    #here there are infinitelly many anyways so it would be impossible
for i in count():
    print i

#must calculate again each sum, so uses more time
for i in count():
    print i

#raise exception to stop

def xrange(n):
    """this is already builtin
    
    count to n
    """
    i = 0
    yield i
    i = i+1
    if i>n:
        raise StopIteration

#generator expressions

#shorthand way to create iterators
for i in (i for i in xrange(10) ):
    print i

#parenthesis can be ommited for single argument func call
#no need to store the entire sequence!
#but you must calculate each new item, so more time expensive if
#you are going to use it more than once
#classic space/time tradeoff
def f(i):
    return i+1
for i in f(i for i in xrange(10) ):
    print i

###next

i = xrange(0)
next(i)
#i.next() #same as above
#0
next(i)
#StopIteration exception

i = xrange(0)
next(i)
#0
next(i, 3)
#3
#default value if over

###iterators can't be rewinded!

        #either store on memory or recalculate

it = iter("asdf")
for i in it:
    print "first"
    print i
for i in it:
    print "second"
    print i

####recalculate

it = iter("asdf")
for i in it:
    print "first"
    print i
it = iter("asdf")
for i in it:
    print "second"
    print i

####on memory

it = list(iter("asdf"))
for i in it:
    print "first"
    print i
for i in it:
    print "second"
    print i

###there is no has_next method
    
#you must catch an exception StopIteration:

try:
    iter.next()
    print 'has next'
except StopIteration:
    print 'does not have next'

###itertools

#hardcore iterator patterns
#http://docs.python.org/2/library/itertools.html#recipes

import itertools

#most important ones:

#- imap: map for iterators
#- izip: count to infinity
#- count: count to infinity

for i, j in itertools.product(xrange(3), xrange(3)):
    print i, j

###default iterators

####enumerate

assert list( enumerate( ['a', 'c', 'b'] ) ) == [(0, 'a'), (1, 'c'), (2, 'b'), ]

####reduce

#2*3 - 1 = 5

#2*5 - 3 = 8

assert reduce( lambda x, y: 2*x - y, [3, 1, 2] ) == 8

#take two leftmost, apply func

#replace the two leftmost by the result

#loop

##decorators

    #<http://stackoverflow.com/questions/739654/understanding-python-decorators>

###creating

def decorator(func):

    def wrapper(a, *args, **kwargs):
        print "before"
        a = a + " modified"
        func(a, *args, **kwargs)
        print "after"

    return wrapper

@decorator
def func1(a, *args, **kwargs):
    print a

func1("inside")

#same as:

def func0(a):
    print a

decorated = decorator(func0)
decorated("inside")

###builtin

####property
        
#####read only properties

class C(object):
    @property
    def p(self):
        return 'val'

c = C()
print c.p
#val

    
#####read write property

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
c.x = '0'
print c.x
del c.x
#ERROR
    #print c

######same

class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

##with

##builtin

#direct acess to all builtin functions:

__builtins__.dir()

###functions

####dir

#list all available names in current scope:

dir()

#list all attruibutes of name (module, class, function):

import 
dir(os)

#see how many there are by default:

def f():
    pass
dir(f)
f.__call__()

#most important is __call__, which calls the function!

#add a new one:

f.a = 'b'
dir(f)

####vars

#list all available names in current scope and their string values:

vars()

####exec

#run string!

exec( 'a = 1' )
assert a == 1

####type()

#determine type of value

print type(1)
#<type 'int'>

print type(1.0)
#<type 'float'>

print type("s")
#<type 'str'>

print type(u"s")
#<type 'unicode'>

print type([])
#<type 'list'>

print type({})
#<type 'dict'>

print type(set())
#<type 'set'>

print type(())
#<type 'tuple'>

print type(lambda:1)
#<type 'function'>

class C: pass

print type(C)
#<type 'cobject'>

#does not return string:

assert type(1) != "<type 'int'>"
print type(type(a))
#<type 'type'>

#can be used to compare

assert type(1) == type(2)
assert type(1) != type(1.0)

#####make classes dynamically

class C(B):
    a = 1
print C.a

#same as

D = type( 'D', (B, ), dict(a = 1) )
print C.a

##streams

#like in linux, files and pipes are both streams
#meaning that you can do many operations to them transparently
#such as read/write

#also as usual, the stdin, stdout and stderr streams are always open by default

#there are however some operations may be only
#available to certain types of streams.
I get
#for example, search operations can be done on files, but not on stdin/out

###read methods

#transprent for both stdout/err and to files,
#meaning, wherever you could use a file, you can also use stdin

####read

#read from handle untill EOF:

sys.stdin.read()
f.read()

#appends a newline at the end!

#read up to 128 bytes:

f.read(128)

#read up to first \n or EOF:

f.readline()

#same as ``f.read().split(\n)``. Rarelly used:

lines = f.readlines()
print lines[2];

#never do for loops with ``readlines``, always user ``xreadlines`` instead
#because that way you don't clutter memory, and you can read files larger
#than memory

#iterator based ``readlines``:

for l in f.xreadlines():
    print l

#this is the way to go for looping over lines one at a time.

###stdout

if sys.stdout.isatty():
    print "terminal"
else:
    print "pipe"

####print function

#this may hidden by the print "statement"

#in python 3.x this will be the only way to print

from __future__ import print_function
print(1, 2, 3, sep = ' ', end = '\n', file = sys.stdout)
print(1, 2, 3, sep = ' ', end = '\n', file = sys.stderr)

###stderr

###stdin
    
#read from stdin until an EOF:
#- program on other side of pipe terminates if pipe coming in
#- user hits ctrl+d on linux (ctrl+z on windows)
sys.stdin.read()

#check if stdin has a pipe comming in or if its the user who is typing

#test.py
if sys.stdin.isatty():
    print True
else:
    print False
ins = sys.stdin.read()
print ins

echo asdf | test.py
#prints False (is a pipe, not a terminal) and asdf (read from sdtin)

test.py
#prints True is a user input terminal (no pipes) and waits for user input
#after ^D, prints what was input by keyboard.

s = unicode(sys.argv[1], 'utf-8')
#reads stdin as if it were utf-8, which should be the case for any sany stdin input

s = unicode(sys.argv[1], sys.stdin.encoding)
#autodetects the encoding of the stdin
#does not work for pipes, since they don't have a default encoding like a terminal!
#do this *EVERYTIME* you take command line arguments which *MIGHT* in some case be unicode!!
#  meaning: whenever the command line args are not programming switches: filenames, natural language, etc.

###file io

#std*
sys.stdin.write("asdf")
sys.stder.write("asdf")
s = sys.stder.read()

#open and close
try:
    with open("a.txt") as f:
        #the close is guaranteed by with
        data = f.read()
except IOError, e:
    logging.error(e)
    continue

#close!
f.close()

#TODO

#http://preshing.com/20110920/the-python-with-statement-by-example
#http://effbot.org/zone/python-with-statement.htm

##time

#seconds after 1970

import time
print time.time()

##datetime

#year month day minute sec milisec oriented time operations

import datetime
now = datetime.datetime.now()
print now - now #timedelta(0)
print now - datetime.timedelta(1) #one day by default
print now - datetime.timedelta(
    years           = 1,
    weeks           = 2,
    days            = 3,
    hours           = 4,
    minutes         = 5,
    seconds         = 6,
    milliseconds    = 7,
    microseconds    = 8
)
print datetime.datetime.fromtimestamp(0) #get a datetime from a seconds after 1970 time.time()

##regex

    import re

###get match objects from compiled re

#match() 	Determine if the RE matches at the beginning of the string.
#search() 	Scan through a string, looking for any location where this RE matches.
#findall() 	return list of all matching *strings*, *not* match objects
#finditer() 	return iterator of match objects

###match object functions

#group() 	Return the string matched by the RE
#start() 	Return the starting position of the match
#end() 	Return the ending position of the match
#span() 	Return a tuple containing the (start, end) positions of the match


###predefined classes

#- \d [0-9]
#- \D [^0-9]
#- \s [ \t\n\r\f\v]
#- \S
#- \w [a-zA-Z0-9_].
#- \W

p = re.compile(r"find(\d)", re.IGNORECASE | re.DOTALL)

###sub

p = re.compile( '(blue|white|red)')
p.sub( 'colour', 'blue socks and red shoes')
'colour socks and colour shoes'
p.sub( 'colour', 'blue socks and red shoes', count = 1)
'colour socks and red shoes'

###sub

#same as sub(), but return a tuple (new_string, number_of_subs_made).

###match

#MUST MATCH FROM BEGINNING OF STRING!!!!!!
re.match(r"a.c", "abc")

r = re.compile(r"a.c")
r.match("abc")
#matches
r.match("0abc")
#DOES NOT MATCH!!!! MUST MATCH FROM BEGINNING OF STRING!!! use search for that

###search

r.search("0abc")
#works

r.search("abcaBc")
#. == b, stops at first match. to find all matches, use finditer

###finditer

matches = list(r.finditer("abcaBc"))
#a list of all matches

re.split(r'[ab]+', '0abba1aaaaa2')
#[0, 1, 2]

##curses

    #python curses insterface
    
    #see curses_cheatsheet.py

###random

import random

random.sample([1, 2, 3, 4, 5, 6], 2)
#takes elements at random from list

for i in random.sample(xrange(2), 2):
    print i;

##os

#if you are going to get paths from a command (like os.list), give UNICODE STRINGS!!!!!
#this way the function will also return unicode string

import os
import shutil

#path separator ('/' linux/mac '\' on windows):
print os.sep.encode('string-escape')

#newline separtor ( '\n' linux, '\r' mac, '\n\r' windows):
print 'os.linesep = ' + os.linesep.encode('string-escape')

os.listdir(u'/')

#makes e, and if inexistent, d, c, b, and a:

os.makedirs('/a/b/c/d/e')

#rm -rf : remove c, and everything inside it IF there are no files?

os.removedirs('/a/b/c')

import os.path

###getcwd

#get current working dir (each process has a cwd)

os.getcwd()

#this is the same as the ``pwd`` of the bash that called the python interpreter.

###os.path

os.path.join('a//', '/b')

os.path.exists('/a')
os.path.isfile('/a')
os.path.isdir('/a')
os.path.islink('/a')

#absolute path:

os.path.abspath(u'/a')

#absolute path resolving *all* links recursivelly:

os.path.relpath(u'/a')

def isparent(path1, path2):
    return os.path.commonprefix([path1, path2]) == path1

def ischild(path1, path2):
    return os.path.commonprefix([path1, path2]) == path2

##shutil

#high level path operations

#recursive directory removal like rm -rf:

shutil.rmtree('/a/')

##tempfile

#create temporary files

#http://www.doughellmann.com/PyMOTW/tempfile/

import os
import tempfile

#suffix and preffix
#dir + prefix + random + suffix
temp = tempfile.NamedTemporaryFile(
    dir = '/tmp',
    prefix = 'prefix_', 
    suffix = '_suffix', 
)

try:
    print 'temp:', temp
    print 'temp.name:', temp.name
    temp.write("asdf")
    temp.flush()
finally:
    #removed on close!
    temp.close()

print 'gettempdir():', tempfile.gettempdir()
print 'gettempprefix():', tempfile.gettempprefix()
#gettempdir() returns the default directory that will hold all of the temporary files
#gettempprefix() returns the string prefix for new file and directory names.

#make a temporary dir in temp location
directory_name = tempfile.mkdtemp(
    dir = '/tmp',
    prefix = 'prefix_', 
    suffix = '_suffix', 
)
print directory_name
os.removedirs(directory_name)

##logging

#standard way to output error messages

#<http://docs.python.org/2/howto/logging.html>

#TODO log all at once

### defult logger

import logging

logging.basicConfig(
    #filename = 'example.log', #default stderr
    #filemode = 'w'

    level = logging.DEBUG,
    #level = logging.INFO,
    #level = logging.WARNING,
    #level = logging.ERROR,
    #level = logging.CRITICAL,

    format = '%(levelname)s %(name)s %(asctime)s %(message)s',

    datefmt = '%m/%d/%Y %I:%M:%S %p', #format for asctime

)

logging.debug('very detailed, debugging only')
logging.info('confirm everything is fine')
logging.warning('unexpected, maybe problem in future')
logging.error('could not perform some function')
logging.critical('serious error. program cant run anymore')
try:
    raise Exception:
except:
    logging.exception('inside exception. also prints exception stack')

### custom loggers

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

##termcolor

#change color and attributes of terminal output

#``` {.bash}
#sudo pip install termcolor
#```

#from __future__ import print_function
#cprint kwargs are the print_function kwargs
#color is obsolete, exists only not to break interface, never use it

import termcolor

termcolor.cprint(
    "red on green",
    'red',
    'on_green',
    attrs = ['bold', 'blink'],
    end = '',
    file = sys.stderr,
)

##environ

#environment variables

import os

#a dictionnary that contains all environment variables:
print os.environ

#get one from the dict:
print os.environ['PATH']

##bad

#this does *not* work!:
os.environ = {'a':'b'}
#child process will not inherit it!

#and now this won't reset environ either
os.environ
#the docs say it only sets os.environ the first time it is imported!

#you have onlly change what the name environ means here.

###setdefault

#if already defined, return old value and do not change the value:
print os.environ.setdefault('PATH', 'asdf')
print os.environ['PATH']

#if not defined, set it and return new value
print os.environ.setdefault['I_AM_PROBABLY_NOT_DEFINED', 'asdf']
print os.environ['I_AM_PROBABLY_NOT_DEFINED']

##command line arguments

print sys.argv[0]
print sys.argv[1:]

##exit code

#if no call is made to sys.exit, exit code is 0.

sys.exit()
sys.exit(0)
sys.exit(1)
