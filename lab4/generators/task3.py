def divisible_by_3_and_4(n):
    for i in range(0,n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
iterable = divisible_by_3_and_4(n)
for i in iterable:
    print(i)