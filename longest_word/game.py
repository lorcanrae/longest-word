# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import copy
import requests


class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [chr(random.randint(ord("A"), ord("Z"))) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        # Check empty string
        if not word:
            return False

        # Check if word is valid
        grid_ = copy.deepcopy(self.grid)
        for letter in word:
            if letter in grid_:
                grid_.remove(letter)
            else:
                return False

        # Check to see if word is in English dictionary
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        """Check if word exists in English dictionary"""
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response["found"]



# if __name__ == '__main__':
#     game = Game()
#     game.grid = [l for l in "OQUWRBAZE"]
#     my_word = "BAROQUE"
#     print(game.is_valid(my_word))
