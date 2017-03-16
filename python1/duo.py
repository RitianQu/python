#!/usr/bin/python
#coding=utf-8
class Speaker(object):
    name = 'mao'

class Calculator(Speaker):
    name = 'luosifu'
    age = 88

class Talker(Speaker):
    name = 'liyong'
    sex = 'man'

class TalkerCalculator(Calculator,Talker):
    pass

A = TalkerCalculator()

print TalkerCalculator.mro()#测试继承顺序

print A.name
print A.sex
print A.age
