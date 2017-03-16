#!/usr/bin/python
# coding=utf-8

import MySQLdb,sys
from socket import *
from time import ctime

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
BUFSIZE = 1024

def do_register(db):
    cursor = db.cursor()
    while True:
        pid = input("input id(int) >>")
        sql = "select * from register where id = %d"%pid
        print sql
        cursor.execute(sql)
        print '============'
        data = cursor.fetchone()

        if not data:
            break
        else:
            print "sorry the id existe"

    passwd = input("input passwd(int) >>")
    name = raw_input("input your name >>")



    sql = "insert into register values(%d,'%s',%d)"%(pid,name,passwd)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()
        return

    print "register OK!"



def do_login(db):
    cursor = db.cursor()
    name = raw_input("input name(string) >>")
    passwd = input("input passwd(int) >>")
    pid = input('input id(int) >>')

    sql = "select * from register where name = '%s' and passwd = %d and id = %d"%(name,passwd,pid)
    cursor.execute(sql)
    data = cursor.fetchone()

    if data == None:
        print "sorry,your name or passwd or pid is error!"
        return
    else:
        dic(db,name)
def dic(db,name):
    while True:
        print '''
        --------------command-------------
        --1: search  2. history  3: quit--
        ----------------------------------
        '''
        n = input('please input >>')
        if n not in [1,2,3]:
            print 'input error!!!'
            sys.stdin.flush()
            continue
        elif n == 1:
            search(db,name)
        elif n == 2:
            history(db,name)
        elif n == 3:
            return

def search(db,name):

    a = raw_input('please input >>')
    cursor = db.cursor()
    sql = "insert into history values('%s','%s','%s')"%(name,ctime(),a)
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print "sorry operation failed"
        db.rollback()


    print "insert OK!"
    f = open('dict.txt','r')
    for i in f:
        b = i.split(' ')
        if a == b[0]:
            print i

def history(db,name):
    cursor = db.cursor()
    sql = "select * from history where name = '%s'" %name
    try:
        cursor.execute(sql)

        results = cursor.fetchall()

        for field in cursor.description:
            print field[0],"            ",

        print ''

        for row in results:
            name = row[0]
            time = row[1]
            word = row[2]
            print "%s    %s    %s    "%(name,time,word)

    except:
        print "sorry operation failed"
        db.rollback()
        return

def main():
    db = MySQLdb.connect('localhost','root','1','dict')
    while True:
        print '''
        --------------command-------------
        --1: login  2. register  3: quit--
        ----------------------------------
        '''
        sockfd = socket(AF_INET,SOCK_STREAM,0)
        sockfd.connect(ADDR)
        num = input("Input command >>")

        if num not in [1,2,3]:
            print "input error!"
            sys.stdin.flush()
            continue
        elif num == 1:
            do_login(db)
        elif num == 2:
            do_register(db)
        elif num == 3:
            break


if __name__ == '__main__':
    main()
