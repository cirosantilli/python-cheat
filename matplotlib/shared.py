#!/usr/bin/env python

"""
Contains stuff that is common to all plots of a project

Takes as input exactly one command line argument which is the path of a python file with a `plot` which has the same signature as `plot`:func:

The goal of this design is to separte separate plots into different files so that:

- it all works well with makefiles so that only plots corresponding to modified `.py` files will be replotted on make

- the code is better organized

sample call:

    ./THIS_FILENAME.py subplots
"""

import sys
import os.path
import imp

import matplotlib.pyplot as plt

#global params:
out_dir = "out"
out_ext = "svg"

class DefaultParameters:
    """
    Encapsulates all the default plot parameters
    """

def plot( plt, params ):
    """plot on an empty plt object

    :param plt: a clean ``matplotlib.pyplot`` object
    :type plt:  ``matplotlib.pyplot``
    :param params: default plot params. Function may override those defaults.
    :type params:  the class `DefaultParameters`:class: (not an instance)
    """
    raise NotImplementedError

if __name__ == '__main__':
    path = sys.argv[1]
    name = os.path.split(os.path.splitext(path)[0])[1]
    try:
        plotter = imp.load_source( name, path )
    except IOError:
        print path
        print name
        raise
    else:
        plotter.plot( plt, DefaultParameters )
        plt.savefig( os.path.join( out_dir, name + '.' + out_ext ) , format=out_ext, bbox_inches='tight' )
        plt.clf()
