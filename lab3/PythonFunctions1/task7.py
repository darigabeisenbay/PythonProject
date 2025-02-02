#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True


x = input("Enter a number: ")
numbers= list(map(int, x.split()))
print(has_33(numbers))