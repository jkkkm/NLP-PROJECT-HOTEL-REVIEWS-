# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:54:28 2023

@author: HP
"""

#QUESTION 2

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

#QUESTION 3
tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

#QUESTION 4
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

#QUESTION 5
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#QUESTION 6
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#QUESTION 7
tuple1 = (11, 22)
tuple2 = (99, 88)
list1 = list(tuple2)
list2 = list(tuple1)
tuple1 = tuple(list1)
tuple2 = tuple(list2)

print(tuple1)
print(tuple2)
tuple1
tuple2

#QUESTION 8
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)

