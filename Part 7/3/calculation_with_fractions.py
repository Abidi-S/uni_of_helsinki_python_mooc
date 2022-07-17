# Write your solution here
from fractions import *

def fractionate(amount: int):
    fraction = Fraction(1, amount)

    return [fraction] * amount
