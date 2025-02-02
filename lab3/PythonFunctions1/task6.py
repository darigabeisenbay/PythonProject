#Write a function that accepts string from user, return a sentence with the words reversed

def reversed_string(s):
    words = s.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

s = input("Enter a sentence: ")
print( reversed_string(s))