#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
## string

## str'

There are 2 commonly used classes which are informaly called *strings* in python:
*str* and *unicode*

*basestring* is their common ancestor.
"""

import sys

assert isinstance(str(), basestring)
assert isinstance(unicode(), basestring)
assert not isinstance(bytearray(), basestring)

if '## string literals':

    if '## Single vs double quotes':

        # There is no semantical difference:

        assert 'abc' == 'abc'

        # Except for excaping quotes themselves:

        assert "'" == '\''
        assert '"' == "\""
        assert "\n" == '\n'

        # Advantages of single quote `'`:

        # - prints as less pixels so less noisy
        # - easier to type on a standard keyboard since no shift required

        # PEP 8 and Google Style say choose one and stick with it.
        # Only use the other to avoid backslash escaping the one.

        # Other styles promote a semantic differentiation:

        # - `'` for identifiers, e.g., map keys
        # - `"` for human readable messages: `print "Hello world!"`

        # But this differentiation harder to maintain.

    if '## multiline strings ## triple quotes':

        # Like in C, whitespace separated strings are glued together:

        assert 'ab' 'cd' == 'abcd'

        # This means that backslash continuation joins strings without newlines:

        assert \
            'ab' \
            'cd' == 'abcd'

        assert """a
b""" == 'a\nb'

        assert '''a
b''' == 'a\nb'

        # Spaces are kept:

        assert '''a
 b''' == 'a\n b'

        def f():
            assert """a
