#!/usr/bin/python

from socket import *
from time import ctime,sleep
import sys,os

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)
print 'put your name',
while True:
    while True:
        data = raw_input()
        sockfd.sendto(data,ADDR)
        break
    data,addr = sockfd.recvfrom(BUFSIZE)
    print '%s log in'%data
    while True:
        data = raw_input()
        sockfd.sendto(data,ADDR)
        data,addr = sockfd.recvfrom(BUFSIZE)
        print data
