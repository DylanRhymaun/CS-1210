"""
Number Guesser Game
Dylan Rhymaun
A game that prompts the user to guess a number
between 1 and 1024 within 10 turns.
"""

import random        # Don't change this line!
import sys           # Don't change this line!

MAX_GUESSES = 10     # Don't change this line!
UPPER_BOUND = 1024   # Don't change this line!


def guess(target, guesses):
    while True:
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > UPPER_BOUND:
            print(f"INVALID! Guesses must be in the range [1, {UPPER_BOUND}]. Try again.")
        elif guess in guesses:
            print(f"INVALID! You have already guessed {guess}. Try again.")
        else:
            guesses.append(guess)
            return guess == target


def play(target):
    guesses = []
    win = False

    for i in range(MAX_GUESSES):
        if guess(target, guesses):
            win = True
            break
        else:
            if guesses[-1] < target:
                print("HIGH!")
            else:
                print("LOW!")
    if win:
        print("WIN!")
    else:
        print("LOSE! The secret number was", target)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        random.seed(sys.argv[1])
    print(f"Try to guess the secret number from 1 to {UPPER_BOUND}.")
    secret_number = random.randint(1, UPPER_BOUND)
    play(secret_number)
