# Creating class in python

print("Let us learn Classes and Object !!:")
class Circle:
   def __init__(self):
       self.radius=1

# Creating a object
print("Creating a Object of class..")
my_circle=Circle()   # Object_name = Class Name
print("Radius is ..:",my_circle.radius)
print("Area of circle is :",2*3.14*my_circle.radius)

my_circle.radius=5
print("Radius is ..:",my_circle.radius)
print("Area of circle is :",2*3.14*my_circle.radius)


'''print("Circle class block finishied...")
# Creating a object
print("Creating a Object of class..")
my_circle=Circle()   # Object_name = Class Name
# Creating a instance Variable
print("Creatinga instance variable..")
my_circle.radius =5
print("Area of Circle is..!")
print(2 * 3.14 * my_circle.radius)


'''
