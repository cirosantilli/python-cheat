#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cheat on the Python language and stdlibs.
"""

import sys
import shutil
import tempfile
import itertools

if "##whitespace":

    # Python forces certain indentations

    # Use backslash '\' for line continuation of long commands:

    assert \
    1+\
        1\
    == 2

    # Parenthesis also work:

    assert (
            1+
        1 ==
    2
    )

    if "##whitespace and functions":

        # Cannot separate `(` from function def:

            #def f
                #(x,y):
                #pass

        # Everything else works.

        # Good:

        def f(x,y):
            """
            docstrings must be indented
            """
            pass

        # My favorite format for lots of args:

        def f(
                x,
                y,
                z,
                w
            ):
            pass

        # Ugly but works:

        def f(
        x
                    ,y,
            z
            ):
            pass

        # Single line only

        def f(): pass

            #def f(): pass
                #pass

        def f(x,y):
            pass

        f(1,2)

        f(1,
        2)

        f(
        1,
        2
        )

        def f():
            g(
                    1,
        2
            )

        # Anything that has `:` like `if`, `while` and `class` works like function.

    if "##multiple commands on a single line":

        #http://stackoverflow.com/questions/6167127/how-to-put-multiple-statements-in-one-line

        # Only possible for multiple simple statements.

        i = 0; i += 1; assert i == 1

        # Only use this for bash one liners.

if "##built-in":

    '''
    Python has three kinds of built-ins:

    - functions
    - constants
    - types

    Built-ins add insanity to the language, but allow us to write much shorter
    and more readable code. It is the classical sanity / sugarness tradeoff of language design.

    Those built-ins are mostly just like user defined types except for some points.

    Notable differences include:

    - they do not need to be imported: they are always available on any scope.

    - some (but not all) built-in types have nice looking literals such as `1`, `[1]` or `{1: 2}`
        It is however be possible to create any type with a built-in factory function.

    - most built-in types are lower case words by convention, while classes usually start with Upper case.
    '''

    if "It is not possible to set attributes of built-in types.":

        class C: pass
        C.i = 1

        try:
            int.i = 1
        except TypeError:
            pass
        else:
            assert False

if "##built-in constants":

    '''
    Python has the following built-in constants:

    - True
    - False
    - None
    - ##NotImplemented

        Vs. `NotImplementedError` built-in exception:

        <http://stackoverflow.com/questions/878943/why-return-notimplemented-instead-of-raising-notimplementederror>

    - Ellipsis
    - __debug__

    Besides those, there are also builtin exception objects.
    '''

if "##built-in functions":

    if "##help":

        '''
        Intended for interactive usage documentation retrieval.

        If linked to a tty, opens the doc of the given object in a pager.

        Else, does nothing.
        '''

        def f():
            """doc"""
        #help(f)

    if "##locals":

        # TODO

        pass

    if "##globals":

        # TODO

        pass

if "##built-in types":

    '''
    <http://docs.python.org/3.3/reference/datamodel.html>

    Types which are already defined by the interpreter,
    and do not need to be imported from the stdlib.

    They may have special (non-class-like) literals like ints `1` and lists: `[1, 2]`.
    All have global function constructors like `list()` or `set()`,

    The built-in types can be classified based on which ABCs they implement.

    All the Python 2 built-in types are:

    - numbers: implement the `numbers.Number` ABC or its derived classes.

        All immutable.

        - integers: `numbers.Integral`

            - int
            - long
            - bool

            - real: `numbers.Real`

                - float

                - complex: `numbers.Complex`

                    - complex

    - sequences:

        It seems that in Python 2 there is not a fixed ABC for them.

        In Python 3 they implement `collections.abc.Sequence`. Much saner.

        - immutable:

            - str
            - unicode
            - tuple

        - mutable:

            - list
            - bytearray
            - memoryview

    - sets: in Python 3 they implement `collections.abc.Set`

        - set
        - frozenset

    - mappings:

        Only one

        - dict

    - super
    '''

    assert(type(int())      == type(0))
    assert(type(float())    == type(0.0))
    assert(type(long())     == type(0L))
    assert(type(complex())  == type(1j))

if "##bytearray":

    '''
    Mutable version of `str`.
    '''

    ba = bytearray(b'ab')
    ba2 = ba
    ba2[0] = ord(b'b')
    assert ba == bytearray(b'bb')

if "##numbers":

    # Defines an hierarchy on numbers. <http://docs.python.org/2/library/numbers.html>

    import numbers

    assert isinstance(0, numbers.Integral)
    assert isinstance(0, numbers.Rational)
    assert isinstance(0, numbers.Real)
    assert isinstance(0, numbers.Complex)
    assert not isinstance(1j, numbers.Real)

    if "##int ##long ##float":

        # int, float and long are classes.
        # It is just that `1` and `1.1` are nice looking literals.

        assert (1).__add__(1) == 2
        assert 1L.__add__(1L) == 2L
        assert 1.1.__add__(1.1) == 2.2

        # It is not possible to omit parenthesis because the lexer would treate
        # the `1.` as a float causing an ambiguity.

        #a = 1.__add__(1) # SyntaxError

        # A less readable alternative is to use a space:

        assert 1 .__add__(1) == 2

        # As any built-in class, they have global constructor functions:

        assert 1 == int(1)
        assert 1 == long(1L)
        assert 1.1 == float(1.1)

        # The constructors also support construction from any numeric type
        # or strings:

        assert 1 == int(1.5)
        assert 1.1 == float('1.1')

        # Each of them has a class with the same name:

        class myint(int):
            pass

        assert myint(1) + myint(2) == myint(3)

    if "##imaginary ##complex":

        '''
        Imaginary numbers have built-in literals of the form `Nj`.
        '''

        assert 1j * 1j == -1

        assert 1 + 2j == complex(1, 2)

        j = 2
        assert 1j * 1j == -1
        assert j * j   == 4

        assert 1j * 1j == -1
        assert (1 + 2j).real == 1
        assert (1 + 2j).imag == 2
        assert 1j.conjugate() == -1j

if "##list":

    # List of any mix of types.

    if "##create new list":

        # List have literals:

        l = [1, 2, "a", "b"]

        # List have a global factory method that takes an iterable.
        # Therefore they can be built from anything that is iterable:

        # From tuples:

        assert list((1, 2)) == [1, 2]

        # From iterators:

        assert list(xrange(0, 3)) == [0, 1, 2]

        if "##range":

            # Creates lists directly:

            assert range(3) == [0, 1, 2]
            assert range(1, 3) == [1, 2]
            assert range(1, 6, 2) == [1, 3, 5]

        if "##list comprehention":

            assert [i for i in xrange(4) if i != 2] == [0, 1, 3]

            # Multilevel / nested: TODO parenthise this to understand it better.

            assert [i for j in [1, 2] for i in [j,-j]] == [1, -1, 2, -2]

        if "##map method":

            assert map(lambda i: 2 * i, xrange(3)) == [0, 2, 4]

        if "##+ for lists":

            l = range(2)
            assert l + [2, 3] == [0, 1, 2, 3]
            assert l == range(2)

        if "##slice":

            l = range(4)
            assert l[:2]  == [0, 1]
            assert l[2:]  == [2, 3]
            assert l[:-2] == [0, 1]
            assert l[-2:] == [2, 3]

            l = range(5)
            assert l[::2]   == [0, 2, 4]
            assert l[:3:2]  == [0, 2]
            assert l[2::2]  == [2, 4]
            assert l[0:3:2] == [0, 2]
            assert l[::-1]  == [4,3,2,1,0] #invert list!

            if "##ellipsis #...":

                '''
                TODO
                '''

        if "##sorted":

            l = [2, 1]
            assert sorted(l) == [1, 2]
            assert l == [2, 1]

        if "##remove dupes":

            assert list(set([1, 2, 1])) == [1, 2]

    if "##modify inplace":

        l = range(3)
        l[0] = 10
        assert l == [10, 1, 2]

        l = range(3)
        assert l.append(3) == None
        assert l == [0, 1, 2, 3]

        l = range(3)
        assert l.extend([3, 4]) == None
        assert l == [0, 1, 2, 3, 4]

        l = range(3)
        assert l.insert(0, 3) == None
        assert l == [3, 0, 1, 2]

        if "##pop":

            l = range(3)
            assert l.pop(1) == 1
            assert l == [0, 2]

            l = range(3)
            assert l.pop() == 2
            assert l == [0, 1]

        if "##remove":

            # Remove first occurence of value.

            l = [0, 1, 0]
            assert l.remove(0) == None
            assert l == [1, 0]

            # If not present, exception:

            l = [0, 1]
            try:
                l.remove(2)
            except ValueError:
                pass
            else:
                assert False

        if "##del":

            '''
            Remove element from list.

            Is a statement.

            You *cannot* get a return value from it:

                a = del l[0]

            Rather insane: why is this not a list method? Why a language *statement*?
            I'd rather use `pop(i)`.
            '''

            l = range(3)
            del l[1]
            assert l == [0, 2]

        if "##sort":

            l = [2, 1, 3]
            assert l.sort() == None
            assert l == [1, 2, 3]
            assert None == l.sort(reverse=True)
            assert l == [3, 2, 1]

    if "##items are references, not copies":

        l0 = range(3)
        l1 = [l0]
        l1[0][0] = 1
        assert l0 == [1, 1, 2]

    if "##access":

        l = [0, 1, 2]
        assert l[0] == 0
        assert l[1] == 1
        assert l[2] == 2

        assert l[-1] == 2
        assert l[-2] == 1

        if "##out of bounds":

            l = [0, 1]
            try:
                l[3]
            except IndexError:
                pass
            else:
                assert False

            # Use default value if out of bounds:

            l = range(3)
            i = 1
            assert l[i] if i < len(l) else "default" == 1
            i = 3
            assert l[i] if i < len(l) else "default" == "default"

    if "##concatenate ##cat":

        assert [0, 2] + [1, 3] == [0, 2, 1, 3]

    if "##find item":

        # First match for criteria with generator expression:

        assert next(pair for pair in [(1, 1), (2, 1), (2, 2)] if pair[0] == 2) == (2, 1)

        # Uses the given default if not found:

        assert next((pair for pair in [(1, 1), (2, 1), (2, 2)] if pair[0] == 3), None) == None

        # If no default, exception:

        try:
            next(pair for pair in [(1, 1), (2, 1), (2, 1)] if pair[0] == 3) == (2, 1)
        except StopIteration:
            pass
        else:
            assert False

    if "##filter":

        # Leave only elements for which a function is True.

        l = range(4)
        assert filter(lambda x: x % 2 == 1, l) == [1, 3]
        assert l == range(4)

        ##itertools.ifilter for iterators.

if "##iterators ##yield":

    '''
    Iterators are more memory efficent for iterations than lists
    since there is no need to store the entire sequence!

    However, if you must calculate each new item, so more time expensive if
    you are going to use it more than once

    It is a classic space/time tradeoff.
    '''

    if "##create":

        # An iterator is just a function with a `yield` method:

        def count():
            """this is already built-in"""
            i = 0
            yield i
            i = i+1

        # Raise exception when over:

            def myxrange(n):
                i = 0
                yield i
                i = i+1
                if i > n:
                    raise StopIteration

        if "##generator expressions":

            # Shorthand way to create iterators

            it = (i for i in xrange(10))
            for i in it:
                print i

            # Parenthesis can be ommited for single argument func call:

            def mysum(vals):
                total = 0
                for val in vals:
                    total += val
                return total

            assert mysum(i for i in [0, 2, 5]) == 7

        if "##iter":

            # Converts various types to iterators.

            iter("abc")
            iter([1, 2, 3])

    if "##next":

        # Will not work with `xrange`! <http://late.am/post/2012/06/18/what-the-heck-is-an-xrange>

        #next(xrange(1))

        i = iter(xrange(2))
        assert next(i) == 0
        assert i.next() == 1
        try:
            next(i)
        except StopIteration:
            pass
        else:
            assert False

        # Use default value if over:

        it = iter(xrange(1))
        assert next(it) == 0
        assert next(it, 3) == 3
        assert next(it, 3) == 3

        # There is no has_next method.
        # The only way is to catch the `StopIteration` exception:
        # <http://stackoverflow.com/questions/1966591/hasnext-in-python-iterators>

    if "##iterators can't be rewinded":

        # Either store a list on memory or recalculate.

        # Recalculate:

        it = iter("asdf")
        for i in it:
            print "first"
            print i
        it = iter("asdf")
        for i in it:
            print "second"
            print i

        # Store on memory:

        it = list(iter("asdf"))
        for i in it:
            print "first"
            print i
        for i in it:
            print "second"
            print i

    if "built-in iterator functions":

        if "##enumerate":

            assert list(enumerate(['a', 'c', 'b']) ) == [(0, 'a'), (1, 'c'), (2, 'b'), ]

        if "##reduce":

            '''
            - take two leftmost, apply func
            - replace the two leftmost by the result
            - loop

            On the example below:

            - 2*3 - 1 = 5
            - 2*5 - 3 = 8
            '''

            assert reduce(lambda x, y: 2*x - y, [3, 1, 2]) == 8

    if "###itertools":

        import itertools

        '''
        Hardcore iterator patterns.
        <http://docs.python.org/2/library/itertools.html#recipes>

        Most important ones:

        - imap: map for iterators
        - izip: count to infinity
        - count: count to infinity
        '''

        # Cartesian product:

        for i, j in itertools.product(xrange(3), xrange(3)):
            print i, j

        # Join two iterators:

        assert [i for i in itertools.chain(xrange(2), xrange(2))] == [0, 1, 0, 1]

    if "##iterable combos":

        if "Merge two lists of same length odd / even elements":

            # http://stackoverflow.com/questions/18041840/python-merge-two-lists-even-odd-elements

            # Same length:

            x = [0, 1]
            y = [2, 3]
            assert [ x for t in zip(x,y) for x in t ] == [0, 2, 1, 3]

if "##string ##str":

    '''
    There are 2 commonly used classes which are informaly called *strings* in python:
    *str* and *unicode*

    *basestring* is their common ancestor.
    '''

    assert isinstance(str(), basestring)
    assert isinstance(unicode(), basestring)
    assert not isinstance(bytearray(), basestring)

    if "##literals":

        if "###single vs double quotes":

            # There is no semantical difference:

            assert "abc" == 'abc'

            # Except for excaping quotes themselves:

            assert "'" == '\''
            assert '"' == "\""

            # By convention, `'` is more used for identifiers (say, map keys)
            # while `"` is more used for messages: `print "Hello world!"`.

        if "##multiline strings ##triple quotes":

            # Like in C, whitespace separated strings are glued together:

            assert "ab" "cd" == "abcd"

            # This means that backslash continuation joins strings without newlines:

            assert \
                'ab' \
                'cd' == 'abcd'

            assert """a
