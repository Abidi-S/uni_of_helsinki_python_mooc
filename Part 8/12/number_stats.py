# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0

    def add_number(self, number:int):
        if number:
            self.numbers += number
            self.count += 1

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers

    def average(self):
        if self.count > 0:
            return self.numbers/self.count
        return 0

print("Please type in integer numbers: ")
all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    number = int(input())
    if number == -1:
        break
    all_stats.add_number(number)

    if number%2 == 0:
        even_stats.add_number(number)
        continue
    odd_stats.add_number(number)

print(f"Sum of numbers: {all_stats.get_sum()}")
print(f"Mean of numbers: {all_stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")