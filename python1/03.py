#!/usr/bin/python

a = input()
b = input()
c = input()

if a > b:
    a ^= b
    b ^= a
    a ^= b
if b > c:
    b ^= c
    c ^= b
    b ^= c
if a > c:
    a ^= c
    c ^= a
    a ^= c
print (a,b,c)
