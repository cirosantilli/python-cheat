# Python from C

How to call Python from c.

This is called embedding python.

It basically means calling the Python interpreter from C, and passing values between the two.

Documented at: <https://docs.python.org/3/extending/embedding.html>

Examples:

-   [eval.c](eval.c): simply `eval` a Python string in C, don't communicate any values between the two. Not very exciting.

-   [pure.py](pure.py) and [pure.c](pure.c): full integration, pass function arguments and get results back.

    Also shows how to extend Python with C through the embedding, providing a C implementation of a Python functionality.

Run all examples:

    ./test

Source: [test](test)
