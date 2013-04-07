#docstrings
def func(name, state=None):
    """short summary

    longer explanation
    latex math: :math:`\\alpha`.
    refers to a function: :func:`function1`
    refers to a class: TODO

    **kwargs vs named args**:
        note that in python, there is no difference for the end user
        between kwargs and args named on function def: so you document
        them in the same way

    :param arg1: the first value
    :param arg2: the first value
    :param arg3: the first value
    :type arg1: int
    :type arg2: int
    :type arg3: int
    :returns: arg1/arg2 +arg3
    :rtype: int
    :raises: AttributeError, KeyError

    :example:

    >>> import template
    >>> a = template.MainClass1()
    >>> a.function1(1,1,1)
    2

    .. note:: can be useful to emphasize
        important feature
    .. seealso:: :class:`MainClass2`
    .. warning:: arg2 must be non-zero.
    .. todo:: check that arg2 is non zero.This function does something.

    """
    return 0
