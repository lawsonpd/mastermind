from mastermind import Mastermind

def test():
    mm = Mastermind()

    # Manually set secret code. Otherwise won't know what it is.
    mm.secret = ['red', 'red', 'purple', 'red']
    clue = mm.make_guess('purple red red red')
    assert clue.sort() == ['black', 'black', 'white', 'white']
    assert not mm.gameover
    # Make 9 more (incorrect) guesses and check that game is over
    incorrect_guess = 'blue blue blue blue'
    for _ in range(9):
        mm.make_guess(incorrect_guess)
    assert mm.gaveover
    assert len(mm.guesses) == len(mm.clues)

    mm = Mastermind()
    mm.secret = ['red', 'red', 'purple', 'red']
    clue = mm.make_guess('red red purple red')
    assert mm.gaveover

