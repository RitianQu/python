#!/usr/bin/python
#coding=utf-8

class Node(object):
    def __init__(self,val,next = None):
        self.value = val
        self.next = next
#定义一个模型节点
class Linklist(object):
    def __init__(self):
        self.head = None#头节点

    def __getitem__(self,key):
        if self.is_empty():
            print "linklist is empty"
            return
        else:
            return self.getitem(key)

    def __setitem__(self,key,value):
        if key < 0 or key >self.getlength():
            print "The given key is error"
            return
        else:
            self.delete(key)
            return self.insert(key,value)

    def initlist(self,data):
        self.head = Node(0)#设置头结点，默认头结点里为无用值
        p = self.head

        for i in data:
            node = Node(i)#实例化一个对象
            p.next = node#指针指向下一个节点
            p = p.next

    def getlength(self):
        p = self.head.next
        l = 0
        while p != None:

            l += 1
            p = p.next
        return l#计算长度

    def show(self):
        p = self.head.next

        while p != None:
            print p.value,
            p = p.next
        print ""#显示所有节点里的值

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False#判断长度是否为0

    def clear(self):
        self.head = None#清除列表，

    def append(self,value):
        p = self.head

        while p.next != None:

            p = p.next

        p.next = Node(value)

    def insert(self,index,value):
        if index < 0 or index > self.getlength():
            print "index is error"
            return

        p = self.head

        i = 0
        while p.next != None and i < index:
            p = p.next
            i += 1

        node = Node(value)
        node.next = p.next
        p.next = node

    def delete(self,index):
        if index < 0 or index >self.getlength():
            print "index is error"
            return

        p = self.head

        i = 0
        while i < index:
            p = p.next
            i += 1

        p.next = p.next.next

    def index(self,value):
        if self.is_empty():
            print "Linklist is empty"
            return
        p = self.head.next
        i = 0
        while p != None and p.value != value:
            p = p.next
            i += 1

        if p == None:
            return -1
        else:
            return i

    def getitem(self,index):
        if self.is_empty():
            print "link is empty"
            return

        i = 0
        p = self.head.next

        while p != None and i < index:
            i += 1
            p = p.next

        if p == None:
            return -1
        else:
            return p.value
