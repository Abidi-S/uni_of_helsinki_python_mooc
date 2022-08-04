# Write your solution here:
# problems:
# 1. no randomness
# 2. while loop "ew"
# def word_generator(characters: str, length: int, amount: int):
#     while amount > 0:
#         yield (characters[i: i + length] for i in range(len(characters) - length))
#         amount -= 1

from random import choice

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield "".join(choice(characters) for _ in range(length))
