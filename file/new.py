#!/usr/bin/python
import os

l = os.listdir('.')
f_new = open('new.txt','w+')

for i in l:
    if os.path.isfile(i):
        f = open(i,'r')
        a = f.read()
        print a

        f_new.write(a)
    elif os.path.isdir(i):
        os.chdir('./'+i)
        l1 = os.listdir('.')
        for j in l1:
            f1 = open(j,'r')

            b = f1.read()
            print b
            f_new.write(b)
