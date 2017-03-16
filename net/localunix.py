#!/usr/bin/python

import socket
import sys
import os

server_address = './test'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

print 'starting up on %s'%server_address
sock.bind(server_address)
sock.listen(5)

while True:
    print 'waiting for a connection'
    connection,client_address = sock.accept()
    print >>sys.stderr,'connection from',client_address
    while True:
        data = connection.recv(16)
        print >>sys.stderr,'received "%s"'%data
        if data:
            print >>sys.stderr,'sending data back to the client'
            connection.sendall(data)
        else:
            print >>sys.stderr,'no data from',client_address
            break
    connection.close()