b""" == "a\nb"

            assert '''a
b''' == "a\nb"

            # Spaces are kept:

            assert '''a
 b''' == "a\n b"

            def f():
                assert """a
b""" == "a\nb"
            f()

        # Backslash escapes are like in C.

        assert "\x61" == "a"
        assert "\n" == "\x0A"

        if "##raw string literals ##r literals":

            # Raw literals lose all backslash escape magic.

            assert r"\n" == "\\n"
            assert r"\\" == "\\\\"

            # The exception is to escape the character that would terminate the string (`'` or `"`).
            # In that case, the backslash *remains* in the string:

            assert r"\"" == "\\\""

            # A consequence is that it is impossible to write a raw string literal that ends in backslash.

            assert "\\" != r""

            '''
            Raw string literals are often used with regular expressions,
            which often contain many literal backslashes.
            '''

    if "##format strings ##precision ##decimal places":

        '''
        Mostly like C printf.

        There are two forms: tuple or dict.

        Single value form: only works for a single input.
        '''

        assert "%d" % 1 == "1"

        try:
            assert "%d %d" % 1, 2 == "1 2"
        except TypeError:
            pass
        else:
            assert False

        # Tuple form: works for any number of arguments.

        assert "%d"     % ( 1 )         == "1"
        assert "%d %d"  % ( 1, 2 )      == "1 2"
        assert "%.2f"   % ( 1.2 )       == "1.20"
        assert "%5.2f"  % ( 1.2 )       == " 1.20"
        assert "%s"     % ( "abc" )     == "abc"

        # Map form:

        assert "%(v1)s %(#)03d %(v1)s %(#)03d" % {'v1':"asdf", "#":2} == 'asdf 002 asdf 002'

        if "##python3 format":

            '''
            The percent format operator becomes deprecated in Python 3.1,

            The `format` method is introduced and backported to Python 2,

            On one hand, this is saner since we now have a method instead of a magic operator `%`.

            On the other, C printf format strings are gone, and that is a shame.
            Yet another format syntax to learn.

            <http://www.python.org/dev/peps/pep-3101/>

            Only operators `[]` and `.` are supported inside the formats.
            '''

            assert '{1} {0} {1} {2[0]} {a}'.format(0, 1, [0, 1], a=2 ) == '1 0 1 0 2'

            # Escape, literals:

            assert '{{}}{{a}}'.format(0) == '{}{a}'

            assert '{} {}'.format(0, 1) == '0 1'

            # Cannot use both automatic numbering and numbered references:

            try:
                '{} {0}'.format(0)
            except ValueError:
                pass
            else:
                assert False

            # Does not work like in Ruby where strings are magic: only the format method interprets anything.

            a = 2
            assert "{a}" != "2"

            # Format is of the form:

            #{<id>:<format-string>}

            # It is C printf like, but **NOT** the same!

            # Fill:

            assert '{:2d}'.format(1)    == " 1"
            assert '{:02d}'.format(1)   == "01"

            # Align left:

            assert '{:<2d}'.format(1)   == "1 "

            # Decimal places:

            assert '{:.2f}'.format(1.0)    == "1.00"
            assert '{0:.2f}'.format(1.0)   == "1.00"
            assert '{x:.2f}'.format(x=1.0) == "1.00"

            # Format via an argument combo:

            assert '{0:.{1}f}'.format(1.23456, 4) == "1.2346"
            assert '{number:.{digits}f}'.format(number=1.23456, digits=4) == "1.2346"

            if "##table printing":

                # There seems to be no built-in one liner.

                # Two rows built-in solution:

                print "Label value table combo:"
                labels = ["label 0", "very long label 1", "l 2"]
                values = [0, 1, 2]
                sys.stdout.write("{:<{l}}{}\n{:<{l}}{}\n{:<{l}}{}\n".format(
                    *[x for t in zip(labels,values) for x in t],
                    l=len(max(labels, key=len)) + 2
                ))

                # Output:

                #label 0            0
                #very long label 1  1
                #l 2                2

                # Many solutions with external libraries since Python is so scientific based:
                # - http://stackoverflow.com/questions/9535954/python-printing-lists-as-tabular-data
                # - http://stackoverflow.com/questions/17279059/print-list-in-table-format-in-python

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

    ##cat

    assert "ab" + "cd" == "abcd"

    #implicit: only works for strings

    assert "ab" "cd" == "abcd"
    assert "ab" * 3 == "ababab"

    # replace: replaces at most once:

    assert "aabbcc".replace("b", "0")   == "aa00cc"
    assert "aabbcc".replace("bb", "0")  == "aa0cc"
    assert "aabbcc".replace("b", "0", 1) == "aa0bcc"

    if "##string import":

        import string

        if "##constants":

            print "string.whitespace = " + string.whitespace.encode('string-escape')

    if "#split":

        # Split string into array of strings:

        assert "0ab1ab2".split("ab") == ['0', '1', '2']
        assert "0abab2".split("ab")  == ['0', '', '2']

        # If string not given, splits at `string.whitespace*` **regex**!:
        # Very confusing default that changes behaviour completely!

        assert "0 1\t \n2".split() == ['0', '1', '2']

        # Split at ``[\n\r]+`` regex:

        assert "0\n1\r2\r\n3".splitlines()  == ['0', '1', '2', '3']

    if "##strip ##rstrip ##lstrip":

        '''
        Strip chars either from either beginning or end, *not* middle!

        Characters to strip are given on a string.

        Default argument: `string.whitespace`

        r and l strip for one sided versions.
        '''

        assert "cbaba0a1b2ccba".strip("abc") == "0a1b2"
        assert "\t\n0 1 2\v \r".strip() == "0 1 2"

    if "##startswith":

        assert "abc".startswith("ab") == True
        assert "abc".startswith("bc") == False

        # Remove prefix: <http://stackoverflow.com/questions/599953/python-how-to-remove-the-left-part-of-a-string>

        # If sure that the prefix is there:

        prefix = "ab"
        assert "abcd"[len(prefix):] == "cd"

        # Otherwise:

        prefix = "ab"
        s = "abcd"
        if s.startswith(prefix):
            assert s[len(prefix):] == "cd"

    if "##contains substring":
        assert "bc" in "abcd"
        assert "bc" not in "abdc"
        # The empty string is contained in all others:
        assert "" in ""
        assert "" in "a"

    # String to number:

    assert int("123") == 123
    assert float("12.34e56") == 12.34e56

    # Char to int:

    assert ord('a') == 97

    # Encode:

    assert '\n'.encode('string-escape') == '\\n'

    if "##unicode ##encodings":

        '''
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
        '''

        '''
        To be able to use utf8 directly in Python source.
        The second line of the file *must* be:

            -*- coding: utf-8 -*-

        Otherwise, you must use escape characters.

        This changes in Python 3 where utf-8 becomes the default encoding.
        '''

        if "##u backslash escapes ##unicode literals":

            '''
            Unicode literals are just like string literals, but they start with `u`.

            The string below has 2 characters. Characters are treated differently depending on
            if strings are str or unicode.
            '''

            u = u'\u4E2D\u6587'
            assert u[0] == u'\u4E2D'
            assert u[1] == u'\u6587'

            '''
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

                It is very rare to have to use `\UAAAAAAAA`, since characters in that region
                map mostly to languages with very small number of speakers (or none for ancient languages)<
                and most computers don't even have fonts to render those characters.

            Remember: `\` escapes are interpreted inside multiline comment strings.
            Therefore, if you write an invalid escape like `\\xYY`, your code will not run!
            '''

            assert u'\u4E2D\u6587' == u'中文'
            assert u'\U00010000' == u'𐀀'

            '''
            A is done to confirm that a byte is a known unicode character.
            For example `\UAAAAAAAA` does not currently represent any Unicode character,
            so you cannot use it.
            '''

            #u'\UAAAAAAAA'

            #Unicode \u escapes are only interpreted inside unicode string literals.

            s = '\u4E2D\u6587'
            assert s[0] == '\\'
            assert s[1] == 'u'
            assert s[2] == '4'

        '''
        ##encode ##decode

            Encode transforms an `unicode` string to a byte string `str`.

            Decode transforms a byte string `str` to an `unicode` string.
        '''

        assert u'中'.encode('utf-8') == '\xE4\xB8\xAD'
        assert u'中' == '\xE4\xB8\xAD'.decode('utf-8')

        # Most escapes in str literals strings are also interpreted inside unicode strings.

        assert u'\n'.encode('ASCII') == '\n'

        # When mixing encodings implicily, ASCII is assumed by default, so things break only if there are non-ASCII chars.
        # Don't do any of the following:

        assert u"a" == "a"
        assert u"\u20AC" != "\x20\xAC"
        assert u"\u20AC" + "a" == u"\u20ACa"
        try:
            str(u"\u20AC")
        except UnicodeEncodeError:
            #'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
            pass
        else:
            raise
        try:
            unicode("\x20\xAC")
        except UnicodeDecodeError:
            #'ascii' codec can't decode byte 0xac in position 1: ordinal not in range(128)
            pass
        else:
            raise

        '''
        ##normalization

            Some unicode characters can be represented by multiple sequences.

            This is so for backwards compatibility with older encodings,
            and happens most often for accentuated versions of latin characters.

            unicode strings with different normalizations compare False.

            Normalization may be modified via `unicodedata`.
        '''

        assert u'\u00EAtre' != u'e\u0302tre'

        import unicodedata
        assert unicodedata.normalize('NFC', u'\u00eatre') == unicodedata.normalize('NFC', u'e\u0302tre')

        '''
        IO is typically done via arrays of bytes since that is how the system really sees it,
        and not via unicode chars.

        This includes operations like:

        - print
        - sys.stdout.write
        - file open + write

        There may be however some convenience wrappers that deal with encoding.
        For example, `codecs.open` opens a file in a encoding aware manner.
        '''

        '''
        ##unicode and file IO

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
        '''

        print 'sys.stdout.encoding = ' + str(sys.stdout.encoding)

        # BAD: will raise an exception if output to a pipe!

        #print u'中文'

        # GOOD:

        print u'中文'.encode('utf-8')

if "##tuple":

    # Immutable list of elements of any type

    # Special constructor notation:

    t = (1, 2, 3)

    # Global factory method from list:

    assert tuple([1, 2, 3]) == (1, 2, 3)

    # Doest not exist:

        #t = tuple(1, 2, 3)

    t2 = (4, 5, 6)
    t3 = (4, 5, 1)
    tb = (False, False, True)
    tm = (1, 1.1, True, "asdf")

    # Index access:

    t = (1, 2, 3)
    assert t[0] == 1
    assert t[1] == 2
    assert t[2] == 3

    # Unpack:

    a, b, c = (1, 2, 3)
    assert a == 1
    assert b == 2
    assert c == 3

    if "tuples are immutable":

        t = (0)
        try:
            t[0] = "a"
        except TypeError:
            pass
        else:
            assert False

    # Concatenate:

    assert (0, 1) + (2, 3) == (0, 1, 2, 3)

    t = (0, 1)
    assert t * 2  == (0, 1, 0, 1)
    assert 2 * t  == (0, 1, 0, 1)

    # Compare: does alphabetical like compare from left to right.

    assert (0, 1)  == (0, 1)
    assert (0, 1)  < (1, 2)
    assert (0, 10) < (1, 1)
    # TODO why:
    #assert (0, 1)  > (1)

    # The list global functions also work on tuples:

    assert len((0,1)) == 2
    assert max((0,1)) == 1
    assert min((0,1)) == 0
    assert any((True, False)) == True
    assert all((True, False)) == False

if "##memoryview":

    '''
    TODO
    '''

##map

    # See dict.

if "##dict":

    # Unordered map of hashable keys and to values of any type.

    if "##create":

        # Built-in constructor syntax:

        d = {1: 'a', 'b': 2, 1.1: 2}

        # Global factory function.

        # From list of pairs:

        assert dict([(0, 'zero'), (1, 'one')]) == {0: 'zero', 1: 'one'}

        # From kwargs (keys can only be strings):

        assert dict(zero=0, one=1) == {'zero': 0, 'one': 1}

        # Dict comprehension:

        assert {key: value for (key, value) in [(1, 2), (3, 4)]} == {1: 2, 3: 4}

        # Keys must be hashable. This excludes all mutable built-in types like lists.

        try:
            d = {[1]: 2}
        except TypeError:
            pass
        else:
            assert False

    # To list of pairs:

    d = {1: 'one', 2: 'two'}
    assert set(d.items()) == set([(1, 'one'), (2, 'two')])

    # Get list of keys (undefined order)

    d = {1: 'one', 2: 'two'}
    assert set(d.keys()) == set([1, 2])

    # To string:

    print "dict str() = "
    print d

    # Undefined output because undefined key order.

    # Get value of key:

    d = {1: 'one', 2: 'two'}
    assert d[1] == 'one'

    # If not in dict, `KeyError` exception:

    d = {}
    try:
        d['not-a-key']
    except KeyError:
        pass
    else:
        assert False

    # Check if key is in dict:

    d = {1: 2}

    if 1 in d:
        pass
    else:
        assert False

    if 2 in d:
        assert False

    # Get default value if not present:

    assert d.get('not-a-key', 'default value') == 'default value'

    # Add new pair:

    d= {}
    d[0] = 'zero'
    assert d == {0: 'zero'}

    # Remove pair:

    d= {0: 'zero'}
    del d[0]

    # If key not present, KeyError:

    try:
        del d[0]
    except KeyError:
        pass
    else:
        assert False

    # Add new pair if key not present:

    d = {1: 2}
    assert d.setdefault(1, 3) == 2
    assert d == {1: 2}

    d = {}
    assert d.setdefault(1, 3) == 3
    assert d == {1: 3}

    if "##update":

        # Add update all keys on d0 with those of d1:

        d0 = {0: 'zero', 1: 'one'}
        d1 = {0: 'zero2', 2: 'two'}
        d0.update(d1)
        assert d0 == {0: 'zero2', 1: 'one', 2: 'two'}

        # Create a new dict that is the union of two other dicts:

        d0 = {0: 'zero', 1: 'one'}
        d1 = {0: 'zero2', 2: 'two'}
        d01 = d0.copy()
        d01.update(d1)
        assert d01 == {0: 'zero2', 1: 'one', 2: 'two'}

    if "Iterate / loop over dict":

        # Unspecified order. Python 3 has `collections.OrderedDict`.

        # Keys only:

        assert sorted([i for i in {1:-1, 2:-2}]) == [1, 2]

        # Keys value pairs ##iteritems:

        assert sorted([(i,j) for i,j in {1:-1, 2:-2}.iteritems()]) == [(1, -1), (2, -2)]

        # Iteritems sorted by key. Must pull all into memory first.

        assert [(i,j) for i,j in sorted({2:-2, 1:-1}.iteritems())] == [(1, -1), (2, -2)]

        # Iteritems is out of Python3. Items is present in both 2 and 3 but returns a list, not an iterator.
        # 2to3 converts it automatically.

if "##set":

    '''
    Unordered set of unique elements.

    Quick method ref:

    - len(s) 	  	                    cardinality of set s
    - x in s 	  	                    test x for membership in s
    - x not in s 	  	                test x for non-membership in s
    - s.issubset(t) 	                s <= t 	test whether every element in s is in t
    - s.issuperset(t) 	                s >= t 	test whether every element in t is in s
    - s.union(t) 	                    s | t 	new set with elements from both s and t
    - s.intersection(t) 	            s & t 	new set with elements common to s and t
    - s.difference(t) 	                s - t 	new set with elements in s but not in t
    - s.symmetric_difference(t) 	    s ^ t 	new set with elements in either s or t but not both
    - s.copy() 	  	                    new set with a shallow copy of s
    - s.update(t) 	                    s |= t 	return set s with elements added from t
    - s.intersection_update(t) 	        s &= t 	return set s keeping only elements also found in t
    - s.difference_update(t) 	        s -= t 	return set s after removing elements found in t
    - s.symmetric_difference_update(t)	s ^= t 	return set s with elements from s or t but not both
    - s.add(x) 	  	                    add element x to set s
    - s.remove(x) 	  	                remove x from set s; raises KeyError if not present
    - s.discard(x) 	  	                removes x from set s if present
    - s.pop() 	  	                    remove and return an arbitrary element from s; raises KeyError if empty
    - s.clear() 	  	                remove all elements from set s
    '''

    # Literals:

    assert {0, 1} == set([0, 1])

    # List *without* order of unique elements:

    assert {2, 1} == {1, 2}

    # Iteration order undefined.

    # Factory built-in method: takes any iteratorable.

    assert set([1, 2]) == set((1, 2))

    # Add new element:

    s = {1, 2}
    assert s.add(3) == None
    assert s == {1, 2, 3}

    # If already present, do nothing:

    s.add(2)
    assert s == {1, 2, 3}

    # Remove an element:

    s = {1, 2}
    assert s.remove(2) == None
    assert s == {1}

    # If not present, raises `KeyError`:

    try:
        s.remove(2)
    except KeyError:
        pass
    else:
        assert False

    # Elements must implement `__hash__`. This *excludes* any mutable built-in type.

    s = set()
    try:
        s.add([1])
    except TypeError:
        pass
    else:
        assert False

if "##frozenset":

    '''
    Immutable version of set.

    As a consequence, it is hashable.
    '''

    fs = frozenset([0, 1])
    try:
        fs.add(2)
    except AttributeError:
        pass
    else:
        assert False

    assert fs == set([0, 1])

if "##operator":

    '''
    In python everything is an object.

    Therefore, every operator has a correponding method.

    In Python, methods that can become operators are prefixed and suffixed by `__`.

    For example:

    - `==` and `__eq__()`
    - `+` and `__add__()`
    - `**` and `__pow__()`
    - `//` and `__TODO__()`

    Built-in classes like `int` simply implement those methods.
    '''

    assert 0 == 0

    assert 2 * 3 == 6

    # C like division arithmetic:

    assert 1 / 2        == 0
    assert 1 / 2.0      == 0.5
    assert 1 / float(2) == 0.5

    # Floor division:

    assert 9.0 // 2.0 == 4

    # pow:

    assert 2 ** 3

    if "##boolean operator":

        assert not True         == False
        assert True and False   == False
        assert True or  False   == True

if "##branching":

    if "##if":

        if False:
            assert False
        elif False:
            assert False
        else:
            pass

        if "##multiline condition":

            # Multiline conditions must have parenthesis:

            if (a
                and b
                and c
                and d):
                pass

        if "##single line":

            # Behaves like the C question mark `?` operator.

            # Must have the else part:

            a = 1 if True  else 2
            assert a == 1
            a = 1 if False else 2
            assert a == 2

    if "##is":

        # `is` is stricter than `==`, as it also checks type.

        assert 1 == True
        assert not 1 is True

        assert 0 == False
        assert not 0 is False

        assert not None == False
        assert not None is False

        assert not "" == False
        assert not "" is False
        assert not "" == None

        assert not [] == False
        assert not [] is False

    if "##truth value testing for objects":

        '''
        Any object can be used on an if or while.

        In Python 2, an object evaluates to false iff:

        - it implements `__nonzero__` and `__nonzero__()` if False.
        - else if it impements `__len__`, and `__len__() == 0`

        Any other object evaluates to True.

        For the built-in types, the only the following are test False:

        - None
        - False
        - zero of any numeric type, for example, 0, 0L, 0.0, 0j.
        - any empty sequence, for example, '', (), [], set().
        - any empty mapping, for example, {}.
        '''

        if "":
            assert False

        if " ":
            pass
        else:
            assert False

        if []:
            assert False

        if [False]:
            pass
        else:
            assert False

        if None:
            assert False

        '''
        Truth value testing can differ from `__eq__` to True or false!

        Something that is not equal to True can still works for an if!
        '''

        assert -1 != True

        if -1:
            pass
        else:
            assert False

    if "##while":

        i = 0
        while i < 10:
            print i
            i += 1

        i = 0
        while i < 10:
            print i
            if i == 5:
                break
            i += 1

        i = 0
        while i < 10:
            print i
            i += 1
            if i == 5:
                continue

    if "##for":

        for i in [1, 3, 2]:
            print i

        for i in [1, 3, 2]:
            print i
            if i == 3:
                break

        for i in [1, 3, 2]:
            print i
            if i == 3:
                continue

    if "##and ##or":

        """
        And and or are actually branching instructions:
        analogous to ``&&`` and ``||`` in bash.

        - and evaluates the first expression. If False return it, if true return the second.
        - or evaluates the first expression. If True return it, if false return the second one.
        """

        assert (True  and 1) == 1
        assert (False and 1) == False

        assert (True  or 1) == True
        assert (False or 1) == 1

if "##function":

    if "##arguments":

        def f(a, b = 0, *args, **kwargs):
            """
            args is a tuple
            kwargs a dicdt

            those names are just a convention,
            any name can be used, ex:

                def g(*myArgs, **myEtraKwargs)
            """

            #args is a tuple.
            for arg in list(args):
                pass
            #you can iterate over it.

            #this is a standard way to give default values:
            kw1 = kwargs.get(1, "default1")
            kw2 = kwargs.get(2, "default2")
            kw2 = kwargs.get(3, "default3")

            return a, b, list(args), kwargs

        #ERROR:  argument a vas no value

            #f()

        assert f(1)                             == (1, 0, []   ,    {}              )
        assert f(1, 2)                          == (1, 2, []   ,    {}              )

        assert f(1, 2, 3)                       == (1, 2, [3],      {}              )
        assert f(1, 2, 3, 4)                    == (1, 2, [3, 4],   {}              )

        assert f(1, 2, 3, 4,    c=5, d=6)       == (1, 2, [3, 4],   {'c':5, 'd':6}  )
        assert f(1, 2,          c=5, d=6)       == (1, 2, [],       {'c':5, 'd':6}  )

        # If a named parameter exists already, it does not go into kwargs:

        assert f(a = 1)                 == (1, 0, [], {} )
        assert f(a = 1, b = 2)          == (1, 2, [], {} )
        assert f(b = 2, a = 1)          == (1, 2, [], {} )
        assert f(a = 1, b = 2, c = 5)   == (1, 2, [], {'c':5} )

        if "##unpack argument lists":

            # Transform list or dictionnaries into function arguments.

            assert f(*[0, 1]) == (0, 1, [], {})
            assert f(0, 1, *[2, 3]) == (0, 1, [2, 3], {})

            # Part of them may be named arguments, part may be *args.

            assert f(0, *[1, 2, 3]) == (0, 1, [2, 3], {})

            # ERROR: only named arguments may follow unpacked list

            assert f(0, 1, *[2, 3], c=4) == (0, 1, [2, 3], {'c':4})
            #assert f(0, 1, *[2, 3], 4) == (0, 1, [2, 3, 4], {})

            # Also possible with dictionnaries:

            assert f(1, 2, 3, 4, **{'c': 5, 'd': 6})    == (1, 2, [3, 4],   {'c': 5, 'd': 6}  )
            assert f(1, 2,       **{'c': 5, 'd': 6})    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # Can combine dict unpack with named arguments:

            assert f(1, 2,       d=6, **{'c': 5}   )    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # ERROR: dict unpack must be the last thing:

                #assert f(1, 2,       **{'c': 5}, d=6   )    == (1, 2, [],       {'c': 5, 'd': 6}  )

            # Can use list unpack with dict unpack:

            assert f(1, *[2, 3, 4], d=6, **{'c': 5}) == (1, 2, [3, 4],   {'c': 5, 'd': 6}  )

        # ERROR: multiple values for `a`:

            #f(1, a = 1)

        # ERROR: can only pass dictionnaries if there is a kwargs

        #def g(a): pass
        #g(a = 1)

        # OK: we have kwargs:

        def g(a, **kwargs): pass
        g(a = 1)

        # ERROR: cannot change the order of normal args, *args and **kwargs:

        #def f(*args, a): pass
        #def f(**kwargs, a): pass
        #def f(**kwargs, *args): pass

        # ERROR: cannot use integer (5) as keyword for kwargs: must use strings

            #f(1, 2, *[3, 4], **{5:6})

        if "##overload":

            """there is no function overloading in python"""

            def f(a):
                """
                completely destroys last existing f
                """
                return a

            def f(a, b):
                return a + b

            "too many args:"

            #f(1, 2, 3)

        if "default values for lots of kwargs":

            # If you have default values to a large number of them kwargs
            # this is a good way, which saves you from writting lots of ``gets``

            def f( **non_default_kwargs ):

                kwargs = {
                    'a':1,
                    'b':2,
                }
                kwargs.update( non_default_kwargs )

                f2( **kwargs )

        if "variables can contain functions":

            def f(x):
                return x + 1
            g = f
            assert g(0) == 1

        if "##immutable types #mutable types":

            """
            Literals like `1` and `1.1` are objects.

            Immutable type: there is no way (function, member, etc.) to modify the object itself.
            It is only possible to point to a different object of the same type.

            For all standard types, doing `a = b` always makes a point to a different thing,
            and does not change what `a` was pointing to.

            For other operators this may vary: `a += 1` may change what `a` points to, or the object pointed to
            depending on the type.

            Immutable types include:

            - numeric types like integers and floats
            - strings
            - tuples

            Mutable types include:

            - lists
            - dictionnaries
            """

            if "immutable:":

                x = 1
                assert id(x) == id(1)

                y = x
                assert id(x) == id(y)

                y = 2
                assert x == 1
                assert id(y) == id(2)

                # Unlike `=`, for immutable types `x += 1` makes `x` point to another address.
                x = 1
                x += 1
                assert id(x) == id(2)

                def f(y):
                    # Same as y = x
                    y += 1
                x = 1
                f(x)
                assert x == 1

            if "mutable:":

                x = [1]
                assert id(x) != id([1])
                assert x == [1]

                x = [1]
                y = x
                assert id(y) == id(x)

                x = [1]
                y = x
                assert id(y) == id(x)

                y[0] = 2
                assert x == [2]
                assert id(x) == id(y)

                # For mutable types, `+=` may change the actuabl object, not just the address to which `y` points to.
                y += [3]
                assert id(x) == id(y)
                assert x == [2, 3]

                # Doing `y = ` however does change the address pointed to.
                y = [0]
                assert id(x) != id(y)

                def f(y):
                    y[0] = 2
                x = [1]
                f(x)
                assert x == [2]

            '''
            Immutable built-in types all implement `__hash__`. Mutable built-in types are not.
            User defined types are all hashable.
            '''

            s = set()
            s.add(1) # OK: hashable.
            try:
                s.add([1]) # KO: not hashable
            except TypeError:
                pass
            else:
                assert False

            '''
            list constructor does shallow copies.
            '''

            x = [0, [10]]
            y = list(x) # or x[:]
            y[0] = 1
            y[1][0] = 11
            assert x == [0, [11]]
            assert y == [1, [11]]

        if "##pass by value ##pass by reference":

            """
            Flamethrower battle: <stackoverflow.com/questions/986006/python-how-do-i-pass-a-variable-by-reference>

            Only modifications on mutable objects inside a function have effect outside it.
            """

            def f(a, b):
                a = a + b

            # integer: immutable

            a = 0
            f(a, 1)
            assert a == 0

            def g(i):
                return i + 1
            a = 0
            a = g(a)
            assert a == 1

            # string: immutable
            a = "a"
            f(a, "b")
            assert a == "a"

            def g(s):
                return s + "b"
            a = "a"
            a = g(a)
            assert a == "ab"

            # list: mutable
            a = [0]
            f(a, [1])
            assert a == [0]

            def g(a):
                a.append(1)
            a = [0]
            g(a)
            assert a == [0, 1]

    if "#return value":

        if "##multiple return values":

            """
            there is no real multiple return values,

            but you can return a single tuple of values and open it

            this is one of the major motivations for tuples existing in the language
            """

            def f():
                """
                returns multiple arguments
                """
                return 1, 2
                #SAME:
                    #return (1, 2)

            a, b = f()
            assert a == 1
            assert b == 2

        if "##can return nothing":

            """
            If a function does not end on a return statement, it returns `None`.
            """

            def f(b):
                if b:
                    return 1

            assert f(True)  == 1
            assert f(False) == None

    if "##redefine":

        # Like any python object, you can redfine functions whenever you want.

        def f():
            return 0

        def f():
            return 1

        assert f() == 1

        class f:
            pass

    if "##functions can have attributes":

        # Function attributes have no relation to local variables.

        def f():
            c = 1
            return c
        f.c = 2
        assert f() == 1
        assert f.c == 2

        # View all the function attributes:

        print 'dir(f) = ' + str(dir(f))

        # The most important attribute is `__call__` which allows us to call the function:

        assert f.__call__() == 1

    if "##lambda":

        '''
        Lambda is a function without name

        Lambda functions can only contain a single expression.

        This means in particular that they cannot contain assigments,
        so they are very limited.
        '''

        f = lambda x: x + 1
        assert f(0) == 1
        assert f(1) == 2

    if "##scope":

        '''
        If the value of a variable was not defined inside the function,
        the value in the currently executing scope is taken.
        '''

        def f(b):
            return a == b

        a = 1
        assert f(1) == True

        a = 2
        assert f(1) == False

        if "##global":

            def global_inc_a_wrong():
                a = 2

            def global_inc_a():
                global a
                a = a + 1

            a = 1
            global_inc_a_wrong()
            assert a == 1
            global_inc_a()
            assert a == 2

            # If the variable was not yet defined on global scope,
            # it then gets defined once the function is called
            # and the assignement occurs:

            def global_def():
                global defined_in_global_def
                #This will define the variable on global scope:
                defined_in_global_def = 1

            try:
                print defined_in_global_def
            except NameError:
                pass
            else:
                assert False

            global_def()

            print defined_in_global_def

            # Global means *global*, and *not* inside another function:

            def outer():
                x = 1
                def inner():

                    #This x is not the same as the first one,
                    #but one on a global scope
                    global x

                    x = 2

                #Here we do not see the global x,
                #but the one inside outer:
                inner()
                assert x == 1

            #Here we see the global x defined inside inner:
            outer()
            assert x == 2

            # Compare this to what happens with nonlocal in Python 3.

    if "##nested functions":

        # This is the way to go:

        def ex8():
            ex8.var = 'foo'
            def inner():
                ex8.var = 'bar'
                print 'inside inner, ex8.var is ', ex8.var
            inner()
            print 'inside outer function, ex8.var is ', ex8.var
        ex8()

    if "##call function from its name on a string":

        #http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python

        pass

if "##class":

    '''
    Python classes are designed such that some of its syntax is analogous to C++
    classes.

    However, Python classes are much more dynamic and allow for many things which C++
    classes do not.

    In most cases, Python classes are used with syntax similar to C++ syntax.

    However, there are practical cases where the full flexibility of Python classes are used,
    and your C++ knowledge breaks.

    The faster you learn about how exacly Python classes work, the faster the magic will go away.

    The key points are:

    - classes and everythin else in Python are objects
    - attributes and the dot `.` operator
    - __dict__
    - bound methods
    '''

    if "classes are objects":

        class C(object):
            i = 1
            pass

        # You can assign it to a variable:

        D = C
        assert D.i == 1

        # You can add attributes to it:

        C.j = 2
        assert C.j == 2

        # You can return it from functions:

        def f(i):
            class C(object):
                if i == 0:
                    j = 0
                else:
                    j = 1
            return C
        assert f(0).j == 0
        assert f(1).j == 1

    if "#everything is an object":

        # All built-in types like `int`, `string` and `list`:

        assert (1).__class__ == int
        assert "ab".__class__ == str
        assert [1, 2].__class__ == list

        # Functions:

        def f(): pass
        print f.__class__

        # Classes:

        class C(object): pass
        assert C.__class__ == type
        assert C().__class__ == C

        # Modules:

        import os
        print os.__class__

    if "##__metaclass__ ##__new__":

        '''
        TODO
        '''

    if "##bound method ##unbound method":

        '''
        <http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static>
        '''

        class C(object):
            def __init__(self, i):
                self.i = i
            def m(self):
                return self.i

        c = C(1)

        # When we call a bound method:

        assert c.m() == 1

        # Python executes exactly the following call to an unbound method:

        assert C.m(c) == 1

        # This is why methods without a `self` always fail.

    if "##object":

        '''
        Base type of all Python built-in types.

        In Python 2, it is possible for a user defined object not to
        inherit from `object` (old style class).

        In Python 3, user defined classes automatically inherit from it,
        so every type derives from `object`.
        '''

        assert isinstance(1, object)
        assert isinstance("ab", object)

        def f(): pass
        assert isinstance(f, object)

        class C(object): pass
        assert isinstance(C, object)
        assert isinstance(C(), object)

        import os
        assert isinstance(os, object)

        # This is everything objects give to classes:
        print 'dir(object) = ' + str(dir(object))
        print 'dir(object()) = ' + str(dir(object()))

    if "##type":

        '''
        Built-in function type does two things:

        - determine the type of an object
        - dynamically create classes from strings

        Important rules:

        - the type of any type (built-in or user defined) is `type`.
        - the type of any object is its type,
            also known as class for user defined types.
        '''

        if "determine type of value":

            '''
            The `type` object is at the base of all the hierarchy.
            '''

            assert type(type)   == type
            assert type(object) == type
            assert type(1)      == int
            assert type(1.0)    == float
            assert type("abc")  == str
            assert type(u"s")   == unicode
            assert type([])     == list
            assert type({})     == dict

            print type(lambda:1)
            #<type 'function'>

            class C(object): pass
            assert type(C) == type
            assert type(C()) == C

            import os
            print type(os)
            #<type 'module'>

        if "make classes dynamically":

            class B(object): pass

            class C(B):
                a = 1

            # Same as above.

            C = type('C', (B,), {'a': 1})
            assert C.a == 1

    if "##__class__":

        '''
        Corresponding class object of a object.

        The only difference from `type()` seems to be for old style classes:
        <http://stackoverflow.com/questions/1060499/difference-between-typeobj-and-obj-class>

        Therefore, there is no difference in Python 3.
        '''

        assert object.__class__ == type
        assert (1).__class__    == int

        '''
        `__class__` can be set to something else however.

        This has no special effect.
        '''

        class D(object): pass

        class C(object):
            __class__ = D

        assert type(C()) == C
        assert C().__class__ == D

    if "##isinstance":

        '''
        TODO: like type but also considers base types?
        '''

        assert isinstance(object, type)
        assert isinstance(1, int)
        class C0(object): pass
        class C1(C0): pass
        assert isinstance(C1(), C1)
        assert isinstance(C1(), C0)

    if "##attributes":

        '''
        Anything you can get from an object via a dot `.`, including methods and memebers.

        Good tutorial: <http://www.cafepy.com/article/python_attributes_and_methods/contents.html>

        How the dot searches for attributes on `obj.attr`:

        1) `obj.__dict__` itself
        2) `obj.__class__.__dict__`
        3) then searches all base classes via MRO.
        '''

        class C:
            pass

        # Create a new attribute for class object C:

        C.i = 1

        c = C()
        c2 = C()

        # Attribute not found on object. Look at class:

        assert c.i == 1

        # Add attribute to object.

        c.i = 2

        # Attribute found on object. Ignore class attributes:

        assert c.i == 2

        # Can use __class__ to reach the class attribute:

        assert c.__class__.i == 1

        # Create a new function attribute for the class:

        def m(self):
            return 1
        C.m = m
        assert C().m() == 1

        if "##hasattr":

            class A:
                a = 1
                def f():
                    pass

            assert hasattr(A, 'a')
            assert hasattr(A, 'f')
            assert not hasattr(A, 'b')

            assert hasattr(A(), 'a')
            assert hasattr(A(), 'f')
            assert not hasattr(A(), 'b')

        if "##geattr":

            class C:
                def __init__(self, i):
                    self.attribute = i
            c = C(1)
            c.attribute2 = 2
            assert getattr(c, "attribute") == 1
            assert getattr(c, "attribute2") == 2
            assert getattr(c, "notanattribute", "default") == "default"

        if "##setattr":

            class A: pass

            setattr(A, 'name', 'value')
            assert A.name == 'value'

            ###any expression goes

            hasa = True
            class A:
                if hasa:
                    a = 1
                else:
                    a = 0

            assert A.a == 1

    if "##__dict__":

        """
        Contains all attributes of an object.

        Represents a base data structure for objects, and is used on the magic dot `.` attribute lookup.
        """

        if "Does not contain attributes inherited through `__class__` and MRO.":

            class B(object):
                a = 1
                def __init__(self):
                    self.b = 1

            class C(B):
                c = 2
                def __init__(self):
                    self.d = 2
                    super(C, self).__init__()

            print 'C.__dict__ = ' + str(C.__dict__)

            C.__dict__
            assert C().__dict__ == {'b':1, 'd':2}

        if "It is possible to write directly to it from both sides.":

            class C(object): pass
            c = C()
            c.__dict__['a'] = 1
            assert c.a == 1

            c.a = 2
            assert c.__dict__['a'] == 2

            class C(object): pass
            c = C()
            c.__dict__ = {'a':1, 'b':2}
            assert c.a == 1
            assert c.b == 2

            c.__dict__.update({'a':2, 'c':3})
            assert c.a == 2
            assert c.c == 3

            # TODO why not here:

            class C(object): pass
            try:
                C.__dict__['a'] = 1
            except TypeError:
                #'dictproxy' object does not support item assignment
                pass
            else:
                assert False

        # Built-in functions and types don't have a dict.
        # It is not possible to set their attributes.

        try:
            (1).__dict__
        except AttributeError:
            #'int' object has no attribute '__dict__'
            pass
        else:
            assert False

        try:
            (1).a = 2
        except AttributeError:
            #'int' object has no attribute 'a'
            pass
        else:
            assert False

        try:
            (len).a = 2
        except AttributeError:
            #'builtin_function_or_method' object has no attribute 'a'
            pass
        else:
            assert False

        # Functions:

        def f():
            """doc"""
            a = 1
        assert f.__dict__ == {}

        f.a = 1
        assert f.__dict__['a'] == 1

        f.__dict__['b'] = 2
        assert f.b == 2

        print 'f.__dict__ = ' + str(f.__dict__)

        # Sample output:

        #{'a': 1, '__module__': '__main__', '__doc__': 'doc', 'f': <function f at 0x9cb82cc>}

    if "##dir":

        '''
        Returns a list of all attributes of an object.

        Includes attributes available through `__class__` and base classes.

        Does a search in the `__dict__` attributes in the same order as the dot `.` operator.
        '''

        print 'dir(1) = ' + str(dir(1))
        class C(object): pass
        print 'dir(C) = ' + str(dir(C))
        print 'dir(C()) = ' + str(dir(C()))
        import os
        print 'dir(os) = ' + str(dir(os))

    if "##inspect":

        '''
        Module that can do many introspective things on Python objects.
        '''

    if "##reflection":

        # Get meta info objects.

        class C:
            """doc"""

            def __init__(self, name):
                """initdoc"""
                self.name = name

            def print_attrs(self):
                """print_attrs_doc"""
                for name in dir(self):
                    attr = getattr(self, name)
                    if not callable(attr):
                        print name, ':', attr


            def print_method_docs(self):
                """print_method_docs.doc"""
                for name in dir(self):
                    attr = getattr(self, name)
                    if callable(attr):
                        print name, ':', attr.__doc__

        c = C('the my object')
        c.print_attrs()

        # TODO: sane way to get only user defined attributes: http://stackoverflow.com/questions/4241171/inspect-python-class-attributes

    if "##vars":

        #list all available names in current scope and their string values:

        vars()

    if "##old style ##new style ##classic":

        '''
        In Python 2 there are 2 types of classes:

        - classic classes. The only type that existed up to `2.1`.
            They are deprecated and existed only for backwards compatibility.

        - new-style classes. Appeared in 2.2. To create a new-style class
            it must derive from `object`.

        Always use new style classes for new code.

        In Python 3 classic classes disappear, and it is not necessary
        to derive from `object` anymore.

        <http://stackoverflow.com/questions/2399307/python-invoke-super-constructor>

        Behaviours that have changed between old and new style classes:

        - super added
        - MRO changed
        - descriptors added
        - `__slots__` added
        '''

        class Old:
            pass

        class New(object):
            pass

        class New2(New):
            pass

    if "##members":

        # This shows how the concept of instance member variables are usually implemented.

        class A(object):

            def __init__(self, a):
                """
                Constructor.

                Members are defined in the constructor as `self.a = `
                """

                self.member = a

        a = A(0)
        assert a.member == 0
        a.member = 1
        assert a.member == 1

    if "##methods":

        # This shows how the concpet of instance methods variables are usually implemented.

        class A(object):

            def __init__(self, i):
                self.i = i

            def method(self):
                """
                Every non static method must receive self as the first arg.
                """
                return self.i

        assert A(1).method() == 1

    if "##private":

        '''
        By convention the underline '_' indicates private varibales and methods.

        Nothing in the language prevents you from using it outside
        except your code breaking later on because you broke the convention.
        '''

        class C:
            _private_static = 1
            def __init__(self):
                self._private_member = 2
            def _private_method(self):
                return 3

        assert C._private_static == 1
        assert C()._private_member == 2
        assert C()._private_method() == 3

    if "##static":

        class A(object):

            #static fields:
            static = 0
            static_refcount = 0

            def __init__(self, a=0, b=1):
                """
                Constructor
                """

                # Direct access fail:

                try:
                    static
                except NameError:
                    #global name 'static' is not defined
                    pass
                else:
                    assert False

                # The best way is to use `__class__`:

                self.__class__.static_refcount += 1

                # Also works but not DRY as it repeats the class name;

                A.static = 0

                # Since this is so verbose, just use `self.` instance attributes for singleton classes.
                # - memory is not duplicated because singleton

            @classmethod
            def class_method(cls, x):
                return cls, x

            @staticmethod
            def static_method(x):
                return x

        assert A.static == 0
        A.static = 1
        assert A.static == 1

        if "##classmethod and ##staticmethod":

            '''
            The only difference between classmethod and staticmethod is that classmethod
            also gets a reference to the class as argument.

            This means that:

            - classmethod is more versatile and verbose.

                It is required if the method relies on static variables since `self.__class__` is not possible.

            - staticmethod is recommended if the method does not need to access the class,
                since using it serves as self documentation of that fact.

            <http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python>
            '''

            a = A()
            assert a.class_method(0) == (A, 0)
            assert A.class_method(0) == (A, 0)
            assert a.static_method(0) == 0
            assert A.static_method(0) == 0

        if "Static variables are attributes of the class.":

            '''
            It is possible to read them as attributes of objects directly,
            if they are not already an attribute of the object, since attribute
            lookup looks at the object and then its class.

            It is not possible to assign to them, or you create a new attribute
            of the object which will shadow that of the class.
            '''

            a = A()
            b = A()

            A.static = 0
            assert A.static == 0
            assert a.static == 0
            assert b.static == 0

            A.static = 1
            assert A.static == 1
            assert a.static == 1
            assert b.static == 1

            a.static = 2
            assert A.static == 1
            assert a.static == 2
            assert b.static == 1

            b.static = 3
            assert A.static == 1
            assert a.static == 2
            assert b.static == 3

            '''
            You could however achieve that using `__class__`.

            This could be useful if you don't want to repeat the class name.
            '''

            a = A()
            b = A()

            A.static = 0
            assert A.static == 0
            assert a.static == 0
            assert b.static == 0

            A.static = 1
            assert A.static == 1
            assert a.static == 1
            assert b.static == 1

            a.__class__.static = 2
            assert A.static == 2
            assert a.static == 2
            assert b.static == 2

            b.__class__.static = 3
            assert A.static == 3
            assert a.static == 3
            assert b.static == 3

    if "##abstract class ##pure virtual method":

        """
        Method that must be overridden on inheritting class.

        There is no language feature that implements that feature,
        since it is a restriction, and Python leaves out all features
        which are simple restrictions.

        There are however conventional idioms that translate it.
        """

        # NotImplementedError idiom.
        # Allows instantiation, but breaks if method is used.

        class C(object):
            def m(self):
                raise NotImplementedError

        c = C()
        try:
            c.m()
        except NotImplementedError:
            pass
        else:
            assert False

        # abstractmethod idiom.
        # Attempt to instantiate class raises `TypeError`.

        import abc

        class C(object):
            __metaclass__ = abc.ABCMeta

            @abc.abstractmethod
            def m(self, i):
                return

        try:
            c = C()
        except TypeError:
            pass
        else:
            assert False

    if "##inheritance":

        class A(object):

            static = 0
            static_overridden = 1

            def __init__(self):
                self.member = 0
                self.member_overridden = 1

            def method(self):
                return 0

            def method_overridden(self):
                return 1

        class B(A):
            """
            This class inherits from A
            """

            static_overridden = 2

            def __init__(self):

                # It is mandatory to call base class constructors explicitly if you want them called.
                super(B, self).__init__()

                # This must come after the base constructor to have an effect:
                self.member_overridden = 2

            def method_overridden(self):
                return 2

        a = A()
        b = B()

        assert B.static == 0
        assert b.member == 0
        assert b.method() == 0

        assert B.static_overridden == 2
        assert b.member_overridden == 2
        assert b.method_overridden() == 2

        #B.static and A.static are two different variables
        B.static = 2
        B.static_overridden = 2
        assert A.static == 0
        assert A.static_overridden == 1

        if "##super":

            '''
            Both a:

            - built-in type (seldom used directly)

            - method that can only be used inside classes, commonly used to call
                constructors of base classes
                TODO what does it return? How does it work?
                <http://www.artima.com/weblogs/viewpost.jsp?thread=236275>
            '''

            class A(object):
                def __init__(self, i):
                    self.i = i

            class B(A):
                def __init__(self, i):
                    super(B, self).__init__(i)
                    assert type(super(B, self)) == super

            assert B(1).i == 1

            '''
            Only works for new style classes.
            '''

            class A():
                pass

            class B(A):
                def __init__(self):
                    super(B, self)

            try:
                B()
            except TypeError:
                pass
            else:
                assert False


        if "##inheritance constructor combos":

            class B(A):
                def __init__(
                            self,
                            for_derived_only,
                            named_to_modify,
                            *args,
                            **kwargs
                        ): #note that other named args, before or after modified one will fall into args, so youre fine

                    self.for_derived_only = for_derived_only

                    named_to_modify = named_to_modify + 1

                    #modify args
                    args = [ a+1 for a in args ]

                    #kwargs
                    self.creator = kwargs.pop('arg_derived_only', "default")
                    kwargs['override'] = "new value"

                    #call base calss constructor
                    super(B, self).__init__(named_to_modify, *args, **kwargs)

        if "##__bases__":

            '''
            Tuple of direct base classes.
            '''

            class C00(object): pass
            class C01(object): pass
            class C02(object): pass
            class C1(C01, C00, C02): pass
            assert C1.__bases__ == (C01, C00, C02)

        if "##MRO ##method resolution order ##C3 linearization":

            '''
            Order in which attributes (including methods) are searched for on its base classes.

            This has changed from old style classes to new style classes:

            - old style classes: search from left to right depth first. Stop at first match.
            - new style classes: [C3 linearization](http://en.wikipedia.org/wiki/C3_linearization)

                C3 MRO works as follows: <http://www.python.org/download/releases/2.3/mro/>

            C3 is also used on Perl 6.

            C3 is called C3 *linearization* because it takes as input an inheritance tree
            and outputs a linear list which represents the search order.

            ##__mro__ ##mro()

                The `__mro__` attribute is a tuple of class objects that contains the
                MRO order for the class.

                It only exists for new style classes.

                `mro()` is a method that returns an `__mro__` tuple.
                It can be overridden, and its result is sotored in `__mro__` at class
                instanciation.
            '''

            # Old:

            class C: i = 0
            class C1(C): pass
            class C2(C): i = 2
            class C12(C1, C2): pass
            class C21(C2, C1): pass

            assert C12().i == 0
            assert C21().i == 2

            try:
                C12.__mro__
            except AttributeError:
                pass
            else:
                assert False

            # New:

            class C(object): i = 0
            class C1(C): pass
            class C2(C): i = 2
            class C12(C1, C2): pass
            class C21(C2, C1): pass

            assert C12().i == 2
            assert C21().i == 2

            assert C12.__mro__ == (C12, C1, C2, C, object)
            assert C21.__mro__ == (C21, C2, C1, C, object)

            '''
            Some hierarchies do not admit linearization.

            In those cases, an exception is raised.
            '''

            class C11(object): pass
            class C12(object): pass
            class C21(C11, C12): pass
            class C22(C11, C12): pass
            class C3(C21, C22): pass

    if "##special attributes":

        class A(object):
            """
            The methods here are often accessed via operators such as `<`,
            or are used by global functions such as `str()` (should be inheritance like Java).

            Full list:

            <http://docs.python.org/2/reference/datamodel.html#special-method-names>
            """

            def __init__(self, a=0, b=1):
                self.a = a
                self.b = b

            #def __cmp__(self, other):
                #"""
                #deprecated in 3., forget it!
                #"""

            def __eq__(self, other):
                """
                >>> a = A()
                >>> b = A()
                >>> a == b
                """
                return self.a == other.a

            def __ge__(self, other):
                """
                defines >=
                """
                return

            def __gt__(self, other):
                """
                defines  >
                """
                return

            def __le__(self, other):
                """
                defines <=
                """
                return

            def __lt__(self, other):
                """
                defines <
                """
                return

            def __ne__(self, other):
                """
                defines !=
                """
                return

            def __add__(self, other):
                """
                >>> A(1,2) + A(3,4)
                """

            def __hash__(self, other):
                """
                makes hashable, allowing it to be for example a dictionnary key
                """
                return

            def __str__(self):
                """should return bytes in some encoding,

                called string for compatibility, changed to __bytes__ in python 3"""
                return unicode(self).encode('utf-8')

            def __unicode__(self):
                """informal description, return (possibly unicode) chars

                http://stackoverflow.com/questions/1307014/python-str-versus-unicode

                changed to __str__ in python 3
                """
                return 'a'

            def __repr__(self):
                """
                Difference from str: formal and very precise string represenation of the object.

                What you get if you put an object on a interctive session directly:

                >>> A()
                class A()
                """
                return self.a + ' ' + self.b

            def __len__(self):
                """
                >>> len(a)
                """
                return len(self.a)

            d = {}

            def __setitem__(self, k, v):
                """
                >>> self[k] = v
                """
                d[k] = v

            def __getitem__(self, k):
                """
                >>> self[k]
                """
                return self.d[k]

            def __contains__(self, v):
                """
                >>> v in self
                """
                return v in d

            def __call__(self, n):
                """
                Allows object to be callable as:

                >>> a = A()
                >>> a(1) == 2
                >>> a.__call__(1) == 2
                """
                return n + 1

            '''
            Special attributes which shall not be discussed in this class
            because they deserved a more involved discussion:

            - `__slots__`
            - `__get__`, `__set__` and `__delete__`
            '''

        if "##__name__":

            def NameFunc(): pass
            assert NameFunc.__name__ == 'NameFunc'

            class NameClass(object):
                def NameMethod():
                    pass
            assert NameClass.__name__ == 'NameClass'
            assert NameClass.NameMethod.__name__ == 'NameMethod'

        if "##equality operator for classes ##__eq__":

            """
            Default does not compare member by member,
            compares adress of object.
            """

            class C:
                def __init__(self,i):
                    self.a = i

            c = C(1)
            c2 = C(1)
            assert c != c2
            c = c2
            assert c == c2

            if "##compare by all members automatically do this":

                class C:
                    def __init__(self, i=0, j=1):
                        self.i = i
                        self.j = j

                    def __eq__(self, other):
                        """
                        all attributes of objects are equal
                        """
                        if type(other) is type(self):
                            return self.__dict__ == other.__dict__
                        return False

                c = C(1)
                c2 = C(1)
                assert c == c2
                c2 = C(2)
                assert c != c2

            if "##__eq__ and None":

                """
                always compare to `None` with is, never with `==`, because `==` can be overwriden by `__eq__`
                for example, to always true, while `is` cannot

                <http://jaredgrubb.blogspot.com.br/2009/04/python-is-none-vs-none.html>
                """

                class A(object):
                    def __eq__(self, other):
                        return True

                a = A()
                assert not a is None
                assert a == None

            if "##__ne__":

                # *Not* automatically deduced from __eq__.

                class C:
                    def __eq__(self, other):
                        return True

                assert C() == C()
                assert C() != C()

        if "##descriptors ##__get__ ##__set__ ##__delete__":

            '''
            Allow to control what the dot `.` does on access, assignment and del
            of an attribute.

            Descriptor protocol:

                descr.__get__(self, obj, type=None) --> value

                descr.__set__(self, obj, value) --> None

                descr.__delete__(self, obj) --> None
            '''

            class Desc(object):

                def __init__(self):
                    self.i = 0

                def __get__(self, obj, cls=None):
                    return self.i + 1

                def __set__(self, obj, val):
                    self.i = val*val

                def __delete__(self, obj):
                    self.i = 0

            class HasDesc(object):
                i = Desc()

            o = HasDesc()
            o.i = 2
            assert o.i == 5
            del o.i
            assert o.i == 1

            #TODO what do obj and cls do?


            '''
            Only work for new style classes
            '''

            class Desc():

                def __init__(self):
                    self.i = 0

                def __get__(self, obj, cls=None):
                    return self.i + 1

            class HasDesc():
                i = Desc()

            o = HasDesc()
            assert o.i != 1

            if "##property":

                '''
                Allows to make descriptors with a single class.
                '''

                assert type(property) == type

                class HasDesc(object):

                    def __init__(self):
                        self._i = 0

                    def geti(self):
                        return self._i + 1

                    def seti(self, val):
                        self._i = val * val

                    def deletei(self):
                        self._i = 0

                    i = property(geti, seti, deletei, "doc")

                o = HasDesc()
                o.i = 2
                assert o.i == 5
                del o.i
                assert o.i == 1

            if "##property as decorators":

                # It is very idiomatic to use property as a decorator as follows:

                class HasDesc(object):

                    def __init__(self):
                        self._i = 0

                    @property
                    def i(self):
                        return self._i + 1

                    @i.setter
                    def i(self, val):
                        self._i = val * val

                    @i.deleter
                    def i(self):
                        self._i = 0

                o = HasDesc()
                o.i = 2
                assert o.i == 5
                del o.i
                assert o.i == 1

            # Application: create a readonly value:

            class HasDesc(object):

                def __init__(self):
                    self._i = 0

                @property
                def i(self):
                    return self._i + 1

            o = HasDesc()
            assert o.i == 1
            try:
                o.i = 2
            except AttributeError:
                pass
            else:
                assert False

        if "##__slots__":

            '''
            Only available in new style classes.

            Fixes exactly what attributes a class can have.

            Only to be used as a memory optimization tool when
            there are many many objects of a given type in a performance critical point.
            '''

            class Foo(object):
                __slots__ = ['x']
                def __init__(self, n):
                    self.x = n

            y = Foo(1)
            assert y.x == 1
            y.x = 2
            assert y.x == 2

            # This would work for an object without `__slots__`.

            try:
                y.z = 3
            except AttributeError:
                pass
            else:
                assert False

        if "##operators that cannot be overloaded":

            """
            <http://stackoverflow.com/questions/3993239/python-class-override-is-behavior>

            -   is: always implements id compairison.

            -   not, and and or: only depend on the truth value assignment of objects,
                which depends on `__notzero__` and `__len__` in Python 2.

            - assignment: makes no sense since assignment always replaces one object for another.
            """

            class A(object):

                def __is__(self):
                    return True

                def __not__(self):
                    return True

                def __and__(self, other):
                    return True

                def __or__(self, other):
                    return True

            #assert not A()
            #assert A() and A()
            #assert A() or A()

        if "##automaticaly print all members of objects":

            class C:

                def __init__(self, i=0, j=1):
                    self.i = i
                    self.j = j

                def __str__(self):
                    out = '\n' + 30 * '-' + '\n'
                    for k in self.__dict__.keys():
                        out += k + ':\n'
                        out += str(self.__dict__[k]) + '\n\n'
                    return out

            print C()
            print C(1,2)

    if "##assignment operator for classes":

        """
        Objects are mutable, so assignment throws old object away,
        and a is a reference to b now!

        To get around this you can use the copy package.
        """

        class A(object):
            def __init__(self, i):
                self.i = i

        a = A(0)
        b = A(1)

        a = b
        assert a.i == 1
        assert a == b
        a.i = 2
        assert b.i == 2

    if "##copy":

        # Makes copies and deepcopies of objects.

        import copy

        class A(object):
            def __init__(self, i):
                self.i = i

        b = A(1)
        a = copy.copy(b)
        assert a.i == 1
        assert not a == b
        a.i = 2
        assert b.i == 1


    if "##classes can be made inside functions":

        def func(val):
            class A:
                a = val
            return A
        a = func(1)
        print a.a
        b = func(2)
        print b.a
        print a.a #unaltered

    if "##mixin":

        '''
        Hard to say what it is in Python, people don't agree much.

        <http://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful>
        '''

        if "single inheritance definition":

            import abc

            class ComparableMixin(object):
                """This clas has methods which use `<=` and `==`,
                but this class does implement those methods."""
                def __ne__(self, other):
                    return not (self == other)
                def __lt__(self, other):
                    return self <= other and (self != other)
                def __gt__(self, other):
                    return not self <= other
                def __ge__(self, other):
                    return self == other or self > other

            class Integer(ComparableMixin):
                def __init__(self, i):
                    self.i = i
                def __le__(self, other):
                    return self.i <= other.i
                def __eq__(self, other):
                    return self.i == other.i

            assert Integer(0) <  Integer(1)
            assert Integer(0) != Integer(1)
            assert Integer(1) >  Integer(0)
            assert Integer(1) >= Integer(1)

            c = ComparableMixin()

            # This particular example could have been achieved via the `functools.total_ordering()` decorator.

            import functools

            @functools.total_ordering
            class Integer(object):
                def __init__(self, i):
                    self.i = i
                def __le__(self, other):
                    return self.i <= other.i
                def __eq__(self, other):
                    return self.i == other.i

            assert Integer(0) < Integer(1)
            assert Integer(0) != Integer(1)
            assert Integer(1) > Integer(0)
            assert Integer(1) >= Integer(1)

        if "multiple inheritance definition":

            class HasMethod1(object):
                def method(self):
                    return 1

            class HasMethod2(object):
                def method(self):
                    return 2

            class UsesMethod10(object):
                def usesMethod(self):
                    return self.method() + 10

            class UsesMethod20(object):
                def usesMethod(self):
                    return self.method() + 20

            class C_1_10(HasMethod1, UsesMethod10): pass
            class C_1_20(HasMethod1, UsesMethod20): pass
            class C_2_10(HasMethod2, UsesMethod10): pass
            class C_2_20(HasMethod2, UsesMethod20): pass

            assert C_1_10().usesMethod() == 11
            assert C_1_20().usesMethod() == 21
            assert C_2_10().usesMethod() == 12
            assert C_2_20().usesMethod() == 22

