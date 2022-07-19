# Write your solution here
from random import sample

def generate_password(number):
    pool = "abcdefghijklmnopqrstuvwxyz"
    draw = sample(list(pool), number)
    password = ""
    for i in draw:
        password += i
    return password
