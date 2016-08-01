#docstrings
def f(name, state=None):
    r"""Short summary.

    Longer explanation.

    LaTeX math: :math:`a^2 + \alpha`.

    Function link: :func:`f2`

    Class link: :class:`C`

    Relative module function link: :func:`.a.f`

    Cannot have headers here.

    Othernormal `reST <http://docutils.sourceforge.net/rst.html>`_

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
    """
    :ivar i: instance variable
    :vartype i: int

    :var v: TODO variable? TODO shows the same as the others in 1.2.2.
    :vartype v: int

    :cvar c: class variable. TODO shows the same as the others in 1.2.2.
    :vartype c: int
    """

    def __init__( self ):
        self.i = 0
