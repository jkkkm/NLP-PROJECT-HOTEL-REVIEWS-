# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:40:22 2023

@author: HP
"""
#Find all matching string that contains “ai”.
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
x

#Make a search that returns no match:
import re
 
Substring ='string'
 
 
String1 ='''We are learning regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))

#Replace the first two occurrences of a white-space character with the digit 5
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '5')
  str1 = char + str1[2:]

  return str1

print(change_char('restart'))