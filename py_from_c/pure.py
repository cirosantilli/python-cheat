# This is provided by the C file.
# But since we are embedding Python, we don't even need to create a separate
# .so file: it is provided directly through the Python invocation!
import emb

def multiply_plus_2(a,b):
    c = 0
    for i in range(0, a):
        c = c + b
    return c + emb.get_offset()
