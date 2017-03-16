#!/usr/bin/python

class C1(object):
    def setname(self,who):
        self.name = who
        print "in:%s"%(self.name)

I1 = C1()
I1.setname('bob')
print "out:%s"%(I1.name)
