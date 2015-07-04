#!/usr/bin/env python

"""
## re

## Regular expressions

Perl like.

General operation:

- *string regexes* must frist be compiled into *pattern* objects. This has some overhead.
- compiled pattern objects can be used to find *match objects* on test strings.

##regex methods

        match() 	    get match for **THE ENTIRE**!!!!!!! string
        search() 	    first match anywhere in the string
        findall() 	    iterator of matching *strings*, **NOT**!!! match objects
        finditer() 	iterator of match objects

##match object methods

        group() 	Return the string matched by the RE
        start() 	Return the starting position of the match
        end() 	    Return the ending position of the match
        span() 	    Return a tuple containing the (start, end) positions of the match

##predefined character classes

    - \d [0-9]
    - \D [^0-9]
    - \s [ \t\n\r\f\v]
    - \S
    - \w [a-zA-Z0-9_].
    - \W
"""

import re

if '## Lookahead':

    # Don't eat front part or regex

    p = re.compile(r'a.')
    assert p.sub('0', 'abaac') == '00c'

    p = re.compile(r'a(?=.)')
    assert p.sub('0', 'abaac') == '0b00c'

if '## flags':

    """
    ##DOTALL: dot matches all characters, including newlines
    ##MULTILINE: ^ and $ also matches at \n
    """

    p = re.compile(r'a', re.IGNORECASE | re.DOTALL)

if '## sub':

    p = re.compile('(a.|b.)')

    # By string:

    assert p.sub('0', 'a_b_abc') == '000c'

    # By callable:

    assert p.sub(lambda m: m.group(1)[1:], 'a_b-abc') == '_-bc'

    # Count:

    assert p.sub('0', 'a_b_abc', count=1) == '0b_abc'

if '## subn':

    # Same as sub but also returns number of subs made:

    assert p.subn('0', 'a_b_abc') == ('000c', 3)

if '## match':

    #MUST MATCH FROM BEGINNING OF STRING!!!!!!

    re.match(r"a.c", "abc")

    r = re.compile(r"a.c")
    r.match("abc")
    #matches
    r.match("0abc")
    #DOES NOT MATCH!!!! MUST MATCH FROM BEGINNING OF STRING!!! use search for that

if '## search':

    r.search("0abc")
    #works

    r.search("abcaBc")
    #. == b, stops at first match. to find all matches, use finditer

if '## finditer':

    matches = list(r.finditer("abcaBc"))
    #a list of all matches

if '## split':

    re.split(r'[ab]+', '0abba1aaaaa2')
    #[0, 1, 2]

