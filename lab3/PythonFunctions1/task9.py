#Write a function that computes the volume of a sphere given its radius.

def vol(radius):
    volume = 3.14 * (radius ** 3) * 3/4
    return volume
radius = int(input("Enter a radius: "))
print(vol(radius))