#!/usr/bin/env python

"""
this is *not* the best method to do subplots:
always use `Figure.subplots` method instead.

2,2,1 is the same as 221 but more computational, so always use use it on
non interactive sessions
"""

def plot( plt, params ):
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax1.plot([0,0])
    ax2 = fig.add_subplot(2,2,2)
    ax2.plot([0,1])
    ax3 = fig.add_subplot(2,2,3)
    ax3.plot([1,0])
    ax4 = fig.add_subplot(2,2,4)
    ax4.plot([1,1])
