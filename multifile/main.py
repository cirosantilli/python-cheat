#!/usr/bin/env python

import os
import sys

if '##__init__ ##module':

    # A *module* is either:

    # - a `.py` or `.pyc` file

    # - dir with and `__init__.py`

        # `__init__.py` code is executed when the module is loaded,

        # Just like code in a file is executed when it is loaded

    # It is not possible to distinguish between both except by looking at <#__file__>

    import a
    assert a.f() == 'a.f()'
    assert a.C().m() == 'a.C.m()'

    import d
    assert d.f() == 'd.f()'

if '##module search path':

    # View current python module search path:

    print sys.path

    if '##append to module search path':

        if '##environment variable':

            # Simplest way to change path for all system.

            # Change this variable in `bashrc`.

            # A bit platform dependent (harder to to in windows...).

            if 'PYTHONPATH' in os.environ:
                print os.environ['PYTHONPATH']

            #`:` separated list of paths to search for *before* other paths

            #- has higher precedence than installation default paths (`/usr/lib/pythonX.X/`)
            #- has lower precedence than stuff installed with `pip` or `setup.py`: `/usr/local/lib/python2.7/dist-packages/`

        if '##site package':

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

            # Set search path on a per program basis:

            sys.path.append('/the/new/path')
            sys.path.insert(0, '/the/new/path')

            # Doing this will also change the system path on modules
            # imported by this module:

            import a
            assert a.syspath == sys.path

            # Remember that doing:

            #sys.path = ['.']

            # TODO: how does that work for sys.path? It does not work for other lists.

            import contains_list
            contains_list.l[0] = 1
            import a

if "##import":

    if "Imports of imports are not imported":

        # Imports inside imports are not put in current namespace.

        # Even if module `imported_from_a` was imported in a, it is not defined here!

        import a

        try:
            imported_from_a.n
        except NameError:
            pass
        else:
            assert False

        # Therefore, this is not the same as copying code from the module and pasting here
        # as a c include does!

        # If you really want to copy code from a file and execute it use <#execfile>

    if "##relative imports":

        # Only work inside dirs structure with `__init__` files, that is, submodule structure

        if "##Can't call method from d.a by importing only d but not importing d.a":

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

        if "Can only be done inside module structure":

            try:
                from . import re
                assert re.f() == "re.f()"
            except ValueError:
                pass
            else:
                assert False

            # Does not work here because we have no `__init__.py` in current dir!

            # See <#/d/d/d/a> for an example

        if "Can only import modules, not their attributes":

            try:
                import a.f
            except ImportError:
                pass
            else:
                assert False

        if "Go up on module structure":

            pass

            # Up once:

            #from .. import a
            #a.f()

            # Up two modules:

            #from ... import a
            #a.f()

            # Up three modules:

            #from .... import a
            #a.f()

    if "##from":

        from d import a2
        assert a2.f() == "d.a2.f()"

        #can also be used to import module contents:

        from a import f
        assert f() == 'a.f()'

        if '##star ##*':

            # Never use this except for bad practice.

            # Makes it very hard to know what is being imported or not and what is its name!

            from d import *
            assert a2.f() == "d.a2.f()"
            assert d2.f() == "d.d2.f()"

            # Can also be used to import module contents:

            from a import *
            assert f() == 'a.f()'
            assert g() == 'a.g()'

            # If module is a dir, imports both its:

            from d import *
            assert f() == 'd.f()'
            assert a2.f() == 'd.a2.f()'
            assert d2.f() == 'd.d2.f()'

            # Will import nothing, since a has no submodules.

        if '##as':

            from a import f as g
            assert g() == 'a.f()'

            # ERROR:

            #from d import d as d2
            #import d2.d

            # Must use import `d.d.d`

            ##multiline

            from d import (
                a2,
                d2,
            )

    if 'Stuff defined in import overrides definitions of importer scope':

        # First define some names on current scope:

        import imported_from_main

        a = 'a'
        def f():
            return 'f()'

        # Now the import will override them:
        import a

        assert a.a == 'a.a'
        assert a.f() == 'a.f()'

    if 'You can reassign what modules symbols mean':

        """
        Once imported, a module is just another dict like namespace,
        and you can edit it was you wish in the current namespace.

        Those changes will not however reflect on other modules that imported that module!
        """

        a.a = 1
        assert a.a == 1

        a = 2
        assert a == 2

        # Reassign on parent modules disables the children also:

        import d
        import d.a
        d = 1
        try:
            d.a
        except AttributeError:
            pass
        else:
            assert False

    if 'Uncaught ##exceptions at imported blow up at importer':

        try:
            import raise_exception
        except Exception:
            pass
        else:
            assert False

    if '##__import__':

        '''
        Backend for the `import` statement.

        Import module with name that cannot be variable, e.g. hyphens in executables:

            test_mod = __import__('test-mod')
        '''

