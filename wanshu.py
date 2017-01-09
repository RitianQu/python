#!/usr/bin/python
# coding=utf-8



for i in range(1,1001):
    num = 0
    for j in range (1,i / 2 + 1):#每个数不会比该数一半大的数整除，除去自身
        if i % j == 0:
            num += j

    if num == i:#如果每个因子相加等于她本身，那么这个数为完数
        print "%d "%num,

print ""
