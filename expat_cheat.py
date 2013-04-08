import os.path
from xml.parsers import expat

class Parser:

    def __init__(self):
	self._result = '<ul>\n'
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self.start
        self._parser.EndElementHandler = self.end
        self._parser.CharacterDataHandler = self.data

    def feed(self, data):
        self._parser.Parse(data, 0)

    def close(self):
        self._parser.Parse("", 1) # end of data
        del self._parser # get rid of circular references
	self._result += '</ul>'

    def start(self, tag, attrs):
	id = attrs['id']
        self._result += '<li><a href="index.html?' + id  + '">' + id + '</a></li>\n'

    def end(self, tag):
	1
#        self._result += "END" + str(tag) + "\n"

    def data(self, data):
	1
#        self._result+= "DATA" + repr(data)

    def result(self):
	return self._result

home_dir = os.path.dirname(os.path.dirname(__file__))

input_path = os.path.join(home_dir,'toc.xml')
output_path = os.path.join(home_dir,'toc.html')

#get input from file
file = open(input_path,'r')
input = file.read()
file.close()

#transform xml
p = Parser()
p.feed(xml_data)
p.close()
output = p.result()

#do something with output
print result
#file = open(output_path,'w')
#file.write(output)
#file.close()
