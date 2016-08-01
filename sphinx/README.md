# Sphinx

HTML/PDF documentation from rst markup.

May use docstrings with a default extension.

It is used on the python official documentation

The automatic doc finding / generation is not yet very good IMHO, but the rest works well.

## Directory structure structure

This simulates a real project, with documentation in `doc/`, and `mod` and `mod2` are modules.

### Build

    cd doc
    make html

I added a make `firefox` rule to the `Makefile` to make it easier to test:

    make firefox

And also automated `sphinx-autodoc` generation on my `Makefile`.

## Extensions

### Autodoc

Generate doc from docstrings

Enable `autodoc`. Add:

    'sphinx.ext.autodoc',

To `extensions` and the module to path:

    import os.path

    sys.path.append( os.path.join( os.path.dirname( os.getcwd() ) ) )

in `conf.py`.

From now on, you can the following directive once for each module in path you want to auto-generate documentation do:

    .. automodule:: mod.a
        :members:
        :undoc-members:
        :show-inheritance:

Autodoc does **not** however recursively search for all modules in path, but you can use the default tool `sphinx-apidoc` to do this for you:

    sphinx-apidoc -o py-source-root doc-root

where:

- `doc-root` is the same dir that contains `index.rst` and `conf.py`
- `py-source-root` is the same dir that contains all the python files that you want to document.

This generates the two files in your documentation root:

- `modules.rst`
- `mod.rst`

and finally all you have to do to use them is include them in you `index.rst`.

You could either do:

    .. include:: modules.rst

or add mod it to the `toctree`:

    .. toctree:

        (files)
        mod

which searches for a file mod.(rst|txt) in current dir and adds its doctree here.

#### First time

You can all of this automatically the first time by using the `-F` option:

    sphinx-apidoc -F -o py-source-root doc-root

Which also generates the templates that were generated with `sphinx-quickstart`, but adapted for `apidoc`.

Note however that in current version if you add a file to your module, it is not automatically added on the default make, and you have to run `sphinx-apidoc` manually.

### Math

there are two default methods: MathJax or PNG.

#### PNG

I prefer PNG because it loads instantaneously.

For PNG math, you need to have the `dvipng` program installed and in your path.

This program converts DVI to PNG *surprise!*

On Ubuntu 12.04:

    sudo aptitude install dvipng

### doctest

Check all `>>>` unit test snippets.

Enable extension:

    'sphinx.ext.doctest',

Build for it:

    sphinxbuild -b doctest
