#!/usr/bin/python

from socket import *

HOST = '10.1.1.144'
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    sockfd.send(data)
    data = sockfd.recv(BUFSIZE)

    if not data:
        break;
    print(data)

sockfd.close()
