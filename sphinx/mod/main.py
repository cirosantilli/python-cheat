#docstrings
def f(name, state=None):
    r"""short summary

    longer explanation

    latex math: :math:`a^2 + \alpha`.

    refers to a function: :func:`f2`

    refers to a function: :class:`C`

    refers to a function on another relative module: :func:`.a.f`

    cannot have headers here

    othernormal `reST <http://docutils.sourceforge.net/rst.html>`_

    - l1
    - l2

    :param arg1: the first value
    :type arg1: int

    :param arg2: the first value
    :type arg2: int

    :param arg3: the first value
    :type arg3: int

    :returns: 0
    :rtype: int

    :raises: AttributeError, KeyError

    :example:

    .. doctest::

        >>> 1+1
        2
        >>> 1+1
        1

    .. note:: can be useful to emphasize
        important feature
    .. seealso:: :class:`MainClass2`
    .. warning:: arg2 must be non-zero.

    """
    return 0

def f2():
    pass

class C():
    pass
