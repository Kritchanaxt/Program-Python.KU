
#? Ex.OOP1 - #4

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length * self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return 3.14 * (self.radius **2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
     
rectangle = Rectangle(2, 10)
print(f"Rectangle are: {rectangle.area()}, Perimeter:{rectangle.perimeter()}")

circle = Circle(4)
print(f"Circle area: {circle.area()} Perimeter: {circle.perimeter()}")