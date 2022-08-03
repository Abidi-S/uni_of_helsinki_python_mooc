# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    if number <= 1:
        return number
    return number + recursive_sum(number - 1)