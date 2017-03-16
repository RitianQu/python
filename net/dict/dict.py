#!/usr/bin/python
# coding=utf-8

import MySQLdb,sys
from socket import *

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.bind(ADDR)
sockfd.listen(5)

while True:


    connfd,addr = sockfd.accept()
    print 'connected from :',addr
