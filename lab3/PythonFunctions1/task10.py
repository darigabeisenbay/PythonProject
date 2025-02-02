#Write a Python function that takes a list and returns a new list with unique elements of the first list. Note: don't use collection

def unique_elements(nums):
    unique_set = set()
    unique_lst = []
    for i in nums:
        if i not in unique_set:
            unique_lst.append(i)
            unique_set.add(i)
    return unique_lst

x = input("Enter numbers: ")
nums = list(map(int, x.split()))
print(unique_elements(nums))