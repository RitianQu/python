#!/usr/bin/python

from time import ctime,sleep
import os,threading

def music(name):
    print ('i was listening to mucis %s ,%s'%(name,ctime()))
    #print os.getpid()
    sleep(2)

def move(name):
    print ('i was at the movie %s! %s'%(name,ctime()))
    #print os.getpid()
    sleep(5)
def player(name):
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    else:
        print('error:The format is not recogzed')
l = ['Baby.mp3','Avatar.mp4']
threads = []
# t1 = threading.Thread(target = music,args = ('baby',))
# t2 = threading.Thread(target = move,args = ('afanda',))
files = range(len(l))
for i in files:
    t = threading.Thread(target = player,args = (l[i],))
    threads.append(t)
# threads.append(t1)
# threads.append(t2)

if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    print os.getpid()
    print ('all over %s'%ctime())
