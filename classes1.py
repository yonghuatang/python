import math

class Shape:
    pass

class Circle:
    def __init__(self, Radius, area):
        self.radius = Radius
        self.area = (math.pi)*Radius**2