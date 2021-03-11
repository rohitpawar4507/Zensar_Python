print("Let Implements pre-build method on  Object")

class Student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

print("Creating Object ..!")
s1=Student(354,"Rohit Pawar",21)
print("ID: ",s1.id,"Name: ",s1.name,"Age : ",s1.age)

# Print the attribute name of the object
print("Getting the value of Name..")
print("The Name is:", getattr(s1, 'name'))

# Reset the value of attribute age to 22
print("Setting the value of Age..")
print("The Age is:", setattr(s1, 'age'))

# Print true if the student contains the attribute with name id
print("Checking if Id is present for s1..")
print("The Name is:", hasattr(s1, 'id'))

# Deletes the attribute age
print("Deleting  the age..")
delattr(s1,'age')

print("Checking if Age is present for s1..")
print("Is Age present? ",hasattr(s1, 'age'))



