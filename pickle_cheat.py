#!/usr/bin/env python
import pickle

if 'slots':

    if 'Default getstate and setstate with slots':

        # Use -1 pickling version.
        # http://stackoverflow.com/questions/2204155/why-am-i-getting-an-error-about-my-class-defining-slots-when-trying-to-pickl/2204702#2204702

        class C(object):
            __slots__ = 'a'
            def __init__(self, a):
                self.a = a
        s = pickle.dumps(C(1), -1)
        assert pickle.loads(s).a == 1

        # Expects a tuple of (__dict__, dict with __slots__ as keys).
        # https://www.python.org/dev/peps/pep-0307/

        class C(object):
            __slots__ = 'i', 'j'
            def __init__(self, i):
                self.i = i
                self.j = -i
            def __getstate__(self):
                return (None, {'i': self.i})
        assert pickle.loads(pickle.dumps(C(1), -1)).i == 1
        try:
            assert pickle.loads(pickle.dumps(C(1), -1)).j == -1
        except AttributeError:
            pass
        else:
            raise

        class C(object):
            __slots__ = 'i'
            def __init__(self, i):
                self.i = i
            def __setstate__(self, t):
                d = t[1]
                self.i = d['i']
        assert pickle.loads(pickle.dumps(C(1), -1)).i == 1

        # Or fully explicit dict.

        class C(object):
            __slots__ = ('i',)
            def __init__(self, i):
                self.i = i
            def __getstate__(self):
                return { k:getattr(self, k) for k in self.__class__.__slots__ }
            def __setstate__(self, d):
                for k in d:
                    setattr(self, k, d[k])
        assert pickle.loads(pickle.dumps(C(1), -1)).i == 1

        # All but one.
        # http://stackoverflow.com/questions/6635331/pickle-all-attributes-except-one/41896767#41896767

        class C(object):
            _pickle_slots = ['i']
            __slots__ = _pickle_slots + ['j']
            def __init__(self, i, j):
                self.i = i
                self.j = j
            def __getstate__(self):
                return (None, {k:getattr(self, k) for k in C._pickle_slots})
        o = pickle.loads(pickle.dumps(C(1, 2), -1))
        assert o.i == 1
        try:
            o.j
        except:
            pass
        else:
            raise

if 'instancemethod error':

    # http://stackoverflow.com/questions/27318290/why-can-i-pass-an-instance-method-to-multiprocessing-process-but-not-a-multipro

    # Basic example

    class A(object):
        def z(self):
            return  1
    try:
        pickle.dumps(A.z, -1)
    except pickle.PicklingError:
        pass
    else:
        raise

    # Less obvious via inner member:

    class A(object):
        def __init__(self):
            self.f = self.f
        def f():
            return 1
    try:
        pickle.dumps(A(), -1)
    except pickle.PicklingError:
        pass
    else:
        raise

    # Fine with regular functions:

    def f():
        return 1
    class A(object):
        def __init__(self):
            self.f = f
    s = pickle.dumps(A(), -1)
    pickle.loads(s).f() == 1

if '# getstate # setstate':

    if 'Minimal example':

        """
        - __getstate__ spits a dict
        - __setstate__ reads the dict and uses it to setup an object
        """

        class C(object):

            def __init__(self, i):
                self.i = i

            def f(self):
                return self.i + 1

            def __getstate__(self):
                return {'a': self.i}

            def __setstate__(self, d):
                self.i = d['a']

        assert pickle.loads(pickle.dumps(C(1), -1)).i == 1

        # You don't need to pickle methods.
        assert pickle.loads(pickle.dumps(C(1), -1)).f() == 2

    if 'Example that shows call order':

        x = 0

        class C(object):

            def __init__(self, i):
                self.i = i

            def __getstate__(self):
                global x
                x = 1
                self.i *= 2
                return self.__dict__

            def __setstate__(self, d):
                global x
                x = 2
                self.__dict__ = d
                self.i *= 3

        c = C(1)
        assert c.i == 1
        assert x == 0

        s = pickle.dumps(C(1))
        # __getstate__ was called.
        assert x == 1
        # But it is not called on the original object, which was not changed.
        assert c.i == 1

        c2 = pickle.loads(s)
        # __setstate__ was called.
        assert x == 2
        assert c.i == 1
        assert c2.i == 6

if '# inheritance':

    # Works by default without custom methods.

    class C(object):
        def __init__(self, i):
            self.i = i
    class D(C):
        def __init__(self, i, j):
            super(self.__class__, self).__init__(i)
            self.j = j
    assert pickle.loads(pickle.dumps(C(1), -1)).i == 1
    assert pickle.loads(pickle.dumps(D(1, 2), -1)).i == 1
    assert pickle.loads(pickle.dumps(D(1, 2), -1)).j == 2
