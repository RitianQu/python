#!/usr/bin/python

f = open('text.txt','a+')

l = ['nihao\n','zaijian\n','hello\n','goodbye\n']

f.writelines(l)
