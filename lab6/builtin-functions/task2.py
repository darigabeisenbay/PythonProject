def count_case_letters(text):
    upper_count = sum(c.isupper() for c in text)
    lower_count = sum(c.islower() for c in text)
    return upper_count, lower_count

user_input = input()
upper, lower = count_case_letters(user_input)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
