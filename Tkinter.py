# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:59:34 2023

@author: HP
"""

#1 create Button that contain two option Quit and Hello using tkinter
import tkinter as tk   

def write_text():
    print("Tkinter is easy to create GUI!")

parent = tk.Tk()
frame = tk.Frame(parent)
frame.pack()

text_disp= tk.Button(frame, 
                   text="Hello", 
                   command=write_text
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="Exit",
                   fg="green",
                   command=quit)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()



#2 Create Simple Menu with sub options
import tkinter as tk
from tkinter import Menu

# root window
root = tk.Tk()
root.title('Menu Demo')

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

root.mainloop()








#3 to create loan calculator



from tkinter import *
class LoanCalculator: 

  def __init__(self): 

    window = Tk() 
    window.title("Loan Calculator")  
    
    Label(window, text = "Annual Interest Rate").grid(row = 1, 
                    column = 1, sticky = W) 
    Label(window, text = "Number of Years").grid(row = 2, 
                  column = 1, sticky = W) 
    Label(window, text = "Loan Amount").grid(row = 3, 
                column = 1, sticky = W) 
    Label(window, text = "Monthly Payment").grid(row = 4, 
                  column = 1, sticky = W) 
    Label(window, text = "Total Payment").grid(row = 5, 
                  column = 1, sticky = W) 

     
    self.annualInterestRateVar = StringVar() 
    Entry(window, textvariable = self.annualInterestRateVar, 
          justify = RIGHT).grid(row = 1, column = 2) 
    self.numberOfYearsVar = StringVar() 

    Entry(window, textvariable = self.numberOfYearsVar, 
        justify = RIGHT).grid(row = 2, column = 2) 
    self.loanAmountVar = StringVar() 

    Entry(window, textvariable = self.loanAmountVar, 
      justify = RIGHT).grid(row = 3, column = 2) 
    self.monthlyPaymentVar = StringVar() 
    lblMonthlyPayment = Label(window, textvariable =
            self.monthlyPaymentVar).grid(row = 4, 
            column = 2, sticky = E) 

    self.totalPaymentVar = StringVar() 
    lblTotalPayment = Label(window, textvariable =
          self.totalPaymentVar).grid(row = 5, 
          column = 2, sticky = E) 
    
    
    btComputePayment = Button(window, text = "Compute Payment", 
                command = self.computePayment).grid( 
                row = 6, column = 2, sticky = E) 
    window.mainloop() 


   
  def computePayment(self): 
        
    monthlyPayment = self.getMonthlyPayment( 
    float(self.loanAmountVar.get()), 
    float(self.annualInterestRateVar.get()) / 1200, 
    int(self.numberOfYearsVar.get())) 

    self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f')) 
    totalPayment = float(self.monthlyPaymentVar.get())* int(self.numberOfYearsVar.get()) 

    self.totalPaymentVar.set(format(totalPayment, '10.2f')) 

  def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):  
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - (1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))) 
    return (monthlyPayment) 
    r = Tk() 


LoanCalculator()

