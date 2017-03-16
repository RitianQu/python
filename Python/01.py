#!/usr/bin/python
#coding=utf-8

# 杨辉三角
l = []

for x in range(0,10): #取十行
    l.append([])      #每循环一次添加一个空列表
    l[x].append(1)    #每循环一次 以x为列表名并且在列表中添加一个1
    for y in range(1,x+1):
        num = l[x-1][y-1]+l[x-1][y] #利用下角标计算出要求的变量和
        l[x].append(num) #把num变量添加到列表当中
    l[x].append(0)  #在每个列表后加入一个0
for x in range(0,10):
    for y in range(x+1):
        print "%d"%l[x][y],
    print ""
