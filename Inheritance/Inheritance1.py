print("Trying to create the Parent Class..! ")
print("This is an Inheritance..")

# parent clas
class Parent:
    parent_name =""
    def display_parent(self):
        print("This is parent class method..")
        print("The Parent Name is ",self.parent_name)

# Son class Inherit parent class
print("Trying to create Son Class..!")

class Son(Parent):  # Inherit parent class
    chilid_name =""
    def display_child(self):
        print("This is child class method..")
        print("The Child name is ",self.chilid_name)

# Create object of child class
print("Object of child class Created")
s1=Son()  # Object of son class
s1.parent_name ='Harishchandra'
s1.chilid_name ='Rohit'

# Calling the parent class method
s1.display_parent()
# Calling the child class method
s1.display_child()
