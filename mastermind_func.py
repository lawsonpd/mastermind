# Implementation of Mastermind that uses only functions and no classes.

import random

def make_secret(colors, k=4):
    return random.choices(colors, k=k)