if "##docstring":

    '''
    It is possible to access them at runtime.

    This can be used by documentation generators.
    '''

    def f():
        """doc0"""

    assert f.__doc__ == 'doc0'

if '##exception':

    # They go up until somthing catches them:

    def e():
        raise Exception

    def d():
        e()

    try:
        d()
    except:
        print "exception!"

    '''
    If nothing catches them, they explode on stdX and stop program excecution!

    What gets printed:

    - traceback: where the exception came from (modules, functions, lines)
        #this is userful for debug, so you can find where the problem comes from

    - <Exception class>: <exception.__repr__>
        raise Exception("repr")
        print "cant reach here"
    '''

    if '##else':

        # Only execute if the exception did not happen.

        try:
            raise Exception()
        except:
            pass
        else:
            assert False

        e = False
        try:
            pass
        except:
            assert False
        else:
            e = True
        assert e

    if '##finally':

        # Always executed, wether the exception happened or not.

        f = False
        try:
            raise Exception()
        except:
            pass
        else:
            assert False
        finally:
            f = True
        assert f

        f = False
        try:
            pass
        except:
            assert False
        else:
            pass
        finally:
            f = True
        assert f

    if 'What can be raised':

        # Only old style classes or derived classes from exception can be raised.

        # In particular, strings cannot be raised, or that raises a `TypeError` instead of the string.

        # This was made possible around Python 2.5, but removed in Python 2.6.

        class Old: pass
        try:
            raise Old()
        except Old:
            pass
        else:
            assert False

        class New(object): pass
        try:
            raise New()
        except TypeError:
            pass
        else:
            assert False

        class New(Exception): pass
        try:
            raise New()
        except New:
            pass
        else:
            assert False

        # Since `'str'` is a new style object:

        try:
            raise 'str'
        except TypeError:
            pass
        else:
            assert False

        # A lightweight alternative is to raise Exception with a custom message:

        try:
            raise Exception('str')
        except Exception:
            pass
        else:
            assert False

    ###except catches derived classes only

    try:
        raise Exception()
    except ZeroDivisionError:
        print "ZeroDivisionErrorOnly or derived classes"
    except Exception:
        print "Exception, or its derived classes, therefore all exceptions"
    except:
        print "same as above"

    ###passing args to exceptions

    try:
        raise Exception(1, 2)
        #raise Exception, (1, 2) #same as above, but more verbose and implicit. NEVER user this
    except Exception, e:
        print "e is an instance of Exception"
        print Exception, e
        print e.args[0], e.args[1]
        print e

    ###reraise

    # Can be used to add/modify info

    # It is hard to modify and reraise i python 2

    # It seems python 3 introduces the `raise from` statement which makes that much easier!

    #<http://stackoverflow.com/questions/696047/re-raising-exceptions-with-a-different-type-and-message-preserving-existing-inf>

    try:

        raise Exception("msg")

    except Exception, e:

        # You lose the traceback:

        #raise Exception("updated msg\n" + str(e))

        # To keep the traceback:

        #import traceback
        #traceback.print_exc(
            ##file = sys.stdout #stderr is the default
        #)

        # For more info on current exception:

        print "sys.exc_info() = "
        print sys.exc_info()
        print "sys.exc_type() = "
        print sys.exc_type
        print "sys.exc_value() = "
        print sys.exc_value
        print "sys.exc_traceback() = "
        print sys.exc_value

        # The following forms keep the traceback:

        #raise e
        #raise

    if "##built-in exceptions":

        '''
        Like other built-ins, the following exceptions are always available
        without any imports.

        <http://docs.python.org/2/library/exceptions.html>
        '''

        try:
            print 1/0
        except ZeroDivisionError:
            print "division by zero"
        else:
            print "no exception"

        try:
            int("a")
        except ValueError:
            print "not a number"

        try:
            f = open("NONEXISTENT")
        except IOError, (err, msg):
            if err == 2:
                print "does not exist", msg
            else:
                print "no exception"

        if "##KeyboardInterrupt":

            # Program got a SIGINT, generated when user presses control c on Linux terminals.

            if False:
                try:
                    for i in itertools.count():
                        pass
                except KeyboardInterrupt:
                    print "had enough of waiting"

    ###custom exception

    class CustomException(Exception):
        def __init__(self, value):
            self.parameter = value
        def __str__(self):
            return repr(self.parameter)

    try:
        raise CustomException("msg")
    except CustomException, (instance):
        print instance.parameter

