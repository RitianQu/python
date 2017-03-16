#!/usr/bin/python

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next

class Linklist(object):
    def __init__(self):
        self.head = None

    def initlist(self,data):
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)
            p.next = node
            p = p.next

    def show(self):
        p = self.head.next
        while p != None:
            print p.value,
            p = p.next
        print ""

    def apphead(self,value):
        p = self.head

        node = Node(value)
        node.next = p.next
        p.next = node

    def delete(self):
        p = self.head

        p.next = p.next.next
