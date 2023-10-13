# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:25:22 2023

@author: HP
"""
#To check the files is exist or not in drive otherwise throw exception
try: 
    with open('/path/to/file', 'r') as fh:
        pass
except FileNotFoundError: 
    pass
# Leverage the OS package
import os 
exists = os.path.isfile('/path/to/file')
# Wrap the path in an object for enhanced functionality
from pathlib import Path
config = Path('/path/to/file') 
if config.is_file(): 
    pass

#Problem statment : Find number that divide by zero otherwise throw exception
import random
try:
  ri = random.randint(0, 2)
  if ri == 0:
    infinity = 1/0
  elif ri == 1:
    raise ValueError("Message")
    #raise ValueError, "Message" # Deprecated
  elif ri == 2:
    raise ValueError # Without message
except ZeroDivisionError:
  pass
except ValueError as valerr:
# except ValueError, valerr: # Deprecated?
  print(valerr)
  raise # Raises the exception just caught
except: # Any other exception
  pass
finally: # Optional
  pass # Clean up

class CustomValueError(ValueError): pass # Custom exception
try:
  raise CustomValueError
  raise TypeError
except (ValueError, TypeError): # Value error catches custom, a derived class, as well
  pass                          # A tuple catches multiple exception classes
  
#Program to print the reciprocal of even numbers
num = int(input("Enter a number: "))

try:
    assert num % 2 == 0
    reciprocal = 1/num
    print(reciprocal)

except ZeroDivisionError:
    print("error")

except:
    print("Not an even number!")


