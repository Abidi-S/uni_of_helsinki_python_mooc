# Write your solution here
from http.client import PAYMENT_REQUIRED
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        if len(player2_word) > len(player1_word):
            return 2
        return 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        vowels_1 = 0
        vowels_2 = 0
        for char in player1_word:
            if char in vowels:
                vowels_1 += 1
        for char in player2_word:
            if char in vowels:
                vowels_2 += 1
        if vowels_1 > vowels_2:
            return 1
        if vowels_2 > vowels_1:
            return 2
        return 0

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        """ rewrite this Hot Garbage as a dictionary"""

        # allowed = ["rock", "paper", "scissors"]
        # if player1_word == player2_word or (player1_word not in allowed and player2_word not in allowed):
        #     return 0

        # if player1_word in allowed:
        #     if player1_word == allowed[0] and player2_word == allowed[2]:
        #         return 1
        #     if player1_word == allowed[1] and player2_word == allowed[0]:
        #         return 1
        #     if player1_word == allowed[2] and player2_word == allowed[1]:
        #         return 1
        # else:
        #     return 2

        # if player2_word in allowed:
        #     if player2_word == allowed[0] and player1_word == allowed[2]:
        #         return 2
        #     if player2_word == allowed[1] and player1_word == allowed[0]:
        #         return 2
        #     if player2_word == allowed[2] and player1_word == allowed[1]:
        #         return 2
        # else:
        #     return 1