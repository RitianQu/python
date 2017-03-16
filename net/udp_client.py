#!/usr/bin/python

from socket import *
from time import ctime
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

sockfd = socket(AF_INET,SOCK_DGRAM)
while True:
    data = raw_input()
    if not data:
        break

    sockfd.sendto(data,ADDR)
    data,addr = sockfd.recvfrom(BUFSIZE)
    print data
