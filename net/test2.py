#!/usr/bin/python

from socket import *

HOST = '192.168.1.106'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    sockfd.send(data)
    data = sockfd.recv(BUFSIZE)

    if not data:
        break;
    print(data)

sockfd.close()
