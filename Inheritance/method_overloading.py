print("Trying to do method overloading")

class Overload:
    def display(self):
        print("This is the display..!")

    def display(self,name):
        print("This is display with name ",name)

print("Creating the object")

abc = Overload()

print("Calling the display method")
abc.display()
abc.display("Rohit Pawar")





