#!/usr/bin/env python

import os
import sys

"""
What `import os` does:

Search for module named `os` in the following order:

- relative to current file ( possibly != from `os.getcwd()` ! )
- python module search path
"""

if "##module search path":

    #view current python module search path:

    print sys.path

    if "##append to module search path":

        if "##environment variable":

            #simplest way to change path for all system

            #change this variable in `bashrc`

            #a bit platform dependent (harder to to in windows...)

            if 'PYTHONPATH' in os.environ:
                print os.environ['PYTHONPATH']

            #`:` separated list of paths to search for *before* other paths

            #- has higher precedence than installation default paths (`/usr/lib/pythonX.X/`)
            #- has lower precedence than stuff installed with `pip` or `setup.py`: `/usr/local/lib/python2.7/dist-packages/`

        if "##site package":

            pass

            #- applies to all system
            #- less platform dependent

            #goes after `PYTHONPATH`

            #USER_SITE="$(python -c $'import site\nprint site.USER_SITE')"
            #NEW_PATH="`mktemp -d`"
            #echo "$NEW_PATH" > "$USER_SITE"/anything.pth
            #echo 'a = 123456' > "$NEW_PATH"/innewpath.py
            #python -c $'import innewpath\nprint innewpath.a'

        if "##sys.path":

            #you can do this on a per program basis:

            sys.path.append( '/the/new/path' )
            sys.path.insert( 0, '/the/new/path' )

if "##__init__":

    #a *module* is either:

    #- a `.py` or `.pyc` file
    #- dir with and `__init__.py`

        #`__init__.py` code is executed when the module is loaded,

        #just like code in a file is executed when it is loaded

    #it is not possible to distinguish between both except by looking at <#__file__>

    import a
    assert a.f() == "a.f()"

    import d
    assert d.f() == "d.f()"

if "##imports of imports are not imported":

    #imports inside imports are not put in current namespace.

    #therefore, even if module `imported_from_a` was imported in a, it is not defined here!

    import a

    try:
        imported_from_a.n
    except NameError:
        pass
    else:
        assert False

    #therefore, this is not the same as copying code from the module and pasting here
    #as a c include does!

    #if you really want to copy code from a file and execute it use <#execfile>

if "##execfile":

    #copy contents of file and exec them here

    #same as `exec(read("file.py"))`

    defined_in_execed = 0
    execfile("execed.py")
    assert defined_in_execed == 1

    #paths are either absolute or relative to `os.getcwd()`!

    ###usually a bad idea

    #for the same reason that `from BLA import *` is a bad idea.

    #always prefer: `from module import var1, var2`,
    #so that you keep control of what is being imported

if "##stuff defined in import overrides definitions of importer scope":

    #first define some names on current scope:

    import imported_from_main

    a = 'a'
    def f():
        return 'f()'

    #now the import will override them:
    import a

    assert a.a == 'a.a'
    assert a.f() == 'a.f()'

if "##you can reassign what modules symbols mean":

    """
    Once imported, a module is just another dict like namespace,
    and you can edit it was you wish in the current namespace.

    Those changes will not however reflect on other modules that imported that module!
    """

    a.a = 1
    assert a.a == 1

    a = 2
    assert a == 2

    #reassign on parent modules disables the children also:

    import d
    import d.a
    d = 1
    try:
        d.a
    except AttributeError:
        pass
    else:
        assert False

if "##magic methods don't work":

    try:
        assert a() == "a.__call__()"
    except TypeError:
        pass
    else:
        assert False

if "##uncaught exceptions at imported blow up at importer":

    try:
        import raise_exception
    except Exception:
        pass
    else:
        assert False

if "##relative imports":

    #only work inside dirs structure with `__init__` files, that is, submodule structure

    ##can't call method from d.a by importing only d but not importing d.a

    import d

    try:
        d.a.f()
    except AttributeError:
        pass
    else:
        assert False

    import d.a2
    assert d.a2.f() == "d.a2.f()"

    import d.d2.a3
    assert d.d2.a3.f() == "d.d2.a3.f()"

    if "##can only be done inside module structure:":

        try:
            from . import re
            assert re.f() == "re.f()"
        except ValueError:
            pass
        else:
            assert False

        #does not work here because we have no `__init__.py` in current dir!

        #see <#/d/d/d/a> for an example

        ##can only import modules, not their attributes:

        try:
            import a.f
        except ImportError:
            pass
        else:
            assert False

    if "##go up on module structure":

        pass

        #from .. import a
        #a.f()

        #up two modules:

        #from ... import a
        #a.f()

        #up three modules:

        #from .... import a
        #a.f()

if "##submodule vs attribute":

    #*never define in your __init__ file an attribute which has the same name as a module*

    import d.a
    assert d.a.a == 'd.a'

    #TODO1

    import d
    #assert d.a == 'd.a'

if "##importing a submodule also imports parent":

    d = 1

    try:
        assert d.a == 'd.a'
    except AttributeError:
        pass
    except:
        assert False

    #TODO2 related to TODO1

    import d.a2
    #assert d.a == 'd.a'

if "##from":

    from d import a2
    assert a2.f() == "d.a2.f()"

    #can also be used to import module contents:

    from a import f
    assert f() == "a.f()"

    if "##star ##*":

        #never use this except for bad practice

        #makes it very hard to know what is being imported or not and what is its name!

        from d import *
        assert a2.f() == "d.a2.f()"
        assert d2.f() == "d.d2.f()"

        #can also be used to import module contents:

        from a import *
        assert f() == "a.f()"
        assert g() == "a.g()"

        #if module is a dir, imports both its 

        from d import *
        assert f() == "d.f()"
        assert a2.f() == "d.a2.f()"
        assert d2.f() == "d.d2.f()"

        #will import nothing, since a has no submodules

    if "##as":

        from a import f as g
        assert g() == "a.f()"

        #ERROR:
        #from d import d as d2
        #import d2.d
        ##must use import d.d.d

        ##multiline

        from d import (
            a2,
            d2,
        )

if "##module attributes":

    if "###__file__":

        """
        contains the full path of a file

        only defined for imported modules

        not defined on the file script being executed run!

        possible reason: modules are always loaded from files,
        while scripts may exist in RAM only:

           #echo "print __file__" | python

        *it is impossible to get the path to the script being run*

        check if a module is in path and if yes print its path:
        """

        try:
            import os
        except:
            print "not found"
        else:
            print os.__file__

    if "##__name__":

        #if file was imported, TODO

        #if the file is being executed it equals '__main__'

        import a
        assert a.__name__ == 'a'

        import d.a2
        assert d.a2.__name__ == 'd.a2'

        import a as b
        assert b.__name__ == 'a'

        assert __name__ == '__main__'

if "##symlink":

    #act exactly as files that have the same content as their destination

    #can even link to non `.py` files:

    import a
    import aln
    assert aln.a == 'a'
    assert os.path.splitext( aln.__file__ )[0] == os.path.join( os.path.dirname( a.__file__ ), 'aln' )

    import d.aln
    assert d.aln.a == 'a'
    assert os.path.splitext( d.aln.__file__ )[0] == os.path.join( os.path.dirname( a.__file__ ), 'd', 'aln' )

if "##imp":

    #do import/find in path operations!

    import imp

    #import relative from *os.getcwd()*, *not* to file location:

    b = imp.load_source('c','a.py')

    assert b.f() == 'a.f()'
    assert b.__name__ == 'c'

    ##__dict__ and modules

    import dict_cheat
    for k in dict_cheat.__dict__:
        print k
        print dict_cheat.__dict__[k]
        print 30 * '='
