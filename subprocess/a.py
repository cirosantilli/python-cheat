#!/usr/bin/env python

#stdin --> stdout
#argv  --> stderr

import sys

#read until EOF (ctrl+d on terminal or pipe close by other program)
input = sys.stdin.read() 

##newline hell

#this automatically converts '\n' chars to the newline of the specific system:

sys.stdout.write( 'stdout:\n%s\n' % input )
sys.stderr.write( 'stderr:\n%s\n' % '\n'.join( sys.argv[1:] ) )

#so this looks good to print to shell screens,
#but potentially bad if you are using pipes!!

#exit status is given here:
sys.exit(0)
