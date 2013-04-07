#!/usr/bin/env python

#read line by line from:

#1) files with filenames in stdin[1:], one by one
#2) stdin

#if stdin is a tty, waits for input

#this emulates the typical gnu interface

## bash tests

#loop over lines of stdin:

#``` {.bash}
#echo -en 'a\nb' | fileinput.py
#```

#loop over lines of a.tmp and then b.tmp:

#``` {.bash}
#echo -en 'a\nb' > a.tmp
#echo -en 'c\nd' > b.tmp
#fileinput.py a.tmp b.tmp
#```

#only a.txt is used:

#``` {.bash}
#echo -en 'a\nb' | fileinput.py a.tmp
#```

import fileinput

for line in fileinput.input():
    print line
