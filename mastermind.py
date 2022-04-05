import random

def get_index(coll, target):
    for i, item in enumerate(coll):
        if item == target:
            return i

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
                clue.append("black")
                sec[i] = None
                continue
            j = get_index(sec, color)
            if j is not None:
                if j < i or guess[j] != color:
                    clue.append("white")
                    sec[j] = None
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

def test():
    mm = Mastermind()
    mm.secret = ['red', 'red', 'purple', 'red']
    clue = mm.evaluate_guess('purple red red red'.split())
    assert clue.sort() == ['black', 'black', 'white', 'white']

def play():
    mm = Mastermind()
    print("Welcome to Mastermind!\n")
    print(f"The computer will choose a secret sequence of 4 colors, each of which can be one of the following: {', '.join(color for color in mm.colors)}.\n")
    print("Enter your guess in the following format: 'color1 color2 color3 color4'.\n")
    print("You have 10 tries. Let's go!\n")
    while not mm.gameover:
        guess = mm.make_guess(input("Enter your guess: "))

if __name__ == '__main__':
    play()
