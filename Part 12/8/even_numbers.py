# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for number in range(beginning, maximum + 1):
        if number%2 == 0:
            yield number
