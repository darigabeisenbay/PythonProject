"""
Define a class named `Rectangle` which inherits from `Shape` class from task 2. Class instance can be constructed by a `length` and `width`. The `Rectangle` class has a method which can compute the `area`.
"""
class Shape:
    def __init__(self):
        pass
    def area (self):
        print("The area is equal to 0")




class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        print( self.length * self.width)

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))
rect = Rectangle(l, w)
rect.area()






