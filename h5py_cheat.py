#!/usr/bin/env python3

'''
http://docs.h5py.org/en/stable/
'''

import sys

import h5py
import numpy

size = 1000000000

if len(sys.argv) == 1:
    # Create a sample file.
    with h5py.File('h5py_cheat.tmp.hdf5', 'w') as f:
        x = numpy.arange(size + 1)
        x[size] =  size / 2
        f.create_dataset('x', data=x, dtype='int64')
        y = numpy.arange(size + 1) * 2
        y[size] =  3 * size / 2
        f.create_dataset('y', data=y, dtype='int64')
        z = numpy.arange(size + 1) * 4
        z[size] = -1
        f.create_dataset('z', data=z, dtype='int64')

# Read the sample file and assert some values.
with h5py.File('h5py_cheat.tmp.hdf5', 'r') as f:
    x = f['x']
    assert x[0] == 0
    assert x[1] == 1
    assert x[2] == 2
    assert x[size - 3] == size - 3
    assert x[size - 2] == size - 2
    assert x[size - 1] == size - 1
    assert x[size - 0] == size / 2
    y = f['y']
    assert y[0] == 0
    assert y[1] == 2
    assert y[2] == 4
    assert y[size - 3] == 2 * (size - 3)
    assert y[size - 2] == 2 * (size - 2)
    assert y[size - 1] == 2 * (size - 1)
    assert y[size - 0] == 3 * size / 2
    z = f['z']
    assert z[0] == 0
    assert z[1] == 4
    assert z[2] == 8
    assert z[size - 3] == 4 * (size - 3)
    assert z[size - 2] == 4 * (size - 2)
    assert z[size - 1] == 4 * (size - 1)
    assert z[size - 0] == -1
