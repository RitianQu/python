#!/usr/bin/python

for i in range(1,1001):
    a = 0
    for j in range(1,1001):
        if i % j == 0 and i > j:
            a += j
    if i == a:
        print "%d"%a
