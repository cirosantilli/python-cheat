fileinput emulates the typical gnu interface:

1) read from files with filenames in stdin[1:], one by one
2) if none is given, read from stdin.

to run the tests on main, do:

    ./test_main.py

to see what `main.py` does, try it out:

    ./main.py a b
    ./main.py b a
    echo 'c\nc2' | ./main.py
    echo 'c\nc2' | ./main.py a b