if "##decorator":

    """
    Decorators are syntaxical sugar syntax that allows to write functions or classes in the forms:

        @decorator
        def f():
            pass

        @decorator
        class C:
            pass

    Where `decorator` is any callable such as a function of a class that implements `__call__`.

    They are documented together with function and class definition syntax.
    """

    if "Create a function based function decorator":

        def decorator(func):
            def wrapper(i, *args, **kwargs):
                return func(i, *args, **kwargs) + 1
            return wrapper

        # Decorator sugar

        @decorator
        def f(i):
            return i

        assert f(1) == 2

        # Exact same but without decorator sugar:

        def f(i):
            return i

        decorated = decorator(f)
        assert decorated(1) == 2

    if "Multiple decorators":

        def decorator(func):
            def wrapped(i):
                return func(i) + 2
            return wrapped

        def decorator2(func):
            def wrapped(i):
                return func(i) * 2
            return wrapped

        @decorator
        @decorator2
        def f(i):
            return i

        assert f(0) == 2

    if "Create a callable class based function decorator":

        class Decorator:
            def __init__(self, j):
                self.j = j

            def __call__(self, func):
                def wrapper(i, *args, **kwargs):
                    return func(i, *args, **kwargs) + self.j
                return wrapper

        # Decorator sugar

        @Decorator(2)
        def f(i):
            return i

        assert f(1) == 3

    if "Create a function based ##class decorator":

        def decorator(cls):
            def f(self):
                return 1
            cls.f = f
            return cls

        @decorator
        class C(object):
            pass

        assert C().f() == 1

    if "It is only possible to decorate functions or classes, not variables.":

        def d():
            pass
        #@d #SyntaxError
        a = 1

    if "Decorators can take multiple arguments.":

        def decorator(func, j):
            def wrapper(i, *args, **kwargs):
                return func(i, *args, **kwargs) + j
            return wrapper

        # Decorator sugar

        #@decorator
        def f(i):
            return i

        # TODO get working
        #assert f(1) == 3

    if "Decorator must take at least one argument to not raise a TypeError.":

        def d():
            pass
        try:
            @d
            def f():
                pass
        except TypeError:
            pass
        else:
            assert False

    if "Decorator functions of __call__ methods must take at exactly one argument.":

        '''
        If you want to pass parameters to a decorator, make a class based decorator
        and use its __init__ method for the arguments.
        '''

        # Direct function approach fails.

        def decorator(func, j):
            def wrapper(i, *args, **kwargs):
                return func(i, *args, **kwargs) + j
            return wrapper

        try:
            @decorator(2)
            def f(i):
                return i
        except TypeError:
            pass
        else:
            assert False

    if "The decorator call is only made at function / class definition.":

        def decorator(func):
            global i
            i += 1
            def wrapper(*args, **kwargs):
                pass
            return wrapper

        i = 0
        @decorator
        def f():
            pass
        assert i == 1
        f()
        assert i == 1

    if "Decorators can return anything.":

        def d(g):
            return 1

        @d
        def f():
            pass

        assert f == 1

