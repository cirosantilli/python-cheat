#!/usr/bin/env python

"""
cheat on math operations supported by the stdlib
"""

assert abs(-1) == 1
assert max(1,-2,0) == 1
assert max([1,-2,0]) == 1

##math

import math

assert abs( math.sin(0) - 0.0 ) < 0.01 
assert abs( math.cos(0) - 1.0 ) < 0.01 
assert abs( math.exp(0) - 1.0 ) < 0.01 

##sqrt

assert abs( math.sqrt(4) - 2.0 ) < 0.01 

try:
    math.sqrt(-1)
except ValueError:
    pass
else:
    assert False

assert abs( math.pi     - 3.14 ) < 0.01 
assert abs( math.exp(0) - 1.0  ) < 0.01 
assert abs( math.exp(1) - 2.71 ) < 0.01 
assert math.floor( 1.5 ) == 1 

##random

import random

###uniform

#real on interval

n = 1000
su = 0
l = 0
r = 1
for i in xrange(n):
    rand = random.uniform(l,r)
    #print rand
    assert rand >= l and rand <= r
    su += random.uniform(0,1)

#check average

assert su/float( (r - l) ) - n < 1

###randint

#uniform int on interval

print random.randint(0,3)

###sample

#takes n *different* elements at random from iterable:

vals = {1:0, 2:0, 3:0}
n = 2
for i in random.sample(vals.keys(), 2):
    assert i in vals.keys()
    vals[i] += 1

for i in vals.keys():
    assert vals[i] == 0 or vals[i] == 1

assert sum( vals[k] for k in  vals.keys() ) == n
