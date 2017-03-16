#!/usr/bin/python
# coding=utf-8

import MySQLdb

db = MySQLdb.connect('localhost','root','1','testdb')#生成操作数据库的对象

cursor = db.cursor()#生成操作内容的对象

cursor.execute('select version()')#使用execute可以使用sql的语句

data = cursor.fetchone()#使用fetchone可以获得数据库一条信息

print 'Database version:',data

cursor.execute('drop table if exists newtab')

sql = '''create table newtab (first_name char(20) not null,
         last_name char(20),
         age int,
         sex char(1),
         income float)'''

cursor.execute(sql)#创建表

sql = '''insert into newtab values ('mac','mohan',20,'m',5000)'''#插入信息

try:
    cursor.execute(sql)
    db.commit()#提交
except:
    print '========='
    db.rollback()#返回到提交前状态

db.close()
