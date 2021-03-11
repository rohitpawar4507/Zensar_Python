str = 'Rohit' + 'Pawar'
print(str)

str1="Welcome to python"
print(str1)
print(str1[0]) # Accessing the string character using index
print(str1[2])
print(str1[8])
print(type(str1))

print(len(str1)) # find the length of string
print(max(str1)) # find the maximum privilage a number / value

# Re assigning a value is not possible
'''str1[0]='w'  # String is immutable -> we cannot change or modified it.
print(str1) '''

# Using + or * operator in string
print(str * 3) # print string n number of time.
str1 = "Python is cool "+''+ str  # concatention
print("Modified string is: ",str1)
print("Printing the string multiple times :",str1*2)

# Finding the character in the given string Using Find()

print("Finding the character position using find func:")
str2 = 'Python Programing'
print(str2)
a=str2.find('P')
print("Print the character is at position : ",a)

str2 = 'Welcome to Python Programing'
print(str2)
a=str2.find('e')
print("Print the character is at position : ",a)

print(str.capitalize()) #

## Slicing

test = 'Python Programing'
print("String ",test)
# test[start:stop:step/differnce]  by default [start=0:stop=last character:step=1]

# first character
print()
# Last character
print(test[-1])

print(test[:16])

# Reverse order
print(test[::-1])

