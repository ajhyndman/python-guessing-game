#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Guessing Game from teamtreehouse.com's Python Basics course.
# @author: Andrew Hyndman


import random





answer = random.randint(1, 10)

print("I have picked a number between 1 and 10.  Try to guess it!")

guesses_remaining = 5
guess = 0


while guesses_remaining > 0:
    print("You have {} guesses remaining".format(guesses_remaining))
    guess = int(input("::: "))
    guesses_remaining -= 1
    if guess == answer:
        print("Congratulations!  You guessed my number [{}] in {} guesses!".format(answer, (5 - guesses_remaining)))
        break
    elif guess > answer:
        print("Nope.  My number is less than that.")
    else:
        print("Nope.  My number is greater than that.")


if 0 == guesses_remaining:
    print("I win!  Muahahaha!")
