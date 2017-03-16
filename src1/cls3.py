#!/usr/bin/python

class Person():
    age = 10

    def color(self,color):
        print "%s is %s"%(self.name,color)


Lilei = Person()

print Lilei.age

Lilei.name = "Lilei"

print Lilei.name

Lilei.color('black')

print dir(Lilei)
