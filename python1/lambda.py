#!/usr/bin/python
#coding=utf-8
class People(object):
    name = "nice" #共有属性
    age = 22

    def color(self,color):
        self.language = "English" #对象的属性
        print "%s is %s,he is a %s,he speak %s"%(self.name,color,self.sex,self.language)
me = People()
print me.name
print me.age
me.sex = "man"
#print People.sex
me.color("black")
print me.language
