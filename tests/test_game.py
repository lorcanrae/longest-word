from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):

        # setup
        new_game = Game()

        # exercise
        grid = new_game.grid

        # verify
        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        new_game = Game()

        assert new_game.is_valid("") == False

    def test_is_valid(self):

        # setup
        new_game = Game()

        ## set grid and test word
        test_grid = "OQUWRBAZE"
        test_word = "BAROQUE"
        new_game.grid = list(test_grid)

        # exercise
        assert new_game.is_valid(test_word) == True

        # verify
        assert new_game.grid == list(test_grid)

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = "QEULNNNNK"
        test_word = "BAROQUE"

        ## Set grid and test word
        new_game.grid = list(test_grid)

        # exercise
        assert new_game.is_valid(test_word) == False

        # verify
        assert new_game.grid == list(test_grid)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should not be valid"""
        new_game = Game()
        new_game.grid = list("KWIENFUQW")
        assert new_game.is_valid('FEUN') is False
