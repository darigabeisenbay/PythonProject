def square_generator(N):
    for num in range(N + 1):
        yield num ** 2

N = int(input())
s = square_generator(N)
for i in s:
    print(i)
