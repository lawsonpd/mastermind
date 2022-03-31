import random

def scramble(nums: list) -> list:
    '''
    Scrambles a list of (sorted or unsorted) numbers.

    @param nums: list of numbers

    Returns new list of numbers in `nums` with numbers in random order
    '''
    for i in range(len(nums)):
        rand = random.randrange(0, len(nums))
        # print(f'i: {i}, rand: {rand}')
        nums[i], nums[rand] = nums[rand], nums[i]

    return nums

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
            elif color in sec[:i] or color in sec[i+1:]:
                idx = sec.index(color)
                if guess[idx] != color:
                    clue.append("white")
                    sec[i] = None
        self.clues.append(scramble(clue))
        return clue

    def make_guess(self, guess):
        "Add guess to self.guesses and return clue if not last guess, otherwise end game."
        # assert len(self.guesses) < 10 # Only 10 guesses allowed
        guess = guess.split()
        self.guesses.append(guess)
        result = self.evaluate_guess(guess)
        if result == "correct":
            print("Your guess was correct! You win!")
            self.gameover = True
        elif len(self.guesses) == 10:
            print(f"That was your last guess, but it was incorrect! The secret was [{' '.join(color for color in self.secret)}]. Game over :(")
            self.gameover = True
        else:
            print("Your guess was incorrect. Here's your clue:")
            print(f"[{' '.join(color for color in result)}]\n")

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
