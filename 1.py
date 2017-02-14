#!/usr/bin/python
#coding=utf-8

#杨辉三角
a = input()

l = [ [1],[1,1] ]

for i in range(2,a):#终端输入a从2到a循环
    #print l
    l.append([1,1])#在列表l中加入一个【1,1】的列表
    for j in range(1,i):
        l[i].insert(j,(l[i-1][j-1]+l[i-1][j]))#在l【i】列表中添加以j为位置的变量

for x in l:
    for y in x:
        print "%5d"%y,
    print ''
