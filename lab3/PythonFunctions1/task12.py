#Define a functino `histogram()` that takes a list of integers and prints a histogram to the screen. For example, `histogram([4, 9, 7])` should print the following:

def histogram(nums):
    for i in nums:
        print("*" * i)


x = input("Enter numbers: ")
nums = list(map(int, x.split()))
histogram(nums)