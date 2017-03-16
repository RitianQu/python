#!/usr/bin/python

def func(self):
    print 'bar'

def decorator(cls):
    cls.bar = func
    print cls
    return cls

@decorator
class Foo():
    pass

foo = Foo()
foo.bar()
