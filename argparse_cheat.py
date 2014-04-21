#!/usr/bin/env python

"""
stdlib.

Makes it very easy to create complex POSIX / GNU command line interfaces!
"""

import argparse
import sys

if "Basic usage":

    # parse_args takes by default sys.argv[1:], which we have artificially set here.
    sys.argv = ['program_name', '0', '1']
    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    parser.add_argument('b')
    args = parser.parse_args()
    # Same:
    #args = parser.parse_args(sys.argv)
    assert args.a == '0'
    assert args.b == '1'

    '''
    Thigs this does already include:

    - add a `-h` / `--help` option that prints usage and exits after `parse_args`.
    '''

if "Good parser template":

    parser = argparse.ArgumentParser(
        # One line description.
        description="",
        # Full description.
        epilog=r"""
    EXAMPLES

    %(f)s
    """.format(f=sys.argv[0]),                           # f contains command name.
        formatter_class=argparse.RawTextHelpFormatter,   # Keep newlines.
    )

if "##Automatic option names.":

    """
    Given the command line argument form, argparse automatically derives a Python variable name from it:

    - removes leading '-'
    - transforms middle '-' to '_'
    """

    # In case of name conflicts, it becomes simply impossible to access one of the variables.

    parser = argparse.ArgumentParser()
    parser.add_argument('a')
    parser.add_argument('-a')
    args = parser.parse_args(['-a', '1', '2'])
    # Impossible to access -a.
    #assert args.-a == '2'
    assert args.a == '2'

    # This can be resolved this with the `dest` parameter.

    if "##dest":

        # Specifies where input is stored explicitly.

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            '--a-long',
            dest="d",
        )
        args = parser.parse_args(['--a-long', '1'])
        assert args.d == '1'
        args = parser.parse_args(['-a', '1'])
        assert args.d == '1'
        assert not hasattr(args, 'a')
        assert not hasattr(args, 'a_long')

if "##Positional args":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
    )
    args = parser.parse_args(['1'])
    assert args.a == '1'
    # Exit process and prints help:
    #args = parser.parse_args([])

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '0',
        default=""
    )
    args = parser.parse_args(['a'])
    assert True
    #TODO

if "##help":

    # Gives description to users in case of error/help. Always define it.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        help = 'help text',
    )
    args = parser.parse_args(['1'])

if "##Optional args":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a',
    )
    args = parser.parse_args(['-a', '1'])
    assert args.a == '1'
    #ok, a is optional because the name starts with '-':
    args = parser.parse_args([])
    assert args.a == None

if "##default":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a',
        default='2',
    )
    args = parser.parse_args([])
    assert args.a == '2'
    args = parser.parse_args(['-a', '1'])
    assert args.a == '1'

    # Does nothing with positional args:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        default='1'
    )

if "##Long name":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a',
        '--a-long',
    )
    args = parser.parse_args(['--a-long', '1'])
    assert args.a_long == '1'
    args = parser.parse_args(['-a', '1'])
    assert args.a_long == '1'
    assert not hasattr(args, 'a')

if "##type":

    # int

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        type=int,
        default=1,
    )
    args = parser.parse_args(['1'])
    assert args.a == 1

    # float

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        type=float,
        default=1.0,
    )
    args = parser.parse_args(['1.0'])
    assert args.a == 1.0

    # boolean: see <#store_true> <#action>

if "##nargs":

    # Fixed number:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        nargs=2,
        default=['1', '2']
    )
    args = parser.parse_args(['1', '2'])
    assert args.a == ['1', '2']
    # ERROR: there must be exactly 2:
    #parser.parse_args(['1'])

    # nargs=1 still is storea a list, not the object directly.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        nargs=1,
        default=['1']
    )
    args = parser.parse_args(['1'])
    assert args.a == ['1']
    assert args.a != '1'

    # Zero or more arguments:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        nargs='*',
        default=[],
    )
    args = parser.parse_args(['1', '2', '3', '4'])
    assert args.a == ['1', '2', '3', '4']
    args = parser.parse_args([])
    assert args.a == []

    # Zero or one. Doe not store return a list, but the element itself.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        nargs='?',
        default='2'
    )
    args = parser.parse_args(['1'])
    assert args.a == '1'
    args = parser.parse_args([])
    assert args.a == '2'

    # One or more.

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'a',
        nargs='+',
        help='1 or more args (must be last arguments)'
    )
    args = parser.parse_args(['1', '2', '3', '4'])
    assert args.a == ['1', '2', '3', '4']
    # ERROR: even if default:
    #args = parser.parse_args([])

if "##action":

    if "##store":

        # Is the default action:

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action='store',
            default='2'
        )
        args = parser.parse_args(['-a', '1'])
        assert args.a == '1'
        args = parser.parse_args([])
        assert args.a == '2'

    if "##store_true false":

        # Good to make switches:

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action="store_true",
            default=False,
        )
        args = parser.parse_args([])
        assert args.a == False
        args = parser.parse_args(['-a'])
        assert args.a == True

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action="store_false",
            default=True,
        )
        args = parser.parse_args([])
        assert args.a == True
        args = parser.parse_args(['-a'])
        assert args.a == False

    if "##store_const":

        # Generalizes `store_true`.

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action='store_const',
            const='1',
            default='2'
        )
        args = parser.parse_args(['-a'])
        assert args.a == '1'
        args = parser.parse_args([])
        assert args.a == '2'

    if "##append":

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action='append',
            default=[],
        )
        args = parser.parse_args(['-a', '1'])
        assert args.a == ['1']
        args = parser.parse_args(['-a', '1', '-a', '2'])
        assert args.a == ['1', '2']

    if "##append_const":

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            action='append_const',
            const='1',
        )
        args = parser.parse_args(['-a'])
        assert args.a == ['1']
        args = parser.parse_args(['-a', '-a'])
        assert args.a == ['1', '1']

    if "##custom actions":

        class FooAction(argparse.Action):
            def __call__(self, parser, namespace, values, option_string=None):
                """only called if not default value"""
                #print('%r %r %r' % (namespace, values, option_string))
                setattr(namespace, self.dest, values)

        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--foo',
            action=FooAction
        )
        parser.add_argument(
            'bar',
            action=FooAction
        )
        args = parser.parse_args('--foo 1 2'.split())
        assert args.foo == '1'
        assert args.bar == '2'

if "##choices":

    # Restrict argument to a set.

    if "##list":

        # Argment must be in the list.

        parser = argparse.ArgumentParser()
        parser.add_argument(
            'a',
            type=int,
            choices=[1, 2, 3]
        )
        args = parser.parse_args(['1'])
        assert args.a == 1
        args = parser.parse_args(['2'])
        assert args.a == 2
        # ERROR:
        #args = parser.parse_args(['4'])

    if "##string":

        # Argment must be a character in the string.

        parser = argparse.ArgumentParser()
        parser.add_argument(
            'a',
            choices='abc'
        )
        args = parser.parse_args(['a'])
        assert args.a == 'a'
        args = parser.parse_args(['b'])
        assert args.a == 'b'
        #error:
            #args = parser.parse_args(['d'])

if "##inheritnace via arguments":

    # *add_help=False is obligatory here*!!
    # or else will conflict with child help argument.
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('parent')

    foo_parser = argparse.ArgumentParser(parents=[parent_parser])
    foo_parser.add_argument('child')

    args = foo_parser.parse_args(['2', '1'])
    assert args.parent == '2'
    assert args.child == '1'
