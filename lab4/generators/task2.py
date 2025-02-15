def even_nums(n):
    for i in range(0,n):
        if i % 2 == 0:
            yield i

n = int(input())
s = even_nums(n)
for i in s:
    print(i)