#!/usr/bin/env python

"""
contains stuff that is common to all plots of a project

takes as input exactly one command line argument which is the
path of a python file with a `plot` which has the same signature as `Plotter.plot`:func:

the goal of this design is to separte separate plots into different
files so that:

- it all works well with makefiles so that
    only plots corresponding to modified `.py` files will be replotted on make

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
    encapsulates all the default plot parameters
    """

class Plotter:
    def plot( plt, params ):
        """plot on an empty plt object

        :param plt: a clean ``matplotlib.pyplot`` object
        :type plt:  ``matplotlib.pyplot``
        :param params: default plot params. Function may override those defaults.
        :type params:  the class `DefaultParameters`:class: (not an instance)
        """
        raise NotImplementedError

def save( name, path_head=out_dir, ext=out_ext ):
    """helper to plot svgs
    
    :param name: basename without extension of the output
    :type  name: string
    :param path_head: path without basename of output
    :type  path_head: string
    """
    plt.savefig( os.path.join( path_head, name + '.' + ext ) , format=ext, bbox_inches='tight' )

def save_clear( name, path_head=out_dir, ext=out_ext ):
    """same as `save_svg`:func: but also clears plot afterwards"""
    save( name, path_head, ext )
    plt.clf()

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
        save_clear( name )
