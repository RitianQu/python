#!/usr/bin/python
flag = 1
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            flag = 0
            break
            print "%d"%i