if "##with":

    '''TODO'''

if "##__builtins__":

    #TODO

    #direct acess to all builtin functions:

    __builtins__.dir()

if "##exec":

    # Interpret a string at given point.

    a = 0
    exec('a = 1')
    assert a == 1

if "##streams":

    """
    Like in C, files and pipes are both similar objects
    meaning that you can do many operations to them transparently
    such as read/write

    The stdin, stdout and stderr streams are always open by default.

    There are however, as in POSIX, some operations may be only
    available to certain types of streams.

    For example, search operations can be done on files, but not on stdin/out.
    """

    if "##print statement":

        '''
        In 2.X there is the `print` statement (not a regular function)
        which will be replaced by the print function in 3.X.
        This will make the interface more standard and support more options.

        In 2.X, the `print s` is exactly the same as `sys.stdout.write(s)`.
        '''

    if "##stdout":

        sys.stdout.write("stdout")
        print

        # Best way to print without a newline in 2.X:

        # Many shells don't show input immediately until the next newline. To force that use flush.

        import sys
        sys.stdout.write('no newline')
        sys.stdout.flush()
        print

    if "##stderr":

        sys.stderr.write("stderr")

    if "##stdin":

        # Read from stdin until an EOF, that is until:
        #
        # - program on other side of pipe terminates if pipe coming in
        # - user hits ctrl+d on linux (ctrl+z on windows)

        if False:
            sys.stdin.read()

        if "##isatty":

            #check if stdin has a pipe comming in or if its the user who is typing

            if False:

                #test.py
                if sys.stdin.isatty():
                    print True
                else:
                    print False
                print ins

                #echo asdf | test.py

            # prints False (is a pipe, not a terminal) and asdf (read from sdtin)

                #test.py

            # prints True is a user input terminal (no pipes) and waits for user input
            # after ^D, prints what was input by keyboard.

    if "##file IO":

        if "binary":

            # Best way to open binary files:

            path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
            data = "a\nb"
            try:
                with open(path, "w") as f:
                    f.write(data)
            except IOError, e:
                print e
                raise
            try:
                with open(path, "r") as f:
                    assert f.read() == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            # `with` is exception safe: on exception will first close file.

            #http://preshing.com/20110920/the-python-with-statement-by-example
            #http://effbot.org/zone/python-with-statement.htm

        if "unicode":

            '''
            If all you want to do is slurp read, then encoding manually is a fine option as shown here.

            There however operations which are non trivial to do, for example reading linewise,
            which requires knowledge about the encoding to be done. For this kind of operation, use `codecs`.
            '''

            path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
            # Euro sign
            data = u"\u20AC"
            try:
                with open(path, "w") as f:
                    # Raises on most implemtatoins:
                    #     UnicodeEncodeError: 'ascii' codec can't encode character u'\u20ac' in position 0: ordinal not in range(128)
                    #f.write(data)
                    f.write(data.encode('utf-8'))

                    # Might work because Python knows if its outputing to a terminal, and uses LC_CTYPE to determine encoding.
                    # May fail if you pipe however, even if output to terminal works fine. In that case Python uses None as encoding.
                    #sys.stdout.write(data)

                    # To automatically change the default encoding non non terminal output, use on you main imported file:
                    # http://stackoverflow.com/questions/2276200/changing-default-encoding-of-python
                    #Output UTF-8 by default.
                    #import sys
                    #reload(sys)  # Reload is required.
                    #sys.setdefaultencoding('utf-8')
            except IOError, e:
                print e
                raise
            try:
                with open(path, "r") as f:
                    read = f.read()
                    assert type(read) == str
                    # Because str, only the first byte!
                    assert read[0] != data
                    assert read.decode('utf-8')[0] == data
            except IOError, e:
                print e
                raise
            os.unlink(path)

            if "##codecs":

                import codecs

                # Linewise read. Requires the encoding to be known, and is a non trival operation.

                path = os.path.join(tempfile.gettempdir(), "pythone_fileio.tmp")
                # Two line terminated euro signs.
                data = u"\u20AC\n\u20AC\n"
                with open(path, "w") as f:
                    f.write(data.encode('utf-8'))
                # 'r' is the default
                f = codecs.open(path, encoding='utf-8', mode='r')
                lines = []
                for line in f:
                    lines.append(line)
                f.close()
                assert lines[0] == u"\u20AC\n"
                assert lines[1] == u"\u20AC\n"
                os.unlink(path)

    if "##read methods":

        # Read from handle untill EOF:

            #sys.stdin.read()
            #f.read()

        # Appends a newline at the end!

        # Read up to 128 bytes:

            #f.read(128)

        # Read single ascii char:

            #f.read(1)

        # Read up to first \n or EOF:

            #f.readline()

        # Same as `f.read().split(\n)`. This is amost never useful because of `xreadlines`.

            #lines = f.readlines()
            #print lines[2];

        # Never do for loops with `readlines`, always user `xreadlines` instead
        # because that way you don't clutter memory, and you can read files larger
        # than memory.

        # Iterator based `readlines`:

            #for l in f.xreadlines():
            #    print l

        # This is the way to go for looping over lines one at a time.

        pass

