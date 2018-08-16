# This is provided by the C file.
# But since we are embedding Python, we don't even need to create a separate
# .so file: it is provided directly through the Python invocation.
import emb

def multiply(a,b):
    print "Number of arguments", emb.numargs()
    print "Will compute", a, "times", b
    c = 0
    for i in range(0, a):
        c = c + b
    return c
