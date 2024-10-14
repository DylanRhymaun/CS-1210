"""
Number Guesser Game
Dylan Rhymaun

"""

import random        # Don't change this line!
import sys           # Don't change this line!

MAX_GUESSES = 10     # Don't change this line!
UPPER_BOUND = 1024   # Don't change this line!


def guess(target, guesses):
    """This function takes `target` (the secret number) and `guesses` (a list
    of guesses so far) as arguments. It should prompt the user to enter
    their guess and validate input. If the user has guessed the secret number,
    this function should return True, otherwise it should return False.

    If the user enters a number outside the specified range, i.e., either less
    than one or greater than 1024, then the function should print INVALID! and
    remind the user of the specified range [1, 1024], and then prompt the user
    to try again.

    If the user enters a number that's already in the list of guesses, the
    function should print INVALID! and remind the user that they've already
    guessed that number, and then prompt the user to try again.

    Examples assuming target is 502 and guesses is the list [700, 345, 401]:

        Enter your guess: 345
        INVALID! You have already guessed 345. Try again.
        Enter your guess: -7
        INVALID! Guesses must be in the range [1, 1024]. Try again.
        Enter your guess: 488

    At this point, the function should append the guess to the list of guesses
    and return False. If the user guesses the secret number, then the function
    should append the guess to the list of guesses and return True.

    Only append the user's guess to the list of guesses if it is not already
    in the list! Reporting whether a guess is HIGH! or LOW! should be done in
    the play() function.
    """
    # Complete this function.
    pass  # Remove this line and put your code here.


def play(target):
    """This function should take a secret number (target) and play the game.
    You'll need a list to hold the user's guesses, and then prompt the user to
    make guesses until they WIN! or they run out of guesses, in which case they
    LOSE! You should have a loop, and within the loop you should call the
    guess() function (above) as needed. It is in this function that you should
    report the number of guesses remaining, whether the current guess is HIGH!
    or LOW! (if not a WIN!), and the final outcome of the game: WIN! or
    LOSE! """
    guesses = []
    win = False
    # Complete this function.


if __name__ == '__main__':
    if len(sys.argv) > 1:                # Don't change this line!
        random.seed(sys.argv[1])         # Don't change this line!
    print(f"Try to guess the secret number from 1 to {UPPER_BOUND}.")     
    secret_number = 0   # Use random.randint() here.
    play(secret_number)                  # Don't change this line!
    # No more lines are needed here!