if "##time":

    import time

    if "##time":

        # Get number of seconds since 1970:

        print 'time.time() = ' + str(time.time())

    if "##clock":

        # Quoting the man: "This is the function to use for benchmarking Python or timing algorithms."

        start_time = time.clock()
        "-".join(str(n) for n in range(10000))
        elapsed_time = time.clock() - start_time
        print 'clock elapsed = {0:.6f}s'.format(elapsed_time)

        # Not accurate for wall time. Does not measure time of external programs.

    if "##timeit":

        # Benchmark code snippets from strings. Relies internally on either time or clock.

        import timeit
        print "timeit time of all iterations= {0}s".format(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))

        # From the command line:

            #python -m timeit '"-".join(str(n) for n in range(100))'

    if "##sleep":

        '''Sleep for the given number of seconds'''

        #time.sleep(3)

if "##datetime":

    import datetime

    #year month day minute sec milisec oriented time operations

    import datetime
    now = datetime.datetime.now()
    print 'now = ' + str(now)
    print now - now #timedelta(0)
    print now - datetime.timedelta(1) #one day by default
    print now - datetime.timedelta(
        #years          = 1, # Not a valid argument.
        weeks           = 2,
        days            = 3,
        hours           = 4,
        minutes         = 5,
        seconds         = 6,
        milliseconds    = 7,
        microseconds    = 8
    )
    print datetime.datetime.fromtimestamp(0) #get a datetime from a seconds after 1970 time.time()

