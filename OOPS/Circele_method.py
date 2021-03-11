# Methods : It is regular function
# Self : similar to this keyword in java. -> reference to the current object

print("Creating a circle class..!")

class Circle:
    def __init__(self):
        self.radius =1

    def area(self):
        return 2*3.14*self.radius

print("Creating the object...")
c=Circle()

print("Radius is: ",c.radius)
print("Area of Circle is :",c.area())

c.radius=3
print("Radius is: ",c.radius)
print("Area of Circle is :",c.area())



# 1 - Self is set to the newly created instance when __init__ is run.
# 2 - We create Circle instance object
# 3 - Radius is already initailized
# 4 - We override the radius field
# __init__ -> Nothing but constructor

