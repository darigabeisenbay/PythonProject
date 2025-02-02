#Write a program able to play the `"Guess the number"` - game, where the number to be guessed is randomly chosen between 1 and 20.

import random
n = random.randint(1,20)
greet = input("Hello! What's your name? ")
print("Well,", greet, "I am thinking of a number between 1 and 20.")
count = 1
while True:
    x = int(input("Take a guess."))
    if x > n:
        print("Your guess is too high.")
    elif x < n:
        print("Your guess is too low.")
    elif x == n:
        print("Good job", greet, "You guessed my number in", count, "guesses!")
        break
    count += 1
