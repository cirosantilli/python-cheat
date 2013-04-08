#!/usr/bin/env python

#?usefulness = 8

"""
parse command line arguments

print nice help and error messages

stdlib

very easy to make complex command line argument interfaces!
"""

import argparse
import os.path
import sys

##basic usage
sys.argv = ['program_name','0','1']

parser = argparse.ArgumentParser()
parser.add_argument('a')
parser.add_argument('b')
args = parser.parse_args() #by default takes sys.argv[1:]
assert args.a == '0'
assert args.b == '1'
    
##good parser template

parser = argparse.ArgumentParser(
    description="", #one line summary of program
    epilog=r"""
EXAMPLES

%(f)s
""" % { 'f' : sys.argv[0] },                    #f contains command name
    formatter_class=argparse.RawTextHelpFormatter,   #keep newlines
)

##name conversions

#- removes leading '-'
#- transforms middle '-' to '_'

##positional args

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
)
args = parser.parse_args(['1'])
assert args.a == '1'
#exits process and prints help:
    #args = parser.parse_args([])

parser = argparse.ArgumentParser()
parser.add_argument(
    '0',
    default=""
)
args = parser.parse_args(['a'])
assert True
#TODO

##help

#gives description to users in case of error/help. always define it.

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    help = 'help text',
)
args = parser.parse_args(['1'])

##optional args

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
)
args = parser.parse_args(['-a','1'])
assert args.a == '1'
#ok, a is optional because the name starts with '-':
args = parser.parse_args([])
assert args.a == None

#see <#name conversion>

#in practice, always give a <default>

##default

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    default='2',
)
args = parser.parse_args([])
assert args.a == '2'
args = parser.parse_args(['-a','1'])
assert args.a == '1'

###does nothing with positional args

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    default='1'
)
#exits process:
    #args = parser.parse_args([])

###name conflict

#bad

parser = argparse.ArgumentParser()
parser.add_argument('a')
parser.add_argument('-a')
args = parser.parse_args(['-a','1','2'])
assert args.a == '2'

#impossible to access '-a'

#may resolve this with <#dest>

##long name

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    '--a-long',
)
args = parser.parse_args(['--a-long','1'])
assert args.a_long == '1'
args = parser.parse_args(['-a','1'])
assert args.a_long == '1'
assert not hasattr(args,'a')

##dest

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    '--a-long',
    dest="d",
)
args = parser.parse_args(['--a-long','1'])
assert args.d == '1'
args = parser.parse_args(['-a','1'])
assert args.d == '1'
assert not hasattr(args,'a')
assert not hasattr(args,'a_long')

##type

###int

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    type=int,
    default=1,
)
args = parser.parse_args(['1'])
assert args.a == 1

###float

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    type=float,
    default=1.0,
)
args = parser.parse_args(['1.0'])
assert args.a == 1.0

###boolean

#see <#store_true> <#action>

##nargs

###number

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    nargs=2,
    default=['1','2']
)
args = parser.parse_args(['1','2'])
assert args.a == ['1','2']
#error: must be exactly 2:
    #parser.parse_args(['1'])

###1

#still is a list.

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    nargs=1,
    default=['1']
)
args = parser.parse_args(['1'])
assert args.a == ['1']
assert args.a != '1'

###star

#zero or more

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    nargs='*',
    default=[],
)
args = parser.parse_args(['1','2','3','4'])
assert args.a == ['1','2','3','4']
args = parser.parse_args([])
assert args.a == []

###interrogation

#zero or one

#doe not return a list

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

###plus

#one or more

parser = argparse.ArgumentParser()
parser.add_argument(
    'a',
    nargs='+',
    help='1 or more args (must be last arguments)'
)
args = parser.parse_args(['1','2','3','4'])
assert args.a == ['1','2','3','4']
#error: even if default:
    #args = parser.parse_args([])

##action

###store_true false

#good to make switches:

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

###store

#is the default action:

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    action='store', 
    default='2'
)
args = parser.parse_args(['-a','1'])
assert args.a == '1'
args = parser.parse_args([])
assert args.a == '2'

###store_const

#more general than store_true false, but less useful:

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

###append

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    action='append',
    default=[],
)
args = parser.parse_args(['-a','1'])
assert args.a == ['1']
args = parser.parse_args(['-a','1','-a','2'])
assert args.a == ['1','2']

###append_const

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a', 
    action='append_const',
    const='1',
)
args = parser.parse_args(['-a'])
assert args.a == ['1']
args = parser.parse_args(['-a','-a'])
assert args.a == ['1','1']

###custom actions

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
args = parser.parse_args( '--foo 1 2'.split() )
assert args.foo == '1'
assert args.bar == '2'

##choices

#select from a set

###list

#1, 2 or 3 only:

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
#error:
    #args = parser.parse_args(['4'])

###string

#chars.

#a, b or c only:

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

##inheritnace via arguments

#*add_help is obligatory here*!!
#or else will conflict with child help argument.
parent_parser = argparse.ArgumentParser( add_help = False )
parent_parser.add_argument( 'parent' )

foo_parser = argparse.ArgumentParser( parents=[parent_parser] )
foo_parser.add_argument('child')

args = foo_parser.parse_args(['2', '1'])
assert args.parent == '2'
assert args.child == '1'
