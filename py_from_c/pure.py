# This is provided by the C file.
# But since we are embedding Python, we don't even need to create a separate
# .so file: it is provided directly through the Python invocation!
import defined_in_c

def multiply_plus_2(a,b):
    c = 0
    for i in range(0, a):
        c = c + b
    return c + defined_in_c.get_offset()
