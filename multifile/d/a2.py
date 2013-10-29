def f():
    return "d.a2.f()"

#imports are relative to current dir:

import d2

assert d2.f() == "d.d2.f()"

#using from . only imports relative to current dir, does not look into python path:

from . import os

assert os.f() == "d.os.f()"

#only works because we are a submodule!
