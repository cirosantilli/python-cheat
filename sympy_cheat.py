#!/usr/bin/env python

"""
Good tutorial on docs:

http://docs.sympy.org/0.7.2/tutorial.html

Does precisely:

-   fractions

-   + * **

-   simplification

-   substitution: x**2, x = y+1

-   derivatives of known functions

        1/(x^2+1) = 1/y + 1/z

Attempts with heuristics:

-   integrals

-   exact solution of differential equations!
"""

from sympy import Symbol, cos
x = Symbol("x")
(1/cos(x)).series(x, 0, 10)
