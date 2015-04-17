# How to hack Python projects

Next, you might want to do the following to isolate the development version of a package:

-   create a dir: `$DEVPATH`

-   add it to the `PYTHONPATH` variable. This will insert it in the `sys.path` before distro's installation paths

-   symlink all the packages of the project into `$DEVPATH`

-   to turn off your dev version of Matplotlib and fall back to the stable distro installed one, just rename `matplotlib` as `matplotlib.off`

-   if the project contains C/C++ extensions, you can:

        python setup.py build_ext --inplace

    The first time, and whenever you modify a C/C++ extension.

    This will place the compiled c/c++ outputs side by side with the python code in the repo, exactly where they need to be, without touching anything outside the repo.
