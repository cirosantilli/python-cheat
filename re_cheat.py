#!/usr/bin/env python3

'''
https://docs.python.org/3/library/re.html
'''

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

        assert re.match('a', 'A', re.IGNORECASE)

        # Need flags= for re.sub, or set the count=
        # https://stackoverflow.com/questions/42581/python-re-sub-with-a-flag-does-not-replace-all-occurrences/42597#42597
        assert re.sub('^a', '0', 'ab\nab\n', flags=re.MULTILINE) == '0b\n0b\n'

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

        # search and group
        assert re.search(r'a(.)c(.)e', 'Xa0c1eYa2c3eZ').group(1) == ('0')
        assert re.search(r'a(.)c(.)e', 'Xa0c1eYa2c3eZ').group(2) == ('1')
        assert re.search(r'a(.)c(.)e', 'Xa0c1eYa2c3eZ').group(1, 2) == ('0', '1')

    if '## finditer':

        # A list of all non-overlapping match objects.

        matches = list(re.finditer(r'a.c', 'abcaBc'))

    if '## split':

        assert re.split(r'[ab]+', '0abba1aaaaa2') == ['0', '1', '2']

        # https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators
        assert re.split('(0|1)', 'a0bc1d0ef') == ['a', '0', 'bc', '1', 'd', '0', 'ef']

        # https://stackoverflow.com/questions/24443995/list-comprehension-joining-every-two-elements-together-in-a-list
        def split_and_keep(reg, string):
            lst = re.split(reg, string)
            if len(lst) % 2 == 1:
                lst.append('')
            for x, y in zip(lst[0::2], lst[1::2]):
                yield x + y
        assert list(split_and_keep('(0|1)', 'a0bc1d0ef')) == ['a0', 'bc1', 'd0', 'ef']

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
