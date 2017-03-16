#!/usr/bin/python

class List(object):
    def __init__(self,l):
        MAX = 24
        self.l = []
        while MAX:
            self.l.append(None)
            MAX -= 1
        for i in range(len(l)):
            self.l[i] = l[i]

    def my_append(self,value):
        i = 0
        while self.l[i] != None:
            if i >= len(self.l):
                print "error"
                break
            i += 1
        self.l[i] = value
    def my_insert(self,index,value):
        i = 0
        while self.l[i] != None:
            if i >= len(self.l):
                print "error"
                break
            i += 1
        while i != index:
            self.l[i] = self.l[i-1]
            i -= 1
        self.l[index] = value
    def my_remove(self,value):
        i = 0
        while self.l[i] != value:
            if i >= len(self.l):
                print "error"
                break
            i += 1
        while self.l[i] != None:
            self.l[i] = self.l[i + 1]
            i += 1
        self.l[i] = None


a = List([1,2,3,4,5])

a.my_remove(2)
print a.l
