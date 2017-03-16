#!/usr/bin/python
#coding=utf-8
class A(object):
    '''
    This is a test
    '''

    def __getattr__(self,name):
        print "U use getattr"

    def __setattr__(self,name,value):
        print "U use setattr"
        self.__dict__[name] = value
    pass

a = A()

print dir(a)

print a.__doc__
print a.__class__

a.x#调用一个不存在的变量时会调用getattr
a.x = 7#给一个不存在的变量赋值时会调用setattr
print a.x
print a.__dict__
