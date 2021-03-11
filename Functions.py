'''
# Creating a function
# Why ?
1.Reuse code
2.Length is cut short
3. Program logic is simple
4. can return value

define -- func-name  func- brackets

def my_function():   //fun declaration
    statements
    :return<expression>  # none

my_function  # Calling a function (function call)

# Example
def Hello():
    print("Hello World")

'''

print("Let us Learn Function in Python.....")

# Define a function / Declared  a function
def Hello():   # function declaration
    print("This is a Function")
    a=10
    print("The value of a is..",a)
    # return None -> By default None return type
    # return 1 -> Printing 1

# By defalut python function return "None".
# Every function must return value/something

print("This is main program!!!")
# Executing the function by calling this
print("Executing a function")
Hello()  # Calling the function (function call)
print("The function execution is complete!!!")

print(Hello())  # Return a None value because not give return type

# Defining function with parameter
def Hello(name):   # function with Arguments
    print("This is a Function with Arguments")
    print("Hello,Welcome to Python :",name)
    return name
    # return None -> By default None return type
    # return 1 -> Printing 1

print("This is main program!!!")
# Executing the function by calling this
print("Executing a function")
s1='Rohit'
Hello(s1)  # Calling the function  by passing arguments
print("The function execution is complete!!!")
print(Hello("Pawar")) # 2nd time excute and return this name

# Python Function to print student details.

# defining the function
def display(a='Rohit',b=21):
    print("The name of Student is ",a)
    print("The age of Student is ",b)

# Taking values from the user
a=str(input("Enter the Student Name: "))
b=int(input("Enter the Student Age: "))

# Printing the details
print("Calling the display() function ")
display(a,b)

print("Calling the display () ...")
display()

print("Calling the display ()....")
display(a)


# Function 2
def display1(b,a=21):
    print("The name of student is ",a)
    print("The age of student is ",b)

print("Calling the function 2")
display1(15,'Rohit')
print("Calling a function 2")
display1('Rohit')


# passing mutable Object(List):
print("Passing the list to the function")
# defining the function
def update_list(num):
    print("Inside the function")
    print("List inside function =",num)
    num.append(200)
    num.append(300)
    print("Modified list inside function = ",num)

# Defining the list
num=[100,300,400,500]
print("The list is: ",num)

# Calling the function
print("Calling the list...")
update_list(num)
print("List outside the function = ",num)

# Passing a String
def update_string(str):
    str = str + "Python is Cool."
    print("Printing the string Inside the Function: ",str)

string1="Python is a Developer Friendly.."
print("The string is: ",string1)

# Calling the function
print("Calling the function")
update_string(string1)

print("The String outside the function :",string1)

# defining a function
def display2(a,b):
    print("The age is :",b)
    print("The name is :",a)

# Taking values from users
a=str(input("Enter the name: "))
b=int(input("Enter the age :"))
print(a,"---",b)

# Calling a function
print("Calling a function")
display2(a,b)

print("Calling a function")
display2(b='Mauli',a=36)  #Keyword argument function call