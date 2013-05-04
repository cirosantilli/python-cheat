#!/usr/bin/env python

"""
the best way to do subplots is via the subplots method instead of `add_subplot()`
"""

import itertools

def plot( plt, default_params ):
    fig, axs = plt.subplots(2, 2)
    for x,y in itertools.product( [0,1], [0,1] ):
        axs[x,y].plot([x,y])
