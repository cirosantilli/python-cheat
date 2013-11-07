#!/usr/bin/env python

"""
WSGI is a Python standrad interface for server communication.

It is much like CGI, but Python specific.

The stdlib funishes a WSGI reference implementation.

There are however other important implementations:

- Apache mod_wsgi
- gunicorn

The advantage of WSGI is that a single python web script can be run on several
different implementations with same results.
"""

def application(environ, start_response):
    """
    This function is the central piece that implements WSGI.

    Inputs:

    - `environ` string to string dict.

        Contains key information about the query that allows our server to generate the correct response.

        For example:

            REQUEST_METHOD: GET
            PATH_INFO: /a/b
            QUERY_STRING: c=d
            RAW_URI: /a/b?c=d

        This may or may not contain `os.environ`.

    - `start_response`: TODO function of string and list of string pairs

    Return value

    - response_body string.

    The function name is optional for the wsgiref server,
    but is very coventional may be obligatory for apache's mod_wsgi,
    so always use it.
    """
    env = [
        '%s: %s' % (key, value)
        for key, value in sorted(environ.items())
    ]
    response_body = 'WSGI Test\n\n'
    response_body += '\n'.join(env)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':

    ##wsgiref

    # Set server params:

    from wsgiref.simple_server import make_server

    httpd = make_server(
        'localhost', # hostname
        8051,        # port
        application  # the function with the given WSGI specifications
    )

    # Handle single request and quit:

    #`httpd.handle_request()`

    # Handle requests forever:

    httpd.serve_forever()

    ##apache mod_wsgi

    # First install and load mod_wsgi:

    #``` {.bash}
    #sudo aptitude install -y libapache2-mod-wsgi
    #```

    # Exceptions are now logged to the server log file.

    # Put this in your `apache.conf`:

    #WSGIScriptAlias /the/url /var/www/path/to/wsgi.py

    # Works just like a `ScriptAlias`

    # Append dir to the *end* of the python search path:

        #WSGIPythonPath /path/to/dir1:/path/to/dir2

    ##gunicorn

    #DO:

        #gunicorn main:application
