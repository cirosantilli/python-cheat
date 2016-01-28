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
import sys
import time

if '## Default logger':

    logging.basicConfig(
        # Log to a file. Default is sys.stderr.
        # This can only take file path strings.
        # To log to stdout, use:
        #filename = 'example.log',
        # Mode defaults to `a`, which appends to old log.
        #filemode = 'w'

        # Minimum log level that will get printed.
        # Often taken as a CLI parameter.
        level = logging.DEBUG,
        #level = logging.INFO,
        #level = logging.WARNING,
        #level = logging.ERROR,
        #level = logging.CRITICAL,

        # Default does not contain time, so you very likely want to override this.
        format = '  %(levelname)s %(asctime)s %(message)s',

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

if '## Align':

    """
    http://stackoverflow.com/questions/7771912/how-to-right-align-level-field-in-python-logging-formatter
    http://stackoverflow.com/questions/20618570/python-logging-formatter-is-there-any-way-to-fix-the-width-of-a-field-and-jus

    For the level name, use: `%(levelname)8s`
    """

if '## UTC time':

    # http://stackoverflow.com/questions/6321160/python-logging-how-to-set-time-to-gmt

    logging.debug('not UTC')
    logging.Formatter.converter = time.gmtime
    logging.debug('UTC')

if '## Threading':

    """
    logging is thread safe:
    http://stackoverflow.com/questions/2973900/is-pythons-logging-module-thread-safe?lq=1

    You will likely want to log the thread name on every log write:
    http://stackoverflow.com/a/2357652/895245
    """