if 'Magic methods dont work':

    try:
        assert a() == 'a.__call__()'
    except TypeError:
        pass
    else:
        assert False

if '##submodules':

    if 'Submodule vs attribute':

        # *never define in your __init__ file an attribute which has the same name as a module*

        import d.a
        assert d.a.a == 'd.a'

        #TODO1

        import d
        #assert d.a == 'd.a'

    if '##importing a submodule also imports parent':

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

if '##Inform end user that package is missing.':

    """
    try:
        import bs4
    except ImportError:
        print 'ERROR: Missing dependencies. Install with:\n\nsudo pip install -r requirements.txt'
        sys.exit(1)
    """

if '##module attributes':

    # https://docs.python.org/2/reference/datamodel.html#the-standard-type-hierarchy

    if '##__file__ ##file':

        """
        Contains the full path of a file.

        Only defined for imported modules.

        Not defined on the file script being executed run!

        Possible reason: modules are always loaded from files,
        while scripts may exist in RAM only:

           #echo 'print __file__' | python
        """

        # Check if a module is in path and if yes print its path:

        try:
            import os
        except:
            print 'not found'
        else:
            print os.__file__

    if '##__name__':

        # If file was imported, TODO.

        # If the file is being executed it equals '__main__'.

        import a
        assert a.__name__ == 'a'

        import d.a2
        assert d.a2.__name__ == 'd.a2'

        import a as b
        assert b.__name__ == 'a'

        assert __name__ == '__main__'

if '##symlink':

    # Acts exactly as files that have the same content as their destination.

    # Can even link to non `.py` files:

    import a
    import aln
    assert aln.a == 'a'
    assert os.path.splitext( aln.__file__ )[0] == os.path.join( os.path.dirname( a.__file__ ), 'aln' )

    import d.aln
    assert d.aln.a == 'a'
    assert os.path.splitext( d.aln.__file__ )[0] == os.path.join( os.path.dirname( a.__file__ ), 'd', 'aln' )

if '##execfile':

    # Copy contents of file and exec them here

    # Same as `exec(read('file.py'))`

    defined_in_execed = 0
    execfile('execed.py')
    assert defined_in_execed == 1

    # Paths are either absolute or relative to `os.getcwd()`!

    # Usually a bad idea for the same reason that `from BLA import *` is a bad idea.

    # Always prefer: `from module import var1, var2`,
    # so that you keep control of what is being imported.

if '##imp':

    # Do explicit import / find in path operations.

    import imp

    # Import relative from *os.getcwd()*, *not* to location of this file:

    try:
        b = imp.load_source('c', 'a.py')
    except IOError:
        # Raised if file not found.
        pass

    assert b.f() == 'a.f()'
    assert b.__name__ == 'c'

    # In practice this is unusable as it fails for requires that require other files:
    # http://stackoverflow.com/questions/9066777/howto-import-modules-with-dependencies-in-the-same-absolute-relative-path
    # The best thing to do is to play with the path.

    # Create a new empty module:

    dynamic_module = imp.new_module('dynamic_module_name')
    assert dynamic_module.__name__ == 'dynamic_module_name'

    ##__dict__ and modules

    import dict_cheat
    for k in dict_cheat.__dict__:
        print k
        print dict_cheat.__dict__[k]
        print 30 * '='
