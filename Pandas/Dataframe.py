'''#create and print DataFrame


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
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})

employees.columns = ['EmpCode', 'EmpName', 'EmpOccupation', 'EmpDOJ', 'EmpAge']

print("\n",employees)

#set Index and Columns
import pandas as pd

employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])

print("\n",employees)

#Drop DataFrame Column(s) by Name and Index:
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print(employees)

print("\n Drop Column by Name \n")
employees.drop('Age', axis=1, inplace=True)
print(employees)

print("\n Drop Column by Index \n")
employees.drop(employees.columns[[0,1]], axis=1, inplace=True)
print(employees)'''

#Basic ways to select rows

import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\nUse == operator\n")
print(employees.loc[employees['Age'] == 23])

print("\nUse < operator\n")
print(employees.loc[employees['Age'] < 30])

print("\nUse != operator\n")
print(employees.loc[employees['Occupation'] != 'Statistician'])

print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] != 'Statistician') &
                    (employees['Name'] == 'John')])


'''#Iterate over rows and columns
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n Example iterrows \n")
for index, col in employees.iterrows():
    print(col['Name'], "--", col['Age'])


print("\n Example itertuples \n")
for row in employees.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), "--", getattr(row, "Age"))

#Add Column to DataFrame:
import pandas as pd

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

employees['City'] = ['London', 'Tokyo', 'Sydney', 'London', 'Toronto']

print(employees)


#Dictionary to DataFrame:
import pandas as pd

data = ({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   })
print(data)

df = pd.DataFrame(data)

print(df)

#Determine DataFrame Columns DataType

import pandas as pd

df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)'''