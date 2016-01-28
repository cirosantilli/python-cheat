#!/usr/bin/env python

"""
http://stackoverflow.com/questions/1450132/proxy-with-urllib2
"""

import urllib2

urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': '127.0.0.1:9050'})))
print(urllib2.urlopen(urllib2.Request('http://checkip.amazonaws.com/')).read())
