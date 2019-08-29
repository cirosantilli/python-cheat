#!/usr/bin/env python

import notmain
import d.notmain

assert notmain.notmain_var == 1
assert d.notmain.d_notmain_var == 2
assert d.notmain2.d_notmain2_var == 3
