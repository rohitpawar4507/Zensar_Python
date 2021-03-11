
# This is method overriding
# In python method overloading is not possible

import math
import cmath
# Super Class



class Polygon:
    def number_of_sides(self):
        return 0
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

    # Triangle class inherits from polygons
class Triangle(Polygon):
        def number_of_sides(self):
            return 3

        def area(self,base,height):
            return 1/2 * base * height

        def perimeter(self,a,b,c):
            if a+b>c:
                return a+b+c
            else:
                return "Invalid input "
print("Creating object of triangel class")
tri=Triangle()
print("Calling object of trinagle clas")
print("Triangle area",tri.area(15,34))
print("Perimeter:",tri.perimeter(15,20,25))



