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
        pass

    def dist(self):
        pass

