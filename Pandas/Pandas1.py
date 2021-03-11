import pandas as pd

# Creating Series using list:

s1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
print(s1)
type(s1)

# Creating Series using the index:

s1 = pd.Series([1,2,3,44,5,6],index=['a','b','c','d','e','f'])
print(s1)

#Creating Series of string values with name:

ser2 = pd.Series(["India", "Canada", "Germany"], name="Countries")
print(ser2)

#Creating Series using dictionary:
import pandas as pd

ser4 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
print(ser4)