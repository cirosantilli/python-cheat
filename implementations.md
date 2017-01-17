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

## Bytecode

### pyc

TODO: CPython implementation detail?

<https://www.quora.com/What-is-Python-byte-code>

Can differ between minor versions: <http://stackoverflow.com/questions/10547099/python-2-and-3-are-the-bytecode-pyo-pyc-backward-compatible>

Only for loading modules faster, not running: <http://stackoverflow.com/questions/3878479/python-pyc-files-main-file-not-compiled>

### pyd

### pyo

<http://stackoverflow.com/questions/8822335/what-do-the-python-file-extensions-pyc-pyd-pyo-stand-for>
