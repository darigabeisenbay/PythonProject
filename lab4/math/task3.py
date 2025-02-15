import math
num = int(input("Input the number of the sides: "))
length = float(input("Input the len of sides: "))
area = (num * length**2) / (4 * math.tan(math.pi / num))
area = round(area, 2)
print("The area of the polygon is ",area )

