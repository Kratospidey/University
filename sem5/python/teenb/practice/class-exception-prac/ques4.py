# Write a Python class named Circle with constructor for radius 
# and two methods which will compute the area and the perimeter of a circle.

import math

class Circle():
    def __init__(self, radius):
      self.radius = radius
      
    def area(self):
        print(f"{(math.pi * (self.radius ** 2)):.3f}")
        
    def perimeter(self):
        print(f"{(2*math.pi* self.radius):.3f}")
    
          
circ1 = Circle(69)
circ1.area()
circ1.perimeter()