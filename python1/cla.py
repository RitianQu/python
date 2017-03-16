#!/usr/bin/python

class Person(object):


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def color(self,color):
        print "%s is %s,he is %d"%(self.name,color,self.age)

Lilei = Person("Lilei",20)
Hanmei = Person("Hanmei",22)

Lilei.color("black")
Hanmei.color("yellow")
