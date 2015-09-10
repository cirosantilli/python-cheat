# Implementations

Python specifies the language and stdlib interfaces, not the implementation.

The main interpreter implementations are:

- [CPython](http://www.python.org/getit/source/). Reference implementation.
- PyPy. Supposed to be faster than CPython. No GIL. <https://en.wikipedia.org/wiki/PyPy> <http://stackoverflow.com/questions/18946662/why-shouldnt-i-use-pypy-over-cpython-if-pypy-is-6-3-times-faster> <http://stackoverflow.com/questions/2591879/pypy-how-can-it-possibly-beat-cpython>
- JPython. Compiles to Java Object Code.
- IronPython. Compiles to `.NET` object code.
- Cython. Translate Python as C? <https://en.wikipedia.org/wiki/Cython>

## Global Interpreter Lock

## GIL

<http://programmers.stackexchange.com/questions/186889/why-was-python-written-with-the-gil>

<https://wiki.python.org/moin/GlobalInterpreterLock>
