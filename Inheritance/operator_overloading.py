class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

     # Like toString method in Java : -> Print the content of Object
    def __str__(self):
        return  "({0},{1})".format(self.x, self.y)

# Pre-defined method __add__ is overloaded here
    def __add__(self, other): # p3=p1+p2 [(p3x,p3y)=(x1+x2),(y1+y2)]
        # Operand1 + oprand2
        x= self.x + other.x
        y= self.y + other.y
        return (x, y)

    def __sub__(self, other): # p3=p1-p2 [(p3x,p3y)=(x1-x2),(y1-y2)]
        # Operand1 - oprand2
        x = self.x - other.x
        y = self.y - other.y
        return (x, y)




# addition of Oobject is not possible
p1=Point(5,13)
print("This are the x and y co-ordinates of P1")
print(p1)

p2=Point(3,7)
print("This are the x and y co-ordinates of P2")
print("Adding two point using operator overloading")
p3=p1+p2 # p3=p1+p2 [(p3x,p3y)=(x1+x2),(y1+y2)]
print("After addition the new point is ",p3)

p4=p1-p2
print("After two point subtraction is",p4)

