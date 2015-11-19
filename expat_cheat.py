#!/usr/bin/env python

"""
Sequential XML parsing.

No child/parent concept.

Harder to use if you need node wise operations,
but very fast and memory efficient as it does not need to read the entire file at once.

Python has many other XML parsing methods:
http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python
"""

import os.path
import xml.parsers.expat

class Parser:

    def __init__(self):
        self._output = ''
        self._parser = xml.parsers.expat.ParserCreate()

        # Set what function does what.
        self._parser.StartElementHandler  = self.tagOpen
        self._parser.EndElementHandler    = self.tagClose
        self._parser.CharacterDataHandler = self.tagData

        # Find attributes of matching opening tag of a closing tag.
        self._attr_stack = []

    def feed(self, data, isfinal):
        """
        Pass XML data string to process.

        Can be called multiple times with different pieces of a given XML.

        isfinal == True iff this is th last call.

        For input from file use instead:

            self._parser.ParseFile(open('path.xml', 'r'))
        """
        self._parser.Parse(data, isfinal)

    def output(self):
        """
        Return the processed input.
        """
        return self._output

    def tagOpen(self, tag, attrs):
        self._output += 'open: ' + tag + ' ' + str(attrs) + '\n'
        self._attr_stack.append(attrs)

    def tagData(self, data):
        self._output+= 'data: ' + repr(data) + '\n'

    def tagClose(self, tag):
        self._output += 'close: ' + tag + ' ' + str(self._attr_stack[-1]) + '\n'
        del self._attr_stack[-1]

xml_string0 = """
<t a="v" a2="v2">
    d
    d2
    <t2 a21="v" a22="v2">
"""
xml_string1 = """
        d3
        d4
    </t2>
    d5
    d6
</t>
"""

# Parse.
p = Parser()
p.feed(xml_string0, False)
p.feed(xml_string1, True)
print p.output()
