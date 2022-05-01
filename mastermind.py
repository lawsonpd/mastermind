import random

class Mastermind:
    def __init__(self):
        self.colors = ['blue', 'purple', 'red', 'orange', 'green', 'yellow']
        self.secret, self.guesses, self.clues, self.gameover = random.choices(self.colors, k=4), [], [], False

    def make_guess(self, guess):
        "Add guess (str) to self.guesses and return clue if not last guess, otherwise end game."
        assert(not self.gameover, "Game is over") # Necessary?
        guess = guess.split()
        self._record_guess(guess)
        clue = self._evaluate_guess(guess)
        self._record_clue(clue)
        if clue == ["black"] * 4 or len(self.guesses) == 10:
            self._end_game()
        return clue

    def _evaluate_guess(self, guess):
        "Evaluate guess and return (shuffled) clue."
        sec = self.secret.copy() # Make copy to modify
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
        random.shuffle(clue)
        return clue

    def _record_guess(self, guess):
        "Add guess to guesses store"
        self.guesses.append(guess)

    def _record_clue(self, clue):
        "Add clue to clues store"
        self.clues.append(clue)

    def _end_game(self):
        "Trigger game over"
        self.gameover = True

    def previous_guesses(self):
        "Return player's previous guesses"
        return self.guesses

    def previous_clues(self):
        "Return player's previous clues and corresponding guesses"
        return self.clues

def test():
    mm = Mastermind()
    mm.secret = ['red', 'red', 'purple', 'red']
    clue = mm.make_guess('purple red red red'.split())
    assert clue.sort() == ['black', 'black', 'white', 'white']

def game():
    mm = Mastermind()
    print("Welcome to Mastermind!\n")
    print(f"The computer will choose a secret sequence of 4 colors, each of which can be one of the following: {', '.join(color for color in mm.colors)}.\n")
    print("Enter your guess in the following format: 'color1 color2 color3 color4'.\n")
    print("You have 10 tries. Let's go!\n")
    while not mm.gameover:
        guess = input("Enter your guess: ")
        clue = mm.make_guess(guess)
        print(f"Your guess: {guess}")
        if clue == ['black'] * 4:
            print("Correct! You win!")
        else:
            print("Incorrect!")
            print(f"Your clue: {clue}\n")

if __name__ == '__main__':
    game()
