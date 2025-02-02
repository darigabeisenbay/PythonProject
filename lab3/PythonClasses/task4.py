# Write the definition of a Point class. Objects from this class should have a
#     - a method `show` to display the coordinates of the point
#     - a method `move` to change these coordinates
#     - a method `dist` that computes the distance between 2 points

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        self.x = y
        self.y = x
        print(self.x, self.y)

    def dist(self):
        distance = ((y **2 - x **2) **0.5)
        print(distance)
s = Point(x, y)
s.show()
s.move()
s.dist()

