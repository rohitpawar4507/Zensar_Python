
print("This is the first program...!")  # to print the data on the screen.
print(233)
print('The number is',123)
print(10+13)

# what is variable ?
#  Variable are the Storage Unit , used to store data.

a=200  # variable a holds value 20.
print(a) # Print the variable value.

# What is dynamic programing ?
# -> dynamic means automatic process of variable memory allocation
# String - Sequence / set of character

a='This is python'
print("Let learn the python...", a)

''' This is multiline comments
We use triple quotation
'''

# For Loop
print("Trying to use for loop")
str = 'Welcome'
print("The string is..",str)
for i in str:
    print(i,end=' ')
print("Running once again")
for i in str:
    print(i)

# Range Function
for i in range(10):  # Start =0,End = 9
    print(i,end=' ')
print("Runs once again..")
for i in range(4,10):  # Start =0,End = 9
    print(i,end=' ')
print('Runs once agains...')

for i in range(4,44,4):  # Start =4,End = 40 and difference /step =4
    print(i,end=' ')
print("Runs once agains")
for i in range(0,10,2):  # Start =0,End = 9
    print(i,end=' ')
# print the table any one
n=int(input("\n Enter the number :"))
for i in range(1,11):
    c=n*i
    print(n,"*",i,"=",c)

# Nested For Loop
# Eg. printing patteren or number
rows = int(input('Enter the rows : '))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end='')
    print()

# For printing star
rows = int(input('Enter the rows : '))
for i in range(0,rows+1):
    for j in range(i):
        print("*",end='')
    print()

# Using else statement with for loop

rows = int(input('Enter the rows : '))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end='')
    print()
else:
    print("For loop completly executed...")

# While Loop
# it is also known as pre- tested loop or entry loop
# The while loop will iterate until condition becomes false..

i=8
print("Value of i :",i)
# The while loop will iterate until condition becomes false..
while(i>=1):
    print(i)
    i=i-1

i=0
print("Value of i :",i)
# The while loop will iterate until condition becomes false..
while(i<=10):
    print(i)
    i=i+1
else:
    print("While loop excuted...")

# Break Statement

print('Trying to print for loop..')
str = 'Python'
print(str)
for i in str:
    if i=='o':
        break # to give away the control from the loop
    print(i)

print('We are out of the loop')

# Continue Statement
print(str)
for i in str:
    if i=='o':
        continue # to skip the iteration
    print(i)

print('We are out of the loop')

