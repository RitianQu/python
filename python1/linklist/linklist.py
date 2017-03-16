#!/usr/bin/python
#coding=utf-8

class Node(object):
    def __init__(self,val,p = None):
        self.value = val
        self.p = p
        self.prior = None
#做一个类，为每次创建结点时调用
class Linklist(object):
    def __init__(self):
        self.head = None#头结点为None

    def initlist(self,data):#初始化链表
        self.head = Node(0)
        p = self.head

        for i in data:
            node = Node(i)

            p.next = node
            node.prior = p
            p = p.next
        p.next = self.head
        self.head.prior = p
    def show(self):
        p = self.head.next

        while p != self.head:
            print p.value,
            p = p.next
        print ""

    def insert(self,index,value):
        p = self.head
        j = 0
        while p.next != self.head and j < index:
            p = p.next
            j += 1
        q = Node(value)
        q.next = p.next
        p.next.prior = q
        p.next = q
        q.prior = p

    def delete(self,index):
        p = self.head
        i = 0
        while p != self.head and i < index:
            p = p.next
            i += 1
        p.next = p.next.next
        p.next.prior = p
