"""
Define a class named `Shape` and its subclass `Square`. The `Square` class has an `init` function which takes a `length` as argument. Both classes have a `area` function which can print the area of the shape where Shape's area is 0 by default.

from lab3.PythonClasses.task1 import ToUpper
"""


class Shape:
    def __init__(self):
        pass
    def area (self):
        print("The area is equal to 0")
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = int(input("Enter the length of the square: "))
    def area (self):
        print("The area is equal to 0 but it's ", self.length **2 )
s = Shape()
sq = Square(Shape)
s.area()
sq.area()


