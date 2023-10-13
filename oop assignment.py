# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:01:22 2023

@author: HP
"""
#question 1 Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Zeeshan')
p.say_hi()

#question 2 Create clock class that containt Hr min sec. Accept the value and display it
class clock:   
    def __init__(self):
        self._hours = 12
        self._minutes = 0
        self._seconds = 0

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def show(self):
        print ("%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))
class clock:   
    def __init__(self, hours, minutes, seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds



clk = clock(12, 34, 2)
clk


        