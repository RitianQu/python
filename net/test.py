#!/usr/bin/python

from socket import *

HOST = '10.1.1.144'
PORT = 8887

sockfd = socket(AF_INET,SOCK_STREAM,0)

sockfd.bind((HOST,PORT))

sockfd.listen(5)


while True:
    sockfd.setblocking(False)
    connfd,addr = sockfd.accept()
    buf = connfd.recv(1024)
    connfd.send(buf)
    connfd.close()
    print '+++++++++++++'
