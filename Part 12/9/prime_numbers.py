# Write your solution here
def prime_numbers():
    number = 2
    while number:
        if is_prime(number):
            yield number
        number += 1

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# numbers = prime_numbers()
# for i in range(8):
#     print(next(numbers))

# print(is_prime(4))