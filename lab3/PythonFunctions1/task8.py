#Write a function that takes in a list of integers and returns True if it contains `007` in order

def spy_game(nums):
    pattern = [0, 0, 7]
    index = 0
    for num in nums:
        if num == pattern[index]:
            index += 1
        if index == len(pattern):
            return True

x = input("Enter numbers separated by spaces: ")
nums = list(map(int, x.split()))
print(spy_game(nums))
