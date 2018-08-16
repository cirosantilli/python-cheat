# C from Python

This dir shows how to call C functions from Python on Linux.

This is called "extending Python with C", and is documented at:

* https://stackoverflow.com/questions/145270/calling-c-c-from-python
* https://docs.python.org/2/extending/extending.html

Examples:

-   [cpython_cheat.c](cpython_cheat.c) and [cpython_cheat.py](cpython_cheat.py) demonstrate the usage of the Python standard library's `cpython` module.

    Notice how that module allows importing completely unmodified C functionality from a `.so` shared library into Python without any Python specifics to it.

    [cpython_cheat_relative.py](cpython_cheat_relative.py) imports the library with a relative path, and can be used to see that `LD_LIBRARY_PATH` is used to find the `.so`.

-   TODO [import_cheat.c](import_cheat.c) and [import_cheat.py](import_cheat.py) show that `.so` libraries can also be imported directly with the `import` statement.

    However, those libraries must contain Python specifics such as defining the init module function.

    The `PYTHONPATH` is used when searching for the `.so` files with `import` instead of `LD_LIBRARY_PATH`.

    See also: <https://stackoverflow.com/questions/24226001/importerror-dynamic-module-does-not-define-init-function-initfizzbuzz>
