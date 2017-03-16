#!/usr/bin/python

import re
# pattern = re.compile('[a-zA-Z]')
# print pattern
#
# result = pattern.findall('as3SiOPdj#@23qwe')
#
# print result
# result = re.findall(pattern,'as3SiOPdj#@23qwe')
# print result

# def testsearchandmatch():
#     s1="helloworld, i am 30 !"
#     w1 = "world"
#     m1 = re.search(w1, s1)
#     if m1:
#         print("find : %s" % m1.group())
#     if re.match(w1, s1) == None:
#         print("cannot match")
#     w2 = "helloworld"
#     m2 = re.match(w2, s1)
#     if m2:
#         print("match : %s" % m2.group())
# testsearchandmatch()

link = re.compile('\d+')
content = 'laowang-222hahah'
info = re.sub(link,'www.cnpythoner.com',content)
print info
