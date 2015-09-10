# Pros and cons

## Pros

Python is part of the [LSB](http://refspecs.linux-foundation.org/LSB_4.1.0/LSB-Languages/LSB-Languages/python.html), so any Linux distribution must have it. Perl is too, but Java and Ruby are not.

Python is great for small / medium projects:

-   built-in lists and dictionary literals `[]` `{}`. Really helpful to type less for shorter scripts.

-   dynamic typing:

        a = 1
        a = "abc"

    Good when writing smaller scripts because it means much less typing.

-   domains it dominates for scripting:

    - scientific: 
    - binary executable analysis automation for hackers: http://www.amazon.com/dp/1593271921/ , https://github.com/aquynh/capstone , IDA Pro https://www.hex-rays.com/products/ida/support/idapython_docs/

## Cons

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

