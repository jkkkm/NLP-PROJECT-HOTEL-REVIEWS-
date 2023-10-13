# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:29:44 2023

@author: HP
"""
#question 1
import datetime

print(datetime.datetime.today().time())

#question 2
import datetime

print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(5))

#question 3
import datetime

print('current date:')
print(datetime.date.today())
print('current date and time:')
print(datetime.datetime.now())
print('current year:')
print(datetime.date.today().year)
print('current month:')
print(datetime.date.today().month)
print('current month name:')
print(datetime.date.today().strftime('%B'))
print('current week of year:')
print(datetime.date.today().isocalendar()[1])
print('current weekday of the week:')
print(datetime.date.today().isoweekday())    # MON is 1
print('current day of year:')
print(datetime.date.today().strftime('%j'))
print('current day of month:')
print(datetime.date.today().strftime('%d'))
print('current day of week:')
print(datetime.date.today().strftime('%A'))

#question 4
import datetime

day = 'Jan 1 2023 2:43PM'
print(datetime.datetime.strptime(day, '%b %d %Y %I:%M%p'))

#QUESTION 5
import datetime

print(datetime.date.today()-datetime.timedelta(1))
print(datetime.date.today())
print(datetime.date.today()+datetime.timedelta(1))

#QUESTION 6
import datetime
x= datetime.datetime.now()
y = x + datetime.timedelta(0,5)
print(x.time())
print(y.time())

#QUESTION 7
import datetime
print(datetime.date(2015, 6, 16).isocalendar()[1])

#QUESTION 8
import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print()

#QUESTION 9
from datetime import date
f_date = date(2013, 7, 10)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#QUESTION 10
from calendar import monthrange
year = 2016
month = 2
print(monthrange(year, month))