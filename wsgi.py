#! /usr/bin/env python

## about

#wsgi python interface for server communication

#standard wsgi server reference implementation

#much like cgi, but python specific

#can have many implementations

#on apache, is commonly implemented with mod_wsgi

##thanks to

#<http://webpython.codepoint.net/wsgi_environment_dictionary>

from wsgiref.simple_server import make_server

def application(environ, start_response):
    """
    this function must have this signature:

    inputs:
        take environ dict
        start_response function of string and list of string pairs

    return:
        response_body

    the function name is optional for the wsgiref server,
    but is very coventional may be obligatory for apache's mod_wsgi,
    so always use it.
    """

    response_body = [
        '%s: %s' % (key, value)
        for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

## test

### test server

#### set server params

httpd = make_server(
    'localhost', #hostname
    8051, #port
    application #the function with the given specifications
)

#### run server

#handle single request:

#``httpd.handle_request()``

#handle infinite requests:

httpd.serve_forever()

### apache

#use mod_wsgi

#first install and load mod_wsgi:

#``` {.bash}
#sudo aptitude install -y libapache2-mod-wsgi
#```

#exceptions are now logged to the server log file

#put this in you apache.conf:

    #WSGIScriptAlias /the/url /var/www/path/to/wsgi.py

#works just like ``ScriptAlias``

#### optional configurations

#append dir to the *end* of the python search path:

    #WSGIPythonPath /path/to/dir1:/path/to/dir2

## try server out

    #firefox localhost:8051

# with a path:

    #firefox localhost:8051/some/path/to/html.html

#it contains /some/path/to/html.html
#this allows you to serve what you want for that path.
