Every Python file in this dir must implement the `plot` method and can generate only a single figure (`svg`, `png`, etc.).

This will automatically be done with a `Makefile` outside this dir.

If you want to generate more than one plot per file, put the file that will do that outside this dir and customize the makefile.
