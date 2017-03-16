#!/usr/bin/python

l = [[2,5,6,3],[5,7,8,3],[1,6,7,3]]

max = l[0][0]
x = y = 0
for i in range(3):
    for j in range(4):
        if l[i][j] > max:
            max = l[i][j]
            x = i
            y = j
print "l[%d][%d] =%d" %(x,y,max)
