#!/usr/bin/env python

"""
Sequential XML parsing.

No child/parent concept.

Harder to use if you need node wise operations,
but very fast and memory efficient as it does not need to read the entire file at once.
"""

import os.path
from xml.parsers import expat

class Parser:

    def __init__(self):
        self._result = 'begin\n'
        self._parser = expat.ParserCreate()

        # Set what function does what.
        self._parser.StartElementHandler    = self.tagOpen
        self._parser.EndElementHandler      = self.tagClose
        self._parser.CharacterDataHandler   = self.tagData

        # Find attributes of matching opening tag of a closing tag.
        self._attr_stack = []

    def feed(self, data):
        """
        Set data to process.
        """
        self._parser.Parse(data, 0)

    def close(self):
        """
        Called after input is over.
        """
        #self._parser.Parse("", 1)   # end of data
        #del self._parser            # get rid of circular references
        self._result += 'end\n'

    def result(self):
        """
        Returns the processed input.
        """
        return self._result

    def tagOpen(self, tag, attrs):
        self._result += 'open: ' + tag + ' ' + str(attrs) + '\n'
        self._attr_stack.append(attrs)

    def tagData(self, data):
        self._result+= 'data: ' + repr(data) + '\n'

    def tagClose(self, tag):
        self._result += 'close: ' + tag + ' ' + str(self._attr_stack[-1]) + '\n'
        del self._attr_stack[-1]

xml_data = """
<t a="v" a2="v2">
    d
    d2
    <t2 a21="v" a22="v2">
        d3
        d4
    </t2>
    d5
    d6
</t>
"""

# Get input from file:
#file = open(argv[1],'r')
#xml_data = file.read()
#file.close()

# Parse.
p = Parser()
p.feed(xml_data)
p.close()
output = p.result()

print output

# Save outpt to a file:
#output_path = os.path.join(home_dir,'a.html')
#file = open(output_path,'w')
#file.write(output)
#file.close()
