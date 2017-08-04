#! python 3
"""
Project:    Utilities
Filename:   guess_the_number
Created by: PJC
Created on: June 11, 2016
"""

import random

answer = random.randrange(1, 21)
guess = None
guesses = 0

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20.')

for turn in range(1, 6):

    print('Take a guess.')

    while guess is None:

        try:

            guess = int(input())

        except ValueError as e:

            print('You must guess an integer between 1 and 20!')

    guesses += 1

    if guess == answer:

        print('Good job, {0}!  You guessed my number in {1} guesses!'.format(name, str(guesses)))

        quit()

    elif answer < guess < 21:

        print('Your guess is too high.')

    elif answer > guess > 0:

        print('Your guess is too low.')

    else:

        print('That was a wasted guess.  The number is between 1 and 20')

    guess = None

print('Nope, the number I was thinking of was {0}'.format(answer))
