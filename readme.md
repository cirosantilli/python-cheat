Cheats and information on python and libraries.

Whenever possible, I make the cheat runnable and full of assertions!

Watch out for not naming a module with the same as in the stdlib,
or you will import the module from current dir instead!
this is why some files are named *cheat.py.

#sources

- <http://www.diveintopython.net/index.html>

    good beginners tutorial

#command line options

- `-O`: optimize.

    - `assert` is removed from `.pyc`

    - `__debug__ == False`

        You can write stuff like

            if __debug__: print "debug"

        and it will only show show is `-O` is off.

#pros of python

Python is great for small/medium projects:

- builtin lists [] and dictionnaries {}.
    Really helpful to type less for shorter scripts.

    Has the downside of being harder to document, but still is a good thing.

- dinamically typing:

        a = 1
        a = "abc"

    good when writting smaller scripts because it means much less typing.

#cons of python

- dinamically typing:

        a = 1
        a = "abc"

    what this means is that tons of projects will not document what types of objects functions need to get
    and large projects become a mess...

- putting self in every class method: `__init__(self)`

- global functions that should be class functions: `len([1,2])` instead of `[1.2].len()`

- package management is still not perfect.

- autodocumentation tools are still not perfect (`Shpinx`)

#how to hack python projects

- create a dir: `$DEVPATH`

- add it to the `PYTHONPATH` variable. This will insert it in the `sys.path` before distro's installation paths

- symlink all the packages of the project into `$DEVPATH`

- to turn off your dev version of matplotlib and fall back to the stable distro installed one,
    just rename `matplotlib` as `matplotlib.off`

- if the project contains c/c++ extensions, you can:

        python setup.py build_ext --inplace

    the first time, and whenever you modify a c/c++ extension.

    This will place the compiled c/c++ outputs side by side with the python code in the repo,
    exactly where they need to be, without touching anything outside the repo.

#good python libraries

##science

- numpy
- scipy
- matplotlib

##web

- django

    most used python web framework.

- trac

    top django bugtracker.

    Not Django based.
