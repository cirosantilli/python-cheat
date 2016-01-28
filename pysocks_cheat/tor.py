#!/usr/bin/env python

"""
http://stackoverflow.com/questions/711351/using-urllib-with-tor
http://stackoverflow.com/a/34493721/895245

Before running, make sure that Tor is running on port 9050. Ubuntu 15.10:

    sudo apt-get install tor

Multiple connections at the same time: http://stackoverflow.com/a/8100870/895245
"""

import socket
import socks
import urllib2

ipcheck_url = 'http://checkip.amazonaws.com/'

# Actual IP.
print(urllib2.urlopen(ipcheck_url).read())

# Tor IP.
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)
socket.socket = socks.socksocket
print(urllib2.urlopen(ipcheck_url).read())
print(urllib2.urlopen(ipcheck_url).read())

# Another Tor IP.
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9052)
#print(urllib2.urlopen(ipcheck_url).read())
