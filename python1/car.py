#!/usr/bin/python
#coding=utf-8

class Qiche(object):
    lun = 4
    fangxiangpan = 1
    fadongji = 1
    paiqiguan = 1
class Bus(Qiche):
    zuo = 32

class Car(Qiche):
    zuo = 2
    qigang = 4

class Suv(Qiche):
    zuo = 4

class Runcar(Car):
    qigang = 12
    print 'qigang'

A = Qiche()
B = Bus()
C = Car()
D = Suv()
E = Runcar()
print E.qigang
print E.fadongji
