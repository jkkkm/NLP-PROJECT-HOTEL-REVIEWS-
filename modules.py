# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:11:33 2023

@author: HP
"""
#question 1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#question 2
def other_function(parameter):
    return parameter + 5

def main_function():
    x = 10
    print(x)    
    x = other_function(x)
    print(x)
    
#question 3
def function_local(a):
	print('a is -> ',a)
	a = 50
	print('After new value within the function a is -> ',a)
a = 100
function_local(40)
print('Value of a is ->',a)

def function_local():
        global a
        print('a is -> ',a)
        a = 50
        print('After new value within the function a is -> ',a)
a = 100
function_local()
print('Value of a is ->',a)

