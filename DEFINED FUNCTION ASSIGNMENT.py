# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 23:43:05 2023

@author: HP
"""

#question 1
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

#question 2
def multiply(numbers):  
    total = 1
    for n in numbers:
        total *= n  
    return total  
print(multiply((8, 2, 3, -1, 7)))

#question 3
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

#QUESTION 4
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 

#QUESTION 5
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))

#QUESTION 6
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

#QUESTION 7
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(10))

#QUESSTION 8
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

#QUESTION 9
def printValues():
	l = list()
	for i in range(1,30):
		l.append(i**2)
	print(l)
		
printValues()

