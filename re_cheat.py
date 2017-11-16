#!/usr/bin/env python

"""
## re

## Regular expressions

Perl like.

General operation:

- *string regexes* must frist be compiled into *pattern* objects. This has some overhead.
- compiled pattern objects can be used to find *match objects* on test strings.

## Regex methods

    match() get match for **THE ENTIRE**!!!!!!! string
    search() first match anywhere in the string
    findall() iterator of matching *strings*, **NOT**!!! match objects
    finditer() iterator of match objects

## Predefined character classes

    - \d [0-9]
    - \D [^0-9]
    - \s [ \t\n\r\f\v]
    - \S
    - \w [a-zA-Z0-9_].
    - \W
"""

import re

if '## Syntax':

    if '## Lookahead':

        # Don't eat front part or regex

        p = re.compile(r'a.')
        assert p.sub('0', 'abaac') == '00c'

        p = re.compile(r'a(?=.)')
        assert p.sub('0', 'abaac') == '0b00c'

if '## re module':

    if '## compile':

        """
        Return a RegexObject object.

        Caches the regex parsing to make it faster.

        Always use this unless you will long match once.

        Contains basically the same methods as the `re` module.
        """

        p = re.compile(r'a.c')
        assert p.match('abc')

    if '## flags':

        """
        ##DOTALL: dot matches all characters, including newlines
        ##MULTILINE: ^ and $ also matches at newlines
        """

        assert re.match(r'a', 'A', re.IGNORECASE)

    if '## sub':

        # Replce what was matched.

        p = re.compile('(a.|b.)')

        # By string:

        assert p.sub('0', 'a_b_abc') == '000c'

        # By callable:

        assert p.sub(lambda m: m.group(1)[1:], 'a_b-abc') == '_-bc'

        # Count:

        assert p.sub('0', 'a_b_abc', count=1) == '0b_abc'

    if '## subn':

        # Same as sub, but also returns number of subs made:

        assert p.subn('0', 'a_b_abc') == ('000c', 3)

    if '## match':

        re.match(r'a.c', 'abc')

        assert re.match(r'a.c', 'abc')

        # Must match from beginning of string!
        # Consider re.search instead.
        # http://stackoverflow.com/questions/28840903/python-regex-match-middle-of-string

        assert re.match(r'a.c', '0abc') is None

        # Does not however have to match until the end:

        assert re.match(r'a.c', 'abc0')

    if '## search':

        """
        Like match, but also matches in the middle.
        """

        assert re.search(r'a.c', '0abc')
        # Works.

        assert re.search(r'a.c', 'abcaBc')
        # . == b, stops at first match. to find all matches, use finditer

        # Line start and end are still honoured.
        assert not re.search(r'^a', 'ba')

    if '## finditer':

        # A list of all non-overlapping match objects.

        matches = list(re.finditer(r'a.c', 'abcaBc'))

    if '## split':

        assert re.split(r'[ab]+', '0abba1aaaaa2') == ['0', '1', '2']

"""
## Match object

## MatchObject

https://docs.python.org/2/library/re.html#re.MatchObject

Impossible to access this class: http://stackoverflow.com/questions/4835352/how-to-subclass-the-matchobject-in-python ...

Important methods: TODO examples

    group() Return the string matched by the RE
    start() Return the starting position of the match
    end() Return the ending position of the match
    span() Return a tuple containing the (start, end) positions of the match
"""

"""
## RegexObject

Returned by compile.

https://docs.python.org/2/library/re.html#re.RegexObject
"""
