#!/usr/bin/python
from signal import *
import socket,traceback,os,sys

host = ''
port = 8889

s = socket.socket()
s.bind((host,port))
s.listen(5)

print 'Parent at %d listening for connections'%os.getpid()

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    signal(SIGCHLD,SIG_IGN)

    pid = os.fork()

    if pid:
        c.close()
        continue
    else:
        s.close()
        try:
            print 'Child from %s being hanled PID %d'%(c.getpeername(),os.getpid())

            while True:
                data = c.recv(1024)
                if not len(data):
                    break
                print data
                c.send('recv your message')
        except (KeyboardInterrupt,SystemExit):
            raise
        except:
            traceback.print_exc()
        c.close()
        sys.exit(0)
