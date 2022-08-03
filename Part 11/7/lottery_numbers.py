# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, lotto_numbers: list):
        self.week = week
        self.lotto_numbers = lotto_numbers

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.lotto_numbers])

    def hits_in_place(self, numbers: list):
        return [number if number in self.lotto_numbers else -1 for number in numbers]