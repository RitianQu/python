#!/usr/bin/python

from SocketServer import *
from time import ctime

class Server(ThreadingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'got connection from',addr
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            self.request.send('[%s] :%s'%(ctime,data))

server = Server(('10.1.1.144',8888),Handler)

server.serve_forever()
