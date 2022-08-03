# TEE RATKAISUSI TÄHÄN:
class SimpleDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __gt__(self, another):
        if self.year < another.year:
            return False
        if self.month < another.month and self.month != another.month:
            return False
        if self.day < another.day and self.day != another.day:
            return False
        return True

    def __lt__(self, another):
        if self.year > another.year:
            return False
        if self.month > another.month:
            return False
        if self.day > another.day:
            return False
        return True

    def __eq__(self, another):
        return self.year == another.year and self.month == another.month and self.day == another.day

    def __ne__(self, another):
        return self.year != another.year or self.month != another.month or self.day != another.day

    def __add__(self, days):
        new_date = SimpleDate(0,0,0)
        new_date.day += self.day + days
        new_date.month += self.month
        new_date.year += self.year
        if new_date.day > 30:
            new_date.month += new_date.day//30
            new_date.day %= 30
        if new_date.month > 12:
            new_date.year += new_date.month//12
            new_date.month %= 12
        return new_date

    def __sub__(self, another):
        self_in_days = self.day + self.month*30 + self.year*360
        another_in_days = another.day + another.month*30 + another.year*360
        return abs(self_in_days - another_in_days)
