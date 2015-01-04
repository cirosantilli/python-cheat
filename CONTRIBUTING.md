# Contributing

Style: follow PEP 8 and the Google Style Guide.

Use single quotes for string literals.

The cheats use the following "literate Python" style that mixes prose with runnable code:

## Markdown

Prose is written mostly in markdown, except that code blocks are not indented.

Never use indented lists with runnable code blocks in them as that breaks Python which is indentation based.

## Commented out code

Commented out code, e.g. code that would break the examples or take drastic actions like filesystem writing, has no space after the `#`, prose has one space:

```py
# Look at the following code:

#shtuil.rmtree('')

# But don't run it.
```

## Large comments with triple double quoted strings

We leave it to your discretion what consists of a "large" comment block, but as a rule of thumb we consider 4 lines large.

```py
"""
This explanation:

- spans
- more
- than
- four lines
"""
```

## Headers with if

Headers are replaced by `if` blocks so as to give visual indentation.

Important terms in the headers are prefixed with double hashes `##` so they can be easily searched for later.

E.g.:

```py
if '##string':

    # Strings are useful!

    s = 'Hello world!'

    if '##unicode':

        # Unicode is a pain!

        u = u'Hello world!'

        pass
```

If there is no non-comment line inside and `if` "header", add a `pass` statement to to it right after the `if`:

```py
if '##unicode':

    pass

    # TODO this is too hard, so this section is empty.
```

But note that triple quoted string comments work, so don't add `pass` in that case:

```py
if '##unicode':

    """
    This is too hard.

    This is why this section is empty.
    """
```

Multiple related terms can be hashed in a single `if` to make searching easier:

```py
if '##import ##module':
```
