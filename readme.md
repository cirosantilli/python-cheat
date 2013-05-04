cheats and information on python and libraries.

whenever possible, I make the cheat runnable and full of assertions!

whatch out for not naming a module with the same as in the stdlib,
or you will import the module from current dir instead!
this is why some files are named *cheat.py.

# pros of python

Python is great for small/medium projects:

- builtin lists [] and dictionnaries {}.
    Really helpful to type less for shorter scripts.

    Has the downside of being harder to document, but still is a good thing.

- dinamically typing:

        a = 1
        a = "abc"

    good when writting smaller scripts because it means much less typing.

# cons of python

- dinamically typing:

        a = 1
        a = "abc"

    what this means is that tons of projects will not document what types of objects functions need to get
    and large projects become a mess...

- putting self in every class method: `__init__(self)`

- global functions that should be class functions: `len([1,2])` instead of `[1.2].len()`

- package management is still not perfect.

- autodocumentation tools are still not perfect (`Shpinx`)
