#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Main cheat for setup tools like `distutils`, `setuptools` and `distribute`.

You *need* the files

- `MANIFEST.txt`
- `CHANGES.txt

Or it won't work!

#Gemfile equivalent

To allow users who have downloaded the source to develop it, use a
`requirements.txt` by selecting required output lines from:

    pip freeze

And tell users to install with:

    sudo pip install -r requirements.txt

#Which tool to use to distribute?

    Python distribution is currently messy.

    See:

    - <http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2>
    - <http://python-notes.boredomandlaziness.org/en/latest/pep_ideas/core_packaging_api.html>

    Current best course of action for python only projects:

    - use the non-stdlib `distribute` module to create packages.

        Note that the `distribute` base module is called `setuptools`
        because `distribute` is a fork of `setuptools`.

    - host the packages on pypi: <https://pypi.python.org/pypi>

    - end users can now use `pip` to install packages from pypi very easily.

    The best you can do with the stdlib is `distutils`,
    but this is worse than `distribute`.

#distutils

        The setup function will parse command line arguments which allow you
        to do tons of things from the command line.

    ##setup.cfg

        You can set default options for the commands via the `setup.cfg` script

        Example: `bdist_rpm` is a subcommand, that is you call it as:

            python setup.py bdist_rpm

        `release`, `packager` and `doc_files` are options:

            python setup.py bdist_rpm --release r --packager p --doc_files a b c
            python setup.py bdist_rpm --help

        To set all the values add the following to `setup.cfg`:

            [bdist_rpm]
            release = 1
            packager = Greg Ward <gward@python.net>
            doc_files = CHANGES.txt
                        README.txt
                        USAGE.txt
                        doc/
                        examples/

    ##install and uninstall

        Basic install:

            sudo python setup.py install

        This:

        - moves files to the correct install location
        - overwrites any existing files updating them.
        - creates a build dir in current dir which you should ignore in your gitignore

            it puts everythin in the right place inside this build dir:

            - python files are copyied
            - c/c++ extension `.o` and `.so` are put in there

        **however** there is no automatic way to uninstall!!....
        <http://stackoverflow.com/questions/402359/how-do-you-uninstall-a-python-package-that-was-installed-using-distutils>

        You should use a packag manger like `pip` for that TODO how:

        The best you can currently do without a package manger is:

            sudo python setup.py install --record record.txt

        So that `record.txt` will contain the installed files, so to uninstall you can:

            cat record.txt | xargs sudo rm -rf

        Clearly a hack =)

    ##sdist

        Create a source distribution: pack all the source code into a compressed file
        to give to someone else for them to build

            python setup.py sdist

        Not very useful since people should just use `git` or `hg`...

        `MANIFST.in` files will also be included

    ##build_ext

        Only build c/c++ [extensions](http://docs.python.org/2/extending/):

        ###-inplace

            This will place the compiled c/c++ outputs side by side with the python code in the repo,
            exactly where they need to be, without touching anything outside the repo:

                python setup.py build_ext --inplace

            Great for testing projects that contain c/c++ extensions without having to install every time
            before a test so that you can modify the python files directly.

#distribute specific

    ##bdist

        Built distribution:

        - c/c++ extensions will be compiled
        - could create distro specific distributions like `rpm`

    ##upload

        Uploads to pypi!

    ##develop

            sudo python setup.py develop

        Only installs executables in path, but keeps python modules in place
        so that you can edit them where they are for tests.

    ##test

        TODO

    ##pkc_resource

        Allows to get information about packages installed with distribute,
        and therefore if it was installed with pip this will work too.

        Get package version:

            import pkg_resources
            pkg_resources.get_distribution("srtmerge").version

#egg

    TODO what is
"""

from distutils.core import setup   #only for basic projects
#from setuptools import setup      #this is distutils, which is a currently
                                   #remerging fork of setuptools....

setup(
    name                = 'cirosantilli',
    version             = '0.0.1',
    author              = 'Ciro Duran Santilli',
    author_email        = 'ciro.santilli@gmail.com',
    url                 = 'https://github.com/cirosantilli/',
    license             = 'license.md', #GPL, BSD, or MIT. firefox http://www.codinghorror.com/blog/2007/04/pick-a-license-any-license.html 
    description         = 'my simple python scripts and modules',
    long_description    = open('readme.md').read(),

    ##packages

    #whatever package (dir with ``__init__.py`` and everything under)is listed
    #here will be put in your your pythonpath: #(`/usr/local/lib/python2.7/dist-packages/` for ubuntu):

    packages = [
        'cirosantilli',
        'setup_test_dir',
    ],

    #only python files are copyied.

    #if you want to add data files your package, use [package data]

    ##package data

    #data needed for a single package

    package_data = {
        #'setup_test_dir': ['*.txt']
        #'setup_test_dir': ['*.dat']
    },

    ##package_dir

    #specifies where packages will be put

    #all packages are under ``./lib/``:

        #package_dir = {'': 'lib'},

    #pac package is under ``./lib/``:

        #package_dir = {
            #'pac': 'lib'
        #},

    ##py_modules

    #specify individual modules (``.py`` or a dir with ``__init__.py``, but not all of its contents! )
    py_modules = [
        #'setup_test',
        #'setup_test_dir.setup_test2',
    ],

    ##scripts

    #whatever is listed here will be put in your bin path (`/usr/local/bin` on current ubuntu):
    scripts = [
        #'bin/move_regex.py',
    ],

    ##data_files

    #system independent data files.

    #this data can be used across packages

    #relative paths go under `sys.prefix`, which equals `/usr/` in current Ubuntu for example.

    #basenames cannot be changed

    data_files = [
        #('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),   #files will go under `sys.prefix + bitmaps`
        #('/etc/init.d', ['init-script'])           #files will go under `/etc/init.d/`
    ],

    ##install_requires

    #not in `distutils`, must use `distribute`

    #whatever is listed here will be installed if not already:
    install_requires = [

        #current best packaging tool (non stdlib):
        "distribute",

        "ipython",
        "Sphinx",
        #"matplotlib",  #*
        #"numpy",       #*
        "numpydoc",     #used for numpy and matplotlib docs
        "pygments",
        #"scipy",
        "srtmerge",
        "sympy",        #computer algebra system
        "termcolor",    #output ansi color escape codes
        "unidecode",    #convert unicode to ascii. Ex: à -> a, 中-> zhong

        "virtualenv",

        #view what packages are installed
        #TODO vs pip freeze. I htink this looks under installation not managed by pip
        "yolk",
    ],
    #* failed for this packagebe, better with distro's package manager
)
