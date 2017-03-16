#!/usr/bin/python

import MySQLdb

db = MySQLdb.connect('localhost','root','1','student')
cursor = db.cursor()

# cursor.execute('drop table if exists stu')
#
# sql = '''create table stu (name char(20) not null,
#          sex char(1),
#          age int)'''
#
# cursor.execute(sql)

def my_insert():
    print 'name >>>',
    a = raw_input()
    print 'sex >>>',
    b = raw_input()
    print 'age >>>',
    c = input()
    print 'score >>>',
    d = input()
    sql = ("insert into data values ('%s','%s',%d,%d)"%(a,b,c,d))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print '++++++'
        db.rollback()

def my_delete():
    print 'score >>>',
    a = input()
    sql = ("delete from data where score < %d"%a)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print 'failed delete'
        db.rollback()

def my_updata():
    print 'score >>>',
    a = input()
    print 'name >>>',
    b = raw_input()
    sql = ("update data set score = %d where name = '%s'"%(a,b))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print 'Error : failed update'
        db.rollback()

def my_search():
    try:
        cursor.execute('select * from data')
        data = cursor.fetchall()

        for i in cursor.description:
            print i[0],

        print ''

        for com in data:
            name = com[0]
            sex = com[1]
            age = com[2]
            score = com[3]
            print 'name:{0},sex:{1},age:{2},score:{3}'.format(name,sex,age,score)
    except:
        print 'Error:unable to fecth data'

def my_registry():
    print 'name >>>',
    a = raw_input()
    print 'passwd >>>',
    d = input()
    print 'sex >>>',
    b = raw_input()
    print 'age >>>',
    c = input()

    sql = ("insert into data values ('%s',%d,'%s',%d)"%(a,b,c))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print '++++++'
        db.rollback()

def my_login():
    try:
        print 'name :',
        a = raw_input()
        print 'passwd :',
        b = input()

        cursor.execute('select * from stu')
        data = cursor.getchall()

        for com in stu:
            name = com[0]
            passwd = com[1]
            if name == a and passwd == b:
                print 'login'
            else:
                print 'please registry'


if __name__ == '__main__':
    print '----------------------'
    print '|------1 registry----|'
    print '|------2 login ------|'
    print '|------3 insert------|'
    print '|------4 delete------|'
    print '|------5 updata------|'
    print '|------6 search------|'
    print '|------7  quit ------|'
    print '----------------------'
    while True:
        num = input()
        if num == 3:
            my_insert()
        elif num == 4:
            my_delete()
        elif num == 5:
            my_updata()
        elif num == 6:
            my_search()
        elif num == 7:
            break
        elif num == 1:
            my_registry()
        elif num == 2:
            my_login()
