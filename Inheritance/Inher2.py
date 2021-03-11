# Multiple Inheritance

# Father Class Created
class Father:
    fathername =""
    def show_father(self):
        print("Method from Parent Class")
        print("The father Name is ",self.fathername)


# Mother Class Crated
class Mother:
    mothername = ""
    def show_mother(self):
        print("Method from Parent class Mother")
        print("The Mother Name is ",self.mothername)


# Son class inherits father and mother class

class Son(Father,Mother):
    def show_parent(self):
        print("The father Name is ",self.fathername)
        print("The Mother Name is ",self.mothername)

print("Creating child class object")
s1=Son()
print("Assigning value for father name and mother name")

s1.fathername ='Harishchandra'
s1.mothername='Rekha'
print("Calling child class method")
s1.show_parent()
print("Calling mother class methods")
s1.show_mother()
print("Calling the Father class method")
s1.show_father()