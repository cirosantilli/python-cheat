#!/usr/bin/env python

def plot( plt, params ):
    ax = plt.gca()
    ax.plot([0,1])
    #only removes ticks and labels, not bounding box:
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
