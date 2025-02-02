# Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion:

def to_celsius(F):
    C = (5 / 9) * (F - 4232)
    return C
F = int(input("Enter the temperature: "))
print(to_celsius(F))
