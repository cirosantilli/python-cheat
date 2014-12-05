# Python Cheat ![logo](logo.png)

Python information and cheatsheets.

Stdlib and third party libraries are covered.

On Ubuntu 12.04 install all dependencies with:

	./install-ubuntu.sh

On other systems, install Python-only dependencies with:

	sudo pip install -r requirements.txt

This does not include certain dependencies which may not be installable with `pip` such as SciPy build dependencies.

Most useful files:

- [main.py](main.py): major cheat on the language.
- [argparse_cheat.py](argparse_cheat.py)

Cheats are runnable and full of assertions wherever possible: only unpredictable outputs are printed.

Watch out for not naming a module with the same as in the stdlib, or you will import the module from current dir instead! This is why some files are named `something_cheat.py` instead of simply `cheat.py`.

## Python Implementations

Python specifies the language and stdlib interfaces, not the implementation.

The main interpreter implementations are:

- [CPython](http://www.python.org/getit/source/). Reference implementation.
- PyPy.
- JPython. Compiles to Java Object Code.
- IronPython. Compiles to `.NET` object code.

## Command line options

-   `-O`: optimize.

    - `assert` is removed from `.pyc`

    - `__debug__ == False`

        You can write stuff like

            if __debug__: print "debug"

        and it will only show show is `-O` is off.

## Installation

Use `virtualenv` as early as possible. It's like `rvm` for Python.

## Advantages of Python

Python is part of the [LSB](http://refspecs.linux-foundation.org/LSB_4.1.0/LSB-Languages/LSB-Languages/python.html), so any Linux distribution must have it. Perl is too, but Java and Ruby are not.

Python is great for small / medium projects:

-   built-in lists and dictionary literals `[]` `{}`. Really helpful to type less for shorter scripts.

-   dynamic typing:

        a = 1
        a = "abc"

    Good when writing smaller scripts because it means much less typing.

## Disadvantages of Python

-   dynamic typing:

        a = 1
        a = "abc"

    What this means is that tons of projects will not document what types of objects functions need to get and large projects become a mess.

-   putting self in every class method: `__init__(self)`

-   global functions that should be methods functions: `len([1,2])` instead of `[1.2].len()`

-   there are some key tools missing from the stdlib and without one very dominant implementation:

    - package management
    - auto documentation tools (e.g. Sphinx)
    - Rake equivalent

## How to hack Python projects

First of all, use pip + virtualenv to fix your version and environment.

Next, you might want to do the following to isolate the development version of a package:

-   create a dir: `$DEVPATH`

-   add it to the `PYTHONPATH` variable. This will insert it in the `sys.path` before distro's installation paths

-   symlink all the packages of the project into `$DEVPATH`

-   to turn off your dev version of Matplotlib and fall back to the stable distro installed one, just rename `matplotlib` as `matplotlib.off`

-   if the project contains C/C++ extensions, you can:

        python setup.py build_ext --inplace

    The first time, and whenever you modify a C/C++ extension.

    This will place the compiled c/c++ outputs side by side with the python code in the repo, exactly where they need to be, without touching anything outside the repo.

## Good Python libraries

### Science

Python is very strong on scientific applications, containing libraries such as:

- NumPy
- SciPy
- Matplotlib
- Pandas

### Web

Python is not as strong as Ruby for web development. Important applications are:

-   Django

    Most used Python web framework.

-   Trac

    Top Python-based bug tracker.

    Unfortunately not Django based.

## Sources

-   <http://www.diveintopython.net/index.html>

    Good beginners tutorial.

-   <http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html>

    Explains Python types in detail.
