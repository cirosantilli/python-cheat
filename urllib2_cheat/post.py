#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## POST
"""

import urllib2

'''
## urlopen

    Does the actual request.

    Raises urllib2.URLError on error.

    It timeout not given a global default is used.

    Retruns bytestring, not unicode.

    Encoding can sometimes be inferred from Content-Type HTTP header:

        Content-Type: text/html; charset=ISO-8859-1

    Returns a file like object with some extra methods.

    info() returns an object with methods shown in: <http://docs.python.org/2/library/mimetools.html#mimetools.Message>
'''

req = urllib2.Request(
        'https://api.github.com/markdown',
        '{"text":"**Hello World 你好**", "mode":"gfm", "context":"github/gollum"}')
# Custom request headers;
#request = urllib2.Request("http://www.google.com", headers={"Accept" : "text/html"})
try:
    response = urllib2.urlopen(req, timeout=10)
except urllib2.URLError, e:
    print e
    sys.exit(1)
response_body = response.read()
assert type(response_body) == str
print('response body   = ' + response_body)
print('response status = {}'.format(response.getcode()))
info = response.info()
# Header string list
print('response info   = ' + repr(info.headers))
# Header key val dict
print('response info   = ' + repr(info.items()))

##retry

    # Exponential backoff retry: http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
