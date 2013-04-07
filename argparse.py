#!/usr/bin/env python

"""
parse command line arguments

stdlib
"""

import argparse
import os.path
import sys

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        description="", #one line summary of program
        epilog=r"""
INSTALLATION

EXAMPLES

  %(f)s

  %(f)s
""" % {'f':os.path.basename(__file__)},
        formatter_class=RawTextHelpFormatter, #keep newlines
    )

    parser.add_argument(
        'a',
        help="positional (obligatory) argument because no hyphen before a.",
        default=""
    )
    args = parser.parse_args('1')
    a = args.a
    #1

    parser.add_argument(
        '0',
        help="positional (obligatory) argument because no hyphen before a.",
        default=""
    )
    #a = args. #TODO what name?

    parser.add_argument(
        '-a',
        help="optional argument because there is hyphen before a. Takes a single value.",
        default=""
    )
    parser.parse_args('--foo 1'.split())
    args.a
    #1

    parser.add_argument(
        '-a',
        '--a-long',
        help="provides long name. Must destination is 'along', not 'a'.",
        default=""
    )
    a = parser.parse_args().a_long
    #hyphens are converted to underscores

    parser.add_argument(
        '-a',
        '--a-long',
        dest="d",
        help="provides long name. Must destination is 'along', not 'a'.",
        default=""
    )
    a = args.d

    parser.add_argument(
        '-a', 
        action="store_true", 
        default=False, 
        help='a is False if not present'
    )

    parser.add_argument(
        '-a', 
        action="store_false", 
        default=True, 
        help="a is True if not present"
    )

    parser.add_argument(
        '-a',
        type=int,
        default=1
        help="stores an integer value"
    )

    parser.add_argument('-a'
        nargs='*',
        help="optional. takes 0 or more args. stores a list.",
        default=[])

    parser.add_argument('-a'
        nargs=3,
        help="optional. takes 3 args exatcly. stores a list, even if nargs=1!",
        default=[])

    parser.add_argument('-b', '--blong', 
        action="store", 
        dest="b", 
        help='put string value given into b')
    
    parser.add_argument('--optional', 
        nargs='?', 
        help='0 or 1 args exatcly (must be last arguments)')
    
    parser.add_argument('--all', 
        nargs='*', 
        dest='all', 
        help='0 or more args (must be last arguments)')
    
    parser.add_argument('--one-or-more',
        nargs='+',
        help='1 or more args (must be last arguments)' )
    
    parser.add_argument('-c',
        action='store_const',
        const='value-to-store',
        dest='constant_value',
        help='Store a constant value')

    parser.add_argument('-t',
        action='store_true',
        default=False,
        dest='boolean_switch',
        help='Set a switch to true')
    
    parser.add_argument('-f',
        action='store_false',
        default=False,
        dest='boolean_switch',
        help='Set a switch to false')

    parser.add_argument('-a',
        action='append',
        dest='collection',
        default=[],
        help='Add repeated values to a list')

    parser.add_argument('-A', 
        action='append_const',
        dest='const_collection',
        const='value-1-to-append',
        default=[],
        help='Add different values to list')
    
    parser.add_argument('-B', 
        action='append_const',
        dest='const_collection',
        const='value-2-to-append',
        help='Add different values to list')

    #choices
        #select from a set
        parser.add_argument('a', choices='abc') #a, b or c only
        parser.add_argument('a', type=complex, choices=[1, 1j]) #1 or 1j only

    args = parser.parse_args()
    a = args.a

    #inheritnace can be done via arguments
        >>> parent_parser = argparse.ArgumentParser(add_help=False)
        >>> parent_parser.add_argument('--parent', type=int)

        >>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
        >>> foo_parser.add_argument('foo')
        >>> foo_parser.parse_args(['--parent', '2', 'XXX'])
        Namespace(foo='XXX', parent=2)

        >>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
        >>> bar_parser.add_argument('--bar')
        >>> bar_parser.parse_args(['--bar', 'YYY'])
        Namespace(bar='YYY', parent=None)


    #custom actions!
        >>> class FooAction(argparse.Action):
        ...     def __call__(self, parser, namespace, values, option_string=None):
                    """only called if not default value"""
        ...         print('%r %r %r' % (namespace, values, option_string))
        ...         setattr(namespace, self.dest, values)
        ...
        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument('--foo', action=FooAction)
        >>> parser.add_argument('bar', action=FooAction)
        >>> args = parser.parse_args('1 --foo 2'.split())
        Namespace(bar=None, foo=None) '1' None
        Namespace(bar='1', foo=None) '2' '--foo'
        >>> args
        Namespace(bar='1', foo='2')
