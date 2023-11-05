import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi*self.radius**2
    
class Triangle:
    def __init__(self, base, height):
        self.base=base
        self.height=height
    
    def calculate_area(self):
        return 0.5*self.base*self.height