b""" == 'a\nb'
        f()

    # Backslash escapes are like in C.

    assert '\x61' == 'a'
    assert '\n' == '\x0A'

    if '## raw string literals ## r literals':

        # Raw literals lose all backslash escape magic.

        assert r'\n' == '\\n'
        assert r'\\' == '\\\\'

        # The exception is to escape the character that would terminate the string (`'` or `"`).
        # In that case, the backslash *remains* in the string:

        assert r'\"' == "\\\""

        # A consequence is that it is impossible to write a raw string literal that ends in backslash.

        assert '\\' != r''

        # Raw string literals are often used with regular expressions,
        # which often contain many literal backslashes.

# Character access is like for a list:

assert 'ab'[0] == 'a'
assert 'ab'[1] == 'b'

# Unlike lists, strings are immutable, to it is not possible to assign to an element,
# or `TypeError` is raised.

try:
    'ab'[0] = 'a'
except TypeError:
    pass
else:
    assert False

if '## Concatenate':

    # Used to be inefficient because strings are immutable, but CPython improved it:
    # http://stackoverflow.com/questions/4435169/good-way-to-append-to-a-string

    # If you are really concerned, use and array and then join at the end.

    assert 'ab' + 'cd' == 'abcd'

# For string literals:

assert 'ab' 'cd' == 'abcd'
assert 'ab' * 3 == 'ababab'

# `replace`: replaces at most once:

assert 'aabbcc'.replace('b',  '0')    == 'aa00cc'
assert 'aabbcc'.replace('bb', '0')    == 'aa0cc'
assert 'aabbcc'.replace('b',  '0', 1) == 'aa0bcc'

if '## string module':

    import string

    if '## constants':

        print 'string.whitespace = ' + string.whitespace.encode('string-escape')

if '## split':

    # Split string into array of strings:

    assert '0ab1ab2'.split('ab') == ['0', '1', '2']
    assert '0abab2'.split('ab')  == ['0', '', '2']

    # If string not given, splits at `string.whitespace*` **regex**!:
    # Very confusing default that changes behaviour completely!
    # But kind of useful default.

    assert '0 1\t \n2'.split() == ['0', '1', '2']

    # Split at ``[\n\r]+`` regex:

    assert '0\n1\r2\r\n3'.splitlines()  == ['0', '1', '2', '3']

if '## strip ## rstrip ## lstrip':

    """
    Strip chars either from either beginning or end, *not* middle!

    Characters to strip are given on a string.

    Default argument: `string.whitespace`

    r and l strip for one sided versions.
    """

    assert 'cbaba0a1b2ccba'.strip('abc') == '0a1b2'
    assert '\t\n0 1 2\v \r'.strip() == '0 1 2'

if '## startswith':

    assert 'abc'.startswith('ab') == True
    assert 'abc'.startswith('bc') == False

    # Remove prefix: <http://stackoverflow.com/questions/599953/python-how-to-remove-the-left-part-of-a-string>

    # If sure that the prefix is there:

    prefix = 'ab'
    assert 'abcd'[len(prefix):] == 'cd'

    # Otherwise:

    prefix = 'ab'
    s = 'abcd'
    if s.startswith(prefix):
        assert s[len(prefix):] == 'cd'

if '## contains substring':
    assert 'bc' in 'abcd'
    assert 'bc' not in 'abdc'
    # The empty string is contained in all others:
    assert '' in ''
    assert '' in 'a'

# String to number:

assert int('123') == 123
assert float('12.34e56') == 12.34e56

# Char to int:

assert ord('a') == 97

# Encode:

assert '\n'.encode('string-escape') == '\\n'

# `string-escape` is similar to `repr`.

if '## unicode ## encodings':

    """
    Before reading this you should understand what is ASCII, Unicode,
    UTF8, UTF16.

    The difference between the `unicode` and `str` classes is that:

    -   `str` is just an array of bytes.

        These could represent ASCII chars since those fit into 1 byte,
        but they could also represent UTF8 chars.

        If they represent UTF8 chars, which may have more than 1 byte per char,
        the str class has no way to know where each char begins and ends,
        so s[0] give gibberish.

        `str` is the output of an encode operation, or the input of a decode operation.

    -   `unicode`: represents actual Unicode characters.

        Unicode strings do not have an explicit encoding,
        although Python probably uses one int per char containing the Unicode code of that character.

        `unicode` is the output of a decode operation, or the input of an encode operation.
    """

    """
    To be able to use utf8 directly in Python source.
    The second line of the file *must* be:

        -*- coding: utf-8 -*-

    Otherwise, you must use escape characters.

    This changes in Python 3 where utf-8 becomes the default encoding.
    """

    if '## u backslash escapes ## unicode literals':

        """
        Unicode literals are just like string literals, but they start with `u`.

        The string below has 2 characters. Characters are treated differently depending on
        if strings are str or unicode.
        """

        u = u'\u4E2D\u6587'
        assert u[0] == u'\u4E2D'
        assert u[1] == u'\u6587'

        """
        Each escape character represents exactly one Unicode character,
        however some escapes cannot represent all characters.
        The possile escapes are:

        -   `\xAA` represents one character of up to one byte.

            This is not very useful with Unicode, since most of those characters
            have a printable and therefore more readable ASCII char to represent them.

            Characters with more than 1 byte cannot be represented with a `\xAA` escape.

        -   `\uAAAA`: 2 bytes.

            This is the most useful escape, as the most common unicode code points are
            use either one or 2 bytes.

        -   `\UAAAAAAAA`: 4 bytes

            It is very rare to have to use `\UAAAAAAAA` literals,
            since Unicode plane 0 which contains the most common characters
            fit into one byte.

            Also note that `\U0010FFFF` is the largest possible character:
            the first byte must always be 0, since that is as far as Unicode goes.

        Remember: `\` escapes are interpreted inside multiline comment strings.
        Therefore, if you write an invalid escape like `\\xYY`, your code will not run!
        """

        assert u'\u4E2D\u6587' == u'中文'
        assert u'\U00010000' == u'𐀀'

        """
        A is done to confirm that a byte is a known unicode character.
        For example `\UAAAAAAAA` does not currently represent any Unicode character,
        so you cannot use it.
        """

        #u'\UAAAAAAAA'

        #Unicode \u escapes are only interpreted inside unicode string literals.

        s = '\u4E2D\u6587'
        assert s[0] == '\\'
        assert s[1] == 'u'
        assert s[2] == '4'

    """
    ## encode

    ## decode

        Encode transforms an `unicode` string to a byte string `str`.

        Decode transforms a byte string `str` to an `unicode` string.
    """

    assert u'中'.encode('utf-8') == '\xE4\xB8\xAD'
    assert u'中' == '\xE4\xB8\xAD'.decode('utf-8')

    # Most escapes in str literals strings are also interpreted inside unicode strings.

    assert u'\n'.encode('ASCII') == '\n'

    # When mixing encodings implicily, ASCII is assumed by default,
    # so things break only if there are non-ASCII chars.
    # Don't do any of the following:

    assert u'a' == 'a'
    assert u'\u20AC' != '\x20\xAC'

    try:
        str(u'\u20AC')
    except UnicodeEncodeError:
        #'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
        pass
    else:
        raise

    try:
        assert u'\u20AC'.decode('utf-8')
    except UnicodeEncodeError:
        #'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
        pass
    else:
        raise

    try:
        unicode('\x20\xAC')
    except UnicodeDecodeError:
        #'ascii' codec can't decode byte 0xac in position 1: ordinal not in range(128)
        pass
    else:
        raise

    """
    ## Normalization

        Some unicode characters can be represented by multiple sequences.

        This is so for backwards compatibility with older encodings,
        and happens most often for accentuated versions of latin characters.

        unicode strings with different normalizations compare False.

        Normalization may be modified via `unicodedata`.
    """

    assert u'\u00EAtre' != u'e\u0302tre'

    import unicodedata
    assert unicodedata.normalize('NFC', u'\u00eatre') == unicodedata.normalize('NFC', u'e\u0302tre')

    """
    IO is typically done via arrays of bytes since that is how the system really sees it,
    and not via unicode chars.

    This includes operations like:

    - print
    - sys.stdout.write
    - file open + write

    There may be however some convenience wrappers that deal with encoding.
    For example, `codecs.open` opens a file in a encoding aware manner.
    """

    """
    ## Unicode and file IO

        First remember that `sys.stdout` is a file object,
        so terminal and file IO is much the same.

        Terminal output via `print` or `sys.stdout.write` always uses str byte strings.

        If given unicode, it first decodes via `sys.stdout.encoding`

        TODO how sys.stdout.encoding is determined
        TODO pipes affect `sys.stdout.encoding`?

        If print output goes to a pipe, `sys.stdout.encoding` is `None`,
        in which case `ASCII` conversion is attempted.
        If there are any non ASCII characters, this leads to an exception!
        Therefore, if it is ever possible that there could be unicode chars
        on the output string, encode it explicitly.
    """

    print 'sys.stdout.encoding = ' + str(sys.stdout.encoding)

    # BAD: will raise an exception if output to a pipe!

    #print u'中文'

    # GOOD:

    print u'中文'.encode('utf-8')
