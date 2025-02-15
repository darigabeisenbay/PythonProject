def reversed_nums(n):
    for i in range(n,-1,-1):
        yield i

n = int(input())
s = reversed_nums(n)
for i in s:
    print(i)