#!/usr/bin/python
#coding=utf-8


for  i in [1,2,3,4,5]:
    print "hi,%d"%i
    if i == 3:
        continue
else:
    print "gameover"

for i in range(1,50,2):#从1到50步长为2遍历
    print i,
