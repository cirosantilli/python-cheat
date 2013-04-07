doc html/pdf documentation from rest markdown.

may use docstrings with a default extension.

it is used on the python official documentation

the automatic doc finding/generation is not yet very good IMHO,
but the rest works good.

#install

    sudo pip install sphinx

#dir structure

this simulates a real project, with documentation in `doc/`, and `mod` and `mod2` are modules.

##build

    make html

I added a make `firefox` rule to the `Makefile` to make it easier to test:

    firefox: html
        firefox $(BUILDDIR)/html/index.html

and also automated `sphinx-autodoc` generation on my `Makefile`.

#extensions

##autodoc

generate doc from docstrings

enable `autodoc`. Add:

    'sphinx.ext.autodoc',

to `extensions` and the module to path:

    import os.path

    sys.path.append( os.path.join( os.path.dirname( os.getcwd() ) ) )

in `conf.py`.

From now on, you can the following directive once for each module
in path you want to autogenerate documentation to:

    .. automodule:: mod.a
        :members:
        :undoc-members:
        :show-inheritance:

Autodoc does **not** however recursivelly search for all modules in path,
but you can use the default tool `sphinx-apidoc` to do this for you:

    sphinx-apidoc -o py-source-root doc-root

where:

- `doc-root` is the same dir that conatins `index.rst` and `conf.py`
- `py-source-root` is the same dir that conatins all the python files that you want to document.

this genearates the two files in your documentation root:

- `modules.rst`
- `mod.rst`

and finally all you have to do to use them is include them in you `index.rst`.

You could either do:

    .. include:: modules.rst

or add mod it to the toctree:

.. toctree:

    (files)
    mod

which searches for a file mod.(rst|txt) in current dir and adds its doctree here.

###first time

you can all of this automatically the first time by using the `-F` option:
    
    sphinx-apidoc -F -o py-source-root doc-root

which also generates the templates that were generated with `sphinx-quickstart`,
but adapted for `apidoc`.

Note however that in current version if you add a file to your module, it is not automatically
added on the default make, and you have to run `sphinx-apidoc` manually.

##math

there are two default methods: mathjax or png.

###png

I prefer png because it loads instanteneously.

for png math, you need to have the `dvipng` program installed and in your path.

this program converts dvi to png *surprise!*

on ubuntu:

    sudo aptitude install dvipng

##doctest

check all `>>>` snippets

enable extension:

    'sphinx.ext.doctest',

build for it:

    sphinxbuild -b doctest
