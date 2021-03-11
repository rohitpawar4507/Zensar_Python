# User Defined exception
# we define a class of named error inheriting exception class to create user defind exception

print("Let us learn the Exception")
print("Writing the code in Try block")

print("Creating a class for User defined Exception")
class NumbernotProper(Exception):
    def __init__(self):
        print("This is user defined error")

try:
    a = int(input("Enter a ?"))
    b = int(input("Enter b ?"))
    if b is 0:
        raise NumbernotProper
    else:
        print("a/b =",a/b)

except NumbernotProper:
    print("The value of b can't be 0")
except:
    print('This is except block')

print("This is demo for User defined exception Handling")
