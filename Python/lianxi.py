#!/usr/bin/python
#coding=utf-8
def fun(char):#建立函数
    l = char.split(" ")#以空格为拆分字符
    char = ''.join(l)#用空字符串拼接列表l并赋值给char
    return char#返回值为char

while True:
    s = raw_input()
    if not len(s):#如果不为假则跳出循环
        break

    print "before:",s

    s = fun(s)
    print "after:",s
