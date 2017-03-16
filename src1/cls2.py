#!/usr/bin/python

__metaclass__ = type
class Person():

    print "This is a class"

    age = 10

    def __init__(self,name):
        print "init func"
        self.name = name

    def color(self,color):
        print "%s is %s"%(self.name,color)

Lilei = Person('Lilei')

print Lilei.age

print Lilei.name

Lilei.color('black')

print "****************************8"


Hanmei = Person('Hanmei')

print Hanmei.age

print Hanmei.name

Hanmei.color('yellow')


