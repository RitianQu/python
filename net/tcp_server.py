#!/usr/bin/python
# coding=utf-8

from socket import *
from time import ctime

HOST = '10.1.1.144'
PORT = 8887

sockfd = socket(AF_INET,SOCK_STREAM,0)#创建套接字，第一个参数为ipv4，第二个参数为套接字类型，默认为tcp，第三个参数默认为0

sockfd.bind((HOST,PORT))#绑定主机

sockfd.listen(5)#监听，参数为最多监听5个

connfd,addr = sockfd.accept()#接收客户连接，返回值为一个套接字和访问地址

print connfd
print addr
while True:
    #sockfd.setblocking(0)
    data = connfd.recv(1024)#接收消息，参数为接收消息的最大字节数
    print len(data)
    if data == "\r\n":
        break
    print data
    print type(data)
    connfd.send('[%s]\n'%ctime())#发送消息
