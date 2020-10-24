# Matplotlib

TODO install currently broken!

Scientific plotting library.

## Install

Although it is available in PyPi, there are tons of dependencies which pip may not install, and it even fails silently!

Therefore **don't** use the pip install: but use the distro's package manager. On Ubuntu:

	sudo aptitude install python-matplotlib

## Developing

Clone besides of being able to hack Matplotlib, you also get of tons of example files with this!

If you are on Ubuntu get the built dependencies:

    sudo aptitude build-dep python-matplotlib

Then build C extensions and install with:

    sudo python setup.py install

### Test hacks

You cannot put the Python files in your python path simply without installing, because the compiled dependencies won't go to the correct place without an install (crashes on `_path` not found).

So, after you made changes do again:

    sudo python setup.py install

After you build the files C files, which is what takes the longest, you don't have to build them again, so after you hack just:

The problem with this is that you cannot keep the distro default installed also.

TODO how not to install after every change.

## Architecture

### State machine

Not object based, but state machine based.

This means that you often have a current something, and you modify the current something.

This methods like `gca()` which get you the current something.

Rationale: easier to type on interactive sessions

### Objects

- figure:              everything
- axes:                each subplot, including several axis
- axis (!= axes):      the line with the ticks and numbers

## show

Plot to screen:

    plt.plot([0,1])
    plt.show()

On window close, clears plot, so if you have to replot if you want to reuse the old plot:

    plt.plot([1,0])
    plt.show()

## savefig

Plot to file

Recommended formats are:

- SGV: vector. Very precise, but needs to be transformed into bits before being put in a PDF.
- PNG: lossless compression. Simpler to put in PDF because it represents bits directly.

examples:

    plt.plot([0,1])
    plt.savefig( 'svg.png', format='png', bbox_inches='tight' )
    plt.savefig( 'png.png', format='png', bbox_inches='tight' )

## format options

Many format options can be given on either:

- in a single format string at once
- in separate `kwargs`

use only separate `kwargs` in non-interactive programs since this is more manageable

### string

    plt.plot([0,1], 'r--')
    plt.show()

### kwargs

    plt.plot([0,1,2,3], [0,1,4,9], color='r', linestyle='--'  )
    save_svg_clear('r--kwargs')

## pylab

Part of matplotlib: <http://stackoverflow.com/questions/12987624/confusion-between-numpy-scipy-matplotlib-and-pylab>
