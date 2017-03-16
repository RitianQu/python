#!/usr/bin/python

l = [3,5,1,7,9,2,4,8,6,65,35]
# b = len(l)
# l1 = []
# while True:
#     b -= 1
#     a = min(l)
#
#     l1.append(a)
#     l.remove(a)
#     if b == 0:
#         break
# print l1
# def sort():
#     l = [3,5,1,7,9,2,4,8,6]
#     for i in range(len(l)):
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#     print l
#
# sort()
# def sort():
#     l = [3,5,1,7,9,2,4,8,6,65,35]
#     for i in range(len(l)):
#         min = l[i]
#         for j in range(i+1,len(l)):
#             if min > l[j]:
#                 min = l[j]
#         if l[i] != min:
#             l[i],min=min,l[i]
#     print l
# sort()

def sort():
    for i in range(1,len(l)):
        s = l[i]
        j = i
    while j > 0 and l[j-1] > s:
        l[j] = l[j-1]
        j -= 1

    l[j]=s
    print l
sort()
