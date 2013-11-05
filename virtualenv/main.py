#!/usr/bin/env python

import os
import pkg_resources
import sys

sys.stdout.write(('python version = %d.%d ' + os.linesep) %
        (sys.version_info.major, sys.version_info.minor))
sys.stdout.write('termcolor version = '
        + str(pkg_resources.get_distribution('termcolor').version) + os.linesep)
