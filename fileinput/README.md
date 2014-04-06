`fileinput` implements the typical POSIX / GNU interface:

1) read from files with filenames in stdin[1:], one by one
2) if none is given, read from stdin.

Run the tests:

    ./test_main.py

Understand what `main.py` does:

    ./main.py a b
    ./main.py b a
    echo 'c\nc2' | ./main.py
    echo 'c\nc2' | ./main.py a b
