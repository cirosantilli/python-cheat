#docstrings
def f(arg1, arg2, arg3, state=None):
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

    :param class_with_dot: another class with dot
    :type arg4: :class:`.C`

    :param class_without_dot: another class without dot
    :type class_without_dot: :class:`C`

    :param multi_type: multiple types!
    :type multi_type: :class:`.C` or :class:`.D`

    :param class_and_union: class and Union type hinting together
    :type class_and_union: Union[:class:`C`, :class:`.D`]

    :param type_hint: type_hint
    :type type_hint: List[C]

    http://stackoverflow.com/questions/21799554/how-do-i-automatically-link-to-a-parameter-type-in-rest-docstrings-in-sphinx
    :param :class:`.C` inline_link: inline link

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

    def g(self):
        """
        Method link: :func:`g2`
        """
        pass

    def g2(self):
        """
        """
        pass

    def __init__( self ):
        self.i = 0

class D():
    pass
