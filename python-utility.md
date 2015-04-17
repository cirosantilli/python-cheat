# python utility

-   `-O`: optimize.

    -   `assert` is removed from `.pyc`

    -   `__debug__ == False`

        You can write stuff like

            if __debug__: print "debug"

        and it will only show show is `-O` is off.
