import random

def get_index(coll, target):
    for i, item in enumerate(coll):
        if item == target:
            return i
    return None

class Mastermind:
    def __init__(self):
        self.colors = ['blue', 'purple', 'red', 'orange', 'green', 'yellow']
        self.secret, self.guesses, self.clues, self.gameover = random.choices(self.colors, k=4), [], [], False

    def evaluate_guess(self, guess):
        "Evaluate guess and return result (either 'correct' or clue)."
        if guess == self.secret:
            return "correct"
        sec = self.secret.copy() # Make copy to modify
        clue = []
        for i, color in enumerate(guess):
            if color == sec[i]:
                sec[i] = None
                clue.append("black")
            # The following two lines are doing redundant work. We're looking into
            # the list twice for the color.
            # Try using `get_index` defined above.
            elif color in sec[:i] or color in sec[i+1:]:
                idx = sec.index(color)
                if guess[idx] != color: # Really only need to do this check if idx > i
                    clue.append("white")
                    sec[idx] = None
        self.clues.append(random.shuffle(clue))
        return clue

    def make_guess(self, guess):
        "Add guess to self.guesses and return clue if not last guess, otherwise end game."
        # assert len(self.guesses) < 10 # Only 10 guesses allowed
        guess = guess.split()
        self.guesses.append(guess)
        result = self.evaluate_guess(guess)
        if result == "correct":
            print("Your guess was correct! You win!")
            self.end_game()
        elif len(self.guesses) == 10:
            print(f"That was your last guess, but it was incorrect! The secret was [{' '.join(color for color in self.secret)}]. Game over :(")
            self.end_game()
        else:
            print("Your guess was incorrect. Here's your clue:")
            print(f"[{' '.join(color for color in result)}]\n")

    def previous_guesses(self):
        "Display player's previous guesses"

    def previous_clues(self):
        "Display player's previous clues and corresponding guesses"

    def end_game(self):
        "Trigger game over"
        self.gameover = True

def main():
    mm = Mastermind()
    print("Welcome to Mastermind!\n")
    print(f"The computer will choose a secret sequence of 4 colors, each of which can be one of the following: {', '.join(color for color in mm.colors)}.\n")
    print("Enter your guess in the following format: 'color1 color2 color3 color4'.\n")
    print("You have 10 tries. Let's go!\n")
    while not mm.gameover:
        guess = mm.make_guess(input("Enter your guess: "))

if __name__ == '__main__':
    main()
