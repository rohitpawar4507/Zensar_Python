#using NumPy functions:

import pandas as pd
import numpy as np

ser1 = pd.Series(np.linspace(1, 10, 5))
print(ser1)

ser2 = pd.Series(np.random.normal(size=5))
print(ser2)

#get index and values of series
import pandas as pd
import numpy as np

ser1 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})

print(ser1.values)
print(ser1.index)

print("\n")

ser2 = pd.Series(np.random.normal(size=5))
print(ser2.index)
print(ser2.values)
#Get Length Size and Shape of a Series

import pandas as pd

values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]

code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]

ser1 = pd.Series(values, index=code)

print(len(ser1))

print(ser1.shape)

print(ser1.size)

#get the first or last few rows from a Series

import pandas as pd

values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]

code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]

ser1 = pd.Series(values, index=code)

print("-----Head()-----")
print(ser1.head())

print("\n\n-----Head(2)-----")
print(ser1.head(2))

#Slicing a Series into subsets

import pandas as pd

num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]

idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

series = pd.Series(num, index=idx)

print("\n [2:2] \n")
print(series[2:4])

'''print("\n [1:6:2] \n")
print(series[1:6:2])

print("\n [:6] \n")
print(series[:6])

print("\n [4:] \n")
print(series[4:])

print("\n [:4:2] \n")
print(series[:4:2])

print("\n [4::2] \n")
print(series[4::2])'''

print("\n [::-1] \n")
print(series[::-1])

#create and print DataFrame


import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

print(employees)

#rename DataFrame columns name
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

employees.columns = ['EmpCode', 'EmpName', 'EmpOccupation', 'EmpDOJ', 'EmpAge']

print(employees)