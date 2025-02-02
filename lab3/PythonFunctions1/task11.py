#Write a Python function that checks whether a word or phrase is `palindrome` or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("Enter a word: ")
print(is_palindrome(word))