if "##regex":

    import re

    '''
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
    '''

    if "##lookahead":

        # Don't eat front part or regex

        p = re.compile(r'a.')
        assert p.sub('0', 'abaac') == '00c'

        p = re.compile(r'a(?=.)')
        assert p.sub('0', 'abaac') == '0b00c'

    if "##flags":

        '''
        ##DOTALL: dot matches all characters, including newlines
        ##MULTILINE: ^ and $ also matches at \n
        '''

        p = re.compile(r'a', re.IGNORECASE | re.DOTALL)

    if "##sub":

        p = re.compile('(a.|b.)')

        # By string:

        assert p.sub('0', 'a_b_abc') == '000c'

        # By callable:

        assert p.sub(lambda m: m.group(1)[1:], 'a_b-abc') == '_-bc'

        # Count:

        assert p.sub('0', 'a_b_abc', count=1) == '0b_abc'

    if "##subn":

        # Same as sub but also returns number of subs made:

        assert p.subn('0', 'a_b_abc') == ('000c', 3)

    if "##match":

        #MUST MATCH FROM BEGINNING OF STRING!!!!!!

        re.match(r"a.c", "abc")

        r = re.compile(r"a.c")
        r.match("abc")
        #matches
        r.match("0abc")
        #DOES NOT MATCH!!!! MUST MATCH FROM BEGINNING OF STRING!!! use search for that

    if "##search":

        r.search("0abc")
        #works

        r.search("abcaBc")
        #. == b, stops at first match. to find all matches, use finditer

    if "##finditer":

        matches = list(r.finditer("abcaBc"))
        #a list of all matches

    if "##split":

        re.split(r'[ab]+', '0abba1aaaaa2')
        #[0, 1, 2]

