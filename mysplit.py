#!/usr/bin/python
# coding=utf-8

def fun(char):
    l = char.split(' ')#以空格为分隔符分割
    char = ''.join(l)#以空字符串拼接
    l = char.split('-')#以-为分隔符分割
    char = ''.join(l)

    return char



while True:
    s = raw_input()
    if not len(s):
        break

    print "before :",s

    s = fun(s)

    print "after:",s
