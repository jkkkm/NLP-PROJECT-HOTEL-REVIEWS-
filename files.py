# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:48:53 2023

@author: HP
"""

def file_read(fname):
        content_list = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_list.append(line)
                print(content_list)

file_read("C:/Users/HP/Downloads/SalaryData_Test.csv")