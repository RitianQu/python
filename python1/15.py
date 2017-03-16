#!/usr/bin/python
#coding=utf-8

def fun(a,b):
    print a,b
#位置传参
fun(1,2)
#关键字传参
fun(1,b=2)
#列表传参
l = [5,6]
fun(*l)
#字典传参
d = {'a':1,'b':2}
fun(**d)  #===>fun(b = 1,a = 3)
#def fun1(x,*args（收集散列参数）,**kwargs（收集键值对参数）)：
