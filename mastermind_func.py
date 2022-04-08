# Implementation of Mastermind that uses only functions and no classes.

import random

# Unnecessary - just use try/except
# def get_index(coll, target):
#     for i, item in enumerate(coll):
#         if item == target:
#             return i

def secret_code(colors:list=['black', 'blue', 'green', 'purple', 'white', 'yellow'], k:int=4) -> list:
    "Return list of k randomly chosen colors."
    return random.choices(colors, k=k)

def fmt_text_guess(guess:str) -> list:
    "Takes string repr of guess and returns list of colors in guess."
    return guess.split()

def evaluate_guess(secret:list, guess:list) -> list:
    "Evaluate guess and return clue."
    # We could first check whether secret == guess, but if it is, then we'll make
    # just one pass through the lists in the loop below, and if not, then we'd be
    # making an extra pass to compare each item pair in the secret and guess.
    sec = secret.copy() # Make copy to modify
    clue = []
    for i, color in enumerate(guess):
        if color == sec[i]:
            clue.append("black")
            sec[i] = None
            continue
        try:
            j = sec.index(color)
        except ValueError:
            j = None
        if j is not None:
            if j < i or guess[j] != color:
                clue.append("white")
                sec[j] = None
    return clue

def is_correct_guess(secret, guess):
    "Returns True if the clue for the guess is 4 blacks."
    return evaluate_guess(secret, guess) == ['black', 'black', 'black', 'black']

