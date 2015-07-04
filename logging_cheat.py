#!/usr/bin/env python

"""
## logging

Standard way to output error messages.

Advantages:

- has many useful built-in error formats
- has a level system
- easy to change where logs go, e.g. a file.

http://docs.python.org/2/howto/logging.html

TODO log all at once
"""

import logging

if '## Defult logger':

    logging.basicConfig(
        # Log to a file. Default is sys.stderr.
        # This can only take file path strings.
        # To log to stdout, use:
        #filename = 'example.log',
        #filemode = 'w'

        # Minimum log level that will get printed.
        # Often taken as a CLI parameter.
        level = logging.DEBUG,
        #level = logging.INFO,
        #level = logging.WARNING,
        #level = logging.ERROR,
        #level = logging.CRITICAL,

        format = '  %(levelname)s %(name)s %(asctime)s %(message)s',

        # Format for asctime
        datefmt = '%m/%d/%Y %I:%M:%S %p',
    )
    sys.stderr.write("logging:\n")
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')
    try:
        raise Exception
    except:
        logging.exception('inside exception. also prints exception stack')

if '## Custom loggers':

    # Create logger
    logger = logging.getLogger('logger_name')
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('  %(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to ch
    ch.setFormatter(formatter)

    # Add ch to logger
    logger.addHandler(ch)

    # Usage:
    sys.stderr.write("custom logger:\n")
    logger.debug('debug')
    logger.info('info')
    logger.warn('warn')
    logger.error('error')
    logger.critical('critical')

# TODO: log all / a certain level to stdout
