import unittest
from mastermind import Mastermind

class TestMastermind(unittest.TestCase):
    def test_clue_validity(self):
        "Tests that correct clue is given."
        mm = Mastermind()
        # Manually set secret code. Otherwise won't know what it is.
        mm.secret = ['red', 'red', 'purple', 'red']
        clue = mm.make_guess('purple red red red')
        clue.sort()
        assert clue == ['black', 'black', 'white', 'white']

    def test_not_gameover_after_one_incorrect_guess(self):
        "tests that mm.gameover == False after a single incorrect guess."
        mm = Mastermind()
        mm.secret = ['red', 'red', 'purple', 'red']
        incorrect_guess = 'blue blue blue blue'
        mm.make_guess(incorrect_guess)
        assert not mm.gameover

    def test_gameover_after_10_guesses(self):
        "Tests that mm.gameover == True when 10 guess have been made."
        mm = Mastermind()
        mm.secret = ['red', 'red', 'purple', 'red']
        incorrect_guess = 'blue blue blue blue'
        for _ in range(10):
            mm.make_guess(incorrect_guess)
        assert mm.gameover

    def test_gameover_after_correct_guess(self):
        "Tests that mm.gameover == True when a correct guess has been made."
        mm = Mastermind()
        mm.secret = ['red', 'red', 'purple', 'red']
        clue = mm.make_guess('red red purple red')
        assert mm.gameover

if __name__ == '__main__':
    unittest.main()
