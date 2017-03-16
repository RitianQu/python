#!/usr/bin/python
#coding=utf-8
l = [[5,3,8,6],
     [4,7,2,9],
     [3,1,6,4]]

for i in range(3):
    line_max = max(l[i])#求第i行的最大值
    k = l[i].index(line_max)#把第i行的最大值定位的赋值给k
 #    print "==========%d"%k
    num = l[i][k]#i，k为最大值的下角标
    for j in range(3):
        if l[j][k] > num:
            num = l[j][k]
    if num == line_max:
        print "l[%d][%d] = %d"%(i,k,num)
#打擂台求最大值
max = l[0][0]
x = y = 0
for i in range(3):
    for j in range(4):
        if l[i][j] > max:
            max = l[i][j]
            x = i
            y = j
print "l[%d][%d] = %d"%(x,y,max)
