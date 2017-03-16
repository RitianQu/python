#!/usr/bin/python

class TestStaticMethod(object):
    @staticmethod
    def foo():
        print "calling static method foo()"


class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print "calling class method foo|()"
        print "class",cls.__name__
        print


A = TestStaticMethod()
A.foo()

B = TestClassMethod()
B.foo()
print dir(B)

TestStaticMethod.foo()
