def is_palindrome(text):
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    return cleaned_text == cleaned_text[::-1]

user_input = input()
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
