# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:20:08 2023

@author: HP
"""
#1) From given data set print first and last five rows
import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
df.head(5)

import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
df.tail(5)

#2) Print All Toyota Cars details (hint: use groupby function)
import pandas as pd 
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf

#3) Count total cars per company (by using value_counts function)
import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
df['company'].value_counts()

#4) Find each company’s Higesht price car. (hint: Groupby function and then apply .max function)
import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()
priceDf

#5)  Find the average mileage of each car making company (hint: Groupby function and then apply .mean function)
import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
mileageDf

#6) Sort all cars by Price column (hint: using sort_values function).
import pandas as pd
carsDf = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
carsDf.head(5)

#7) Check for the null values for entire dataset
import pandas as pd
df = pd.read_csv("C:/Users/HP/Desktop/Automobile_data.csv")
# using isnull() function 
df.isnull().count()

#8) Use Crime dataset to do the plottings like plottings like histogram, boxplot, scatterplot, barplot, piechart,dot chart.

import pandas as pd
import matplotlib.pyplot as plt  
#line plot
df = pd.read_csv("C:/Users/HP/Downloads/Datasets/company_sales_data.csv")
df.head()
df.tail()
df.shape
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
#to change the colour of line plot
plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
#multiple line plot
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 9000, 11000, 45000, 10000, 55000, 15000, 18000])
# scatter plot 
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/HP/Downloads/Datasets/company_sales_data.csv")
monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()
#bar chart
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:/Users/HP/Downloads/Datasets/company_sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()
#histogram
profitList = df ['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()
#piehart
monthList  = df ['month_number'].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()








