#!/usr/bin/python

a = raw_input()

flag = 0
for i in a:
    if i == str:
        flag = 0
        print i,
    elif i == ' ':
        flag = 1
        print i,
    elif flag == 1:
        if i == str:
            print i,
        elif i == ' ':
            pass
print a
