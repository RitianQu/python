#!/usr/bin/python
from addhead import *

l = Linklist()
l.initlist([1,2,3,4,5])

l.apphead(10)
l.apphead(11)
l.show()

l.delete()
l.delete()
l.show()