##file operations

    # Mostly under ``os``.

if "##os":

    # Wrappers for os specific stuff.
    # Lots of important file and directory operations.

    import os

    # Path separator ('/' linux/mac '\' on windows):

    print "os.sep = " + os.sep.encode('string-escape')

    # System newline separtor ('\n' Linux, '\r' Mac, '\n\r' Windows):

    print "os.linesep = " + os.linesep.encode('string-escape')

    if "#listdir #ls":

        # **Always** use Unicode input since the output gets the same encoding as this input
        # and filenames may contain non ascii chars!

        print 'os.listdir(u".") = ' + "\n".join(os.listdir(u'/'))

    if "##unlink #rm":

        path = "open.tmp"
        f = open(path, "w")
        assert os.path.isfile(path)
        os.unlink(path)
        assert not os.path.exists(path)

    if "#mkdir #rmdir":

        # Only works if directory is empty.
        # For recursive directory removal, see `shutil.rmtree`.

        path = "dir.tmp"
        os.mkdir(path)
        assert os.path.isdir(path)
        os.rmdir(path)
        assert not os.path.exists(path)

    if "##makedirs":

        path0 = "tmp0"
        path1 = "tmp1"
        path2 = "tmp2"
        path = os.path.join(path0, path1, path2)

        os.makedirs(path)
        assert os.path.isdir(path)
        os.removedirs(path)

    if "##getcwd #pwd #chdir #cd":

        # Get current working dir (each process has a cwd)

        print "os.getcwd() = " + os.getcwd()

    if "##symlink":

        '''
        os.symlink(name, origin)
        Where name is the place the symlinke will be created at,
        and origin what it points to.
        '''

    if "##walk ##find":

        '''
        Walk all subdirectories recursively.

        Out of the box options:

        - up down or down up
        - onerror callback function
        - followlinks or not

        For input like:

            for root, dirs, files in os.walk(u"tests"):
                print root
                print dirs
                print files
                print

        The output is of the form:

            directory path
            [basename of directories inside it]
            [basename of files inside it]

        It loops over all directories.

        **Be paranoid and always use unicode `u"."` in Python 2.7**, since the output has the same encoding as that input,
        and paths are primary examples of things that may contain unicode characters.
        '''

        # Get relative paths to all non-directory files:

        for root, dirs, files in os.walk(u"."):
            for basename in files:
                path = os.path.join(root, basename)
                #print path

        # Get relative paths to all directories:

        for root, dirs, files in os.walk(u"."):
            for basename in dirs:
                path = os.path.join(root, basename)
                #print path

        # Does not include current directory dot `.` nor upper directory two dots `..`.

        # Get relative paths to all files and directories:

        for root, dirs, files in os.walk(u"."):
            for basename in dirs + files:
                path = os.path.join(root, basename)
                #print path

        # To do all of Bash `find` filtering, jus use regular ifs. Sanity!

        for root, dirs, files in os.walk(u"."):
            for basename in dirs + files:
                path = os.path.join(root, basename)
                if os.path.splitext(path)[1] == ".pdf":
                    #print path
                    pass

        # The order and choice of directories which will be descended into is determined by `dirs`.

        # If you modify if in-place, you can alter the descent order! Typical applications include:

        # - `sort` to fix descent order

            # Only sorts each level and the descent order:

            # - files come after directories
            # - shallow come before deep

        for root, dirs, files in os.walk(u"."):
            dirs.sort()
            files.sort()
            for basename in dirs + files:
                path = os.path.join(root, basename)
                #print path

            # For a full sort, the only way is to put all paths in a list and sort the list.

            # That is less efficient because 2n log 2n > 2(n log n and rarely necessary.

        # - `remove` to prune any directories with a given basename:

        for root, dirs, files in os.walk(u"."):
            try:
                dirs.remove(u"prune_me")
            except ValueError:
                pass
            for basename in dirs + files:
                path = os.path.join(root, basename)
                #print path

    if "##path":

        import os.path

        if "##join":

            assert os.path.join('a', 'b', 'c') == 'a{s}b{s}c'.format(s=os.sep)
            os.path.join('a//', '/b')

        if "##split ##splitext":

            path = os.path.join('a', 'b', 'c.e')
            root, basename = os.path.split(path)
            basename_noext, ext = os.path.splitext(basename)
            assert root == os.path.join('a', 'b')
            assert basename_noext == 'c'
            assert ext == '.e'

        if "##exists":

            # Returns False for broken symlinks.
            # lexists returns True in that case.

            temp = tempfile.NamedTemporaryFile()
            assert os.path.exists(temp.name)
            temp.close()
            assert not os.path.exists(temp.name)

            temp = tempfile.mkdtemp()
            assert os.path.exists(temp)
            os.rmdir(temp)

        if "##isfile":

            # Exists and is file, not directory.

            temp = tempfile.NamedTemporaryFile()
            assert os.path.isfile(temp.name)
            temp.close()
            assert not os.path.isfile(temp.name)

            temp = tempfile.mkdtemp()
            assert not os.path.isfile(temp)
            os.rmdir(temp)

        if "##isdir":

            # Exists and is directory.

            temp = tempfile.NamedTemporaryFile()
            assert not os.path.isdir(temp.name)
            temp.close()

            temp = tempfile.mkdtemp()
            assert os.path.isdir(temp)
            os.rmdir(temp)
            assert not os.path.isdir(temp)

        os.path.islink('/a')

        ##Absolute path:

        print "os.path.abspath(u'.') = " + os.path.abspath(u'.')

        # Absolute path resolving links recursively:

        os.path.relpath(u'/a')

        if "#commonprefix":

            assert os.path.commonprefix([
                '{s}a{s}b{s}c{s}d'.format(s=os.sep),
                '{s}a{s}b{s}e{s}d'.format(s=os.sep)
            ]) == '{s}a{s}b{s}'.format(s=os.sep)

            def isparent(path1, path2):
                return os.path.commonprefix([path1, path2]) == path1

            def ischild(path1, path2):
                return os.path.commonprefix([path1, path2]) == path2

    if "#system":

        # Run command from default shell.

        # See subprocess for a better option.

        pass

if "##glob":

    '''
    Searches directories using POSIX glob patterns.

    Applications:

    - list files at a given level: os.glob('*/*/*')
    '''

if "##shutil":

    '''
    High level file operations based on `os`.
    '''

    import shutil

    if "#rmtree #rm -rf":

        # Recursive directory removal like rm -rf:

        temp = tempfile.mkdtemp()
        with file(os.path.join(temp, 'a'), 'a'): pass
        try:
            os.rmdir(temp)
        except OSError:
            pass
        else:
            assert False
        shutil.rmtree(temp)
        assert not os.path.exists(temp)

    if "#copyfile #cp":

        # Not a base utility since it can be done naively with with open read write.

        #shutil.copyfile(src, dst)
        pass

if "##tempfile":

    # Create temporary files.

    #<http://www.doughellmann.com/PyMOTW/tempfile/>

    import tempfile

    # The filename is given by dir + prefix + random + suffix.
    #
    # - dir defaults to gettempdir()
    # - prefix defaults to gettempprefix()
    #
    # Does not return a string, but an object.
    # Use `.name` to get the path string.

    temp = tempfile.NamedTemporaryFile(
        #dir = '/tmp',
        prefix = 'prefix_',
        suffix = '_suffix',
    )

    try:
        print 'temp:', temp
        print 'temp.name:', temp.name
        temp.write("asdf")
        temp.flush()
    finally:
        # File is deleted on close!
        temp.close()

    # Make a temporary directory instead of file.
    # Returns a path string.

    directory_name = tempfile.mkdtemp(
        dir = '/tmp',
        prefix = 'prefix_',
        suffix = '_suffix',
    )
    print directory_name
    shutil.rmtree(directory_name)

    # The default directory that will hold all of the temporary files:

    print 'gettempdir():', tempfile.gettempdir()

    # The basename prefix for new file and directory names:

    print 'gettempprefix():', tempfile.gettempprefix()

if "##logging":

    # Standard way to output error messages.

    # Advantages:

    # - has many useful built-in error formats
    # - has a level system
    # - easy to change where logs go, e.g. a file.

    # <http://docs.python.org/2/howto/logging.html>

    # TODO log all at once

    if "## defult logger":

        import logging

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

    if "##custom loggers":

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

if "##math":

    # Built-in functions:

    assert abs(-1) == 1

    if "##max":

        # Returns the first max item according to some metric:

        assert max(1, -2, 0)   == 1
        assert max([1, -2, 0]) == 1
        assert max([1, -2, 0, 2], key=lambda x: x*x) == -2

        # TODO best way to get the value of key withtout recalculating?

        def f(x): return x*x
        assert f(max([1, -2, 0, 2], key=f)) == 4

    import math

    assert abs(math.sin(0) - 0.0) < 0.01
    assert abs(math.cos(0) - 1.0) < 0.01
    assert abs(math.exp(0) - 1.0) < 0.01

    if "##sqrt":

        assert abs( math.sqrt(4) - 2.0 ) < 0.01

        try:
            math.sqrt(-1)
        except ValueError:
            pass
        else:
            assert False

    assert abs(math.pi     - 3.14) < 0.01
    assert abs(math.exp(0) - 1.0 ) < 0.01
    assert abs(math.exp(1) - 2.71) < 0.01
    assert math.floor( 1.5 ) == 1

    if "##random":

        import random

        if "##uniform":

            # Real on interval:

            n = 1000
            su = 0
            l = 0
            r = 1
            for i in xrange(n):
                rand = random.uniform(l,r)
                #print rand
                assert rand >= l and rand <= r
                su += random.uniform(0,1)

            # Check average:

            assert su/float( (r - l) ) - n < 1

        if "##randint":

            # Uniform int on interval.

            print random.randint(0,3)

        if "##choice":

            # Take one element at random from an iterable.

            assert random.choice([0, 1]) in [0, 1]

        if "##sample":

            # Takes n *different* elements at random from iterable. Returns an iterable.

            vals = {1:0, 2:0, 3:0}
            n = 2
            for i in random.sample(vals.keys(), 2):
                assert i in vals.keys()
                vals[i] += 1

            for i in vals.keys():
                assert vals[i] == 0 or vals[i] == 1

            assert sum(vals[k] for k in  vals.keys()) == n

if "##environ ##environment variables":

    #environment variables

    import os

    #a dictionnary that contains all environment variables:

    print os.environ

    #get one from the dict:

    if 'PATH' in os.environ:
        print "PATH = " + os.environ['PATH']

    for v in os.environ:
        print v + ' = ' + os.environ[v]

    #always check if it is defined!

    ###set values

    ####good

    #one by one

    os.environ['SOME_VAR'] = 'abc'
    assert os.environ['SOME_VAR'] == 'abc'

    #subprocess will inherit this, for example those opened with `Popen`.

    ####bad

    #this does *not* work!:
    os.environ = {'a':'b'}
    #child process will not inherit it!

    #and now this won't reset environ either
    os.environ
    #the docs say it only sets os.environ the first time it is imported!

    #you have onlly change what the name environ means here.

if "##command line arguments ##argv":

    print 'sys.argv[0]  = ' + repr(sys.argv[0])
    print 'sys.argv[1:] = ' + repr(sys.argv[1:])

if "##version":

    import sys
    print sys.version_info

    # Sample output:

        #sys.version_info(major=2, minor=7, micro=4, releaselevel='final', serial=0)

    if sys.version_info[0] == 2:
        #python 2.x code
        pass

    # Get version of module installed with pip:

        #pkg_resources.get_distribution("blogofile").version

    # PEP 8 recommends that modules define `__version__`, but many packages don't do that.
    #http://legacy.python.org/dev/peps/pep-0008/#version-bookkeeping

if "##exit status":

    #if no call is made to sys.exit, exit code is 0.

    sys.exit()
    sys.exit(0)
    sys.exit(1)
