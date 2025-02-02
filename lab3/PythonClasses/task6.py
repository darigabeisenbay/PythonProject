def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = input("Enter a number: ")

numbers = list(map(int, x.split()))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)