#!/usr/bin/python

year=input()
mon=input()
day=input()
print "%d-%d-%d"%(year,mon,day)

if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print "%d :run"%year
    
