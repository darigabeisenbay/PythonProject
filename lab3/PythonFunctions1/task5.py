#Write a function that accepts string from user and print all permutations of that string.

def permute(s, res=""):

    if len(s) == 0:
        print(res)
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[:i] + s[i + 1:]  
        permute(left_substr, res + ch)


str = input("Enter a string: ")
permute(str)
