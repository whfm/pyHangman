import time

name = input("What is your name? ")

print("Hello, " + name, "Time to play hangman!")

print("")

print("Start guessing...")

import random

WORDS = ("banana", "apple", "strawberry", "watermelon", "blueberry", "kiwi", "avocado", "lemon", "orange", "tomato", "orange")
word = random.choice(WORDS)
guesses = ''

turns = len(word)
a = ""

while turns > 0:
    failed = 0
    a = ""
    for char in word:
        if char in guesses:
            a = a + " " + char
        else:
            a = a + " -"
            failed += 1
    print(a)

    if failed == 0:
        print("You won!")
        print("Congratulations!")
        break

    guess = input("Guess a character: ")
    while (len(guess) > 1):
        guess = input("Guess a character (it has to be just one letter: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lost =( !")
            print("The word was: " + word)