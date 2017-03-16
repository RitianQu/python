#!/usr/bin/python

from socket import *
from time import ctime
import sys

HOST = '10.1.1.144'
PORT = 8888
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)
sockfd.bind(ADDR)

while True:
    data,addr = sockfd.recvfrom(BUFSIZE)
    print data

    sockfd.sendto('[%s]'%ctime(),addr)
